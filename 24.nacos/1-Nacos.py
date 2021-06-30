import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="Sentinel"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("Spring Cloud")
r2=s2.getRootTopic()
r2.setTitle("Spring Cloud")


content={
'Spring Cloud微服务技术栈':[
    '一套微服务解决方案',
],
'Spring Cloud Alibaba包含组件':[
    {'Nacos':[
        '动态服务发现、配置管理和服务管理平台'
    ]},
    {'Sentinel':[
        '把流量作为切入点，从流量控制、熔断降级、系统负载保护等多个维度保护服务的稳定性'
    ]},
    {'RocketMQ':[
        '开源的分布式消息系统',
        '基于高可用分布式集群技术，提供低延时的、高可靠的消息发布与订阅服务'
    ]},
    {'Dubbo':[
        '一款高性能Java RPC框架',
    ]},
    {'Seata':[
        '易于使用的高性能微服务分布式事务解决方案'
    ]},
    {'Arthas':[
        '开源的Java动态追踪工具，基于字节码增强技术，功能非常强大'
    ]}
]

}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 