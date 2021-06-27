import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="Sentinel"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("Ribbon")
r2=s2.getRootTopic()
r2.setTitle("Ribbon")


content={
'主流的负载方案':[
     {'集中式负载均衡':[
        '在服务器端再进行负载均衡算法分配，如Nginx',
        '先发送请求',
        '然后通过负载均衡算法',
        '在多个服务器之间选择一个进行访问'
    ]},
    {'客户端做负载均衡':[
        'Ribbon/Dubbo中的loadbalance',
    ]},
],
'Spring Cloud Ribbon':[
    '一套客户端的负载均衡工具',
    {'过程':[
        '客户端会有一个服务器地址列表',
        '在发送请求前通过负载均衡算法选择一个服务器',
        '然后进行访问'
    ]}
],
'常见负载均衡算法':[
    {'随机':[
        '加权随机'
    ]},
    {'轮询':[
        '加权轮询，平滑加权轮询'
    ]},
    {'最小活跃数':[
        ''
    ]},
    {'hash算法':[
        ''
    ]},
],
'模块':[
    {'ribbon-loadbalancer':[
        '负载均衡模块，可独立使用，也可以和别的模块一起使用'
    ]},
    {'Ribbon':[
        '内置的负载均衡算法都实现在其中'
    ]},
    {'ribbon-eureka':[
        '基于Eureka封装的模块，能够快速、方便地集成Eurek',
    ]},
    {'ribbon-transport':[
        '基于Netty实现多协议的支持，比如 HTTP、Tcp、Udp等',
    ]},
    {'ribbon-httpclient':[
        '基于Apache HttpClient封装的REST客户端',
        '集成了负载均衡模块，可以直接在项目中使用来调用接口'
    ]},
    {'ribbon-example':[
        'Ribbon 使用代码示例'
    ]},
    {'ribbon-core':[
        '一些比较核心且具有通用性的代码，客户端API的一些配置和其他API的定义'
    ]}
],
'使用':[
    '可单独使用'
    {'整合Spring Cloud':[
        {'1.引入依赖':[
            'spring‐cloud‐starter‐netflix‐ribbon',
            '注：nacos-discovery依赖了ribbon，可以不用再引入ribbon依赖'
        ]},
        {'2.添加@LoadBalanced注解':[
            '在RestTemplate上'
        ]}
    ]},
],
'内核原理':[
    {'@LoadBalanced 注解原理':[
        '@LoadBalanced利用@Qualifier作为restTemplates注入的筛选条件，筛选出具有负载均衡标识的RestTemplate',
        '被@LoadBalanced注解的restTemplate会被定制，添加LoadBalancerInterceptor拦截器'
    ]},
    {'相关接口':[
        'RibbonClientConfiguration',
        {'IClientConfig':[
            'Ribbon的客户端配置，默认采用DefaultClientConfigImpl实现'
        ]},
        {'IRule':[
            'Ribbon的负载均衡策略，默认采用ZoneAvoidanceRule实现',
            '该策略能够在多区域环境下选出最佳区域的实例进行访问'
        ]},
        {'IPing':[
            'Ribbon的实例检查策略，默认采用DummyPing实现，该检查策略是一个特殊的实现',
            '实际上它并不会检查实例是否可用，而是始终返回true，默认认为所有服务实例都是可用的'
        ]},
        {'ServerList':[
            '服务实例清单的维护机制，默认采用ConfigurationBasedServerList实现'
        ]},
        {'ServerListFilter':[
            '服务实例清单过滤机制，默认采ZonePreferenceServerListFilter',
            '该策略能够优先过滤出与请求方处于同区域的服务实例'
        ]},
        {'ILoadBalancer':[
            '负载均衡器，默认采用ZoneAwareLoadBalancer实现，它具备了区域感知的能力'
        ]}
    ]}
],
'负载均衡策略':[
    {'1.RandomRule':[
        '随机选择一个Server'
    ]},
    {'2.RetryRule':[
        '对选定的负载均衡策略机加上重试机制',
        '在一个配置时间段内当选择Server不成功，尝试使用subRule方式选择一个可用的server'
    ]},
    {'3.RoundRobinRule':[
        '轮询选择， 轮询index，选择index对应位置的Server'
    ]},
    {'4.AvailabilityFilteringRule':[
        '过滤掉一直连接失败的被标记为circuit tripped的后端Server',
        '并过滤掉那些高并发的后端Server或者使用一个AvailabilityPredicate来包含过滤server的逻辑',
        '其实就是检查status里记录的各个Server的运行状态'
    ]},
    {'5. BestAvailableRule':[
        '选择一个最小的并发请求的Server，逐个考察Server',
        '如果Server被tripped了，则跳过'
    ]},
    {'6.WeightedResponseTimeRule':[
        '根据响应时间加权，响应时间越长，权重越小，被选中的可能性越低'
    ]},
    {'7.ZoneAvoidanceRule':[
        '默认的负载均衡策略，即复合判断Server所在区域的性能和Server的可用性选择Server',
        '在没有区域的环境下，类似于轮询(RandomRule)'
    ]},
    {'8.NacosRule':[
        '同集群优先调用'
    ]} 
],
'修改默认负载均衡策略':[
    {'全局配置':[
        '调用其他微服务，一律使用指定的负载均衡算法',
        '修改application.yml'
    ]},
    {'局部配置':[
        '调用指定微服务提供的服务时，使用对应的负载均衡算法',
        '修改application.yml'
    ]}
],
'自定义负载均衡策略':[
    '继承AbstractLoadBalancerRuler类，重写choose()方法'
],
'饥饿加载':[
    'Ribbon默认懒加载，意味着只有在发起调用的时候才会创建客户端',
    '在进行服务调用的时候，如果网络情况不好，第一次调用会超时',
    {'开启饥饿加载，解决第一次调用慢的问题':[
        'ribbon:eager‐load:enabled: true'
    ]}
]

}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 