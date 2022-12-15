import stock
import pandas as pd
import numpy as np
import statsmodels.api as sm
from statsmodels import regression
import baostock as bs
from datetime import timedelta, date, datetime
from chinese_calendar import is_workday

class factors():
    def __init__(self) -> None:
        pass

    def ten_days_beta(self, code, start, end, freq, adj, flag):
        result = stock.get_day_k_num(code, start, end, freq, adj)
        first_day = datetime.strptime(start,"%Y-%m-%d")
        print(result.date)
        date_range = np.array(result.date)
        print(len(date_range))
        # raise Exception(0)
        seen = list()
        count, i = 0, 0
        while count < 10:
            pre_date = first_day - timedelta(i)
            if is_workday(pre_date):
                seen.append(pre_date.strftime("%Y-%m-%d"))
                count += 1
            i += 1
        seen = seen[::-1]+list(result.date)
        print(seen)
        begin = seen[0]
        fin = end
        ten_data_dapan = stock.get_day_k_num(flag, begin, fin, freq, adj)
        ten_data_select = stock.get_day_k_num(code, begin, fin, freq, adj)
        ten_data_dapan = ten_data_dapan[(ten_data_dapan['amount'] > '0') & (ten_data_dapan['volume'] > '0')]
        ten_data_select = ten_data_select[(ten_data_select['amount'] > '0') & (ten_data_select['volume'] > '0')]
        seen = list(ten_data_select['date']) if len(list(ten_data_select['date'])) <= len(list(ten_data_dapan['date'])) else list(ten_data_dapan['date'])
        print(ten_data_select)
        print(seen)
        ten_data_dapan_pctchg = list(np.array(ten_data_dapan['pctChg']).astype(np.float32))
        ten_data_select_pctchg = list(np.array(ten_data_select['pctChg']).astype(np.float32))
        pre, cur = 0, 9
        res = []
        while cur < len(seen):
            dapan_data = np.array(ten_data_dapan_pctchg[pre:cur+1])
            select_data = np.array(ten_data_select_pctchg[pre:cur+1])
            beta = np.cov(select_data, dapan_data)[0][1]/np.var(dapan_data)
            res.append([seen[cur], beta])
            pre += 1
            cur += 1
            # res.append([seen[cur], beta])
        ten_beta_data = pd.DataFrame(res, columns=['date', '10_days_beta'])
        return ten_beta_data

    def twenty_days_beta(self, code, start, end, freq, adj, flag):
        result = stock.get_day_k_num(code, start, end, freq, adj)
        first_day = datetime.strptime(start,"%Y-%m-%d")
        print(result.date)
        date_range = np.array(result.date)
        print(len(date_range))
        # raise Exception(0)
        seen = list()
        count, i = 0, 0
        while count < 20:
            pre_date = first_day - timedelta(i)
            if is_workday(pre_date):
                seen.append(pre_date.strftime("%Y-%m-%d"))
                count += 1
            i += 1
        seen = seen[::-1]+list(result.date)
        print(seen)
        begin = seen[0]
        fin = end
        ten_data_dapan = stock.get_day_k_num(flag, begin, fin, freq, adj)
        ten_data_select = stock.get_day_k_num(code, begin, fin, freq, adj)
        ten_data_dapan = ten_data_dapan[(ten_data_dapan['amount'] > '0') & (ten_data_dapan['volume'] > '0')]
        ten_data_select = ten_data_select[(ten_data_select['amount'] > '0') & (ten_data_select['volume'] > '0')]
        seen = list(ten_data_select['date']) if len(list(ten_data_select['date'])) <= len(list(ten_data_dapan['date'])) else list(ten_data_dapan['date'])
        ten_data_dapan_pctchg = list(np.array(ten_data_dapan['pctChg']).astype(np.float32))
        ten_data_select_pctchg = list(np.array(ten_data_select['pctChg']).astype(np.float32))
        pre, cur = 0, 9
        res = []
        while cur < len(seen):
            dapan_data = np.array(ten_data_dapan_pctchg[pre:cur+1])
            select_data = np.array(ten_data_select_pctchg[pre:cur+1])
            beta = np.cov(select_data, dapan_data)[0][1]/np.var(dapan_data)
            res.append([seen[cur], beta])
            pre += 1
            cur += 1
            # res.append([seen[cur], beta])
        twenty_beta_data = pd.DataFrame(res, columns=['date', '20_days_beta'])
        return twenty_beta_data

    def thirty_days_beta(self, code, start, end, freq, adj, flag):
        result = stock.get_day_k_num(code, start, end, freq, adj)
        first_day = datetime.strptime(start,"%Y-%m-%d")
        print(result.date)
        date_range = np.array(result.date)
        print(len(date_range))
        # raise Exception(0)
        seen = list()
        count, i = 0, 0
        while count < 30:
            pre_date = first_day - timedelta(i)
            if is_workday(pre_date):
                seen.append(pre_date.strftime("%Y-%m-%d"))
                count += 1
            i += 1
        seen = seen[::-1]+list(result.date)
        print(seen)
        begin = seen[0]
        fin = end
        ten_data_dapan = stock.get_day_k_num(flag, begin, fin, freq, adj)
        ten_data_select = stock.get_day_k_num(code, begin, fin, freq, adj)
        ten_data_dapan = ten_data_dapan[(ten_data_dapan['amount'] > '0') & (ten_data_dapan['volume'] > '0')]
        ten_data_select = ten_data_select[(ten_data_select['amount'] > '0') & (ten_data_select['volume'] > '0')]
        seen = list(ten_data_select['date']) if len(list(ten_data_select['date'])) <= len(list(ten_data_dapan['date'])) else list(ten_data_dapan['date'])
        ten_data_dapan_pctchg = list(np.array(ten_data_dapan['pctChg']).astype(np.float32))
        ten_data_select_pctchg = list(np.array(ten_data_select['pctChg']).astype(np.float32))
        pre, cur = 0, 9
        res = []
        while cur < len(seen):
            dapan_data = np.array(ten_data_dapan_pctchg[pre:cur+1])
            select_data = np.array(ten_data_select_pctchg[pre:cur+1])
            beta = np.cov(select_data, dapan_data)[0][1]/np.var(dapan_data)
            res.append([seen[cur], beta])
            pre += 1
            cur += 1
            # res.append([seen[cur], beta])
        thirty_beta_data = pd.DataFrame(res, columns=['date', '30_days_beta'])
        return thirty_beta_data

def ten_days_beta_val(code, start, end, freq, adj):
    if 'sz' in code:
        flag = 'sz.399001'
    elif 'sh' in code:
        flag = 'sh.000001'
    fac = factors()
    return fac.ten_days_beta(code, start, end, freq, adj, flag)
    
def twenty_days_beta_val(code, start, end, freq, adj):
    if 'sz' in code:
        flag = 'sz.399001'
    elif 'sh' in code:
        flag = 'sh.000001'
    fac = factors()
    return fac.twenty_days_beta(code, start, end, freq, adj, flag)

def thirty_days_beta_val(code, start, end, freq, adj):
    if 'sz' in code:
        flag = 'sz.399001'
    elif 'sh' in code:
        flag = 'sh.000001'
    fac = factors()
    return fac.thirty_days_beta(code, start, end, freq, adj, flag)

    # dd = factors()
    # res = []
    # for i in range(0, len(date_range)):
    #     begin = seen[i]
    #     fin = date_range[i]
    #     beta = dd.sz_beta(code, begin, fin, freq, adj)
    #     res.append([fin, beta])
    #     if fin not in seen:
    #         seen.append(date_range[i])
    # # res = np.array(res)
    # print(res)
    # beta_data = pd.DataFrame(res, columns=['date', '10_days_beta'])
    # beta_data.set_index(['date'], inplace=True)
    # beta_data.to_csv('qwer.csv')
    # print(beta_data.date)
    







# code = 'sh.600515'
# start = '2022-10-07'
# end = '2022-12-05'
# adj = '3'
# freq = 'd'
# ten_days_beta_val(code,  start, end, freq, adj)