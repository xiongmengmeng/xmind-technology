import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="netty"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("Netty:Bootstrap启动器")
r2=s2.getRootTopic()
r2.setTitle("Netty:Bootstrap启动器")


content={

'作用':[
    '一个组装和集成器，将不同的Netty组件组装在一起',
    '为组件设置好对应的参数，最后实现Netty服务器的监听和启动'
],
'分类':[
    'ServerBootstrap:server专用',
    'Bootstrap:client专用'
],
'属性':[
    {'EventLoopGroup线程组':[
        '一个多线程版本的反应器'
    ]},
    {'父子通道':[
        {'定义':[
            '有接收关系的NioServerSocketChannel和NioSocketChannel'
        ]},
        {'父通道（ParentChannel）':[
            'NioServerSocketChannel负责服务器连接监听和接收'
        ]},
        {'子通道（ChildChannel）':[
            '对应于每一个接收到的NioSocketChannel传输类通道'
        ]}
    ]},
],
'常用方法':[
    {'group(EventLoopGroup partentGroup,EventLoopGroup childGroup)':[
        '设置两个EventLoopGroup'
    ]},
    {'channel(Class channelClass)':[
        '设置服务器的通道实现',
    ]},
    {'option(ChannelOption co,T value)':[
        '给serverChannel添加配置'
    ]},
    {'childOption()':[
        '给接收到的通道添加配置'
    ]},
    {'childHandle(ChannelHandler ch)':[
        '设置业务处理类'
    ]},
    {'bind(int inetPort)':[
        '占用端囗，返回ChannelFuture，用于服务器端'
    ]},
    {'connect(String host,int inetPort)':[
        '连接服务器，返回ChannelFuture，用于客户端'
    ]}
],
'服务器端启动器的使用':[
    {'实例化ServerBootstrap':[
        'ServerBootsrap b=new ServerBootstrap()'
    ]},
    {'1.创建反应器线程组，并赋值给ServerBootstrap启动器实例':[
        'EventLoopGroup bossLoopGroup=New NioEventLoopGroup(1)',
        'EventLoopGroup workLoopGroup=New NioEventLoopGroup(1)',
        'b.group(bossLoopGroup,workLoopGroup)'
    ]},
    {'2.设置通道的IO类型':[
        'b.channel(NioServerSocketChannel.class)'
    ]},
    {'3.设置监听端口':[
        'b.localAddress(new InetSocketAddress(port))'
    ]},
    {'4.设置传输通道的配置选项':[
        'b.option(ChannelOption.SO_KEEPALIVE, true):开启TCP底层心跳机制',
        'b.option(ChannelOption.ALLOCATOR, PooledByteBufAllocator.DEFAULT)',
        {'ChannelOption通道选项':[
            '1．SO_RCVBUF, SO_SNDBUF:TCP连接的缓冲区大小',
            '2. TCP_NODELAY:立即发送数据',
            '3．SO_KEEPALIVE:底层TCP协议的心跳机制'
        ]},
    ]},
    {'5.装配子通道的Pipeline流水线':[
        'b.childHandler(ChannelHandler childHandler)'
    ]},
    {'6.开始绑定服务器新连接的监听端口':[
        'b.bind(int inetPort)'
    ]},
    '7.自我阻塞，直到通道关闭',
    '8.关闭EventLoopGroup'
]
}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 