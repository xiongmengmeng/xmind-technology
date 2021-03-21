import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="netty"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("通道Channel")
r2=s2.getRootTopic()
r2.setTitle("通道Channel")


content={

'定义':[
    '一个连接就是用一个Channel（通道）',
    '一个通道可以表示一个底层的文件描述符，例如硬件设备、文件、网络连接',
    '涵盖了文件IO、TCP网络、UDP IO、基础IO'
],
'分类':[
    {'FileChannel文件通道':[
        '阻塞模式,用于文件的数据读写',
        {'4个核心操作':[
            {'获取FileChannel通道':[
                'getChannel()'
            ]},
            {'读取FileChannel通道':[
                'int read（ByteBufferbuf）',
                '从通道读取到数据',
                '然后写入到ByteBuffer缓冲区',
                '并且返回读取到的数据量'
            ]},
            {'写入FileChannel通道':[
                'int write（ByteBufferbuf）',
                '从ByteBuffer缓冲区中读取数据',
                '然后写入到通道自身',
                '最后返回写入成功的字节数'
            ]},
            {'关闭通道':[
                'close()'
            ]},
            {'强制刷新到磁盘':[
                'force()方法'
            ]}
        ]}
    ]},
    {'SocketChannel套接字通道':[
        {'定义':[
            '用于Socket套接字TCP连接的数据读写,与OIO中的Socket类对应',
            '支持阻塞和非阻塞两种模式',
            'configureBlocking方法:true为阻塞模式',
            '对应一个连接，两端都有一个负责传输的SocketChannel传输通道',
            '在NIO中，2个涉及网络连接的通道：SocketChannel负责连接传输，ServerSocketChannel负责连接的监听',
            'ServerSocketChannel应用于服务器端，而SocketChannel同时处于服务器端和客户端'
        ]},
        {'4个核心操作':[
            {'获取SocketChannel传输通道':[
                '客户端：先通过SocketChannel静态方法open()获得一个套接字传输通道',
                '然后，将socket套接字设置为非阻塞模式',
                '最后，通过connect()实例方法，对服务器的IP和端口发起连接',
                '服务器：首先通过事件，获得服务器监听通道',
                'accept()方法:获取新连接的套接字通道',
                '将socket套接字设置为非阻塞模式'
            ]},
            '读取SocketChannel传输通道:同上',
            '写入到SocketChannel传输通道:同上',       
            {'关闭SocketChannel传输通道':[
                'shutdownOutput()终止输出方法，向对方发送一个输出的结束标志（-1）',
                '调用socketChannel.close()方法，关闭套接字连接'
            ]}
        ]}
    ]},
    {'ServerSocketChannel服务器嵌套字通道（或服务器监听通道）':[
        '允许我们监听TCP连接请求，为每个监听到的请求，创建一个SocketChannel套接字通道',
        'NIO中的ServerSocketChannel监听通道，对应于OIO中的ServerSocket类'
    ]},
    {'DatagramChannel数据报通道':[
        {'定义':[
            '用于UDP协议的数据读写'
        ]},
        {'4个核心操作':[
            {'获取DatagramChannel数据报通道':[
                '调用DatagramChannel类的open静态方法',
                '调用configureBlocking（false）方法，设置成非阻塞模式',
                '需要接收数据，还需要调用bind方法绑定一个数据报的监听端口'
            ]},
            {'读取DatagramChannel数据报通道数据':[
                'receive（ByteBufferbuf）方法将数据从DatagramChannel读入，再写入到ByteBuffer缓冲区中',
                '返回值，是SocketAddress类型，表示返回发送端的连接地址（包括IP和端口）'
            ]},
            {'写入DatagramChannel数据报通道':[
                '调用send方法,需要指定接收方的地址（IP和端口）'
            ]},
            {'关闭DatagramChannel数据报通道':[
                '调用close()方法'
            ]}
        ]}
    ]}
]


}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 