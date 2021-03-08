import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
xmind_name="dubbo_registry"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("dubbo_registry")
r2=s2.getRootTopic()
r2.setTitle("dubbo_registry")


content={
'分布式应用场景':[
    '高并发',
    '高可扩展',
    '高性能',
    '序列化/反序列化',
    '网络',
    '多线程',
    '设计模式的问题'
],
'Dubbo 分层':[
    '业务层',
    'RPC 层',
    'Remoting 层'
],
'Dubbo 调用工作流':[
    {'四个主体':[
        '服务提供者（Provider）',
        '注册中心（Registration）',
        '网络（Network）',
        '服务消费者（Consumer）'
    ]},
    {'工作流':[
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
    ]},
    {'注意':[
        'Proxy，Invoker，Exporter，Filter调用实体在不同阶段的不同表现形式',
        'Proxy 是用来方便调用者调用的',
        'Invoker 是在调用具体实体时使用的',
        'Exporter 用来注册到注册中心'
    ]}
],
'服务提供者':[
    {'暴露服务流程':[
        '1.会通过Config组件中的ServiceConfig读取服务的配置信息(有三种形式，XML文件，注解和属性文件)',
        '2.读取配置文件生成服务实体后，通过ProxyFactory将Proxy转换成Invoker',
        '3.Invoker被定义Protocol，之后会被包装成Exporter',
        '4.Exporter发送到注册中心，作为服务的注册信息',
        '实现：ServiceConfig中的doExport方法'
    ]},
    {'服务提供者暴露服务的七个步骤':[
        '1.读取其他配置信息到map中，用来后面构造URL',
        '2.读取全局配置信息',
        '3.配置不是remote，也就是暴露本地服务',
        '4.如果配置了监控地址，则服务调用信息会上报',
        '5.通过Proxy转化成Invoker，RegistryURL存放的是注册中心的地址',
        '6.暴露服务以后，向注册中心注册服务信息',
        '7.没有注册中心直接暴露服务'
    ]},
    {'注册中心暴露服务的五个步骤':[
        '1.委托具体协议进行服务暴露，创建NettyServer监听端口，并保持服务实例',
        '2.创建注册中心对象，创建对应的TCP连接',
        '3.注册元数据到注册中心',
        '4.订阅Configurators节点',
        '5.如果需要销毁服务，需要关闭端口，注销服务信息',
        '实现：RegistryProtocol中的Export方法'
    ]}
],
'服务消费者':[
    '服务消费者首先持有远程服务实例生成的 Invoker，然后把 Invoker 转换成用户接口的动态代理引用',
    {'消费者服务调用服务提供者':[
        '1.检查是否是同一个 JVM 内部引用',
        '2.如果是同一个 JVM 的引用，直接使用 injvm 协议从内存中获取实例',
        '3.注册中心地址后，添加 refer 存储服务消费元数据信息',
        '4.单注册中心消费',
        '5.依次获取注册中心的服务，并且添加到 Invokers 列表中',
        '6.通过 Cluster 将多个 Invoker 转换成一个 Invoker',
        '7.把 Invoker 转换成接口代理',
        '框架进行服务引用的入口,ReferenceBean 中的 getObject 方法',
    ]}
],
'注册中心':[
    {'作用':[
        '动态载入服务:服务提供者通过注册中心，把自己暴露给消费者，无须消费者逐个更新配置文件',
        '动态发现服务:消费者动态感知新的配置，路由规则和新的服务提供者',
        '参数动态调整:支持参数的动态调整，新参数自动更新到所有服务节点',
        '服务统一配置:统一连接到注册中心的服务配置'
    ]},
    {'注册中心调用的流程':[
        '提供者（Provider）启动时，会向注册中心写入自己的元数据信息（调用方式）',
        '消费者（Consumer）启动时，也会在注册中心写入自己的元数据信息，并且订阅服务提供者，路由和配置元数据的信息',
        '服务治理中心（duubo-admin）启动时，会同时订阅所有消费者，提供者，路由和配置元数据的信息',
        '当提供者离开或者新提供者加入时，注册中心发现变化会通知消费者和服务治理中心'
    ]},
    {'注册中心工作原理':[
        'Dubbo 有四种注册中心的实现，分别是 ZooKeeper，Redis，Simple 和 Multicast',
        {'ZooKeeper(协调服务式应用)':[
            '通过树形文件存储的 ZNode 在 /dubbo/Service 目录下面建立了四个目录',
            'Providers 目录下面，存放服务提供者 URL 和元数据',
            'Consumers 目录下面，存放消费者的 URL 和元数据',
            'Routers 目录下面，存放消费者的路由策略',
            'Configurators 目录下面，存放多个用于服务提供者动态配置 URL 元数据信息'
        ]},
        {'过程':[
            '客户端第一次连接注册中心的时候，会获取全量的服务元数据，包括服务提供者和服务消费者以及路由和配置的信息',
            '根据 ZooKeeper 客户端的特性，会在对应 ZNode 的目录上注册一个 Watcher，同时让客户端和注册中心保持 TCP 长连接'
            '如果服务的元数据信息发生变化，客户端会接受到变更通知，然后去注册中心更新元数据信息。变更时根据 ZNode 节点中版本变化进行',
        ]}
    ]}
],
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
],
'Dubbo 远程调用':[
    '服务消费者经过容错，Invoker 列表，路由和负载均衡以后，会对 Invoker 进行过滤，之后通过 Client 编码，序列化发给服务提供者',
    {'过程':[
        '1.服务消费者调用服务提供者的前后，都会调用 Filter（过滤器）',
        '2.调用请求经过过滤以后，会以 Invoker 的形式对 Client 进行调用',
        {'3.Client 会交由底层 I/O 线程池处理':[
            '包括处理消息读写，序列化，反序列化等逻辑',
            '将上述服务消息体，根据 Dubbo 协议打包好。框架内部会调用 DefaultFuture 对象的 get 方法进行等待',
            '协议打包好以后就需要给协议编码和序列化(将信息传化成字节流)',
            ''
        ]},
        '4.当服务提供者收到请求协议包以后，先将其放到 ThreadPool 中，然后依次处理',
        '5.由于服务提供者在注册中心是通过 Exporter 的方式暴露服务的，服务消费者也是通过 Exporter 作为接口进行调用的'
        '6.Exporter 是将 Invoker 进行了包装，将拆开的 Invoker 进行 Filter 过滤链条进行过滤以后，再去调用服务实体。最后，将信息返回给服务消费者',

    ]}
]
}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 