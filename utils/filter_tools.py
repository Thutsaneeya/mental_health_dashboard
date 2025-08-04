# filter_tools.py
# Filter DataFrame for Plot Chart

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.import_tools import pd

# Melte DataFrame to long format
def melte_data(df):
    df_melte = df.melt(
                        id_vars = "จังหวัด",
                        var_name = "ประเภทโรค",
                        value_name = "จำนวนผู้ป่วย"
    )
    # convert dtype
    df_melte["จำนวนผู้ป่วย"] = pd.to_numeric(df_melte["จำนวนผู้ป่วย"], errors = "coerce").astype("Int64")
    #print(df_melte.info())
    return df_melte

def unique_disease(df):
    df["ประเภทโรค"].unique()
    return df

# Summarize number of patients
def summarize_by_disease(df):
    return df.groupby("ประเภทโรค")["จำนวนผู้ป่วย"].sum().reset_index()

# Filter by disease
def select_by_disease(df, disease):
    return df[df["ประเภทโรค"] == disease]

# Get top 5 province of highest patients by disease
def top_province(df, disease):
    df_top5 = (df[df["ประเภทโรค"] == disease]
            .groupby("จังหวัด")["จำนวนผู้ป่วย"]
            .sum()
            .reset_index()
            .sort_values("จำนวนผู้ป่วย", ascending = False).head(5)
    )
    return df_top5

