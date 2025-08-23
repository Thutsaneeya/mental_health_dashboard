# filter_tools.py
# Filter DataFrame for Plot Chart

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.import_tools import pd

# Filter DataFrame by year
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
        return df
        
# Filter province by year select
def filter_province(df):
     try:
          # Remove rows "ไม่ระบุจังหวัด" and "รวม" for chroropleth
          df_main = df[~df["จังหวัด"].isin(["รวม", "ไม่ระบุจังหวัด"])]

          # "รวม" row for total_patients
          df_total_row = df[df["จังหวัด"] == "รวม"]

          # Missing province for KPI cards
          df_m_province = df[df["จังหวัด"] == "ไม่ระบุจังหวัด"][["จังหวัด", "รวม"]]
          
          # Filter for data table
          df_patients = df[df["จังหวัด"] != "รวม"][["จังหวัด", "รวม"]]

          # For donut chart
          
          # Get maximum and minimum rows of patients for KPI cards
          df_top_p = df_patients.loc[df_patients["รวม"].idxmax()]
          df_min_p = df_patients.loc[df_patients["รวม"].idxmin()]

          return df_main, df_total_row, df_m_province, df_patients, df_top_p, df_min_p

     except Exception as e:
          print(f"เกิดข้อผิดพลาด: {e}")
          return df
     
# Reshape DataFrame 
def reshape_disease_summary(df):
     try:
          # Total "รวม" rows
          df_totla_raw = df[df["จังหวัด"] == "รวม"]
          df_total = df_totla_raw.drop(columns = ["จังหวัด", "รวม", "pro_code"])
          df_sum = df_total.melt(id_vars = "ปี", var_name = "โรค", value_name = "จำนวนผู้ป่วย")

          # With out "รวม" rows
          df_detail_raw = df[df["จังหวัด"] != "รวม"]
          df_detail = df_detail_raw.drop(columns = ["รวม", "pro_code"])
          df_detail_melted = df_detail.melt(id_vars = ["ปี", "จังหวัด"], var_name = "โรค", value_name = "จำนวนผู้ป่วย")
          df_hotspot = (
                         df_detail_melted.groupby(["ปี", "โรค"])
                         .apply(lambda g: g.loc[g["จำนวนผู้ป่วย"].idxmax()]).reset_index(drop = True)
          )[["ปี", "โรค", "จังหวัด"]]

          # Merge DataFrame for Heatmap
          df_reshape = df_sum.merge(df_hotspot, on = ["ปี", "โรค"], how = "left")

          # Filter for donut chart
          # Top disease by year
          df_top_disease = (
                         df_detail_melted.groupby(["ปี", "โรค"])["จำนวนผู้ป่วย"]
                         .sum()
                         .reset_index()
                         .sort_values(["ปี", "จำนวนผู้ป่วย"], ascending = [True, False])
                         .groupby("ปี")
                         .head(1)
                         .reset_index(drop=True)
          )
          # Top province per disease
          df_top_province = (
                         df_detail_melted[df_detail_melted.set_index(["ปี", "โรค"]).index.isin(df_top_disease.set_index(["ปี", "โรค"]).index)]
                         .groupby(["ปี", "โรค"])
                         .apply(lambda g: g.loc[g["จำนวนผู้ป่วย"].idxmax()])
                         .reset_index(drop=True)[["ปี", "โรค", "จังหวัด"]]
          )

          df_top = df_top_disease.merge(df_top_province, on = ["ปี", "โรค"])

          return df_reshape, df_top

     except Exception as e:
        print(f"เกิดข้อผิดพลาด: {e}")
        #return df

# Sort DataFrame
def sorted_data(df):
     print("Sorted!......")
     # Sort value
     df = df[["จังหวัด", "รวม"]]
     #df_sort = (df.groupby("จังหวัด", as_index = False)["จำนวนผู้ป่วย"].sort_values(by = "จำนวนผู้ป่วย", ascending = False)).reset_index()
     df_sorted = df.sort_values(by = "รวม", ascending = False)
     return df_sorted

# Format for KPI cards
def format_metric(n):
     if n > 1000000:
          print("1 ckecked!...")
          if (n % 1000000 == 0):
               print("2 ckecked!...")
               return f"{n // 1000000} ล้าน"
          else:
               # round to 2 decimal
               print("3 ckecked!...")
               var = round(n / 1000000, 2)
               var_str = f"{var:.2f}"
               
               # If the second decimal digit = 0, drop it for cleaner display
               if var_str[-1] == "0":
                    print("4 ckecked!...")
                    var_str = f"{var:.1f}"
               
               return f"{var_str} ล้าน"
     else:
          return f"{n:,}"
