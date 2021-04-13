import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="netty"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("高并发IM架构的理论基础")
r2=s2.getRootTopic()
r2.setTitle("高并发IM架构的理论基础")


content={
'技术选型':[
    'Netty4.x + spring4.x + ZooKeeper 3.x + redis 3.x + rocketMQ 3.x+ mysql 5.x+ monggo3.x',
    {'短连接spring cloud':[
        '客户端向服务器发起连接，服务器接受客户端连接，在三次握手之后，双方建立连接',
        '客户端与服务器完成一次读写，发送数据包并得到返回的结果之后，通过客户端和服务器的四次握手断开连接',
        '短连接服务器也叫Web服务器，主要功能是实现用户的登录鉴权和拉取好友、群组、数据档案等相对低频的请求操',
        '扩展：短连接Web网关（WebGate），代理大量的Web服务器，从而无感知地实现短连接的高并发，可以使用SpringCloud或者Dubbo等分布式Web技术'
    ]},
    {'长连接 Netty':[
        '客户端向服务器发起连接，服务器接受客户端的连接，双方建立连接',
        '客户端与服务器完成一次读写之后，它们之间的连接并不会主动关闭，后续的读写操作会继续使用这个连接',
        'TCP协议的连接过程是比较烦琐的，建立连接是需要三次握手的，而释放则需要4次握手，所以说每个连接的建立都需要消耗资源和时间',
        '长连接服务器也叫IM即时通信服务器，主要作用就是用来和客户端建立并维持长连接，实现消息的传递和即时的转发',
        '扩展：基于ZooKeeper或者其他的分布式协调中间件，可以非常方便、轻松地实现一个IM服务器集群的管理'
    ]},
    '序列化协议选型:Protobuf'
],
'集群的负载均衡之实践案例':[
    '1. IM节点的POJO类ImNode,有属性id,balance(netty的服务联接数)',
    '2. IM节点的ImWorker类：所有的工作节点都在ZooKeeper的同一个父节点下，创建顺序节点。然后从返回的临时路径上，取得属于自己的那个后缀的编号',
    '3. ImLoadBalance负载均衡器：将计算最佳Netty服务器的算法，放在负载均衡器中',
    '4. 与短连接网关WebGate整合'
],
'即时通信消息的路由和转发的实践案例':[
    '如果连接在不同的Netty Worker工作站点的客户端之间，需要相互进行消息的发送，那么就需要在不同的Worker节点之间进行路由和转发',
    {'Worker节点的路由':[
        '根据消息需要转发的目标用户，找到用户的连接所在的Worker节点',
        '由于节点和节点之间都有可能需要相互转发，因此节点之间的连接是一种网状结构,每一个节点都需要具备路由的能力'
    ]},
    {'实现':[
        {'1.IM路由器WorkerRouter:为每一个Worker节点增加一个IM路由器类':[
            '要订阅到集群中所有的在线Netty服务器，即监控所有子节点（netty节点）',
            '将远程节点信息封装在转发器中，并用一个map来维护'
        ]},
        {'2.IM转发器WorkerReSender':[
            '封装了远程节点的IP地址、端口号以及ID',
            '维持了一个到远程节点的长连接,可以想像IM转发器是一个Netty的客户端，通过Netty channel通道将消息发送到远程节点'
        ]}
    ]}
],
'Feign短连接RESTful调用':[
    '短连接的服务接口都是基于应用层HTTP协议的HTTP API或者RESTful API实现的，通过JSON文本格式返回数据',
    {'四种方式':[
        'JDK原生的URLConnection',
        'Apache的HttpClient / HttpComponents',
        'Netty的异步HttpClient',
        'Spring的RestTemplate'
    ]},
    {'Feign':[
        'Netflix开发的一个声明式、模板化的HTTP客户端，可以进行同接口多服务器的负载均衡'
    ]}
],
'分布式的在线用户统计的实践案例':[
    {'Curator的分布式计数器':[
        '用int类型来计数（SharedCount）',
        '用long类型来计数（DistributedAtomicLong）'
    ]}
]
}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 