from datetime import datetime, timedelta

import pandas as pd


def train_test_split(df:pd.DataFrame, last_n_days:datetime=7):
    """
    마지막  n(default 7)일을 test로 분리하여 반환
    t_dat은 일자 단위로 되어있다고 가정
    """
    
    last_date = df.t_dat.max()
    test_start_date = last_date - timedelta(days=last_n_days)

    train_df = df[df.t_dat < test_start_date]
    test_df = df[df.t_dat >= test_start_date]

    print(f"train: {train_df.t_dat.min().strftime('%Y-%m-%d')} ~ {train_df.t_dat.max().strftime('%Y-%m-%d')}")
    print(f"test: {test_df.t_dat.min().strftime('%Y-%m-%d')} ~ {test_df.t_dat.max().strftime('%Y-%m-%d')}")
    
    return train_df, test_df