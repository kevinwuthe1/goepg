#encoding=utf8

import sys
import pandas

type=sys.getfilesystemencoding()
num = input('请输入频道序号:'.decode('utf-8').encode(type))
if num == 1 :
     print "正在获取卡通频道节目表".decode('utf-8').encode(type)
     df = pandas.read_html('http://www.niotv.com/i_index.php?cont=day&grp_id=8&sch_id=65&way=outter')
     df2 = df[2][:-1]
     df2.columns = df2.iloc[0]
     df3 = df2[1:]
     df4 = df3.dropna(axis=1, how="all")
     df5 = df4.fillna(value='')
     print df5
elif num == 2 :
     print "正在获取卫视合家欢节目表".decode('utf-8').encode(type)
     df = pandas.read_html('http://www.niotv.com/i_index.php?cont=day&grp_id=4&sch_id=28&way=outter')
     df2 = df[2][:-1]
     df2.columns = df2.iloc[0]
     df3 = df2[1:]
     df4 = df3.dropna(axis=1, how="all")
     df5 = df4.fillna(value='')
     print df5
else :
     print "暂无相应的电视节目单".decode('utf-8').encode(type)