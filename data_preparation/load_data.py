# load_data.py
# Data Preparation
# 1. Read raw data, 2. Data information, 3. Cleaning data

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.import_tools import load_csv_from_raw_data, pd

# Load data function
def read_raw_data(filename):
    try:
        # Read CSV
        df = load_csv_from_raw_data(filename)

    except Exception as e:
        print(f"เกิดข้อผิดพลาด: {e}")
        
    return df

# Data information
def data_info(df):
    try:
        print(df.info())
    
    except Exception as e:
        print(f"เกิดข้อผิดพลาด: {e}")

# Clean data
def clean_data(df):
    try:
        # Delete comma 
        for col in df.columns[1:]:
            df[col] = df[col].map(lambda x: str(x).replace(',', '') if pd.notnull(x) else x)
            
        # Replace and filtered ["จังหวัด"]
        df["จังหวัด"] = df["จังหวัด"].replace("ไม่ทราบ", "ไม่ระบุจังหวัด")
        df = df[df["จังหวัด"] != "รวม"]
        
        # Drop column ["รวม"]
        df = df.drop(columns = ["รวม"])

        # Columns rename
        df = df.rename(columns = {
                                'ผู้ป่วยติดเกมส์ในผู้ใหญ่ (15 ปีขึ้นไป)': 'ติดเกมส์ในผู้ใหญ่ (15 ปีขึ้นไป)',
                                'ผู้ป่วยติดเกมส์ในเด็ก (อายุต่ำกว่า 15 ปี)': 'ติดเกมส์ในเด็ก (อายุต่ำกว่า 15 ปี)'
                        }
        )

    except Exception as e:
        print(f"เกิดข้อผิดพลาด: {e}")

    return df