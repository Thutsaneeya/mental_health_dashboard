# plot_section1.py
# Choropleth
# Number of patients by province per year

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.import_tools import px, st

def plot_choropleth(df, geojson):
    # Create choropleth
    fig = px.choropleth(
                        df,
                        geojson = geojson,
                        locations = "pro_code",
                        color = "รวม",
                        featureidkey = "properties.pro_code",
                        #hover_name = df["จังหวัด"],
                        custom_data = ["จังหวัด", "รวม"],
                        color_continuous_scale = "YlOrRd",
    )
    fig.update_geos(fitbounds = "locations", visible = False)
    fig.update_traces(
                        hovertemplate = '<b>%{customdata[0]}<br>' +
                                        '<b>จำนวนผู้ป่วย:</b> %{customdata[1]:,} คน<br>' +
                                        '<extra></extra>'
    )
    fig.update_layout(
                        template = 'plotly_dark',
                        plot_bgcolor = 'rgba(0, 0, 0, 0)',
                        paper_bgcolor = 'rgba(0, 0, 0, 0)',
                        margin = dict(l = 0, r = 0, t = 0, b = 0),
                        height = 450,
                        coloraxis_colorbar = dict(
                                                    title = "จำนวนผู้ป่วย (คน)",
                                                    x = 0.9,       # horizontal (0 = left, 1 = right)
                                                    y = 0.5,        # vertical (0 = bottom, 1 = top)
                                                    len = 0.6,      # length of legend labels
                                                    thickness = 15  
                        )

    )
    st.plotly_chart(fig, use_container_width = True, key = "choropleth")
