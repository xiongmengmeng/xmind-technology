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
'IO基础':[
    'read&write两大系统调用'
],
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
        'SelectionKey选择键'
    ]},
],
'线程模型':[
    '传统阻塞IO服务模型',
    {'Reactor反应器模式':[
        'Reactor反应器+Handlers处理器',
        {'分类':[
            '单Reactor单线程',
            '单Reactor多线程',
            '主从Reactor多线程'
        ]}
    ]},
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
],
'netty':[
    {'基础':[
        '主从Reactor多线程'
    ]},
    {'核心组件':[
        'Bootstrap启动器',
        'NioEventLoop反应器',
        'ByteBuf缓冲区',
        'Channel通道',
        'Pipeline流水线',
        'Handler处理器--ChannelHandlerContext上下文'
        'Future异步任务监听',
        'Decoder与Encoder编解码器'
    ]}

]


}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 