import pandas as pd
import torch
import numpy as np
from torch.utils.data import TensorDataset
from torch.utils.data import DataLoader
import pdb
from sklearn.preprocessing import MinMaxScaler
from sklearn import linear_model
from datetime import timedelta, date, datetime
import prophet
label = 'close'
features = ['open','high','low','close','preclose','volume','amount','turn','pctChg','peTTM','pbMRQ','psTTM','pcfNcfTTM','10_days_beta','20_days_beta','30_days_beta']

def ProphetData():
    from chinese_calendar import is_workday
    df = pd.read_csv('D:\price_forecast\Data_processing\\total_data.csv')
    df['date.1'] = df['date'].copy(deep=True)
    df.set_index('date.1', inplace=True)
    test_df = df[-30:]
    test_df = test_df.rename(columns={'date':'ds'})
    print(test_df)
    last_day = test_df['ds'].values[-1] 
    print('当前最后一天\n',last_day)
    last_day = datetime.strptime(last_day,"%Y-%m-%d")
    futrue_date = list()
    df_workday = pd.DataFrame() 
    count, i = 0, 1
    while count < 7:
        pred_date = (last_day+timedelta(days=i))
        if is_workday(pred_date):
            futrue_date.append(pred_date.strftime("%Y-%m-%d"))
            count += 1
        i += 1
    futrue_date = pd.DataFrame(futrue_date, columns=['ds'])
    print(futrue_date)
    for idx, elem in enumerate(features):
        data_ele = test_df[['ds', elem]].reset_index(drop=True)
        data_ele = data_ele.rename(columns={elem:'y'})
        # print(data_ele)
        model = prophet.Prophet()
        model.fit(data_ele)
        forcast = model.predict(futrue_date)
        print(forcast)
        forcast['yhat_mean'] = forcast[['yhat_upper', 'yhat_lower']].mean(axis=1)
        # df_workday = pd.concat([df_workday, forcast['yhat_upper']], axis=1)
        df_workday = pd.concat([df_workday, forcast['yhat_mean']], axis=1)  #prophet取平均
        # print(df_workday)
    df_workday.columns = features
    df_workday = pd.concat([futrue_date, df_workday], axis=1)
    df_workday.set_index('ds', inplace=True)
    print(df_workday)
    res = pd.concat([test_df[features], df_workday], axis=0)
    res['date'] = res.index
    res.reset_index(drop=True)
    res.to_csv('prophet_data.csv')
    print(res)
    return res  

if __name__ == '__main__':
    ProphetData()