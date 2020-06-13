
# 数据IO部分


## 互联网数据

1，输入
    * 时间范围
    * 股票代码
    * 时间间隔
    enum{
        1:分钟
        2:小时
        3:天
        4:月
    }
2.输出
    * 依照时间间隔返回相应的k线数据
    数据格式待确认





## 数据库部分




### python库  
pymysql


### mysql 

name:表名，pandas会自动创建表结构
con：数据库连接，最好是用sqlalchemy创建engine的方式来替代con
flavor:数据库类型 {‘sqlite’, ‘mysql’}, 默认‘sqlite’，如果是engine此项可忽略
schema:指定数据库的schema，默认即可
if_exists:如果表名已存在的处理方式 {‘fail’, ‘replace’, ‘append’},默认‘fail’
index:将pandas的Index作为一列存入数据库，默认是True
index_label:Index的列名
chunksize:分批存入数据库，默认是None，即一次性全部写人数据库
dtype:设定columns在数据库里的数据类型，默认是None


### 矢量存续 
mbtiles（GDAL）







# 数据统计部分

