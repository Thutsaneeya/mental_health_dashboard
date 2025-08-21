# filter_tools.py
# Filter DataFrame for Plot Chart

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.import_tools import pd

# Filter dataFrame by year
def select_by_year(df, year):
     try:
          if year is None:
               # none filter
               return df 
          else:
               # Filter by year
               return df[df["ปี"] == year]
          
     except Exception as e:
        print(f"เกิดข้อผิดพลาด: {e}")

# Sort DataFrame
def sorted_data(df):
     # Sort value
     df = df[["จังหวัด", "จำนวนผู้ป่วย"]]
     #df_sort = (df.groupby("จังหวัด", as_index = False)["จำนวนผู้ป่วย"].sort_values(by = "จำนวนผู้ป่วย", ascending = False)).reset_index()
     df_sorted = df.sort_values(by = "จำนวนผู้ป่วย", ascending = False)
     return df_sorted

# Format for KPI cards
def format_metric(n, unit = "ราย", lang = "th"):
    if lang == "th":
        if n >= 1_000_000:
            return f"{n / 1_000_000:.1f} ล้าน{unit}"
        elif n >= 1_000:
            return f"{n / 1_000:.1f} พัน{unit}"
        else:
            return f"{n:,} {unit}"
    else:
        if n >= 1_000_000:
            return f"{n / 1_000_000:.1f}M {unit}"
        elif n >= 1_000:
            return f"{n / 1_000:.1f}K {unit}"
        else:
            return f"{n:,} {unit}"
        
# Filter province with out "ไม่ระบุจังหวัด"
def filter_province(df):
     try:
          return df[df["จังหวัด"] != "ไม่ระบุจังหวัด"]

     except Exception as e:
        print(f"เกิดข้อผิดพลาด: {e}")

# Filtter for "ไม่ระบุจังหวัด"
def filter_missing_province(df):
     try:
          return df[df["จังหวัด"] == "ไม่ระบุจังหวัด"]

     except Exception as e:
        print(f"เกิดข้อผิดพลาด: {e}")

# Filter top province by number of patients
def filter_top_row(df):
     try:
          # Get maximum row of "จำนวนผู้ป่วย"
          df_max = df.loc[df["จำนวนผู้ป่วย"].idxmax()]
          # Get minimum row of "จำนวนผู้ป่วย"
          df_min = df.loc[df["จำนวนผู้ป่วย"].idxmin()]

          return df_max, df_min
     
     except Exception as e:
        print(f"เกิดข้อผิดพลาด: {e}")