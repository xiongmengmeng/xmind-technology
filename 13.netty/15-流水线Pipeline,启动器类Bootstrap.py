import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="netty"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("流水线Pipeline,启动器类Bootstrap")
r2=s2.getRootTopic()
r2.setTitle("流水线Pipeline,启动器类Bootstrap")


content={
'流水线Pipeline':[
    {'ChannelPipeline（通道流水线）':[
        '像一条管道，将绑定到一个通道的多个Handler处理器实例，串在一起，形成一条流水线',
        '基于责任链设计模式设计，内部是一个双向链表，支持动态地添加和删除Handler业务处理器'
    ]},
    {'ChannelHandlerContext上下文':[
        '在Handler业务处理器被添加到流水线中时创建，代表了ChannelHandler通道处理器和ChannelPipeline通道流水线之间的关联',
        {'作用':[
            '1.获取上下文所关联的Netty组件实例:如所关联的通道、所关联的流水线、上下文内部Handler业务处理器实例等',
            '2.入站和出站处理方法:只会从当前的节点开始执行Handler业务处理器，并传播到同类型处理器的下一站（节点）'
        ]}
    ]},
    {'Channel、Handler、ChannelHandlerContext三者的关系':[
        'Channel通道拥有一条ChannelPipeline通道流水线'
        '每一个流水线节点为一个ChannelHandlerContext通道处理器上下文对象',
        '每一个上下文中包裹了一个ChannelHandler通道处理器',
        '在ChannelHandler通道处理器的入站/出站处理方法中，Netty都会传递一个Context上下文实例作为实际参数',
        '通过Context实例的实参，在业务处理中，可以获取ChannelPipeline通道流水线的实例或者Channel通道的实例'
    ]},
    {'截断流水线':[
        {'入站':[
            '在channelRead方法中，不再调用父类的channelRead入站方法或不调用ctx.fireChannelXxx()'
        ]},
        {'出站':[
            '流程只要开始执行，就不能被截断。强行截断的话，Netty会抛出异常。如果业务条件不满足，可以不启动出站处理'
        ]}
    ]},
    {'Handler业务处理器的热拔插':[
        '动态地增加、删除流水线上的业务处理器Handler'
    ]}
],
'启动器类Bootstrap':[
    {'作用':[
        '一个组装和集成器，将不同的Netty组件组装在一起',
        '为组件设置好对应的参数，最后实现Netty服务器的监听和启动'
    ]},
    {'分类':[
        'ServerBootstrap:server专用',
        'Bootstrap:client专用'
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
    {'EventLoopGroup线程组':[
        '一个多线程版本的反应器'
    ]},
    {'服务器端启动器的使用':[
        '1.创建反应器线程组，并赋值给ServerBootstrap启动器实例',
        '2.设置通道的IO类型',
        '3.设置监听端口',
        '4.设置传输通道的配置选项',
        '5.装配子通道的Pipeline流水线',
        '6.开始绑定服务器新连接的监听端口',
        '7.自我阻塞，直到通道关闭',
        '8.关闭EventLoopGroup'
    ]},
    {'ChannelOption通道选项':[
        '1．SO_RCVBUF, SO_SNDBUF'
        '2.TCP_NODELAY:立即发送数据',
        '3．SO_KEEPALIVE:底层TCP协议的心跳机制',
        '4．SO_REUSEADDR:地址复用'
    ]}
]
}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 