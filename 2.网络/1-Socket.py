import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="internet"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("Socket")
r2=s2.getRootTopic()
r2.setTitle("Socket")


content={
'协议':[
    {'TCP/IP':[
        'Transmission Control Protocol/Internet Protocol',
        '传输控制协议/网间协议，是一个工业标准的协议集，它是为广域网（WANs）设计的'
    ]},
    {'UDP':[
        'User Data Protocol，用户数据报协议',
        '与TCP相对应的协议。它是属于TCP/IP协议族中的一种',
    ]},
    'TCP/IP协议族包括运输层、网络层、链路层'
],
'Socket':[
    '应用层与TCP/IP协议族通信的中间软件抽象层，它是一组接口',
    '在设计模式中，Socket其实就是一个门面模式，它把复杂的TCP/IP协议族隐藏在Socket接口后面',
    {'客户端与服务器交互过程':[
        '1.服务器端先初始化Socket，然后与端口绑定(bind)，对端口进行监听(listen)，调用accept阻塞，等待客户端连接',
        '2.客户端初始化一个Socket，然后连接服务器(connect)，如果连接成功，这时客户端与服务器端的连接就建立了',
        '3.客户端发送数据请求，服务器端接收请求并处理请求，然后把回应数据发送给客户端',
        '4.客户端读取数据',
        '5.最后关闭连接，一次交互结束'
    ]},
    {'地址识别':[
        '网络层的“ip地址”可唯一标识网络中的主机',
        '传输层的“协议+端口”可唯一标识主机中的应用程序（进程）',
        '网络中的进程通信就可以利用三元组（ip地址，协议，端口）与其它进程进行交互'
    ]}
],
'TCP的三次握手':[
    {'1.客户端向服务器发送一个SYN J':[
        '客户端调用connect，触发了连接请求,connect进入阻塞状态',
    ]},
    {'2.服务器向客户端响应一个SYN K，并对SYN J进行确认ACK J+1':[
        '服务器监听到连接请求，即收到SYN J包，调用accept函数接收请求',
        '向客户端发送SYN K ，ACK J+1，这时accept进入阻塞状态'
    ]},
    {'3.客户端再想服务器发一个确认ACK K+1':[
        '客户端收到服务器的SYN K ，ACK J+1后，这时connect返回',
        '客户端对SYN K进行确认,发送ACK K+1',
        '服务器收到ACK K+1，accept返回'
    ]}
],
'TCP的四次握手释放':[
    '1.某个应用进程首先调用close主动关闭连接，这时TCP发送一个FIN M',
    '2.另一端接收到FIN M之后，执行被动关闭，对这个FIN进行确认',
    '它的接收也作为文件结束符传递给应用进程，因为FIN的接收意味着应用进程在相应的连接上再也接收不到额外数据',
    '3.一段时间之后，接收到文件结束符的应用进程调用close关闭它的socket。这导致它的TCP也发送一个FIN N',
    '4.接收到这个FIN的源发送端TCP对它进行确认'
]
}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 