import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
xmind_name="dubbo"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("工作流")
r2=s2.getRootTopic()
r2.setTitle("工作流")


content={

'四个主体':[
    '服务提供者（Provider）',
    '注册中心（Registration）',
    '网络（Network）',
    '服务消费者（Consumer）'
],
'工作流':[
    '1.服务提供者在启动的时候，会通过读取一些配置将服务实例化',
    '2.Proxy 封装服务调用接口，方便调用者调用。客户端获取 Proxy 时，可以像调用本地服务一样，调用远程服务',
    '3.Proxy 在封装时，需要调用 Protocol 定义协议格式，例如：Dubbo Protocol',
    '4.将 Proxy 封装成 Invoker，它是真实服务调用的实例',
    '5.将 Invoker 转化成 Exporter，Exporter 只是把 Invoker 包装了一层，是为了在注册中心中暴露自己，方便消费者使用',
    '6.将包装好的 Exporter 注册到注册中心',
    '7.服务消费者建立好实例，会到服务注册中心订阅服务提供者的元数据。元数据包括服务 IP 和端口以及调用方式（Proxy）',
    '8.消费者会通过获取的 Proxy 进行调用。通过服务提供方包装过程可以知道，Proxy 实际包装了 Invoker 实体，因此需要使用 Invoker 进行调用',
    '9.在 Invoker 调用之前，通过 Directory 获取服务提供者的 Invoker 列表。在分布式的服务中有可能出现同一个服务，分布在不同的节点上',
    '10.通过路由规则了解，服务需要从哪些节点获取。',
    'Invoker 调用过程中，通过 Cluster 进行容错，如果遇到失败策略进行重试。',
    '调用中，由于多个服务可能会分布到不同的节点，就要通过 LoadBalance 来实现负载均衡。',
    'Invoker 调用之前还需要经过 Filter，它是一个过滤链，用来处理上下文，限流和计数的工作。',
    '生成过滤以后的 Invoker。',
    '用 Client 进行数据传输。',
    'Codec 会根据 Protocol 定义的协议，进行协议的构造。',
    '构造完成的数据，通过序列化 Serialization 传输给服务提供者。',
    'Request 已经到达了服务提供者，它会被分配到线程池（ThreadPool）中进行处理。',
    'Server 拿到请求以后查找对应的 Exporter（包含有 Invoker）。',
    '由于 Export 也会被 Filter 层层包裹',
    '通过 Filter 以后获得 Invoker',
    '最后，对服务提供者实体进行调用'
],
'注意':[
    'Proxy，Invoker，Exporter，Filter调用实体在不同阶段的不同表现形式',
    'Proxy 是用来方便调用者调用的',
    'Invoker 是在调用具体实体时使用的',
    'Exporter 用来注册到注册中心'
]

}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 