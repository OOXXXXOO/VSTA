import os
import tushare as ts
import datetime
import pandas_datareader.data as web
import pymysql
import numpy as np

token="b490dcba8a78ab9106ccc6ac1544d7160786cb282c8feb92ae3c6039"

stock_key={
    "ts_code":"TS代码",
    "symbol":"股票代码",
    "name":"股票名称",
    "area":"所在地域",
    "industry":"所属行业",
    "fullname":"股票全称",
    "enname":"英文全称",
    "market":"市场类型 主板/中小板/创业板/科创板",
    "exchange":"交易所代码",
    "curr_type":"交易货币",
    "list_status":"	上市状态：L上市 D退市 P暂停上市",
    "list_date":"上市日期",
    "delist_date":"退市日期",
    "is_hs":"沪市还是深市"
}


class market():
    """
    抽象市场概念
    """
    def __init__(self):

        print("# ---------------------------------------------------------------------------- #")
        print("#                                Market Toolkit                                #")
        print("# ---------------------------------------------------------------------------- #")

        # Tushare API for chinese market
        ts.set_token(token)
        self.china_market=ts.pro_api()
        self.field_support_list=np.array(list(stock_key.keys()))
        self.customfield=self.field_support_list
        # Yahoo API for global market








    def set_field(self,fields):
        """
        you just need set fields like [0,1,2,3,4,5,6,7,8] that could index to field
            0 ->    "ts_code":"TS代码",
            1 ->    "symbol":"股票代码",
            2 ->    "name":"股票名称",
            3 ->    "industry":"所属行业",
            4 ->    "fullname":"股票全称",
            5 ->    "enname":"英文全称",
            6 ->    "market":"市场类型 主板/中小板/创业板/科创板",
            7 ->    "exchange":"交易所代码",
            8 ->    "curr_type":"交易货币",
            9 ->    "list_status":"	上市状态：L上市 D退市 P暂停上市",
            10 ->   "list_date":"上市日期",
            11 ->   "delist_date":"退市日期",
            12 ->   "is_hs":"沪市还是深市"
        """
        self.customfield=np.array(self.field_support_list[fields])




    def sector(self,keys:list)->list:
        sectors=[]
        for key in keys:
            keysector=self.market_list[(self.market_list["industry"]==key)]
            print("# ===== Sector ",key)
            print(keysector)
            sectors.append({
                key:keysector
            })
        return sectors






    def list(self):
        fields=""
        for index,field in enumerate(self.customfield):
            if index<len(self.customfield)-1:
                fields+=field+","
            else:
                fields+=field
        print("# ===== fields str:",fields)
        self.market_list = self.china_market.stock_basic(exchange='', list_status='L', fields=fields)
        print(self.market_list)

         
"""
STOCK:

1.股票类
2.账户类
3.抽象类



"""

class stock():
    """
    抽象股票概念
    包含单只股票所有的=信息
    """
    def __init__(self,code):
        self.code=code
        self.now=datetime.datetime.now()
        self.filed=[]
    def filed(self,field):
        pass
        # if isinstance(field,list):

    def history(self,type="daily"):
        """
        type:
        daily
        weekly
        monthly
        """
        

    def __call__(self):
        pass


class stock_trade(stock):
    """
    抽象股票的管理概念
    """
    def __init__(self):
        """
        """



def main():
    m=market()
    m.set_field([0,1,3,4,5])
    m.list()
    m.sector(["银行"])




if __name__ == '__main__':
    main()
    