import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="internet"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("性能指标")
r2=s2.getRootTopic()
r2.setTitle("性能指标")


content={
'QPS':[
    'Queries Per Second:每秒请求数',
    '衡量信息检索系统（例如搜索引擎或数据库）在一秒钟内接收到的搜索流量'
],
'TPS':[
    'Transactions Per Second:每秒事务数',
    '事务数/秒。它是软件测试结果的测量单位',
    '一个事务:一个客户端向服务器发送请求然后服务器做出响应的过程',
    '客户端在发送请求时开始计时，收到服务器响应后结束计时，以此来计算使用的时间和完成的事务个数',
    {'QPS vs TPS':[
        '对于一个页面的一次访问，形成一个TPS',
        '一次页面请求，可能产生多次对服务器的请求,计入QPS',
        '如访问一个页面会请求服务器5次，一次访问，产生一个“T”，产生5个“Q”。'
    ]}
],
'RT':[
    'Response-time:响应时间',
    '执行一个请求从开始到最后收到响应数据所花费的总体时间',
    '即从客户端发起请求到收到服务器响应结果的时间'
],
'Concurrency':[
    '并发数:系统同时能处理的请求数量，反应系统的负载能力'
],
'吞吐量':[
    '系统的承压能力',
    '和处理对CPU的消耗、外部接口、IO等因素紧密关联',
    '单个处理请求对CPU消耗越高，外部系统接口、IO速度越慢，系统吞吐能力越低，反之越高',
    {'系统吞吐量有几个重要指标参数':[
        'QPS（TPS）',
        '并发数',
        '响应时间'
    ]}
],
'关系':[
    'QPS（TPS）= 并发数/平均响应时间',
    '并发数 = QPS*平均响应时间'
]
}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 