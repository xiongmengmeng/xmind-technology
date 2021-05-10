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
        {'1.创建ServerSocketChannel,封装为NioServerSocketChannel':[
            '实现channelFactory.newChannel()->NioServerSocketChannel()'
        ]},
        {'2.初始化NioServerSocketChannel':[
            '将配置参数，自定义处理器，ServerBootstrapAcceptor处理器，绑定到NioServerSocketChannel上',
            '实现init(channel)'
        ]},
        {'3.注册ServerSocketChannel到Selector上':[
            '实现config().group().register(channel)->AbstractChannel.register()'
        ]},
        {'4.ServerSocketChannel监听端囗':[
            '实现doBind0(regFuture, channel, localAddress, promise)'
        ]},
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
            '实现doReadMessages(List<Object> buf)'
        ]},
        {'2.执行调用链的读方法':[
            '实现pipeline.fireChannelRead(readBuf.get(i))',
        ]},
        {'3.将SocketChannel注册到childGroup中的一个EventLoop上的selector上':[
            '实现入站处理器ServerBootstrapAcceptor的channelRead()方法'
        ]}
    ]}
]





}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 