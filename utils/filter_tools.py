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
    # Convert dtype
    df_melte["จำนวนผู้ป่วย"] = pd.to_numeric(df_melte["จำนวนผู้ป่วย"], errors = "coerce").astype("Int64")
    print(df_melte.info())
    return df_melte

def health_summary(df):
    # Total number of patients
    total_case = df["จำนวนผู้ป่วย"].sum()
    # number of patients by disease
    top_disease_group = df.groupby("ประเภทโรค")["จำนวนผู้ป่วย"].sum().sort_values(ascending = False)
    # Get max
    top_disease_name = top_disease_group.index[0]
    top_disease_sum = top_disease_group.iloc[0]
    # Get min
    #rare_disease_name = top_disease_group.index[-1]
    #rare_disease_count = top_disease_group.iloc[-1]

    # Get max of province
    top_province = df.groupby("จังหวัด")["จำนวนผู้ป่วย"].sum().sort_values(ascending = False).index[0]

    return top_disease_group, total_case, top_disease_name, top_disease_sum, top_province


# Summarize number of patients
def summarize_by_disease(df):
    return df.groupby("ประเภทโรค")["จำนวนผู้ป่วย"].sum().reset_index()

# Filter by province
def select_by_province(df, province):
   if province is None:
        # none filter
        return df 
   else:
        return df[df["จังหวัด"] == province] 


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

"""def unique_disease(df):
    df["ประเภทโรค"].unique()
    return df"""