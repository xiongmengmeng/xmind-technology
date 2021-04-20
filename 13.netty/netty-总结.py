import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="netty"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("netty总结")
r2=s2.getRootTopic()
r2.setTitle("netty总结")


content={
'read&write两大系统调用':[],
'四种主要IO模型':[
    {'阻塞IO（Blocking IO)':[
        'read函数'
    ]},
    {'非阻塞IO（Non-blocking IO)':[
        '非阻塞read函数'
    ]},
    {'IO多路复用（IO Multiplexing）':[
        '非阻塞read函数+select/pollt/epollt函数'
    ]},
    {'异步IO（Asynchronous IO':[
        '信号/回调'
    ]} 
],
'Java NIO':[
    {'Channel----通道':[
        'SocketChannel套接字通道',
        'ServerSocketChannel服务器监听通道'
    ]},
    {'Buffer----缓冲区':[
        'capacity(容量)',
        'position(读写位置)',
        'limit(读写的限制)'
    ]},
    {'Selector----选择器':[
        'SelectableChannel可选择通道',
        'SelectionKey选择键'
    ]},
],
'Reactor反应器模式':[
    '一个线程处理一个连接(Connection Per Thread)模式',
    '单线程Reactor反应器模式',
    '多线程Reactor反应器模式'
],
'异步':[
    {'java':[
        'Callable接口',
        'FutureTask类',
        'Future接口'
    ]},
    {'Guava异步回调':[
        'ListenableFuture接口',
        '引入FutureCallback接口'
    ]},
    {'Netty异步回调':[
        'Netty的Future接口',
        'GenericFutureListener接口'
    ]}
]


}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 