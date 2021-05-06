import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="netty"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("高并发IO")
r2=s2.getRootTopic()
r2.setTitle("高并发IO")


content={
'IO读写':[
    '会用到操作系统的read&write两大系统调用',
    {'read系统调用':[
        '把数据从【内核缓冲区】复制到【进程缓冲区】'
    ]},
    {'write系统调用':[
        '把数据从【进程缓冲区】复制到【内核缓冲区】',
        '操作系统会对【内核缓冲区】进行监控，等待缓冲区达到一定数量的时候，再进行IO设备的中断处理'
    ]},
    {'注意':[
        {'应用程序的IO操作(read&write两大系统调用)':[
            '不是物理设备级别的读写，都不负责数据在【内核缓冲区】和【物理设备】间的交换',
            '只是【缓存的复制】',
            '所以应用程序的IO读写程序，并没有进行实际的IO操作，而是在进程缓冲区和内核缓冲区间进行数据交换'
        ]},
        '数据在内核缓冲区和物理设间的交换，由操作系统内核来完成'
    ]},
    {'内核缓冲区':[
        {'前提':[
            '外部设备的直接读写，涉及cpu中断',
            'cpu中断时，需保存之前在cpu中的进程数据，中断结束后，需恢复之前的进程数据'
        ]},
        {'作用':[
            '减少中断导致的频繁的上下文切换'
        ]}
    ]}
],
'同步IO':[
    '用户空间的线程是主动发起IO请求的一方，内核空间是被动接受方'
],
'异步IO':[
    '系统内核是主动发起IO请求的一方，用户空间的线程是被动接受方'
],
'四种主要IO模型':[
    {'IO模型':[
        '用【什么样的通道】进行【数据的发送和接收】',
    ]},
    '同步阻塞IO（Blocking IO)',
    '同步非阻塞IO（Non-blocking IO)',
    {'IO多路复用（IO Multiplexing）':[
        '经典的Reactor反应器设计模式',
        '也称为异步阻塞IO',
        'Java中的Selector选择器和Linux中的epoll都是这种模型'
    ]},
    '异步IO（Asynchronous IO）'
],
'操作系统对高并发的底层支持':[
    {'Linux系统中，文件分类':[
        '普通文件',
        '目录文件',
        '链接文件',
        '设备文件'
    ]},
    {'文件句柄，文件描述符':[
        '文件索引：内核为了高效管理已被打开的文件所创建的',
        '所有的IO系统调用(包括socket的读写调用)，都通过文件描述符完成的',
    ]},
    {'解除文件句柄数的限制(默认1024)':[
        '编辑/etc/rc.local开机启动文件(设置成最大1000000):ulimit -SHn 1000000'
    ]}
]
}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 