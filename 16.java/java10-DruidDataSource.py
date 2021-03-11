import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="java"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("DruidDataSource")
r2=s2.getRootTopic()
r2.setTitle("DruidDataSource")


content={
'简介':[
    '一个数据库连接池',
    '阿里巴巴开源的数据库连接池项目',
    '内置提供了一个功能强大的StatFilter插件，能够详细统计SQL的执行性能',
    '内置了一个监控页面，提供了非常完备的监控信息，可以快速诊断系统的瓶颈',
    '提供的Filter机制，很方便编写JDBC层的扩展插件'
],
'学习':[
    '参数学习：https://www.cnblogs.com/txsblog/p/7692458.html',
    '文档：https://www.bookstack.cn/read/Druid/2fa0c5cdf8a9e77e.md',
    '参数设置：https://www.jianshu.com/p/d7bff8249fd9'
]

}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 