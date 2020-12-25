import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="internet"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("protocol")
r2=s2.getRootTopic()
r2.setTitle("协议与网卡")


content={

'简要流程':[
    '应用程序：网络应用程序+Socket库',
    {'操作系统的协议栈':[
        'TCP,UDP协议',
        'IP协议+ICMP+ARP'
    ]},
    '网上驱动程序',
    '硬件：网卡'
],
'1.创建套接字':[
    '1.分配一个套接字所需内存空间，写入初始状态',
    '2.将表示套接字的描述符告知应用程序',
    'netstat -ano显示套接字内容'
],
'2.连接服务器':[
    {'作用':[
        '通信双方交换控制信息,在套接字中记录必要信息',
        '分配缓冲区：一块临时存放要收发的数据的内存空间'
    ]},
    {'通信操作中使用的控制信息':[
        '头部记录的信息',
        '套接字（协议栈中的内存空间）中记录的信息'
    ]},
    {'ACK':[
        {'ACK号等待时间':[
            '据网络包平均往返时间调整ACK号等待时间',
            '滑动窗口与接收缓冲区',
            '滑动窗口：接收方需要告诉发送方自己最多能接收多少数据，发送方根据这个值对数据发送操作进行控制'
        ]},
        '通过“序号”和“ACK号”确认接收方是否收到了网络包',
        'ACK与窗口的合并,减少网络开销'
    ]},
    {'过程':[
        {'1.应用程序':[
            '调用Socket库的connect(<描述符>,<服务器IP地址和端囗号>)，',
            '将IP地址和端口号传递给协议栈中的TCP模块'
        ]},
        {'2.客户端TCP模块':[
            '创建表示连接控制信息的头部:【SYN=1,序号初始值，窗口】',
            '将信息传递给IP模块并委托它进行发送'
        ]},
        '3.客户端IP模块：执行网络包发送操作，网络包通过网络到达服务器',
        '4.服务器的IP模块：将接收到的数据传递给TCP模块',
        {'5.服务器的TCP模块':[
            '根据TCP头部中的信息找到端口号对应的套接字',
            'TCP头部:【ACK=1，窗口,SYN=1,序号初始值】，将其传递给IP模块'
        ]},
        '6.服务器IP模块：执行网络包发送操作，网络包通过网络到达客户端',
        {'7.客户端TCP模块':[
            '通过TCP头部的信息确认连接服务器的操作是否成功',
            '如SYN=1,代表连接成功',
            '向套接字中写入服务器的IP地址、端口号等信息，将状态改为连接完毕',
            '将【ACK设置为1】,将TCP头部传递给IP模块，委托它向服务端返回响应'
        ]}
    ]}
],
'3.收发数据':[
    {'将请求消息交给协议栈':[
        '协议栈收到数据不会立即发送，而是将数据放在内部缓冲区，等待应用程序的下一段数据',
        {'发送数据条件':[
            '每个网络包能容纳的数据长度',
            '时间'
        ]},
        'MTU：一个网络包的最大长度，以太网中一般为1500字节',
        'MSS：除去头部之后，一个网络包所能容纳的TCP数据的最大长度',
    ]},
    {'接收HTTP响应消息':[
        '浏览器:在委托协议栈发送请求消息之后，调用read程序来获取响应消息',
        {'协议栈':[
            '响应消息未返回:将应用程序的委托（从接收缓冲区中取出数据并传递给应用程序）挂起',
            '响应消息返回:执行接收操作',
            '检查收到的数据块和TCP头部内容，判断是否有数据丢失，没有问题则返回ACK号',
            '将数据块暂存到接收缓冲区中，并将数据块按顺序连接还原出原始数据',
            '最后将数据交给应用程序'
        ]}
    ]}
],
'4.服务器断开连接并删除套接字':[
    '1.服务器的应用程序:调用Socket库的close程序',
    '2.服务器的协议栈:生成包含断开信息的TCP头部,【FIN=1】,套接字记录下断开操作的相关信息,委托IP模块向客户端发送数据,',
    '3.客户端的协议栈:将自己的套接字标记为断开操作状态,向服务器返回一个【ACK号】,等待应用程序来取数据',
    '4.客户端应用程序:调用read来读取数据,被告知来自服务器的数据已经全部收到,调用close来结束数据收发操作',
    '5.客户端的协议栈：生成包含断开信息的TCP头部,【FIN=1】，委托IP模块发送给服务器',
    '6.服务器:返回【ACK号】',
    '7.客户端和服务器的通信全部结束',
    '8.套接字等待一段时间之后再被删除,防止误操作'
]
}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 