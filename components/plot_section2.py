# Section2:
# Geographic & Disease-Specific Distribution of Patients
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.import_tools import st, px
from loaders.load_data_main import get_data
from utils.filter_tools import (melte_data, select_by_disease, top_province)

# Get DataFrame
df = get_data()

# Melte DataFrame
df_melted = melte_data(df)

#selected_disease = st.selectbox("เลือกโรค", sorted(df_melted["ประเภทโรค"].unique()), key = "disease_select")

def plot_section2():
    
    # Create slec disease 
    with st.container():
        selected_disease = st.selectbox("เลือกโรค", sorted(df_melted["ประเภทโรค"].unique()), key = "disease_select")
    # Filter by disease
    df_disease = select_by_disease(df_melted, selected_disease)
    # Get top 5 province with the highest number of patients
    df_provinces = top_province(df_disease, selected_disease)

    # Treemap by select disease
    treemap_fig = px.treemap(
                            df_disease,
                            path = ["จังหวัด"],
                            values = "จำนวนผู้ป่วย",
                            custom_data = ["จังหวัด","จำนวนผู้ป่วย"],
                            color_discrete_sequence = px.colors.qualitative.Set3
    )
    treemap_fig.data[0].hovertemplate = [
                                        "" if label == "ทั้งหมด" else f"<b>{label}</b><br>จำนวนผู้ป่วย: {value:,.0f} ราย</br><extra></extra>"
                                        for label, value in zip(treemap_fig.data[0].labels, treemap_fig.data[0].values)
    ]

    treemap_fig.update_layout(title = f"ภาพรวมผู้ป่วย {selected_disease} ในแต่ละจังหวัด (Treemap)")
    st.plotly_chart(treemap_fig, use_container_width = True, key = "treemap_section1")

    # Bar Chart: howing top 5 provinces with the highest number of patients
    bar_fig = px.bar(
                        df_provinces, 
                        x = "จังหวัด", 
                        y = "จำนวนผู้ป่วย",  
                        color = "จังหวัด", 
                        barmode = "group",
                        labels = {
                                    "จำนวนผู้ป่วย": "จำนวนผู้ป่วย (ราย)",
                                    "จังหวัด": "จังหวัด"

                        },
                        color_discrete_sequence = px.colors.qualitative.Set3
    )
    bar_fig.update_traces(
        hovertemplate = '<b>%{x}<br>' +
                        '<b>จำนวนผู้ป่วย: %{y:,.0f} ราย<br>' +
                        '<extra></extra>'
    )
    bar_fig.update_layout(title = f"จังหวัดที่พบผู้ป่วย {selected_disease} มากที่สุด 5 อันดับ")
    st.plotly_chart(bar_fig, use_container_width = True, key = "bar_section2")

def show_section2():
    return plot_section2 ()


