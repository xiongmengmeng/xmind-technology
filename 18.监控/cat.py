import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="cat"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("cat")
r2=s2.getRootTopic()
r2.setTitle("cat")


content={
'简介':[
    '实时和接近全量的监控系统，它侧重于对Java应用的监控',
    '能与Spring、MyBatis、Dubbo 等框架以及Log4j 等结合'
],
'核心模块':[
    {'Transaction':[
        '记录一段代码响应时间',
        'URL/SQL响应时间'
    ]},
    {'Even':[
        '记录一段代码执行次数',
        '如Exception出现次数'
    ]},
    {'Heartbeat':[
        '定期执行某些代码',
        '分钟粒度Cpu,IO',
        '无需其他配置'
    ]},
    {'Metric':[
        '一个指标的变化值',
        '可监控销售额'
    ]},
    {'Problem':[
        '记录整个项目在运行过程中出现的问题，包括一些错误、访问较长的行为',
        '根据Transaction\Event数据分析出来系统可能出现的异常'
    ]}
],
'学习':[
    'https://www.jianshu.com/p/cefd4015a07c',
    'https://blog.csdn.net/caohao0591/article/details/80693289',
    'https://blog.csdn.net/lemon89/article/details/71171146'
]

}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 