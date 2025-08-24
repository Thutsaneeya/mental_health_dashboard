# donut_chart.py

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.import_tools import alt, st

def plot_donut(df):
     # Insert new columns for tooltip
    df["ปี_โรค"] = df.apply(lambda row: f"{row['ปี']} - {row['โรค']}", axis = 1)

    donut_chart = alt.Chart(df).mark_arc(innerRadius = 65).encode(
                                                                      theta = alt.Theta("จำนวนผู้ป่วย:Q", title = "จำนวนผู้ป่วย (คน)"),
                                                                      color = alt.Color("โรค:N", legend = None, title = "โรค", scale = alt.Scale(scheme = "oranges")),
                                                                      tooltip = [
                                                                                     alt.Tooltip("ปี_โรค:N", title = "ปี"),
                                                                                     alt.Tooltip("จำนวนผู้ป่วย:Q", title = "จำนวนผู้ป่วย (คน)", format = ",d"),
                                                                                     alt.Tooltip("จังหวัด:N", title = "พบมากที่สุด")
                                                                      ],
                                                                      stroke = alt.value("black"),
                                                                      # Sets the thickness of that outline in pixels
                                                                      strokeWidth = alt.value(0.25),
                                                                         
    ).properties(width = 130, height = 130)
    st.altair_chart(donut_chart, use_container_width = True, key = "donut_chart")
