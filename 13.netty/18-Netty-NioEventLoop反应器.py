import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="netty"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("Netty:NioEventLoop反应器")
r2=s2.getRootTopic()
r2.setTitle("Netty:NioEventLoop反应器")


content={
'基础':[
    {'服务器通道新连接的IO事件的监听':[
        '一个反应器通过Selector选择器不断地查询注册过的IO事件（选择键）'
    ]},
    {'传输通道的IO事件':[
        '如果查询到IO事件，分发给Handler业务处理器'
    ]},
    {'为及时接受(Accept)到新连接，在服务器端，一般有两个独立的反应器':[
        '一个反应器负责新连接的监听和接受',
        '一个反应器负责IO事件处理'
    ]}
],
'NioEventLoop':[
    '拥有一个Thread线程，负责一个Java NIO Selector选择器的IO事件轮询',
    {'介绍':[
        '内部采用串行化设计，从消息的读取->解码->处理->编码->发送，始终由IO线程NioEventLoop负责',
        '每个NioEventLoop中包含一个Selector,一个taskQueue',
        '每个NioEventLoop的Selector上可以注册监听多个NioChannel',
        '每个NioChannel只会绑定在唯一的NioEventLoop上',
        '每个NioChannel都绑定有一个自己的ChannelPipeline',
    ]},
    {'属性':[
        {'Thread thread':[
            '父类SingleThreadEventExecutor中定义',
            '负责一个Java NIO Selector选择器的IO事件轮询'
        ]},
        {'Selector selector;':[
            'Java NIO选择器Selector类'
        ]},
        {'Queue<Runnable> taskQueue':[
            '父类SingleThreadEventExecutor中定义'
        ]}
    ]}
]




}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 