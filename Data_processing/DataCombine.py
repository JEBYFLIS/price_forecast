import pandas as pd
import torch
import numpy as np
from torch.utils.data import TensorDataset
from torch.utils.data import DataLoader
import stock
import pdb
from sklearn.preprocessing import MinMaxScaler
from sklearn import linear_model
from datetime import timedelta, date, datetime
import prophet
import stock_factor as fac
label = 'close'
features = ['open','high','low','close','preclose','volume','amount','turn','pctChg','peTTM','pbMRQ','psTTM','pcfNcfTTM','10_days_beta','20_days_beta','30_days_beta']


def data_pre(code, start_date, end_date, data_frequent, data_adj):
    df_1 = stock.get_day_k_num(code, start_date, end_date, data_frequent, data_adj)
    # raise Exception('0')
    df_1.index.name = 'days'
    df_beta_ten = fac.ten_days_beta_val(code, start_date, end_date, data_frequent, data_adj)
    df_beta_twenty = fac.twenty_days_beta_val(code, start_date, end_date, data_frequent, data_adj)
    df_beta_thirty = fac.thirty_days_beta_val(code, start_date, end_date, data_frequent, data_adj)
    beta_merged = pd.merge(df_beta_ten, df_beta_twenty)
    beta_merged = pd.merge(beta_merged, df_beta_thirty)
    # df_beta = pd.read_csv('qwer.csv')
    df = pd.merge(df_1, beta_merged)
    print(df.head())
    #使用均值消除数据中的NAN/NULL
    for column in list(df.columns[df.isnull().sum() > 0]): #均值填充
        mean_val = df[column].mean()
        df[column].fillna(mean_val, inplace=True)
    #清除amount=0，volume=0的数据
    df = df[(df['amount'] > '0') & (df['volume'] > '0')]
    df.to_csv('total_data.csv', index=False)

if __name__ == '__main__':
    code = input('输入股票代码:\n')
    start_date = input('输入开始训练日期:\n')
    end_date = input('输入结束训练日期:\n')
    data_frequent = input('数据频率: d日线, m月线\n')
    data_adj = input('是否复权: 1前复权, 2后复权, 3不复权\n')
    data_pre(code, start_date, end_date, data_frequent, data_adj)