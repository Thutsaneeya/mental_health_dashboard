# kpi_cards.py
# Create metric 

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.import_tools import st

# KPI card for total number of patients
def overview_total_patients(df, year):
    return st.metric(label = f"{year}", value = f"{df["จำนวนผู้ป่วย"].sum():,} ราย")

# KPI card for missing province
def overview_missing_province(df):
    return st.metric(label = "ไม่ระบุจังหวัด", value = f"{df["จำนวนผู้ป่วย"].sum():,} ราย")

# KPI for top province by number of patients
def overview_top_patients(df):
    #  delta_color = "inverse"
    return st.metric(label = " ", value = df["จังหวัด"], delta = f"{df["จำนวนผู้ป่วย"]:,} ราย")

# KPI for rare province by number of patients
def overview_min_patients(df):
    return st.metric(label = " ", value = df["จังหวัด"], delta = f"{df["จำนวนผู้ป่วย"]:,} ราย")

