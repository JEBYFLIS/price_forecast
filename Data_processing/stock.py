import baostock as bs
import pandas as pd
from matplotlib import pyplot as plt
import mplfinance as mpf

def get_day_k_num(code, start, end, freq, adj):
    #### 登陆系统 ####
    lg = bs.login()
    # 显示登陆返回信息
    # print('login respond error_code:'+lg.error_code)
    # print('login respond  error_msg:'+lg.error_msg)

    #### 获取历史K线数据 ####
    # query_history_k_data()
    # fields= "date,code,open,high,low,close"
    fields = 'date,code,open,high,low,close,preclose,volume,amount,turn,pctChg,peTTM,pbMRQ,psTTM,pcfNcfTTM'
    rs = bs.query_history_k_data(code, fields,
        start_date=start, end_date=end, 
        frequency=freq, adjustflag=adj) 
    #frequency="d"取日k线，adjustflag="3"默认不复权，
    #1：后复权；2：前复权

    data_list = []
    while (rs.error_code == '0') & rs.next():
        # 获取一条记录，将记录合并在一起
        data_list.append(rs.get_row_data())
    result = pd.DataFrame(data_list, columns=rs.fields)
    result.index=pd.to_datetime(result.date)
    #### 结果集输出到csv文件 ####
    #result.to_csv("c:/zjy/history_k_data.csv", 
    #        encoding="gbk", index=False)
    result.head()
    #### 登出系统 ####
    bs.logout()
    return result

def visaul_line(data):
    print(data.info())
    #将某些object转化numeric
    data=data.apply(pd.to_numeric, errors='ignore')
    data.info()
    data.close.plot(figsize=(16,8))
    ax = plt.gca()  
    ax.spines['right'].set_color('none') 
    ax.spines['top'].set_color('none')    
    plt.show() 

def visaul_k_line(daily):
    daily=daily.apply(pd.to_numeric, errors='ignore')
    mpf.plot(daily, type='candle', style='starsandstripes')

class overview_finance():
    def __init__(self) -> None:
        pass

    def deposit_rate(start, end):
        # 登陆系统
        lg = bs.login()
        # 显示登陆返回信息
        print('login respond error_code:'+lg.error_code)
        print('login respond  error_msg:'+lg.error_msg)

        # 获取存款利率
        rs = bs.query_deposit_rate_data(start_date=start, end_date=end)
        print('query_deposit_rate_data respond error_code:'+rs.error_code)
        print('query_deposit_rate_data respond  error_msg:'+rs.error_msg)

        # 打印结果集
        data_list = []
        while (rs.error_code == '0') & rs.next():
            # 获取一条记录，将记录合并在一起
            data_list.append(rs.get_row_data())
        result = pd.DataFrame(data_list, columns=rs.fields)
        # 结果集输出到csv文件
        # result.to_csv("D:/deposit_rate.csv", encoding="gbk", index=False)
        print(result)
        # 登出系统
        bs.logout()
        return result
    
    def loan_rate(start, end):
        # 登陆系统
        lg = bs.login()
        # 显示登陆返回信息
        print('login respond error_code:'+lg.error_code)
        print('login respond  error_msg:'+lg.error_msg)

        # 获取存款利率
        rs = bs.query_loan_rate_data(start_date=start, end_date=end)
        print('query_deposit_rate_data respond error_code:'+rs.error_code)
        print('query_deposit_rate_data respond  error_msg:'+rs.error_msg)

        # 打印结果集
        data_list = []
        while (rs.error_code == '0') & rs.next():
            # 获取一条记录，将记录合并在一起
            data_list.append(rs.get_row_data())
        result = pd.DataFrame(data_list, columns=rs.fields)
        # 结果集输出到csv文件
        # result.to_csv("D:/deposit_rate.csv", encoding="gbk", index=False)
        print(result)
        # 登出系统
        bs.logout()
        return result

    def required_reserve_ratio_data(start, end):
        # 登陆系统
        lg = bs.login()
        # 显示登陆返回信息
        print('login respond error_code:'+lg.error_code)
        print('login respond  error_msg:'+lg.error_msg)

        # 获取存款利率
        rs = bs.query_required_reserve_ratio_data(start_date=start, end_date=end)
        print('query_deposit_rate_data respond error_code:'+rs.error_code)
        print('query_deposit_rate_data respond  error_msg:'+rs.error_msg)

        # 打印结果集
        data_list = []
        while (rs.error_code == '0') & rs.next():
            # 获取一条记录，将记录合并在一起
            data_list.append(rs.get_row_data())
        result = pd.DataFrame(data_list, columns=rs.fields)
        # 结果集输出到csv文件
        # result.to_csv("D:/deposit_rate.csv", encoding="gbk", index=False)
        print(result)
        # 登出系统
        bs.logout()
        return result      
    
def hangyefenlei(hangye):
    # '银行' '' '交通运输' '汽车' '房地产' '公用事业' '钢铁' '化工' '非银金融' '机械设备' '传媒' '国防军工'
    # '建筑装饰' '通信' '综合' '休闲服务' '医药生物' '商业贸易' '食品饮料' '家用电器' '电子' '轻工制造' '电气设备'
    # '农林牧渔' '计算机' '纺织服装' '有色金属' '采掘' '建筑材料'
    # 登陆系统
    lg = bs.login()
    # 显示登陆返回信息
    print('login respond error_code:'+lg.error_code)
    print('login respond  error_msg:'+lg.error_msg)

    # hangye = '房地产'
    # 获取行业分类数据
    rs = bs.query_stock_industry()#所有数据
    # rs = bs.query_stock_basic(code_name="浦发银行")#按照股票名称选择
    print('query_stock_industry error_code:'+rs.error_code)
    print('query_stock_industry respond  error_msg:'+rs.error_msg)

    # 打印结果集
    industry_list = []
    while (rs.error_code == '0') & rs.next():
        # 获取一条记录，将记录合并在一起
        industry_list.append(rs.get_row_data())
    result = pd.DataFrame(industry_list, columns=rs.fields)
    hy = result.industry.unique()
    print(hy)
    result = result[result.industry == hangye]
    # 结果集输出到csv文件
    # result.to_csv("D:/stock_industry.csv", encoding="gbk", index=False)
    # print(result)
    # 登出系统
    bs.logout()
    return result

def get_allday_allstock():
    lg = bs.login()
    # 显示登陆返回信息
    print('login respond error_code:'+lg.error_code)
    print('login respond  error_msg:'+lg.error_msg)
    rs = bs.query_all_stock(day='2022-11-10')
    #### 打印结果集 ####
    data_list = []
    while (rs.error_code == '0') & rs.next():
        temp = (rs.get_row_data())
    # result = pd.DataFrame(data_list, columns=rs.fields)
        # print(temp[0])
        new_rs = bs.query_history_k_data_plus(temp[0], "date,code,open,high,low,close,preclose,volume,amount,adjustflag,turn,tradestatus,pctChg,isST",
                                            start_date='2021-03-15', end_date='2021-03-16',frequency="d", adjustflag="3")
    # data_box = list()
        while (new_rs.error_code == '0') & new_rs.next():
            data_list.append(new_rs.get_row_data())
    res_all = pd.DataFrame(data_list, columns=new_rs.fields)
    bs.logout()
    return res_all

