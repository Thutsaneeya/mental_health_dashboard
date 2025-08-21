
# dropdown.py
# Create dropdown for province and disease

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.import_tools import st

def get_selections(df):
    selected_year = st.selectbox("ปี", sorted(df["ปี"].unique()), key = "year_select")
    #selected_province = st.selectbox("จังหวัด", sorted(df["จังหวัด"].unique()), key = "province_select")

    # Selected disease
    #with select_col2:
    #selected_disease = st.selectbox("โรค", sorted(df["ประเภทโรค"].unique()), key = "disease_select")

    return selected_year #selected_province, selected_disease
