import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.import_tools import pd, st
from loaders.load_data_main import get_data
from utils.filter_tools import melte_data
from components.dropdown import get_selections
from components.kpi_cards import show_kpi_cards
from utils.filter_tools import describe_data, select_by_province
#from loaders.load_data_main import load_data_main
from components.plot_section1 import plot_scatter, plot_bar
#from components.plot_section2 import show_section2

def show_section1(df_filtered, province):
    tab1, tab2 = st.tabs(["การกระจายตัวของผู้ป่วยแต่ละโรค", "จำนวนผู้ป่วยทั้งหมดในแต่ละโรค"])
    with tab1:
        plot_scatter(df_filtered, province)
    with tab2:
        plot_bar(df_filtered)

def run_dashboard():
    # __________________________ Load and Prepare Data __________________________
    df_raw = get_data()
    df = melte_data(df_raw)

    # __________________________ Get Parameters _________________________________
    # Get parameter from selectbox
    province, disease = get_selections(df)

    # __________________________ Describe Data __________________________________
    total_case, top_disease_name, top_disease_sum, rare_disease_name, rare_disease_count, top_province = describe_data(df)

    # __________________________ Filter and Visualize ___________________________
    # Filter by province
    df_filtered = select_by_province(df,province)
    show_kpi_cards(total_case, top_disease_name, top_disease_sum, rare_disease_name, rare_disease_count, top_province)
    show_section1(df_filtered, province)

run_dashboard()
#show_section1(df_filtered, province)
#run_section2 = show_section2()