# plot_section2.py
# Heatmap.py
# Total number of patients by disease 

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.import_tools import alt, st

def plot_heatmap(df):

    # Insert new columns for tooltip
    df["ปี_โรค"] = df.apply(lambda row: f"{row['ปี']} - {row['โรค']}", axis = 1)

    heatmap = alt.Chart(df).mark_rect().encode(
                                                # Norminal(N): category data (โรค, จังหวัด)
                                                # Ordinal(O): ordered categorical data (ปี)
                                                # Quantitative(Q): can be measured, calculated, or scaled (จำนวนผู้ป่วย, อายุ)
                                                # horizontal: labelAngle = 0, vertical: labelAngle = 90
                                                x = alt.X("โรค:O", axis = alt.Axis(title = "", titleFontSize = 16, titlePadding = 15, titleFontWeight = 900)),
                                                y = alt.Y("ปี:O", axis = alt.Axis(title = "ปี", titleFontSize = 18, titlePadding = 15)),  
                                                color = alt.Color("จำนวนผู้ป่วย:Q", legend = None, scale = alt.Scale(scheme = "yelloworangebrown")),
                                                tooltip = [
                                                            alt.Tooltip("ปี_โรค:N", title = "ปี"),
                                                            alt.Tooltip("จำนวนผู้ป่วย:Q", title = "จำนวนผู้ป่วย (คน)", format = ",d"),
                                                            alt.Tooltip("จังหวัด:N", title = "พบมากที่สุด")
                                                ],
                                                # Color of the outline around each chart element
                                                stroke = alt.value("black"),
                                                # Sets the thickness of that outline in pixels
                                                strokeWidth = alt.value(0.25),
    ).properties(width = 900).configure_axis(labelFontSize = 12, titleFontSize = 12)
    
    st.altair_chart(heatmap, use_container_width = True, key = "heatmap")
