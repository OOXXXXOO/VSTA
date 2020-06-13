from jqdatasdk import *
auth('13146420628','420628')
print("Login:",is_auth())
print("DataUse:",get_query_count())
#将所有股票列表转换成数组
stocks = list(get_all_securities(['stock']).index)

#获得所有指数列表
get_all_securities(['index'])

#获得所有基金列表
df = get_all_securities(['fund'])

#获取所有期货列表
get_all_securities(['futures'])

#获得etf基金列表
df = get_all_securities(['etf'])
#获得lof基金列表
df = get_all_securities(['lof'])
#获得分级A基金列表
df = get_all_securities(['fja'])
#获得分级B基金列表
df = get_all_securities(['fjb'])

#获得2015年10月10日还在上市的所有股票列表
get_all_securities(date='2015-10-10')
#获得2015年10月10日还在上市的 etf 和 lof 基金列表
get_all_securities(['etf', 'lof'], '2015-10-10')