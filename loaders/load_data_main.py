# load_data_main.py
# Load data for load_data.py
# Return DataFrame and geojsone

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from data_preparation.load_data import read_raw_data, data_info, load_geojson
from configs.file_paths import filename, url  

# Return DataFrame
def get_data():
    df_raw = read_raw_data(filename)
    data_info(df_raw)

    return df_raw

# Return geojson
def get_geojson():
    return load_geojson(url)

