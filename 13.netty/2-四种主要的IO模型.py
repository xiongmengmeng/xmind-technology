import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="netty"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("四种主要的IO模型")
r2=s2.getRootTopic()
r2.setTitle("四种主要的IO模型")


content={
'阻塞IO（Blocking IO)':[
    {'内核进行IO执行的两个阶段':[
        {'等待数据':[
            '将数据从【磁盘/网卡】读取到【内核缓冲区】-----阻塞'
        ]},
        {'复制数据':[
            '将数据从【内核缓冲区】读取到【用户缓冲区】-----阻塞'
        ]}
    ]},
    {'read函数':[
        '阻塞IO'
    ]},
    {'结果':[
        '在内核进行IO执行的两个阶段都阻塞'
    ]},
    {'特点':[
        '高并发场景下，需要【大量线程】来维护大量的网络连接，内存、线程切换开销很大'
    ]}
],
'非阻塞IO（Non-blocking IO)':[
    {'内核进行IO执行的两个阶段':[
        {'等待数据':[
            '将数据从【磁盘/网卡】读取到【内核缓冲区】-----立即返回，不阻塞'
        ]},
        {'复制数据':[
            '将数据从【内核缓冲区】读取到【用户缓冲区】-----阻塞'
        ]}
    ]},
    {'非阻塞read函数':[
        '等待数据阶段，立刻返回一个错误值（-1），而不是阻塞地等待',
        {'使用':[
            '只需在调用read前，将文件描述符设置为非阻塞'
        ]}
    ]},
    {'结果':[
        '只一个阶段【复制数据】阻塞'
    ]},
    {'特点':[
        '应用程序的线程需轮询【不断地进行IO系统调用】,会占用大量的CPU时间，效率低下'
    ]}
],
'IO多路复用（IO Multiplexing）':[],
'异步IO（Asynchronous IO）':[
    {'四个步骤':[
        '1.用户线程通过系统调用，向内核注册某个IO操作,用户执行后续的业务操作',
        '2.内核进行整个IO操作（包括等待数据、复制数据两阶段）',
        {'3.完成后，通知用户程序':[
            '内核给用户线程发送一个信号（Signal），或回调用户线程注册的回调接口'
        ]},
        '4.用户线程读取用户缓冲区的数据' 
    ]},
    {'特点':[
        {'非阻塞':[
            '在内核等待数据和复制数据的两个阶段，用户线程不阻塞'
        ]},
        {'信号/事件驱动':[
            '用户线程需要接收内核的IO操作完成的事件，或者用户线程需要注册一个IO操作完成回调函数'
        ]},
        {'内核支持':[
            '应用程序仅需要进行事件的注册与接收，其余的工作都留给了操作系统，因此需底层内核提供支持'
        ]},
    ]}
]


}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 