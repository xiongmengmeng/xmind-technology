import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="netty"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("TCP网络连接的通道")
r2=s2.getRootTopic()
r2.setTitle("TCP网络连接的通道")


content={
'TCP网络连接的通道(2个）':[
    {'SocketChannel':[
        {'作用':[
            '负责连接传输数据',
            '应用于服务器端和客户端,与OIO中的Socket类'
        ]},
        '对应一个连接，两端都有一个负责传输的SocketChannel传输通道',
        {'有阻塞和非阻塞两种模式':[
            'configureBlocking方法:true为阻塞模式'
        ]},
        {'方法':[
            {'open()':[
                '获得一个SocketChannel通道'
            ]},
            {'connect(SocketAddress local)':[
                '连接服务器'
            ]},
            {'configureBlocking(boolean block)':[
                '设置阻塞或非阻塞模式，取值false表示采用非阻塞模块'
            ]},
            {'write(ByteBuffer src)':[
                '往通道里写数据'
            ]},
            {'read(ByteBuffer dst)':[
                '从通道里读数据'
            ]},
            {'register(Selector sel,int ops,Object att)':[
                '注册一个选择器并设置监听事件，最后一个参数可设置共享数据'
            ]}
        ]}
    ]},
    {'ServerSocketChannel':[
        '服务器监听新的客户端Socket连接',
        {'作用':[
            '负责监听TCP连接请求,为每个监听到的请求，创建一个SocketChannel套接字通道',
            '应用于服务器端,对应于OIO中的ServerSocket类'
        ]},
        {'方法':[
            {'open()':[
                '获得一个ServerSocketChannel通道'
            ]},
            {'bind(SocketAddress local)':[
                '设置服务器端囗号'
            ]},
            {'configureBlocking(boolean block)':[
                '设置阻塞或非阻塞模式，取值false表示采用非阻塞模块'
            ]},
            {'accept()':[
                '接受一个新连接，返回代表这个连接的通道对象'
            ]},
            {'register(Selector sel,int ops)':[
                '注册一个选择器并设置监听事件'
            ]}
        ]}
    ]}
],
'4个核心操作':[
    {'获取SocketChannel传输通道':[
        {'客户端':[
            {'1.静态方法open(),获得一个套接字传输通道':[
                'SocketChannel socketChannel = SocketChannel.open()'
            ]},
            {'2.将socket套接字设置为非阻塞模式':[
                'socketChannel.configureBlocking(false)'
            ]},
            {'3.connect()方法，对服务器的IP和端口发起连接':[
                'socketChannel.connect(new InetSocketAddress("127.0.0.1",80))'
            ]},
            {'4.非阻塞,与服务器的连接可能还没真正建立,需不断自旋，检查当前是否是连接到了主机':[
                'while(! socketChannel.finishConnect() ){',
                '   //不断地自旋、等待',
                '}'
            ]}
        ]},
        {'服务器':[
            {'1.通过事件，获得服务器监听通道':[
                'ServerSocketChannel server = (ServerSocketChannel) key.channel()'
            ]},
            {'2.accept()方法:获取新连接的套接字通道':[
                'SocketChannel socketChannel = server.accept()'
            ]},
            {'3.将socket套接字设置为非阻塞模式':[
                'socketChannel.configureBlocking(false)'
            ]},
        ]}
    ]},
    {'读取SocketChannel传输通道':[
        {'read()方法':[
            '将数据读入缓冲区ByteBuffer',
            '返回值:读取的字节数,-1表示读取到对方的输出结束标志，对方已经输出结束，准备关闭连接',
        ]},
        {'例':[
            'ByteBufferbuf = ByteBuffer.allocate(1024);',
            'int bytesRead = socketChannel.read(buf);'
        ]}
    ]},
    {'写入到SocketChannel传输通道':[
        {'write()方法':[
            {'buffer.flip()':[
                '写入前需要读取缓冲区，要求ByteBuffer是读取模式'
            ]},
            'socketChannel.write(buffer)',
        ]}
    ]},       
    {'关闭SocketChannel传输通道':[
        {'1.终止输出方法，向对方发送一个输出的结束标志(-1)':[
            'socketChannel.shutdownOutput()'
        ]},
        {'2.关闭套接字连接':[
            'IOUtil.closeQuietly(socketChannel)'
        ]}
    ]}
],
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
'线程模型':[
    {'传统阻塞IO服务模型':[
        {'特点':[
            '1.采用阻塞IO模式获取输入的数据',
            '2.每个连接都需要独立的线程完成数据的输入，业务处理，数据返回'
        ]},
        {'问题':[
            '1.当并发数据很大，就会创建大量的线程，占用很大的系统资源',
            '2.连接创建后，如当前线程暂无数据可读，线程会阻塞在read操作，造成线程资源浪费'
        ]}
    ]},
    {'Reactor模式':[
        '反应器模式，分发者模式，通知者模式',
        {'针对传参阻塞IO服务模型的问题，解决方案':[
            {'基于IO复用模型':[
                '多个连接共用一个阻塞对象，应用程序只需要在一个阻塞对象上等待，无需阻塞等待所有连接',
                '当某个连接有新的数据可以处理时，操作系统通知应用程序，线程从阻塞状态返回，开始进行业务处理'
            ]},
            {'基于线程池复用线程资源':[
                '不必再为每个连接创建线程，将连接完成后的业务处理任务分配给线程进行处理',
                '一个线程可处理多个连接的业务'
            ]}
        ]},
        {'基本设计思想':[
            'IO复用结合线程池',
            {'详细':
                '1.Reactor模式，通过一个或多个输入同时传递给服务处理器的模式(基于事件驱动) ',
                '2.服务器端程序处理传入的多个请求，并将它们【同步分派】到相应的【处理线程】 ',
                '3.Reactor请求，使用IO复用监听事件，收到事件后，分发给某个线程(进程),这是网络服务器高并发处理的关键'
            ]}
        ]},
        {'核心组成':[
            {'Reactor':[
                '在一个单独线程中运行，负责监听和分发事件，分发给适合的处理程序来对IO事件做出反应'
            ]},
            {'Handlers':[
                '处理程序执行IO事件要完成的实际事件'
            ]}
        ]},
        {'分类(根据Reactor的数量和处理资源池线程的数量)':[
            '单Reactor单线程',
            '单Reactor多线程',
            '主从Reactor多线程'
        ]}
    ]}

]
}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 