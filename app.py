import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.import_tools import pd
from loaders.load_data_main import load_data_main
from components.plot_section1 import show_section1
from components.plot_section2 import show_section2

run_main_data = load_data_main()
run_section1 = show_section1()
run_section2 = show_section2()