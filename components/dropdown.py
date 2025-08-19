
# dropdown.py
# Create dropdown for province and disease

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.import_tools import st

def show_selections(df):
    # Create columns
    select_col1, select_col2 = st.columns(2)

    # Select province
    with select_col1:
        selected_province = st.selectbox("เลือกจังหวัด", sorted(df["จังหวัด"].unique()), key = "province_select")

    # Selected disease
    with select_col2:
        selected_disease = st.selectbox("เลือกโรค", sorted(df["ประเภทโรค"].unique()), key = "disease_select")

    return selected_province, selected_disease

# Get province, disease
def get_selections(df):
    return show_selections(df)