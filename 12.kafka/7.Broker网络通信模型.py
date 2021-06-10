import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
xmind_name="kafka"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("Broker网络通信模型")
r2=s2.getRootTopic()
r2.setTitle("Broker网络通信模型")


content={
'Reactor模式':[
    '网络通信模型的发展:单线程 => 多线程 => 线程池 => Reactor模型',
    '由一个线程来监视一堆连接，同步等待一个或多个IO事件的到来，然后将事件分发给对应的Handler处理'
],
'Broker网络通信模型':[
    {'Acceptor(mainReactor)':[
        '监听新连接的到来',
        '与新连接建连之后轮询选择一个Processor(subReactor)管理这个连接',
        '只是作为新连接建连再分发，没有过多的逻辑，很轻量，一个足矣',
    ]},
    {'网络线程Processor':[
        '监听其管理的连接',
        '当事件到达之后，读取封装成Request，并将Request放入共享请求队列',
        '当事件处理完后，从响应队列读出结果，封装为Response返还给客户端',
        '对应参数num.network.threads,默认3'
    ]},
    {'IO线程池KafkaRequestHandlerPool':[
        '不断的从该队列中取出请求，执行真正的处理',
        '处理完之后将响应发送到对应的Processor的响应队列中',
        '对应参数num.io.threads,默认8'
    ]}
]
}
#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 