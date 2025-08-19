# plot_section3.py
# Top 5 province of highest and rare patients by disease

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.import_tools import st, px, pd
from utils.filter_tools import province_by_disease

def plot_section3(df, disease):

    df_top_province, df_rare_province = province_by_disease(df, disease)

    df_top_province["กลุ่ม"] = "พบมากที่สุด"
    df_rare_province["กลุ่ม"] = "พบน้อยที่สุด"

    combined = pd.concat([df_top_province, df_rare_province], ignore_index = True)
 
    facet_fig = px.bar(
                        combined, 
                        x = "จังหวัด", 
                        y = "จำนวนผู้ป่วย",
                        color = "กลุ่ม",
                        facet_col = "กลุ่ม",
                        text = "จำนวนผู้ป่วย",
                        labels = {
                                    "จำนวนผู้ป่วย": "จำนวนผู้ป่วย (ราย)",
                                    "จังหวัด": "จังหวัด"
                        },
                        color_discrete_sequence = px.colors.qualitative.Set3
    )
    facet_fig.update_traces(
                            hovertemplate = '<b>%{x}<br>' +
                                            '<b>จำนวนผู้ป่วย:</b> %{y:,.0f} ราย<br>' +
                                            '<extra></extra>'
    )
    facet_fig.update_layout(
                            title = f"เปรียบเทียบจังหวัดที่พบบ่อยและพบน้อยที่สุดในโรค{disease}",
                            height = 400,
                            showlegend = False,
                            margin = dict(t = 60, b = 40, l = 40, r = 40),
                            
    )
    print("combined A: ", combined)
    st.plotly_chart(facet_fig, use_container_width = True, key = "facet_section3")

    

