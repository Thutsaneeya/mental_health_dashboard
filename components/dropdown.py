
# dropdown.py
# Create dropdown for year

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.import_tools import st

def get_selections(df):
    # Selectbox year
    selected_year = st.selectbox("ปี", sorted(df["ปี"].unique()), key = "year_select")

    return selected_year
