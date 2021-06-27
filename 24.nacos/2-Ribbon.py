import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="nacos"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("Ribbon")
r2=s2.getRootTopic()
r2.setTitle("Ribbon")


content={
'主流的负载方案':[
     {'集中式负载均衡':[
        '在服务器端进行负载均衡，如Nginx',
    ]},
    {'客户端做负载均衡':[
        'Ribbon/Dubbo中的loadbalance',
    ]},
],
'Spring Cloud Ribbon':[
    '一套客户端的负载均衡工具',
    {'过程':[
        '客户端有一个服务器地址列表',
        '在发送请求前通过负载均衡算法选择一个服务器',
        '然后进行访问'
    ]}
],
'负载均衡算法':[
    {'随机':[
        '加权随机'
    ]},
    {'轮询':[
        '加权轮询，平滑加权轮询'
    ]},
    {'最小活跃数':[
    ]},
    {'hash算法':[
    ]},
],
'负载均衡策略':[
    {'1.RandomRule':[
        '随机'
    ]},
    {'2.RetryRule':[
        '选定的负载均衡策略+重试机制',
        '在一个配置时间段内当选择Server不成功，尝试subRule方式选择一个可用的server'
    ]},
    {'3.RoundRobinRule':[
        '轮询:轮询index，选择index对应位置的Server'
    ]},
    {'4.AvailabilityFilteringRule':[
        '过滤一直连接失败的被标记为circuit tripped的后端Server',
        '过滤高并发的后端Server',
        '或者使用一个AvailabilityPredicate来包含过滤server的逻辑',
        '本质:检查status里记录的各个Server的运行状态'
    ]},
    {'5.BestAvailableRule':[
        '最小活跃数',
        '如Server被tripped了，则跳过'
    ]},
    {'6.WeightedResponseTimeRule':[
        '根据响应时间加权，响应时间越长，权重越小，被选中可能性越低'
    ]},
    {'7.ZoneAvoidanceRule':[
        '默认',
        '根据Server所在区域的性能和Server的可用性选择Server',
        '没有区域的环境下，类似于轮询(RoundRobinRule)'
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
        '调用指定微服务，使用对应的负载均衡算法',
        '修改application.yml'
    ]}
],
'自定义负载均衡策略':[
    '继承AbstractLoadBalancerRuler类，重写choose()方法'
],

}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 