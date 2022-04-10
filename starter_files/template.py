# libraries you have to install 
import pandas as pd
import numpy as np
from datetime import datetime

def get_data():
    # read data in from spreedsheet (will update anytime the regular website updates as well)
    df = pd.read_html('https://docs.google.com/spreadsheets/d/e/2PACX-1vSE0bsn0p8so7jAYi2whjJLt2MyZ_MljJPVgIcK3GutuRHxohzDwmFR4xx_iEPrRyOL0MigxTdfKsuP/pubhtml?', header = 1)[0]

    # data pre-processing
    df.columns = ['0', 'state', '2', 'spending_plans']
    df = df.iloc[1:, [1, 3]]

    # changing everything to lowercase
    df['spending_plans'] = df['spending_plans'].str.lower()
    df['state'] = df['state'].str.lower()

    return df

def opioid_updates(df):
    # searching for the most current month as that can indicate an update to the table?
    current_month = datetime.now().strftime("%B").lower()

    # subset data for rows that only mention the current month
    subset_df = df.loc[df['spending_plans'].str.contains(current_month), :]

    return subset_df

if __name__ == "__main__":
    df = get_data()
    updates = opioid_updates(df)