# kpi_cards.py

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.import_tools import st, px

def show_kpi_cards(total_case, top_disease_name, top_disease_sum, top_province):
    # Create columns
    row1_col1, row1_col2, = st.columns(2)
    row2_col1, row2_col2, = st.columns(2)

    # Create KPI cards
    with row1_col1:
        st.metric(label = "จำนวนผู้ป่วยทั้งหมด", value = f"{total_case:,} ราย")

    with row1_col2:
        st.metric(label = "จังหวัดที่มีผู้ป่วยมากที่สุด", value = top_province)

    with row2_col1:
        st.metric(label = "โรคที่พบมากที่สุด", value = top_disease_name, delta = f"{top_disease_sum:,} ราย")

    with row2_col2:
        st.empty()
        #st.metric(label = "โรคที่พบน้อยที่สุด", value = rare_disease_name, delta = f"{rare_disease_count:,} ราย")
    