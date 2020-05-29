import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def get_all_CO_data(df):
    col_names = df.columns
    co_df = pd.DataFrame(columns=col_names)
    for index, row in df.iterrows():
        if row['sensor'] == "co":
            co_df = co_df.append(row)
    return co_df

def reformat_data(df):
    # start with iterrows for simplicity, upgrade to apply() for performance
    new_df = pd.DataFrame(columns=['timestamp', 'node_id'])
    for index, row in df.iterrows():
        # create new column if it doesn't already exist
        # add data to that column
        pass

# resource: https://towardsdatascience.com/5-ways-to-detect-outliers-that-every-data-scientist-should-know-python-code-70a54335a623
# TODO: pass whole df in instead
def sd_analysis(df):
    # Set upper and lower limit to 3 standard deviation
    data_std = df["value_hrf"].std()
    data_mean = df["value_hrf"].mean()
    anomaly_cut_off = data_std * 3

    lower_limit = data_mean - anomaly_cut_off
    upper_limit = data_mean + anomaly_cut_off
    print(lower_limit)

    # find outliers
    out_df = df.loc[(df["value_hrf"] > upper_limit) | (df["value_hrf"] < lower_limit)]
    return out_df

# take in just a CO df
def detect_anomalies(df):
    return sd_analysis(df)



def main():
    path_monthly = "data/chicago-complete.monthly.2019-04-01-to-2019-04-30/chicago-complete.monthly.2019-04-01-to-2019-04-30_reduced_data_30m/data.csv"
    path_weekly = "data/chicago-complete.weekly.2020-04-08-to-2020-04-14/weekly_April_08_to_14_data_drop.csv"
    df = pd.read_csv(path_weekly)
    print(df.head())

    # co_df = get_all_CO_data(df)
    path_weekly_co = "data/weekly_april_08_to_14_co_data.csv"
    co_df = pd.read_csv(path_weekly_co)
    print(co_df.head())
    anom_df = detect_anomalies(co_df)
    anom_df.to_csv("data/weekly_april_08_to_14_co_data_anomalies.csv")
    # co_df.to_csv("data/monthly_april_2019_reduced_co_data.csv")
    # co_df.to_csv("data/weekly_april_08_to_14_co_data.csv")



if __name__ == "__main__":
    main()