import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="java"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("分布式事务")
r2=s2.getRootTopic()
r2.setTitle("分布式事务")


content={
'分布式事务':[
    '为了保证不同数据库的数据一致性',
    {'过程':[
        '1.	基于XA协议的两阶段提交',
        '2.	消息事务+最终一致性',
        '3.	TCC编程模式'
    ]}
],
'分布式事务解决方案':[
    'https://www.jianshu.com/p/16b5900bb484'
]

}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 