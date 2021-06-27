import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="Sentinel"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("Sentinel")
r2=s2.getRootTopic()
r2.setTitle("Sentinel")


content={
'服务雪崩问题解决':[
    {'超时机制':[
        '提供者的服务一旦超时，就释放资源',
    ]},
    {'服务限流(资源隔离)':[
        '限制请求核心服务提供者的流量，使大流量拦截在核心服务之外',
        '资源隔离：通过线程池+队列的方式，通过信号量的方式'
    ]},
    {'服务熔断':[
        '远程服务不稳定或网络抖动时暂时关闭'
    ]},
    {'服务降级':[
        '是当某个服务熔断之后，服务将不再被调用',
        '此时客户端可以自己准备一个本地的fallback（回退）回调，返回一个缺省值'
    ]}
],
'Sentinel':[
    '面向分布式服务架构的流量控制组件',
    {'特征':[
        '丰富的应用场景',
        '完备的实时监控',
        '广泛的开源生态',
        {'完善的SPI扩展点­':[
            '通过实现扩展点，快速的定制逻辑，如定制规则管理、适配数据源等'
        ]},
    ]}
],
'Sentinel控制台':[
    {'功能':[
        {'查看机器列表以及健康情况':[
            '收集Sentinel客户端发送的心跳包，判断机器是否在线',
        ]},
        {'监控 (单机和集群聚合)':[
            '通过Sentinel客户端暴露的监控API',
            '定期拉取并且聚合应用监控信息，最终可实现秒级的实时监控'
        ]},
        {'规则管理和推送':[
            '统一管理推送规则'
        ]},
        '鉴权'
    ]},
    {'1.实时监控':[
        '监控接口的通过的QPS和拒绝的QPS'
    ]},
    {'2.簇点链路':[
        '显示微服务的所监控的API'
    ]},
    {'3.流控规则':[
    ]},
    {'4.降级规则':[
    ]},
    {'5.热点参数限流':[
        '统计传入参数中的热点参数，对含热点参数的资源调用进行限流',
        {'注':[
            '1.热点规则需使用@SentinelResource("resourceName")注解，否则不生效',
            '2.参数必须是7种基本数据类型'
        ]}
    ]},
    {'6.授权控制规则':[
        '黑白名单控制',
        {'配置项':[
            {'resource':[
                '资源名'
            ]},
            {'limitApp':[
                '对应的黑名单/白名单，不同origin用,分隔，如appA,appB'
            ]},
            {'strategy':[
                '限制模式',
                'AUTHORITY_WHITE 为白名单模式(默认)',
                'AUTHORITY_BLACK 为黑名单模式'
            ]}
        ]},
        {'实现':[
            '实现RequestOriginParser接口',
            '在parseOrigin方法中区分来源，并交给spring管理'
        ]}
    ]}
],

}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 