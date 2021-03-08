import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
xmind_name="dubbo"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("dubbo_集群容错")
r2=s2.getRootTopic()
r2.setTitle("dubbo_集群容错")


content={

'集群容错':[
    '涉及到 Cluster，Directory，Router，LoadBalance 几个核心组件',
    '通过 Cluster 容错机制，Directory 获取 Invoker 列表，Router 找到路由信息，再使用 LoadBalance 知道具体服务',
    {'过程':[
        '1.生成 Invoker 对象。根据 Cluster 实现的不同，生成不同类型的 ClusterInvoker 对象。通过 ClusertInvoker 中的 Invoker 方法启动调用流程',
        '2.获取可调用的服务列表，可以通过 Directory 的 List 方法获取。这里有两类服务列表的获取方式',
        '3.在 Directory 获取所有 Invoker 列表之后，会调用路由接口（Router）。其会根据用户配置的不同策略对 Invoker 列表进行过滤，只返回符合规则的 Invoker',
        '4.Invoker 需要调用最终的服务，但是服务有可能分布在不同的节点上面。所以，需要经过 LoadBalance',
        '5.最后进行 RPC 调用。如果调用出现异常，针对不同的异常提供不同的容错策略'
    ]}
]
}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 