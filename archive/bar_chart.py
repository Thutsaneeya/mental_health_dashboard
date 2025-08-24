# bar_chart.py

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.import_tools import pd, alt, st

def plot_bar(df):
    # Insert new columns for tooltip
    df["ปี_โรค"] = df.apply(lambda row: f"{row['ปี']} - {row['โรค']}", axis = 1)

    bar_chart = alt.Chart(df).mark_bar(size = 40).encode(
                                                    x = alt.X("ปี:N", title = "", axis = alt.Axis(labelAngle = 0, labelFontSize = 10)),
                                                    y = alt.Y("จำนวนผู้ป่วย:Q", title = "จำนวนผู้ป่วย (คน)", stack = "zero"),
                                                    color = alt.Color("โรค:N", title = "", scale = alt.Scale(scheme = "yelloworangebrown")),
                                                    tooltip = [
                                                                alt.Tooltip("ปี_โรค:N", title = "ปี"),
                                                                alt.Tooltip("จำนวนผู้ป่วย:Q", title = "จำนวนผู้ป่วย (คน)", format = ",d"),
                                                                alt.Tooltip("จังหวัด:N", title = "พบมากที่สุด")
                                                    ]
                                                ).properties(height = 300, width = 250)

    st.altair_chart(bar_chart, use_container_width = True, key = "bar_chart")


    """   fig = px.bar(
                        df,
                        x = "ปี", 
                        y = "จำนวนผู้ป่วย",  
                        color = "โรค", 
                        barmode = "group",
                        #title = "จำนวนผู้ป่วยทั้งหมดในแต่ละโรค",
                        labels = {
                                    "จำนวนผู้ป่วย": "จำนวนผู้ป่วย (คน)",
                                    "โรค": "โรค"

                        },
                        color_discrete_sequence = px.colors.qualitative.Set3
        )
        fig.update_traces(
                            hovertemplate = '<b>ปี: %{x}<br>' +
                                            '<b>จำนวนผู้ป่วย:</b> %{y:,.0f} คน<br>' +
                                            '<extra></extra>'
        )
        fig.update_layout(
                            #title = "จำนวนผู้ป่วยในแต่ละโรครายปี",             
                            template = 'plotly_dark',
                            #plot_bgcolor = 'rgba(0, 0, 0, 0)',
                            #paper_bgcolor = 'rgba(0, 0, 0, 0)',
                            #margin = dict(l = 0, r = 0, t = 0, b = 0),
                            #height = 400
        )
        st.plotly_chart(fig, use_container_width = True, key = "bar_chart")"""