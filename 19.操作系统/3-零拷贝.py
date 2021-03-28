import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
xmind_name="internet"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("零拷贝")
r2=s2.getRootTopic()
r2.setTitle("零拷贝")


content={
'传统拷贝过程':[
    '1.操作系统将数据从磁盘读入到内核空间的页缓冲区',
    '2.应用程序将数据从内核空间读入到用户空间的应用层缓冲区',
    '3.应用程序将数据写回到内核空间的Socket套接字缓冲区',
    '4.操作系统将数据从socket缓冲区复制到网卡缓冲区，以便将数据经网络发出',
    {'总结':[
        '4次上下文切换',
        '4次数据的复制',
        '有两次复制操作是由 CPU 完成'
    ]}
],
'DMA 技术':[
    'Direct Memory Access，直接内存存取',
    '允许不同速度的硬件装置来沟通，而不需要依赖于CPU的大量中断负载',
    {'传统的内存访问':[
        '所有的请求都会发送到 CPU ，然后再由 CPU 来完成相关调度工作'
    ]},
    {'DMA 技术':[
        '数据文件在各个层之间的传输，可直接绕过CPU，使得外围设备可以通过DMA控制器直接访问内存',
        '解决批量数据的输入/输出问题'
    ]},
    {'支持DMA技术的硬件':[
        '磁盘、显卡、声卡、网卡'
    ]}
],
'零拷贝技术':[
    '利用DMA技术，通过网卡直接去访问系统内存，实现现绝对的零拷贝，最大程度提高传输性能',
    'Linux中，sendfile系统调用:将数据从页缓存直接传输到 Socket',
    {'sendfile(int out_fd, int in_fd, off_t *offset, size_t count)':[
        'in_fd:输入文件的描述符,文件必须是可以mmap的',
        'out_fd:表输出文件的描述符,必须指向一个套接字'
        '代表在in_fd和out_fd之间传送文件内容（字节）',
        '注：使sendfile只能将数据从文件传递到套接字上',
        '优化：带有文件位置和长度信息的缓冲区描述符添加socket缓冲区去，避免了最后一次拷贝'
    ]},
    {'splice系统调用':[
        '用于在两个文件描述符中移动数据,一方必须是管道设备'
    ]},
    {'结果':[
        '内核缓冲区数据直接拷贝到网卡缓冲区'
    ]}
],
'Java零拷贝':[
    '由 FileChannel.transferTo() 方法实现',
    {'transferTo()':[
        '调用native 方法，依赖底层操作系统的支持',
        '在UNIX 和 Linux系统中，调用这个方法将会引起sendfile()系统调用'
    ]}
],
'零拷贝的使用场景':[
    '较大，读写较慢，追求速度',
    '内存不足，不能加载太大数据',
    '带宽不够，即存在其他程序或线程存在大量的IO操作，导致带宽不够'
]
}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 