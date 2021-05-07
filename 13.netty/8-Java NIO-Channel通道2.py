import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="netty"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("TCP网络连接通道")
r2=s2.getRootTopic()
r2.setTitle("TCP网络连接通道")


content={
'SocketChannel':[
    {'作用':[
        '负责连接传输数据',
        '应用于服务器端和客户端,对应于OIO中的Socket类'
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
            '设置阻塞或非阻塞模式，false表示采用非阻塞模块'
        ]},
        {'write(ByteBuffer src)':[
            '往通道里写数据'
        ]},
        {'read(ByteBuffer dst)':[
            '从通道里读数据'
        ]},
        {'register(Selector sel,int ops,Object att)':[
            '注册一个选择器，设置监听事件，并设置共享数据'
        ]}
    ]}
],
'ServerSocketChannel':[
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
                'while(!socketChannel.finishConnect() ){',
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
            '返回值:读取的字节数,-1表示读取到对方的输出结束标志，对方已输出结束，准备关闭连接',
        ]},
        {'例':[
            'ByteBuffer buf = ByteBuffer.allocate(1024);',
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


}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 