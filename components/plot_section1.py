# plot_section1.py 
# Analyze annual distribution of patients
# Calculate total cases per disease by year

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.import_tools import st, px
from utils.filter_tools import unique_disease, summarize_by_disease

#df_summary = df_filtered.groupby("ประเภทโรค")["จำนวนผู้ป่วย"].sum().reset_index()

#tab1, tab2 = st.tabs(["การกระจายตัวของผู้ป่วยแต่ละโรค", "จำนวนผู้ป่วยทั้งหมดในแต่ละโรค"])

def plot_scatter(df, province):
    #with tab1:
        # Scatter chart:  Analyze annual distribution of patients
        scatter_fig = px.scatter(
                                    df, 
                                    x = "ประเภทโรค", 
                                    y = "จำนวนผู้ป่วย", 
                                    size  = "จำนวนผู้ป่วย",
                                    color = "จังหวัด",
                                    #title = "จำนวนผู้ป่วยในปีงบประมาณ 2566",
                                    labels = {
                                                "จังหวัด": "จังหวัด",
                                                "จำนวนผู้ป่วย": "จำนวนผู้ป่วย (ราย)",
                                                "ประเภทโรค": "ประเภทโรค"

                                    },
                                    color_discrete_sequence = px.colors.qualitative.Set3,
                                    #custom_data = ["ประเภทโรค"]
        )
        scatter_fig.update_traces(
                                    hovertemplate = '<b>%{x}<br>' +
                                                    '<b>จำนวนผู้ป่วย:</b> %{y:,.0f} ราย<br>' +
                                                    '<extra></extra>'

        )
        scatter_fig.update_layout(title = f"การกระจายตัวของผู้ป่วยแต่ละโรคในจังหวัด{province}")
        st.plotly_chart(scatter_fig, use_container_width = True, key = "scatter_section1")

def plot_bar(df):

    df_summary = summarize_by_disease(df)

    #with tab2:
        # Bar Chart: Calculate total cases per disease
    bar_fig = px.bar(
                            df_summary, 
                            x = "ประเภทโรค", 
                            y = "จำนวนผู้ป่วย",  
                            color = "ประเภทโรค", 
                            barmode = "group",
                            #title = "จำนวนผู้ป่วยทั้งหมดในแต่ละโรค",
                            labels = {
                                        "จำนวนผู้ป่วย": "จำนวนผู้ป่วย (ราย)",
                                        "ประเภทโรค": "ประเภทโรค"

                            },
                            color_discrete_sequence = px.colors.qualitative.Set3
        )
    bar_fig.update_traces(
                                hovertemplate = '<b>%{x}<br>' +
                                                '<b>จำนวนผู้ป่วย:</b> %{y:,.0f} ราย<br>' +
                                                '<extra></extra>'
        )

    bar_fig.update_layout(title = "จำนวนผู้ป่วยทั้งหมดในแต่ละโรค")
    st.plotly_chart(bar_fig, use_container_width = True, key = "bar_section1")


#def show_section1(df, province):
 #   return plot_scatter(df, province), plot_bar(df)

