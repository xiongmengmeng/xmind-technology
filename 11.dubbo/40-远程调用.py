import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
xmind_name="dubbo"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("Dubbo 远程调用")
r2=s2.getRootTopic()
r2.setTitle("Dubbo 远程调用")


content={
'过程':[
    '1.从Directory获得Invoker 列表',
    '2.Invoker 列表经过路由和负载均衡选择一个Invoker',
    '3.对 Invoker 进行过滤',
    '4.之后通过 Client 编码，序列化发给服务提供'
],
'负载均衡后的过程':[
    '1.服务消费者调用服务提供者的前后，都会调用 Filter（过滤器）',
    '2.调用请求经过过滤以后，会以 Invoker 的形式对 Client 进行调用',
    {'3.Client 会交由底层 I/O 线程池处理':[
        '包括处理消息读写，序列化，反序列化等逻辑',
        '将上述服务消息体，根据 Dubbo 协议打包好。框架内部会调用 DefaultFuture 对象的 get 方法进行等待',
        '协议打包好以后就需要给协议编码和序列化(将信息传化成字节流)'
    ]},
    '4.当服务提供者收到请求协议包以后，先将其放到 ThreadPool 中，然后依次处理',
    '5.由于服务提供者在注册中心是通过 Exporter 的方式暴露服务的，服务消费者也是通过 Exporter 作为接口进行调用的',
    '6.Exporter 是将 Invoker 进行了包装，将拆开的 Invoker 进行 Filter 过滤链条进行过滤以后，再去调用服务实体。最后，将信息返回给服务消费者',

],
'通信过程:接囗方法调用':[
    {'Invoke执行':[
        '集群负载均衡处理',
        '协议Invoker',
    ]},
    '请求、响应处理器',
    {'发送请求获取结果':[  
        '编解码',
        '发送请求',
        '获取结果'
    ]},
    {'服务端处理请求':[
        '线程派发',
        '获取结果',
        '编解码'
    ]}
],
'入囗InvokerInvocationHandler#invoke':[
    'this.invoker.invoke(new RpcInvocation(method, args)).recreate()',
    '注：this.invoker为DubboInVoker'
]

}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 