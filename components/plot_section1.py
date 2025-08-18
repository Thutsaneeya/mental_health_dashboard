# plot_section1.py 
# Analyze annual distribution of patients
# Calculate total cases per disease by year

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.import_tools import st, px
from loaders.load_data_main import get_data
from utils.filter_tools import melte_data, unique_disease, summarize_by_disease

# Get data
df = get_data()



# Melte DataFrame , filter and summarize by disease
df_melted = melte_data(df)
df_filtered = unique_disease(df_melted)
#df_summary = df_filtered.groupby("ประเภทโรค")["จำนวนผู้ป่วย"].sum().reset_index()
df_summary = summarize_by_disease(df_filtered)

#def kpi_card():

"""kpi_col1, kpi_col2, kpi_col3 = st.columns(3)

with kpi_col1:
    st.metric(label = "จำนวนผู้ป่วยทั้งหมด", value = "123 ราย")

with kpi_col2:
    st.metric(label = "โรคที่พบมากที่สุด", value = "ไข้เลือดออก", delta = "456 ราย")

with kpi_col3:
    st.metric(label = "จังหวัดที่มีผู้ป่วยมากที่สุด", value = "เลย")"""


def plot_section1(df_filtered, df_summary):

    tab1, tab2 = st.tabs(["Scatter chart", "Bar chart"])

    with tab1:
        # Scatter chart:  Analyze annual distribution of patients
        scatter_fig = px.scatter(
                                    df_filtered, 
                                    x = "จังหวัด", 
                                    y = "จำนวนผู้ป่วย", 
                                    size  = "จำนวนผู้ป่วย",
                                    color = "ประเภทโรค",
                                    #title = "จำนวนผู้ป่วยในปีงบประมาณ 2566",
                                    labels = {
                                                "จังหวัด": "จังหวัด",
                                                "จำนวนผู้ป่วย": "จำนวนผู้ป่วย (ราย)",
                                                "ประเภทโรค": "ประเภทโรค"

                                    },
                                    color_discrete_sequence = px.colors.qualitative.Set3,
                                    custom_data = ["ประเภทโรค"]
        )
        scatter_fig.update_traces(
                                    hovertemplate = '<b>%{customdata[0]}<br>' +
                                                    '<b>จังหวัด:</b> %{x}<br>' +
                                                    '<b>จำนวนผู้ป่วย:</b> %{y:,.0f} ราย<br>' +
                                                    '<extra></extra>'

        )
        scatter_fig.update_layout(title = "การกระจายตัวของผู้ป่วยแต่ละโรคต่างๆ")
        st.plotly_chart(scatter_fig, use_container_width = True, key = "scatter_section1")

    with tab2:
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


def show_section1():
    #kpi_card()
    return plot_section1(df_filtered, df_summary)

