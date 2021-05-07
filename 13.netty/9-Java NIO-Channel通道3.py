import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="netty"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("UDP网络连接通道")
r2=s2.getRootTopic()
r2.setTitle("UDP网络连接通道")


content={
'零拷贝':[
    '从操作系统角度看，没有CPU拷贝，只有DMA拷贝',
    {'本质':[
        'linux2.4的sendFile函数',
        '数据不经过用户态，直接从内核缓冲区进入到协议栈',
        '实际有一次cpu拷贝，kernel buffer到socket buffer,但拷贝信息少，消耗低，可忽略',
        {'java应用':[
            'FileChannel的transferTo()方法'
        ]}
    ]}
],
'DatagramChannel数据报通道':[
    '用于UDP协议的数据读写',
    {'4个核心操作':[
        {'获取DatagramChannel数据报通道':[
            '调用DatagramChannel类的open静态方法',
            '调用configureBlocking（false）方法，设置成非阻塞模式',
            '需要接收数据，还需调用bind方法绑定一个数据报的监听端口'
        ]},
        {'读取DatagramChannel数据报通道数据':[
            {'receive(ByteBufferbuf)':[
                '将数据从DatagramChannel读入，再写入到ByteBuffer缓冲区中',
                '返回值，是SocketAddress类型，表示返回发送端的连接地址（包括IP和端口）'
            ]}
        ]},
        {'写入DatagramChannel数据报通道':[
            {'send()':[
                '需指定接收方的地址（IP和端口）'
            ]}
        ]},
        {'关闭DatagramChannel数据报通道':[
            'close()'
        ]}
    ]}
]




}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 