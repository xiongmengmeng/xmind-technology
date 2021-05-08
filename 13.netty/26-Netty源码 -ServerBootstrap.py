import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="netty"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("ServerBootstrap")
r2=s2.getRootTopic()
r2.setTitle("ServerBootstrap")


content={

'属性':[
    {'EventLoopGroup group':[
        '继承自父类AbstractBootstrap'
    ]},
    {'EventLoopGroup childGroup':[
        '指向workGroup'
    ]},
    {'Map<ChannelOption<?>, Object> options':[
        '存放option()方法传入的tcp参数'
    ]},
    {'ChannelHandler handler':[
        '继承自父类AbstractBootstrap'
    ]},
    {'ChannelHandler childHandler':[
        'socketChannel的执行器'
    ]}
],
'方法':[
    {'构造器':[
        '空实现'
    ]},
    {'group(EventLoopGroup parentGroup, EventLoopGroup childGroup)':[
        'parentGroup赋值给group',
        'childGroup赋值给childGroup'
    ]},
    {'channel(Class<? extends C> channelClass)':[
        '继承自父类AbstractBootstrap',
        {'创建内部类BootstrapChannelFactory<T extends Channel>':[
            {'newChannel()':[
                '反射创建channel实例'
            ]}
        ]}
    ]},
    {'option(ChannelOption<T> option, T value)':[
        '将其存入options'
    ]},
    {'handler(ChannelHandler handler)':[
        'handler赋值给handler'
    ]},
    {'childHandler(ChannelHandler childHandler)':[
        'childHandler赋值给childHandler'
    ]},
    {'bind(SocketAddress localAddress)':[
        '服务器在bind方法里启动完成',
        '核心方法doBind(localAddress)'
    ]}
],
'内部类ServerBootstrapAcceptor':[
    {'channelRead(ChannelHandlerContext ctx, Object msg)':[
        '1.msg强转成Channel，实际是NioSocketChannel',
        '2.添加NioSocketChannel的pipeline的handler',
        '3.设置NioSocketChannel的各种属性',
        'childGroup.register(child)',
        '4.将该NioSocketChannel注册到childGroup中的一个EventLoop上，并添加一个监听器',
        '5.childGroup是main方法创建的数组workerGroup',
    ]}
],
'doBind(localAddress)':[
    {'initAndRegister()':[
        '反射创建NioServerSocketChannel及其相关的NIO的对象,pipeline,unsafe,同时为pipeline初始head节点和tail节点',
        {'channelFactory().newChannel()':[
            '通过工厂反射创建一个NioServerSocketChannel对象,初始化其ChannelPipeline',
            '1.通过NIO的SelectorProvider的openServerSocketChannel方法得到JDK的channel',
            '后续让Netty包装JDK的channel',
            '2.创建一个唯一的ChannelId，创建了一个NioMessageUnsafe，用于操作消息',
            '3.创建一个DefaultChannelPipeline管道，双向链表结构，用于过滤所有进出的消息',
            '4.创建一个NioServerSocketChannelConfig对象，用于对外展示一些配置'
        ]},
        {'init(channel)':[
            '初始化这个NioServerSocketChannel对象',
            '获得channel的ChannelPipeline，将handler封装进AbstractChannelHandlerContext对象',
            '将AbstractChannelHandlerContext对象添加到ChannelPipeline'
        ]},
        {'group().register(channel)':[
            '注册NioServerSocketChannel对象到Selector',
            '最终调用AbstractNioChannel#doRegister'
        ]}
    ]},
    {'doBind0()':[
        '对JDK的channel和端口进行绑定，完成Netty服务器的所有启动，并开始监听连接事件',
        'channel.bind(localAddress, promise).addListener(ChannelFutureListener.CLOSE_ON_FAILURE)'
    ]}
]



}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 