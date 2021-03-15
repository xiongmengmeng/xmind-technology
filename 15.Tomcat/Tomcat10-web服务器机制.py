import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="tomcat"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("Web服务器机制")
r2=s2.getRootTopic()
r2.setTitle("Web服务器机制")


content={
'通信协议':[
    'HTTP/HTTPS',
    'HTTP请求/响应模型',
    '解析HTTP报文'
],
'套接字通信':[
    '应用层与传输层TCP/IP协议族通信的中间抽象层，是一组接口',
    '一般由操作系统提供或者由JVM自己实现',
    'TCP/IP协议族中有两种套接字类型，流套接字和数据报套接字，对应TCP协议和UDP协议',
    '一个TCP/IP套接字由一个互联网地址、一个协议及一个端口号唯一确定',
    {'分类':[
        '单播通信',
        {'组播通信':[
            '能在公网内传播',
            '没有可靠传输协议，数据不可靠',
            '路由器',
            '实现类：java.net.MulticastSocket'
        ]},
        {'广播通信':[
            '只能在局域网内传播',
            '交换机',
            '实现类java.net.DatagramSocket'
        ]}
    ]}
],
'服务器端对I/O的处理模型':[
    '单线程阻塞I/O模型',
    '多线程阻塞I/O模型',
    {'单线程非阻塞I/O模型':[
        {'连接的三种检测方式':[
            '应用程序遍历套接字的事件检测',
            {'内核遍历套接字':[
                '套接字的遍历工作交由操作系统内核',
                '对套接字遍历结果组织成一系列事件列表并返回应用层处理',
                '遍历工作下移到内核层',
                '列表从内核复制到应用层,开销大',
                '活跃连接较少时，内核与应用层间存在很多无效的数据副本'
            ]},
            {'内核基于回调':[
                '内核中的套接字都对应一个回调函数',
                '当客户端往套接字发送数据时，内核从网卡接收数据后就会调用回调函数',
                '在回调函数中维护事件列表，应用层获取此事件列表即可得到所有感兴趣的事件',
                {'两种':[
                    '可读列表readList和可写列表writeList标记读写事件(同套接字的数量）',
                    '事件列表'
                ]}
            ]}
        ]},
    ]},
    {'多线程非阻塞I/O模型:Reactor模式':[
        {'改进':[
            '在耗时的process处理器中引入多线程，如使用线程池',
            '直接使用多个Reactor实例，每个Reactor实例对应一个线程'
        ]},
        '充分利用CPU资源，适合于高并发场景'
    ]}
]

}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 