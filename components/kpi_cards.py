# kpi_cards.py
# Create metric 

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.import_tools import st
from utils.filter_tools import format_metric

# KPI card for total number of patients
def overview_year(year):
    # format_metric
    return st.metric(label = "ปีงบประมาณ", value = f"{year}")
def overview_total_patients(df):
    return st.metric(label = "จำนวนผู้ป่วย (คน)", value = f"{format_metric(df['รวม'].iloc[0])} ")
# KPI card for missing province
def overview_missing_province(df):
    return st.metric(label = "ไม่ระบุจังหวัด", value = f"{format_metric(df['รวม'].iloc[0])}")

# KPI for top province by number of patients
def overview_top_patients(df):
    #  delta_color = "inverse"
    return st.metric(label =f"🔴{df['จังหวัด']}", value = f"{format_metric(df['รวม'])}")

# KPI for rare province by number of patients
def overview_min_patients(df):
    return st.metric(label = f"🟢{df['จังหวัด']}", value = f"{format_metric(df['รวม'])}")

