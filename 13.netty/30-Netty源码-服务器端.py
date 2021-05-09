import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="netty"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("服务器端")
r2=s2.getRootTopic()
r2.setTitle("服务器端")


content={
'服务器启动':[
    {'入囗':[
        'ServerBootstrap#doBind(localAddress)'
    ]},
    {'内容':[
        '1.创建ServerSocketChannel,封闭在NioServerSocketChannel(反射创建)',
        {'2.注册ServerSocketChannel到Selector上':[
            '实现在AbstractChannel#register()'
        ]},
        '3.ServerSocketChannel监听端囗',
    ]}
],
'客户端有io事件时':[
    {'入囗':[
        'NioEventLoop#run()->',
        'processSelectedKeys()->',
        'AbstractNioMessageChannel.NioMessageUnsafe#read'
    ]},
    {'详细':[
        {'1.调用serverSocketChannel.accept()创建SocketChannel,并将其封装进NioSocketChannel':[
            '实现方法doReadMessages(List<Object> buf)'
        ]},
        {'2.执行调用链的读方法':[
            '实现方法pipeline.fireChannelRead(readBuf.get(i))',
        ]},
        {'3.调用到入站处理器ServerBootstrapAcceptor的channelRead()方法':[
            '将SocketChannel注册到childGroup中的一个EventLoop上的selector上'
        ]}
    ]}
]





}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 