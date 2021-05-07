import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="netty"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("源码分析")
r2=s2.getRootTopic()
r2.setTitle("源码分析")


content={
'ServerBootstrap':[
    {'属性':[
        {'EventLoopGroup group':[
            '继承自父类AbstractBootstrap'
        ]},
        {'EventLoopGroup childGroup':[
            ''
        ]},
        {'Map<ChannelOption<?>, Object> options':[
            '存放option()方法传入的tcp参数'
        ]},
        {'ChannelHandler handler':[
            '继承自父类AbstractBootstrap'
        ]},
        {'ChannelHandler childHandler':[
            ''
        ]}
    ]},
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
'doBind(localAddress)':[
    {'initAndRegister()':[
        {'channelFactory().newChannel()':[
            '通过工厂反射创建一个NioServerSocketChannel对象,初始化其ChannelPipeline'
        ]},
        {'init(channel)':[
            '初始化这个NioServerSocketChannel对象',
            '获得channel的ChannelPipeline，将handler封装进AbstractChannelHandlerContext对象',
            '将AbstractChannelHandlerContext对象添加到ChannelPipeline'
        ]},
        {'group().register(channel)':[
            '注册NioServerSocketChannel对象'
        ]}
        '',
        ''
    ]},
    {'doBind0()':[
        '对JDK的channel和端囗进行绑定'
    ]}
]
'NioEventLoopGroup':[
    {'':[
        {'EventExecutor[] children':[
            '继承自父类MultithreadEventExecutorGroup'
        ]}
    ]}
    {'构造器':[
        '默认线程个数n:Runtime.getRuntime().availableProcessors() * 2,CPU核数的2倍'
        '创建指定线程数的执行器组children=new EventExecutor[n]',
        '初始化执行器组，添加元素为NioEventLoop实例(实例化时，会初始化一个Selector)'
        '每个NioEventLoop实例添加一个关闭监听器'
    ]}
]

}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 