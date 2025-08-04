# load_data_main.py
# Load data for load_data.py
# Return DataFrame

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from data_preparation.load_data import (read_raw_data, data_info, clean_data)
from configs.file_paths import filename  

def load_data_main():
    df_raw = read_raw_data(filename)
    #print("Loading...")
    df_info = data_info(df_raw)
    #print("Infomation...")
    df_cleaned = clean_data(df_raw)
    #print("Cleaning...")

    return df_cleaned

def get_data():
    return load_data_main()

