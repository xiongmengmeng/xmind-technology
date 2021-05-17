import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
xmind_name="dubbo"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("注册中心1")
r2=s2.getRootTopic()
r2.setTitle("注册中心1")


content={
'实现了分布式环境中各服务之间的注册与发现， 是各个分布式节点之间的纽带':[],
'主要作用':[
    '动态加入:服务提供者通过注册中心，把自己暴露给消费者，无须消费者逐个更新配置文件',
    '动态发现:消费者动态感知新的配置，路由规则和新的服务提供者',
    '动态调整:支持参数的动态调整，新参数自动更新到所有服务节',
    '统一配置:统一连接到注册中心的服务配置'
],
'调用流程':[
    '1.提供者（Provider）启动时，会向注册中心写入自己的元数据信息（调用方式）, 同时订阅配置元数据信息',
    '2.消费者（Consumer）启动时，也会在注册中心写入自己的元数据信息，并且订阅服务提供者，路由和配置元数据的信息',
    '3.服务治理中心（duubo-admin）启动时，会同时订阅所有消费者，提供者，路由和配置元数据的信息',
    '4.当提供者离开或者新提供者加入时，注册中心发现变化会通知消费者和服务治理中心',
    '5.消费方发起服务调用时,异步将调用、统计信息等上报给监控中心（dubbo-monitor・simpl）'
],
'工作原理':[
    'Dubbo 有四种注册中心的实现，分别是 ZooKeeper，Redis，Simple 和 Multicast',
    {'源码模块dubbo-registry,主要内容':[
        'dubbo-registry-api:注册中心的所有API和抽象实现类',
        'dubbo-registry-zookeeper:使用ZooKeeper作为注册中心的实现'
    ]},
    {'ZooKeeper':[
        '树形结构的注册中心',
        {'四种节点类型':[
            '持久节点：服务注册后保证节点不丢失，注册中心重启也会存在',
            '持久顺序节点：在持久节点特性基础上增加了节点先后顺序的能力',
            '临时节点：服务注册后连接丢失或session超时，注册的节点会自动被移除',
            '临时顺序节点：在临时节点特性的基础上增加了节点先后顺序的能力'
        ]},
        'Dubbo使用ZooKeeper作为注册中心，只创建持久节点和临时节点',
        {'树形结构':[
            'Root--根节点:注册中心分组，值来自配置<dubbo:registry>的group 属性，默认是/dubbo',
            'Service--接口名称：服务接口',
            {'Type--四种服务':[
                '通过树形文件存储的ZNode在 /dubbo/Service 目录下面建立了四个目录',
                'Providers 目录下面，存放服务提供者 URL 和元数据',
                'Consumers 目录下面，存放消费者的 URL 和元数据',
                'Routers 目录下面，存放消费者的路由策略',
                'Configurators 目录下面，存放多个用于服务提供者动态配置 URL 元数据信息'
            ]},
            'URL--具体的Dubbo服务URL：URL元数据信息'
        ]},
        {'过程':[
            '客户端第一次连接注册中心时，会获取全量的服务元数据，包括服务提供者和服务消费者以及路由和配置的信息',
            '根据ZooKeeper客户端特性，在对应ZNode目录上注册一个Watcher，同时让客户端和注册中心保持TCP长连接',
            '如服务的元数据信息发生变化，客户端会接受到变更通知，然后去注册中心更新元数据信息。变更时根据ZNode节点中版本变化进行',
        ]}
    ]}
]
}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 