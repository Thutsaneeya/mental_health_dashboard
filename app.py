import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.import_tools import pd
from loaders.load_data_main import get_data
from utils.filter_tools import melte_data
from components.dropdown import get_selections
from components.kpi_cards import show_kpi_cards
from utils.filter_tools import describe_data
#from loaders.load_data_main import load_data_main
from components.plot_section1 import show_section1
#from components.plot_section2 import show_section2

df_raw = get_data()
df_melted = melte_data(df_raw)
province, disease = get_selections(df_melted)
total_case, top_disease_name, top_disease_sum, top_province = describe_data(df_melted)
run_kpi = show_kpi_cards(total_case, top_disease_name, top_disease_sum, top_province)
run_section1 = show_section1()
#run_section2 = show_section2()