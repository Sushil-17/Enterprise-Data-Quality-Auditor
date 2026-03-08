# 🛡️ Enterprise Data Quality Auditor

### Revenue Integrity \& ETL Validation Pipeline



A financial data validation system designed to detect revenue inflation, reconcile legitimate revenue, and automate large-scale transaction auditing using Python, PostgreSQL, and Streamlit.



---



# 📷 Dashboard Preview



![Dashboard Overview](images/dashboard_overview.png)



---



# 📊 Business Problem



Financial forecasting was compromised due to a **26.8% data integrity gap** where **"Phantom Revenue"** and financial noise (postage, processing fees, and untracked entries) were inflating reported income.



From a **£9M gross transaction dataset**, the true actionable revenue was unclear, increasing the risk of **misleading financial reporting and incorrect business decisions**.



---



# 🏆 Executive Impact (Results)



### 💰 Reconciled £7.48M in Actual Revenue

Identified and filtered **£2.2M in revenue inflation** from a £9M gross transaction volume by detecting non-revenue financial records.



### ⚡ Reduced Manual Audit Latency by 90%

Engineered an **automated ETL validation pipeline** that replaced manual auditing with a scalable and high-speed data quality process.



### 🥇 Certified "Gold Standard" Dataset

Processed **541K+ transactions** and generated a clean financial dataset to support **reliable executive-level financial forecasting**.



---



### Integrity Breakdown \& Audit Alerts



![Integrity Breakdown](images/integrity_breakdown.png)



---



# 🛠️ Technical Solution



## Automated ETL Pipeline

Developed a robust ETL pipeline using **Python (Pandas + SQLAlchemy)** to:



- Ingest large-scale raw financial datasets

- Clean and standardize transaction records

- Prepare structured data for validation



## Multi-Layer SQL Validation Engine

Implemented advanced validation logic in **PostgreSQL** using:



- **CTEs (Common Table Expressions)**

- **Window Functions**

- Custom filtering logic



This allowed the system to isolate **non-revenue financial noise** such as fees, postage, and incomplete records.



## Interactive Audit Dashboard

Built a **Streamlit-based analytics interface** to visualize:



- Revenue integrity metrics

- Risk segments

- Profit-at-risk indicators



This dashboard enabled **real-time monitoring of financial data quality**.



---



### Executive Insights & Strategic Recommendations



![Strategic Recommendation](images/strategic_recommendation.png)



---



# 📊 Dataset Scale



- **Transactions Processed:** 541,000+

- **Total Gross Transaction Volume:** £9M

- **Validated Revenue:** £7.48M

- **Revenue Inflation Identified:** £2.2M



---



# 🚀 Tech Stack



### Languages

- Python (Pandas, NumPy, SQLAlchemy)



### Database

- PostgreSQL



### Interface

- Streamlit



---



# 📌 Key Skills Demonstrated



- Data Quality Engineering

- Financial Data Validation

- ETL Pipeline Development

- SQL Analytics

- Large Dataset Processing

- Business Impact Analysis

- Data Integrity Auditing



---







# 📂 Project Structure

├── data/                 # Sample transaction datasets (Anonymized)

├── scripts/              # Python ETL automation \& cleaning scripts

├── sql/                  # Validation queries (CTEs, Window Functions)

└── README.md             # Project documentation and impact summary

