# app.py

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.import_tools import pd, st
from data_preparation.load_data import get_data
from utils.filter_tools import melte_data
from components.dropdown import get_selections
from components.kpi_cards import render_kpi_overview, render_kpi_by_province
from utils.filter_tools import health_summary, select_by_province, select_by_disease
from archive.plot_section1_old import plot_bar
from archive.plot_section2_old2 import plot_scatter
from archive.plot_section3_old import plot_section3

# Section1
def show_section1(df_melted, total_case, top_disease_name, top_disease_sum, top_province):
    # Overview kpi cards
    render_kpi_overview(total_case, top_disease_name, top_disease_sum, top_province)
    # Bar chart
    plot_bar(df_melted)

# Section2
def show_section2(df_by_province, sum_case, disease_name, disease_sum, rare_disease_name, rare_disease_count, province):
    # Province kpi
    render_kpi_by_province(sum_case, disease_name, disease_sum, rare_disease_name, rare_disease_count, province)
    # Scatter chart
    plot_scatter(df_by_province, province)

# Section3
def show_section3(df_by_disease, disease):
    # Facet bar chart
    plot_section3(df_by_disease, disease)

def run_dashboard():
    st.title("Mental Health Dashboard") 
    # __________________________ Load and Prepare Data __________________________
    df, df_copy = get_data()
    df_melted = melte_data(df)

    # __________________________ Get Parameters _________________________________
    # Get parameter from selectbox
    province, disease = get_selections(df_melted)

     # ________________________ Filter __________________________________________
    df_by_province = select_by_province(df_melted, province)
    df_by_disease = select_by_disease(df_melted, disease)

    # __________________________ Describe Data __________________________________
    total_case, top_disease_name, top_disease_sum, top_province = health_summary(df_melted, False)
    sum_case, disease_name, disease_sum, rare_disease_name, rare_disease_count = health_summary(df_by_province, True)

    # __________________________ Visualize _______________________________________
    # Layout    
    tab1, tab2, tab3 = st.tabs(["จำนวนผู้ป่วยทั้งหมด", "การกระจายตัวของผู้ป่วย", "แนวโน้มผู้ป่วยตามพื้นที่"])
    with tab1:
        show_section1(df_melted, total_case, top_disease_name, top_disease_sum, top_province)
    with tab2:
        show_section2(df_by_province, sum_case, disease_name, disease_sum, rare_disease_name, rare_disease_count, province)
    with tab3:
        show_section3(df_by_disease, disease)
    #show_sections(df_filtered, province)

run_dashboard()
#show_section1(df_filtered, province)
#run_section2 = show_section2()