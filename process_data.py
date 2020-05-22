import numpy as np
import pandas as pd


def get_all_CO_data(df):
    col_names = df.columns
    co_df = pd.DataFrame(columns=col_names)
    for index, row in df.iterrows():
        if row['sensor'] == "co":
            co_df = co_df.append(row)
    return co_df


def main():
    path_monthly = "data/chicago-complete.monthly.2019-04-01-to-2019-04-30/chicago-complete.monthly.2019-04-01-to-2019-04-30_reduced_data_30m/data.csv"
    path_weekly = "data/chicago-complete.weekly.2020-04-08-to-2020-04-14/weekly_April_08_to_14_data_drop.csv"
    df = pd.read_csv(path_weekly)
    print(df.head())
    co_df = get_all_CO_data(df)
    # co_df.to_csv("data/monthly_april_2019_reduced_co_data.csv")
    co_df.to_csv("data/weekly_april_08_to_14_co_data.csv")



if __name__ == "__main__":
    main()