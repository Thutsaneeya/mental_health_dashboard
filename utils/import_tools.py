# import_tools.py
# import libraries and functions

import pandas as pd
import streamlit as st
import plotly.express as px
import altair as alt
import requests, json
import os

# Get root Directory
def get_project_root():
    return os.path.dirname(os.path.abspath(__file__))

# Get Files Path of Data/*.csv
def get_data_path(filename):
    return os.path.join(get_project_root(), '..', 'data', filename)

# Load .csv for raw_data
def load_csv_from_raw_data(filename):
    path = get_data_path(filename)
    return pd.read_csv(path)