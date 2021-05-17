import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
xmind_name="dubbo"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("集群容错")
r2=s2.getRootTopic()
r2.setTitle("集群容错")


content={
'核心组件':[
    {'Cluster':[
        'Cluster 容错机制'
    ]},
    {'Directory':[
        '获取 Invoker 列表'
    ]},
    {'Router':[
        '找到路由信息'
    ]},
    {'LoadBalance':[
        '知道具体服务'
    ]}
],
'Cluster的总体工作流程':[
    {'1.生成Invoker对象':[
        '1.1.不同的Cluster实现会生成不同类型的Clusterinvoker对象并返回',
        '1.2.调用Clusterinvoker的Invoker方法，开始正式调用流程'
    ]},
    {'2.获得可调用的服务列表':[
        '通过Directory#list方法获取所有可用的服务列表',
        '调用路由Router接口,根据路由规则过滤一服务,返回符合规则的Invoker'
    ]},
    {'3.做负载均衡':[
        '通过LoadBalance选择一个提供服务的节点'
    ]},
    {'4.做RPC调用':[
        '对于异常情况，使用容错策略做处理'
    ]}
],
'容错的接口':[
    {'分类':[
        'Cluster类',
        'Clusterinvoker类'
    ]},
    {'关系':[
        'Cluster接口下面有多种不同的实现',
        '每种实现中都需要实现接口的join方法，在方法中会“new”一个对应的Clusterinvoker实现'
    ]}
],
'容错Cluster':[
    '容错+串联起获取服务列表、路由、负载均衡等整个流程'
    '一共有9种不同的实现，每种实现分别对应不同的Clusterlnvoke',
    {'FailoverCluster':[
        '失败自动切换(默认)',
        '自动重试其它服务器,用户可以通过retries=n设置重试次数',
        {'适应场景':[
            '读操作或幕等的写操作上'
        ]},
        {'问题':[
            '重试会导致接口的延退增大',
            '在下游机器负载已经达到极限时，重试容易加重下游服务的负载'
        ]},
        'FailoverClusterInvoker#doInvoke'
    ]},
    {'FailfastCluster':[
        '快速失败',
        '当请求失败后，快速返回异常结果，不做任何重试'
    ]},
    {'FailsafeCluster':[
        '失败安全',
        '出现异常，直接忽略',
        {'适应场景':[
            '日志或监控'
        ]},
    ]},
    {'FailbackCluster':[
        '失败自动恢复',
        '记录失败请求，定时重发'
    ]},
    {'ForkingCluster':[
        '并行调用多个服务器，只要一个成功即返回',
    ]},
    {'BroadcastCluster':[
        '广播逐个调用所有提供者，任意一个报错则报错',
    ]},
    {'Mock':[
        '调用失败时，返回伪造的响应结果',
        '或直接强制返回伪造的结果，不会发起远程调用'
    ]},
    {'Available':[
        '不做负载均衡',
        '遍历所有服务列表，找到第一个可用节点，直接请求并返回结果'
    ]},
    {'Mergeable':[
        '把多个节点请求得到的结果进行合并'
    ]}
],
}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 