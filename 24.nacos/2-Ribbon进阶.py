import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="nacos"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("Ribbon进阶")
r2=s2.getRootTopic()
r2.setTitle("Ribbon进阶")


content={
'模块':[
    {'ribbon-loadbalancer':[
        '负载均衡模块，可独立使用，也可和别的模块一起使用'
    ]},
    {'Ribbon':[
        '内置的负载均衡算法都在其中'
    ]},
    {'ribbon-eureka':[
        '基于Eureka封装的模块，能够快速、方便地集成Eurek',
    ]},
    {'ribbon-transport':[
        '基于Netty实现多协议的支持，如HTTP、Tcp、Udp等',
    ]},
    {'ribbon-httpclient':[
        '基于Apache HttpClient封装的REST客户端',
        '集成了负载均衡模块，可以直接在项目中使用来调用接口'
    ]},
    {'ribbon-example':[
        'Ribbon使用代码示例'
    ]},
    {'ribbon-core':[
        '一些比较核心且具有通用性的代码，客户端API的一些配置和其他API的定义'
    ]}
],
'使用':[
    '可单独使用',
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
    {'@LoadBalanced注解原理':[
        '利用@Qualifier作为restTemplates注入的筛选条件，筛选出具有负载均衡标识的RestTemplate',
        '被@LoadBalanced注解的restTemplate会被定制，添加LoadBalancerInterceptor拦截器'
    ]},
    {'相关接口':[
        'RibbonClientConfiguration',
        {'IClientConfig':[
            'Ribbon的客户端配置，默认DefaultClientConfigImpl实现'
        ]},
        {'IRule':[
            'Ribbon的负载均衡策略，默认ZoneAvoidanceRule实现',
            '该策略能够在多区域环境下选出最佳区域的实例进行访问'
        ]},
        {'IPing':[
            'Ribbon的实例检查策略，默认DummyPing实现',
            '实际上它不会检查实例是否可用，而是始终返回true，默认所有服务实例都可用'
        ]},
        {'ServerList':[
            '服务实例清单的维护机制，默认ConfigurationBasedServerList实现'
        ]},
        {'ServerListFilter':[
            '服务实例清单过滤机制，默认ZonePreferenceServerListFilter',
            '该策略能够优先过滤出与请求方处于同区域的服务实例'
        ]},
        {'ILoadBalancer':[
            '负载均衡器，默认ZoneAwareLoadBalancer实现，具备了区域感知的能力'
        ]}
    ]}
],
'饥饿加载':[
    {'Ribbon默认懒加载':[
        '只有在发起调的时才会创建客户端',
        '在进行服务调用时，如网络情况不好，第一次调用会超时'
    ]},
    {'开启饥饿加载，解决第一次调用慢的问题':[
        'ribbon:eager‐load:enabled: true'
    ]}
]

}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 