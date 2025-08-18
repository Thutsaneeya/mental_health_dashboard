# kpi_cards.py

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.import_tools import st, px

def show_kpi_cards(total_case, top_disease_name, top_disease_sum, top_province):
    
    kpi_col1, kpi_col2, kpi_col3 = st.columns(3)

    with kpi_col1:
        st.metric(label = "จำนวนผู้ป่วยทั้งหมด", value = f"{total_case:,} ราย")

    with kpi_col2:
        st.metric(label = "โรคที่พบมากที่สุด", value = top_disease_name, delta = f"{top_disease_sum:,} ราย")

    with kpi_col3:
        st.metric(label = "จังหวัดที่มีผู้ป่วยมากที่สุด", value = top_province)