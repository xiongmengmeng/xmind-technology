import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
xmind_name="dubbo"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("概述")
r2=s2.getRootTopic()
r2.setTitle("概述")


content={
'概述':[
    '单体应用：JEE时期->MVC框架时期',
    '分布式应用：SOA(Web Service和ESB)->微服务化->云原生',
    {'Dubbo':[
        '核心设计原则： 微内核+插件体系， 平等对待第三方'
    ]},
    '总体架构图',
    {'总体分层：':[
        {'业务层(Biz)':[
            'Service'
        ]},
        {'RPC层':[
            'Config',
            'Proxy',
            'Registry',
            'Cluster',
            'Monitor',
            'Protocol'
        ]},
        {'Remoting':[
            'Exchange',
            'Transport',
            'Serialize'
        ]}
    ]},
    'Dubbo的一次总体调用的过程'
],
'分布式应用场景':[
    '高并发',
    '高可扩展',
    '高性能',
    '序列化/反序列化',
    '网络',
    '多线程',
    '设计模式的问题'
],
'Dubbo 分层':[
    '业务层',
    'RPC 层',
    'Remoting 层'
]
}



#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 