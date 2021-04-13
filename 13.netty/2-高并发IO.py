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
    '会用到底层的read&write两大系统调用',
    {'read系统调用':[
        '把数据从内核缓冲区复制到进程缓冲区'
    ]},
    {'write系统调用':[
        '把数据从进程缓冲区复制到内核缓冲区'
    ]},
    {'同步IO':[
        '用户空间的线程是主动发起IO请求的一方，内核空间是被动接受方'
    ]},
    {'异步IO':[
        '系统内核是主动发起IO请求的一方，用户空间的线程是被动接受方'
    ]},
    {'内存缓冲区':[
        '目的是为了减少频繁地与设备之间的物理交换',
        '外部设备的直接读写，涉及cpu的中断',
        '发生系统中断时，需要保存之前在cpu中的进程数据和状态等信息，而结束中断之后，还需要恢复之前的进程数据和状态等信息'
    ]}
],
'四种主要的IO模型':[
    '同步阻塞IO（Blocking IO)',
    '同步非阻塞IO（Non-blocking IO)',
    'IO多路复用（IO Multiplexing）',
    '异步IO（Asynchronous IO）'
     
],
'操作系统对高并发的底层的支持':[
    '在Linux系统中，文件可分为：普通文件、目录文件、链接文件和设备文件',
    '文件句柄，文件描述符（File Descriptor）:内核为了高效管理已被打开的文件所创建的索引',
    '所有的IO系统调用，包括socket的读写调用，都是通过文件描述符完成的',
    'Linux操作系统中文件句柄数的限制，编辑/etc/rc.local开机启动文件:ulimit -SHn 1000000'
]
}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 