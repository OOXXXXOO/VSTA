import os
import tushare as ts
import datetime
import pandas_datareader.data as web
import pymysql




class stock:
    """
    抽象股票概念
    包含单只股票所有的=信息
    """
    def __init__(self,code):
        ts.set_token("b490dcba8a78ab9106ccc6ac1544d7160786cb282c8feb92ae3c6039")
        self.pro=ts.pro_api()
        self.code=code
        self.now=datetime.datetime.now()
        self.filed=[]
    def filed(self,field):
        if isinstance(field,list):



    def __call__(self):


class stock_trade(stock):
    """
    抽象股票的管理概念
    """
    def __init__(self):
        """
        """



def main():
    A=




if __name__ == '__main__':
    main()
    