import pandas as pd
from sqlalchemy import create_engine
import time

# 1. Database Connection (Use your verified credentials)
engine = create_engine('postgresql+psycopg2://postgres:postgres@localhost:5432/data_audit_db')

def load_data_in_chunks(file_path, table_name):
    print(f"🚀 Starting ingestion for {file_path}...")
    start_time = time.time()
    
    # We use chunksize=50000 to handle 541k rows without crashing your RAM
    for i, chunk in enumerate(pd.read_csv(file_path, chunksize=50000, encoding='ISO-8859-1')):
        # Clean column names immediately to avoid SQL errors
        chunk.columns = [c.lower().replace(' ', '_') for c in chunk.columns]
        
        # 'append' ensures we don't overwrite the data with every chunk
        chunk.to_sql(table_name, engine, if_exists='append' if i > 0 else 'replace', index=False)
        print(f"✅ Chunk {i+1} loaded...")

    end_time = time.time()
    print(f"🏁 Total Ingestion Time: {round(end_time - start_time, 2)} seconds")

# Run the loader
load_data_in_chunks('data.csv', 'raw_transactions')