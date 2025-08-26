# app.py
# Build dashboard

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.import_tools import st, alt
from loaders.load_data_main import get_data, get_geojson
from utils.filter_tools import select_by_year, filter_province, reshape_disease_summary, sorted_data, get_top_disease
from components.dropdown import get_selections
from components.kpi_cards import overview_year, overview_total_patients, overview_top_patients, overview_min_patients # overview_missing_province
from components.plot_section1  import plot_choropleth
from components.plot_section2 import plot_heatmap
from components.plot_section3 import data_table

# Page configuration _______________________________________________________________________________________
st.set_page_config(
    page_title = "Mental Health dashboard",
    page_icon = "🍃",
    layout = "wide",
    initial_sidebar_state = "expanded")

alt.themes.enable("dark")

# Define emoji for each disease ______________________________________________________________________________
emoji_map = {
                "โรคทางจิตเวชอื่นๆ": "🩺",
                "โรควิตกกังวล": "😟",
                "โรคจิตเภท": "🧠",
                "ติดสารเสพติดอื่นๆ": "💊",
                "ติดยาบ้า (Amphetamine)":"⚡",
                "ติดแอลกอฮอล์": "🍺",
                "โรคชึมเศร้า": "😔",
                "โรคลมชัก": "💜"
}

# Load DataFrame ______________________________________________________________________________________________
df = get_data()
geojson = get_geojson()

# Slide bar ___________________________________________________________________________________________________
with st.sidebar:
    st.markdown("<h3 style = 'white-space: nowrap;'>🍃รายงานสุขภาพจิตของคนไทย</h3>", unsafe_allow_html = True)
    # Get parameter from selectbox
    year = get_selections(df)

# Filter ________________________________________________________________________________________________________
df_reshape = reshape_disease_summary(df)
df_year = select_by_year(df, year)
df_top_disease = get_top_disease(df_reshape, year)
df_main, df_total_row, df_m_province, df_patients, df_top_p, df_min_p = filter_province(df_year)
df_sorted = sorted_data(df_patients)

# Dashboard panel ________________________________________________________________________________________________

# Create columns
col = st.columns((1, 4.5, 1.5), gap = "medium")

# Layout
with col[0]:
    #st.markdown("##### จำนวนผู้ป่วย (คน)")
    overview_year(year)
    overview_total_patients(df_total_row)
    st.write("")
    #overview_missing_province(df_m_province)
    st.markdown("###### มากสุด/ ต่ำสุด")
    overview_top_patients(df_top_p)
    overview_min_patients(df_min_p)
    st.write("")
    
with col[1]:
        plot_choropleth(df_main, geojson)
        plot_heatmap(df_reshape)

        with st.expander('เกี่ยวกับ', expanded = True):
            st.write('''
                        - 🏛️[ข้อมูลจากคลังข้อมูลการแพทย์และสุขภาพ (HDC) กรมสุขภาพจิต กระทรวงสาธารณสุข](https://dmh.go.th/report/datacenter/hdc/)
                        - 📍[GeoJSON boundaries from OpenGISData-Thailand](https://github.com/chingchai/OpenGISData-Thailand/blob/main/provinces.geojson)
                        - 🧠วิเคราะห์ข้อมูลสุขภาพจิตในระดับจังหวัด โดยเน้นแนวโน้มรายปีและความแตกต่างระหว่างพื้นที่
                        - 🗺️choropleth maps: แสดงการกระจายของผู้ป่วยในแต่ละจังหวัด 
                        - 🔥heatmaps: แสดงความชุกของโรคและจังหวัดที่พบมากที่สุด
                        - 📊สรุปข้อมูลด้วย KPI Cards เช่น จำนวนผู้ป่วยรวม จังหวัดที่พบมากที่สุด และน้อยที่สุด
                        - 📋รายการโรคยอดนิยม: แสดง Top 5 โรคยอดนิยมในแต่ละปี
            ''')

with col[2]:
    st.markdown("###### 🚩จำนวนผู้ป่วยรายจังหวัด")
    data_table(df_sorted)
    with st.expander('Top 5 โรคยอดนิยม', expanded = True):
        for i, row in df_top_disease.iterrows():
            disease = row["โรค"]
            emoji = emoji_map.get(disease)
            st.write(f'''- {emoji}{row['โรค']}''')


st.markdown("""
<style>

[data-testid="block-container"] {
    padding-left: 2rem;
    padding-right: 2rem;
    padding-top: 1rem;
    padding-bottom: 0rem;
    margin-bottom: -7rem;
}

[data-testid="stVerticalBlock"] {
    padding-left: 0rem;
    padding-right: 0rem;
}

[data-testid="stMetric"] {
    background-color: #393939;
    text-align: center;
    padding: 15px 0;
}

[data-testid="stMetricLabel"] {
  display: flex;
  justify-content: center;
  align-items: center;
}


</style>
""", unsafe_allow_html = True)






