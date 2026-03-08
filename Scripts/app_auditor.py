import streamlit as st
import pandas as pd
from sqlalchemy import create_engine, text
import plotly.express as px

# 1. DATABASE CONNECTION
engine = create_engine('postgresql+psycopg2://postgres:postgres@localhost:5432/data_audit_db')

st.set_page_config(page_title="Data Quality Auditor", layout="wide")

# 2. FETCH REAL-TIME METRICS FROM SQL
def get_audit_data():
    with engine.connect() as conn:
        # Row Counts
        total = conn.execute(text("SELECT COUNT(*) FROM raw_transactions")).scalar()
        noise = conn.execute(text("""
            SELECT COUNT(*) FROM raw_transactions 
            WHERE customerid IS NULL OR unitprice <= 0 OR quantity <= 0
        """)).scalar()
        
        null_ids = conn.execute(text("SELECT COUNT(*) FROM raw_transactions WHERE customerid IS NULL")).scalar()
        bad_prices = conn.execute(text("SELECT COUNT(*) FROM raw_transactions WHERE unitprice <= 0")).scalar()
        bad_qty = conn.execute(text("SELECT COUNT(*) FROM raw_transactions WHERE quantity <= 0")).scalar()
        
        # Financial Metrics
        total_sales = conn.execute(text("SELECT SUM(unitprice * quantity) FROM raw_transactions")).scalar() or 0
        phantom_rev = conn.execute(text("""
            SELECT SUM(unitprice * ABS(quantity)) FROM raw_transactions 
            WHERE length(stockcode) < 5 OR unitprice <= 0
        """)).scalar() or 0
        untracked_rev = conn.execute(text("""
            SELECT SUM(unitprice * quantity) FROM raw_transactions 
            WHERE customerid IS NULL AND quantity > 0
        """)).scalar() or 0
        
    return total, noise, null_ids, bad_prices, bad_qty, total_sales, phantom_rev, untracked_rev

total, noise, null_ids, bad_prices, bad_qty, total_sales, phantom_rev, untracked_rev = get_audit_data()

# Calculations
certified_sales = total_sales - (phantom_rev + untracked_rev)
valid_rows = total - noise
score = round((valid_rows / total) * 100, 2)

# 3. UI LAYOUT
st.title("🛡️ Enterprise Data Quality Auditor")
st.subheader("Financial Integrity Audit: Online Retail Dataset")

# KPI Metrics Row with Question Mark (Help) Icons
col1, col2, col3, col4, col5 = st.columns(5)
col1.metric("Total Rows", f"{total:,}")
col2.metric("Data Health", f"{score}%", delta=f"{score - 100:.2f}%", delta_color="inverse")
col3.metric("Raw System Total", f"£{total_sales:,.0f}", help="The raw, uncleaned revenue reported by the system.")
col4.metric("Risk Identified", f"£{phantom_rev + untracked_rev:,.0f}", 
           delta_color="inverse", 
           help="Total Revenue at risk. Includes: 1. Phantom Revenue (Fees/Errors) + 2. Untracked Sales (No Customer ID).")
col5.metric("Actual Real Sales", f"£{certified_sales:,.0f}", 
           help="The 'Gold Standard' Sales: High-integrity revenue tied to valid products and identified customers.")

st.divider()

# Charts & Alerts Row
left, right = st.columns([2, 1])

with left:
    st.subheader("📊 Integrity Breakdown (Row Count)")
    fig_df = pd.DataFrame({
        "Status": ["Certified (Clean)", "Noise (Flagged)"],
        "Count": [valid_rows, noise]
    })
    fig = px.pie(fig_df, values='Count', names='Status', 
                 hole=0.5, 
                 color_discrete_sequence=['#2ECC71', '#E74C3C'])
    st.plotly_chart(fig, use_container_width=True)

with right:
    st.subheader("🚨 Critical Audit Alerts")
    st.error(f"**Identity Failure:** {null_ids:,} rows missing CustomerID.")
    st.warning(f"**Financial Logic:** {bad_prices:,} rows with Price ≤ 0.")
    st.warning(f"**Logistics Error:** {bad_qty:,} rows with Quantity ≤ 0.")
    st.info(f"**Phantom Insight:** £{phantom_rev:,.0f} consists of non-product revenue (Bank charges, Postage, and Adjustments).")

# 4. THE GOLD STANDARD & RECOMMENDATION
st.divider()
st.subheader("🏆 The 'Gold Standard' Certification")
st.success(f"By filtering the noise, we have isolated **£{certified_sales:,.2f}** in high-value, actionable sales.")

st.markdown(f"""
### **📈 Analyst's Strategic Recommendation:**
* **Revenue Verification:** While the system claims **£{total_sales:,.2f}**, only the **Gold Standard (£{certified_sales:,.2f})** should be used for tax and forecasting.
* **Risk Mitigation:** The **£{phantom_rev + untracked_rev:,.2f}** identified as 'Risk' is currently inflating the company's perceived growth by roughly 23%.
* **Data Strategy:** Capturing missing identities for the **£{untracked_rev:,.2f}** in sales could unlock significant marketing ROI through customer re-targeting.
""")

# 5. DATA PREVIEW (The Evidence)
st.subheader("🔍 Sample of Flagged 'Noise' Data")
dirty_sample = pd.read_sql(text("""
    SELECT * FROM raw_transactions 
    WHERE customerid IS NULL OR unitprice <= 0 OR quantity <= 0 
    LIMIT 5
"""), engine)
st.table(dirty_sample)