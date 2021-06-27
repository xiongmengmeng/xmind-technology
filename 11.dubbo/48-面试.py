import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
xmind_name="dubbo"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("面试")
r2=s2.getRootTopic()
r2.setTitle("面试")


content={
'分层(三层)':[
    {'业务逻辑层':[
        '接囗，接囗实现，配置信息',
        'Service'
    ]},
    {'RPC层':[
        '封装了整个PRC调用过程，负载均衡，集群容错，代理',
        'Config、Proxy、Registry、Cluster、Protocol'
    ]},
    {'remoting':[
        '网络传输协议和数据转换的封装',
        'Exchange、Transport、Serialize'
    ]}
],
'工作原理':[
    {'提供者':[
        '将接囗信息封装为URL，注册到注册中心上',
        '将接囗封装为Invoker->Exporter,缓存起来',
        '收到消费者的请求时，通过Invoker,创建代理调用具体的接囗'
    ]},
    {'消费者':[
        '去注册中心上订阅相关服务的信息，缓存在本地',
        '为每个远程服务创建一个代理类，代理类持有一个FailOverClusterInvoker',
        '方法被调用时，通过代理类，负载均衡选择一个提供者进行方法调用'
    ]}
],
'服务暴露':[
    {'触发节点':[
        'spring容器创建完成后，触发contextRefreshEvent事件回调'
    ]},
    '1.创建AbstractProxyInvoker,里面持有服务的引用',
    '2.将Invoker，封装为Exporter,存入一个map中，key为接囗名+版本+组名',
    '3.启动netty服务器',
    '4.将服务封装为URL的形式，注册到zk上',
],
'服务引用':[
    '1.从zk上订阅服务，封装成Invoker，缓存在本地(Directory内)',
    '2.启动netty客户端',
    '3.为服务生成代理对象，持有一个FailOverClusterInvoker'
],
'服务调用':[
    {'消费者':[
        '1.调用代理对象，调用到FailOverClusterInvoker的invoker方法',
        {'2.负载均衡选择一个Invoker,调用其invoker()方法':[
            '2.1.从Directory中取出服务对映的Invoker集合',
            '2.2.使用Router对集合进行过滤',
            '2.3.通过LoadBalance选择一个Invoker'
        ]},
        '3.最终调用DubboInvoker.invoker()方法，选择一个netty客户端连接进行网络调用',
    ]},
    {'提供者':[
        '4.netty服务器接收到请求，对数据进行解码',
        '5.根据invocation，封装为key:接囗名+版本+组名',
        '6.根据key得出对映的Exporter，然后得到Invoker',
        '7.AbstractProxyInvoker.invoker方法，会创建代理，调用服务'
    ]}
],
'集群容错方式(6种)':[
    'FailoverCluster',
    'FailfastCluster',
    'FailsafeCluster',
    'FailbackCluster',
    'ForkingCluster',
    'BroadcastCluster'
],
'负载均衡方式(4种)':[
    '权重随机',
    '平滑加权轮询',
    '最少活跃调用数',
    '一致性hash'
],
'SPI':[
    {'相比java spi':[
        'key-value形式，可只加载部分类',
        '增加对IoC和AOP支持'
    ]},
    {'实现':[
        'ExtensionLoader'
    ]},
    {'扩展点注解':[
        '@SPI',
        '©Adaptive',
        '©Activate'
    ]}
]

}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 