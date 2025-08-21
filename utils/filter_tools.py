# filter_tools.py
# Filter DataFrame for Plot Chart

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.import_tools import pd

# Filter by year
def select_by_year(df, year):
   if year is None:
        # none filter
        return df 
   else:
        return df[df["ปี"] == year]