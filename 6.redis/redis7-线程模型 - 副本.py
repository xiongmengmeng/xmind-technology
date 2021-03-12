import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="redis"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("线程模型")
r2=s2.getRootTopic()
r2.setTitle("线程模型")


content={
'线程模型':[
    '基于Reactor模式开发',
    '文件事件处理器'
],
'Redis称单线程模型':[
    '文件事件分派器队列的消费是单线程的'
],
'文件事件处理器4部分组成':[
    {'多个套接字':[
        '会并发产生不同的操作，每个操作对应不同文件事件',
        {'文件事件':[
            '对socket操作的抽象',
            '当一个socket准备好执行连接accept、read、write、close操作时，会产生一个文件事件'
        ]}
    ]},
    {'IO多路复用程序':[
        '监听多个socket，将socket产生的事件放入队列',
        '通过队列以有序、同步且每次一个socket的方式向文件事件分派器传送socket',
        '当上一个socket产生的事件被对应事件处理器执行完后，I/O多路复用程序才会向文件事件分派器传送下个socket'
    ]},
    {'文件事件分派器':[
        '接收I/O多路复用程序传来的socket',
        '根据socket产生的事件类型，调用相应的事件处理器'
    ]},
    {'事件处理器':[
        '连接应答处理器',
        '命令请求处理器',
        '命令回复处理器'
    ]}
],
'客户端和Redis服务器通信过程':[
    '1.客户端向服务器发起【连接请求】，socket产生一个AE_READABLE事件',
    '2.AE_READABLE事件映射到【连接应答处理器】',
    '3.客户端向服务器发起【命令请求】（不管读还是写请求），socket产生一个AE_READABLE事件',
    '4.AE_READABLE事件映射到【命令请求处理器】',
    '5.服务器向客户端发起【命令响应】',
    '6.AE_WRITABLE事件映射到【命令回复处理器】'
]
}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 