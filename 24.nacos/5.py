import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="Sentinel"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("Nacos")
r2=s2.getRootTopic()
r2.setTitle("Nacos")


content={
'作用':[
    '动态服务发现',
    '服务配置',
    '服务元数据及流量管理'
],
'架构':[
    {'NamingService':[
        '命名服务，注册中心核心接口'
    ]},
    {'ConfigService':[
        '配置服务，配置中心核心接口'
    ]}
],
'注册中心':[
    {'注册表':[
        'mysql存储',
        'server-register',
    ]},
    {'过程':[
        '1.A,B服务启动时，调用注册接囗，执行insert,并且定时发送心跳给注册中心',
        '2.A服务定时拉取B服务列表，缓存到本地',
        '3.A服务根据2过程获取结果，选择一个服务进行远程调用'
    ]},
    {'核心功能':[
        {'服务注册':[
            'Nacos Client会通过发送REST请求的方式向Nacos Server注册自己的服务',
            '提供自身的元数据，比如ip地址、端口等信息',
            'Nacos Server接收到注册请求后，就会把这些元数据信息存储在一个双层的内存Map中'
        ]},
        {'服务心跳':[
            '服务注册后，Nacos Client会维护一个定时心跳来持续通知Nacos Server',
            '说明服务一直处于可用状态，防止被剔除',
            '默认5s发送一次心跳'
        ]},
        {'服务同步':[
            'Nacos Server集群之间会互相同步服务实例，用来保证服务信息的一致性'
        ]},
        {'服务发现':[
            '服务消费者（Nacos Client）在调用服务提供者的服务时，会发送一个REST请求给Nacos Server',
            '获取上面注册的服务清单，并且缓存在Nacos Client本地',
            '同时在NacosClient本地开启一个定时任务定时拉取服务端最新的注册表信息更新到本地缓存'
        ]},
        {'服务健康检查':[
            'Nacos Server会开启一个定时任务用来检查注册服务实例的健康情况',
            '对于超过15s没有收到客户端心跳的实例会将它的healthy属性置为false',
            '如某个实例超过30秒没有收到心跳，直接剔除该实例(被剔除的实例如果恢复发送心跳则会重新注册'
        ]},
    ]},
    {'使用':[
        '属性文件：配置项',
        'RestTemplate进行服务调用：可使用微服务名称（spring.application.name）'
    ]}
]


}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 