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
'应用发展':[
    {'单体应用':[
        'JEE时期->MVC框架时期'
    ]},
    {'分布式应用':[
        'SOA(Web Service和ESB)->微服务化->云原生'
    ]}
],
'Dubbo':[
    {'是什么':[
        '一款高性能、轻量级的开源JavaRPC框架',
        {'三大核心能力':[
            '1.面向接囗的远程方法调用',
            '2.智能容错和负载均衡',
            '3.服务自动注册和发现'
        ]}
    ]},
    {'功能':[
        '服务开发(RPC应用开发)',
        '服务软负载均衡',
        '服务依赖管理',
        '服务监控',
        '服务治理'
    ]},
    {'组件':[
        'Provider服务提供者',
        'Consumer服务消费者',
        'Registry注册中心',
        'Monitor监控中心'
    ]},
    {'特点':[
        {'1.连通性':[
            '注册中心，监控中心，可无',
            '服务消费端可直连'
        ]},
        {'2.健壮性':[
            '服务提供者无状态',
            '任一台宕机不影响使用',
            '全部宕机，无限重连'
        ]},
        {'3.伸缩性':[
            '动态增减注册中心，服务实例'
        ]},
        {'4.升级性':[
            ''
        ]},
    ]},
    {'核心设计原则':[
        '微内核+插件体系， 平等对待第三方'
    ]},
    '总体架构图',
    {'总体分层':[
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
        {'Remoting层':[
            'Exchange',
            'Transport',
            'Serialize'
        ]}
    ]},
]
}



#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 