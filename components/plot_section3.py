# plot_section3.py
# Data table
# The number of patients by province per year support for choropleth

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.import_tools import pd, px, st

def data_table(df):
    
    # Replace value
    df["จังหวัด"] = df["จังหวัด"].replace("รวม", "ทั้งหมด")
    # Rename column
    df.rename(columns = {"รวม": "จำนวนผู้ป่วย (คน)"}, inplace = True)
    
    # Create DataFrame
    st.dataframe(
                    df,
                    column_order = ("จังหวัด", "จำนวนผู้ป่วย (คน)"),
                    hide_index = True,
                    width = None,
                    column_config = {
                                       "จังหวัด": st.column_config.TextColumn(
                                           "จังหวัด",
                                       ),
                                       "จำนวนผู้ป่วย (คน)": st.column_config.ProgressColumn(
                                           "จำนวนผู้ป่วย (คน)",
                                           format = "%d",
                                           min_value = 0,
                                           max_value = int(df["จำนวนผู้ป่วย (คน)"].max()),
                                       ) 
                    }
    )