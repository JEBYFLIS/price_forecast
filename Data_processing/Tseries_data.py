import pandas as pd
from datetime import timedelta
import numpy as np
import torch
from sklearn.preprocessing import MinMaxScaler
from torch.utils.data import TensorDataset
from torch.utils.data import DataLoader

total_data = pd.read_csv('total_data.csv', encoding='gbk')
useful_data = total_data[['date', 'close']]
print(useful_data.head())

def add_date_cols(dataframe: pd.DataFrame, date_col: str = "date"):
    # add time features like month, week of the year ...
    dataframe[date_col] = pd.to_datetime(dataframe[date_col], format="%Y-%m-%d")
    dataframe["day_of_month"] = dataframe[date_col].dt.day / 31
    dataframe["day_of_year"] = dataframe[date_col].dt.dayofyear / 365
    dataframe["month"] = dataframe[date_col].dt.month / 12
    dataframe["week_of_year"] = dataframe[date_col].dt.isocalendar().week / 53
    dataframe["year"] = (dataframe[date_col].dt.year - 2000) / 5

    return dataframe, ["day_of_month", "day_of_year",
                       "month", "week_of_year", "year"]
 

# df, col_name = add_date_cols(useful_data)
# print(df)

def stock_data(df, features):
    # df = data_pre()
    print(df)
    if df.isnull().any().any() == True: #在上一步添加新数据之后，日期和股票代码是NAN这个地方之后需要调整
        print('数组中有空值')
    # pdb.set_trace()
    data_ha = []
    lenth = len(df)
    for idx, elem in enumerate(features):
        # print(df[elem].isnull())
        data_ele = df[elem].values.astype(np.float64)
        data_ele = data_ele.reshape(lenth, 1)
        data_ha.append(data_ele)
    X_hat = np.concatenate(data_ha, axis=1)
    scaler = MinMaxScaler(feature_range=(-1, 1))
    X_hat = scaler.fit_transform(X_hat)
    print('x_hat\n', X_hat)
    max1 = np.max(X_hat,axis=0)
    print('最大值\n',max1)
    x_convert = torch.from_numpy(X_hat) #将numpy数组转化为tensor
    y_data = x_convert[:,3:4].type(torch.float32)
    y_data=y_data.reshape(y_data.shape[0],1)
    x_data = torch.from_numpy(np.delete(X_hat, 3, axis=1)).type(torch.float32)
    dataset = TensorDataset(x_data, y_data)
    data_loader=DataLoader(dataset,batch_size=1,shuffle=False)
    return data_loader