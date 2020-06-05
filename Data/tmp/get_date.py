#!/usr/bin/env python
#coding:utf-8


import pymysql
import tushare as ts
import re
import datetime
import requests
import io

import pymysql.cursors
import pymysql
import pandas as pd
import numpy as np




# token='b490dcba8a78ab9106ccc6ac1544d7160786cb282c8feb92ae3c6039'
#
# ts.set_token(token)
#
# pro=ts.pro_api()

class data_collect(object):

    def __init__(self):
        ans = self.collectDATA()

    def collectDATA(self):
        # 建立数据库连接，获取日线基础行情(开盘价，收盘价，最高价，最低价，成交量，成交额)
        db = pymysql.connect(host='127.0.0.1', user='root', passwd='localhost', db='stock', charset='utf8')
        cursor = db.cursor()
        try:
            with db.cursor() as cursor:
                sql = "select * from stock_name_all"
                cursor.execute(sql)
                done_set = cursor.fetchall()

        finally:
            db.close();
        #     'ts_code','symbol','name','area','industry','market','list_date','is_hs'

        if len(done_set) == 0:
            raise Exception
        self.ts_code = []
        self.symbol = []
        self.name = []
        self.area = []
        self.industry = []
        self.market = []
        self.list_date = []
        self.is_hs = []
        for i in range(len(done_set)):
            self.ts_code.append(done_set[i][0])
            self.symbol.append(done_set[i][1])
            self.name.append(done_set[i][2])
            self.area.append(done_set[i][3])
            self.industry.append(done_set[i][4])
            self.market.append(done_set[i][4])
            self.list_date.append(done_set[i][6])
            self.is_hs.append(done_set[i][7])
        cursor.close()
        print("self.ts_code",self.ts_code)
        # # db.close()
        # # 将日线行情整合为训练集(其中self.train是输入集，self.target是输出集，self.test_case是end_dt那天的单条测试输入)
        # self.data_train = []
        # self.data_target = []
        # self.data_target_onehot = []
        # self.cnt_pos = 0
        # self.test_case = []
        #
        # for i in range(1,len(self.close_list)):
        #     train = [self.open_list[i-1],self.close_list[i-1],self.high_list[i-1],self.low_list[i-1],self.vol_list[i-1],self.amount_list[i-1]]
        #     self.data_train.append(np.array(train))
        #
        #     if self.close_list[i]/self.close_list[i-1] > 1.0:
        #         self.data_target.append(float(1.00))
        #         self.data_target_onehot.append([1,0,0])
        #     else:
        #         self.data_target.append(float(0.00))
        #         self.data_target_onehot.append([0,1,0])
        # self.cnt_pos =len([x for x in self.data_target if x == 1.00])
        # self.test_case = np.array([self.open_list[-1],self.close_list[-1],self.high_list[-1],self.low_list[-1],self.vol_list[-1],self.amount_list[-1]])
        # self.data_train = np.array(self.data_train)
        # self.data_target = np.array(self.data_target)
        return 1



# # 创建连接
# db = pymysql.connect(host='127.0.0.1', user='root', passwd='localhost', db='stock', charset='utf8')
# cursor = db.cursor()
# # 执行sql语句
# try:
#     with db.cursor() as cursor:
#         sql = "select * from stock_name_all"
#         cursor.execute(sql)
#         result = cursor.fetchall()
#
# finally:
#     db.close();
# print("result\n",result)
#
# df1 = np.array(result)
# print("df1:",df1)
# df = pd.DataFrame(df1,columns=['ts_code','symbol','name','area','industry','market','list_date','is_hs'])  # 转换成DataFrame格式  ,columns=['ts_code,symbol,name,area,industry,market,list_date,is_hs']
# print("df",df)
# data_ts_code=df.get('ts_code')
# print("data_ts_code:")
# print(data_ts_code)
#
#
#
