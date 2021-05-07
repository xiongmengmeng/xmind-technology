import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="netty"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("Netty")
r2=s2.getRootTopic()
r2.setTitle("Netty")


content={
'组件':[
    'Bootstrap启动器',
    'ByteBuf缓冲区',
    'NioEventLoop反应器',
    'Handler处理器',
    'Future异步任务监听',
    'Channel通道',
    'Pipeline流水线',
],
'Netty模型':[
    '1.Netty抽象出两组线程池，BossGroup专门负责接收客户端的连接，WorkerGroup专门负责网络的读写',
    '2.BossGroup和WorkerGroup类型都是NioEventLoopGroup',
    '3.NioEventLoopGroup相当于事件循环组，这个组中包裹有多个事件循环，每个事件循环都是一个NioEventLoop',
    '4.NioEventLoop表示一个不断循环的执行处理任务的线程，每个NioEventLoop都有一个Selector,用于监听绑定在其上socke网络通道',
    '5.NioEventLoopGroup可以有多个线程，即可含有多个NioEventLoop',
    {'6.每个boss NioEventLoop循环执行3个步骤':[
        '6.1.轮询accept事件',
        '6.2.处理accept事件，与client建立连接，生成NioSocketChannel,并将其注册到某个work NioEventLoop上的selector',
        '6.3.处理任务队列的任务，即runAllTasks'
    ]},
    {'7.每个worker NioEventLoop循环执行3个步骤':[
        '7.1.轮询read,write事件',
        '7.2.处理io事件，即read,write事件，在对应的NioSocketChannel处理',
        '7.3.处理任务队列的任务，即runAllTasks'
    ]},
    {'BossGroup':[
        '其线程维护Selector，只关注Accept事件',
        '当接收到Accept事件，获取对应的SocketChannel，封装成NIOSocketChannel,',
        '注册到WorkerGourp线程(事件循环)，并进行维护'
    ]},
    {'WorkerGroup':[
        '当WorkerGroup线程监听到Selector中通道发生自己感兴趣的事件后，就进行处理(由handler)'
    ]},
    {'NioEventLoop':[
        '内部采用串行化设计，从消息的读取->解码->处理->编码->发送，始终由IO线程NioEventLoop负责',
        '每个NioEventLoop中包含一个Selector,一个taskQueue',
        '每个NioEventLoop的Selector上可以注册监听多个NioChannel',
        '每个NioChannel只会绑定在唯一的NioEventLoop上',
        '每个NioChannel都绑定有一个自己的ChannelPipeline',
    ]}
]



}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 