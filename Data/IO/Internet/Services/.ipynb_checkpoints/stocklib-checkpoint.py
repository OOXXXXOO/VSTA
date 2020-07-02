import tushare as ts
import datetime

import pymysql
# import get_date
import pandas_datareader.data as web

import os

"""
        tushare Sources:
        
        SZ
        SH

        3851
        

        Dataloader Sources:

            Tiingo
            IEX
            Alpha Vantage https://www.alphavantage.co/documentation/
            Enigma
            Quandl
            St.Louis FED (FRED)
            Kenneth French’s data library
            World Bank
            OECD
            Eurostat
            Thrift Savings Plan
            Nasdaq Trader symbol definitions
            Stooq
            MOEX

        设计:
        1.数据获取部分
        tushare获取国内a股数据
        以上dataloader获取国际数据
        需要逐个将key添加到环境变量中去
        需要bash化

        将以上市场的数据做检视功能


        2.需要将不同的数据转换为统一的dataframe格式从而绘制固定的seaborn
        从而将数据可视化

        3.行为部分
        设立买卖概念,
        设立账户概念,
        建立现金,
        备选股票池,
        购入股票池,

        4.统计与绘图部分
        
        







"""

class STOCK():
    def __init__(self):
        ts.set_token("b490dcba8a78ab9106ccc6ac1544d7160786cb282c8feb92ae3c6039")
        self.pro=ts.pro_api()
        print("# ---------------------------------------------------------------------------- #")
        print("#                             STOCK PROCESS Toolkit                            #")
        print("# ---------------------------------------------------------------------------- #")
        self.stock_pool=[]
    def add(self,stock_code):

        print("# ===== Add Stock |{stock}|to the stock pool".format(stock=stock_code))


    def show_china(self):
        data = self.pro.stock_basic(exchange='', list_status='L', fields='ts_code,symbol,name,area,industry,list_date')
        print(data)

    def get(self):
        """
        av-intraday - Intraday Time Series
        av-daily - Daily Time Series
        av-daily-adjusted - Daily Time Series (Adjusted)
        av-weekly - Weekly Time Series
        av-weekly-adjusted - Weekly Time Series (Adjusted)
        av-monthly - Monthly Time Series
        av-monthly-adjusted -
        """

        f = web.DataReader("AAPL", "av-daily", start=datetime(2017, 2, 9),end=datetime(2017, 5, 24),api_key=os.getenv('ALPHAVANTAGE_API_KEY'))
        # print(f)



def main():
    s=STOCK()
    s.show_china()

if __name__ == '__main__':
    main()
    