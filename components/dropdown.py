
# dropdown.py
# Create dropdown for province and disease

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.import_tools import st

# selected province
def show_selections(df_melted):

    select_col1, select_col2 = st.columns(2)

    with select_col1:
        selected_province = st.selectbox("เลือกจังหวัด", sorted(df_melted["จังหวัด"].unique()), key = "province_select")

# selected disease
    with select_col2:
        selected_disease = st.selectbox("เลือกโรค", sorted(df_melted["ประเภทโรค"].unique()), key = "disease_select")

    return selected_province, selected_disease

# get province, disease
def get_selections(df_melted):
    return show_selections(df_melted)