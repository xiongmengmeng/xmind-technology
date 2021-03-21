import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="netty"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("Netty:通道Channel,反应器")
r2=s2.getRootTopic()
r2.setTitle("Netty:通道Channel,反应器")


content={

'组件':[
    '服务器启动器',
    '缓冲区',
    '反应器',
    'Handler业务处理器',
    'Future异步任务监听',
    '数据传输通道'
],
'Channel通道':[
    {'定义':[
        '反应器的查询和分发的IO事件的来源',
        '每一种通信连接协议，Netty都实现了自己的通道'
    ]},
    {'抽象类AbstractChannel':[
        {'构造器':[
            'parent属性:对于每一条传输通道（如NioSocketChannel实例），parent属性的值为接收到该连接的服务器连接监听通道',
            'pipeline属性:一条通过，一条流水线'
        ]},
        {'几个重要方法':[
            {'ChannelFuture connect(SocketAddress address)':[
                '连接远程服务器,在客户端的传输通道使用'
            ]},
            {'ChannelFuture bind（SocketAddress address）':[
                '绑定监听地址，开始监听新的客户端连接,在服务器的新连接监听和接收通道使用'
            ]},
            {'ChannelFuture close()':[
                '关闭通道连接，返回连接关闭的ChannelFuture异步任务'
            ]},
            {'Channel read()':[
                '读取通道数据，并且启动入站处理'
            ]},
            {'ChannelFuture write（Object o）':[
                '启程出站流水处理'
            ]},
            {'Channel flush()':[
                '将缓冲区中的数据立即写出到对端'
            ]}
        ]}
    ]},
    {'EmbeddedChannel（嵌入式通道）':[
        '模拟入站与出站的操作，底层不进行实际的传输，不需要启动Netty服务器和客户端,辅助测试使用'
    ]},
    {'NioSocketChannel类':[
        '继承自Java NIO的SelectableChannel',
        'TCP协议对应的传输通道类型',
        '对映服务器监听类NioServerSocketChannel'
    ]}
],
'反应器':[
    {'定义':[
        '服务器通道新连接的IO事件的监听:一个反应器通过Selector选择器不断地查询注册过的IO事件（选择键）',
        '传输通道的IO事件:如果查询到IO事件，分发给Handler业务处理器',
        '为了及时接受（Accept）到新连接，在服务器端，一般有两个独立的反应器，一个反应器负责新连接的监听和接受，另一个反应器负责IO事件处理'
    ]},
    {'NioEventLoop':[
        '对应于NioSocketChannel通道',
        {'两个重要的成员属性':[
            'Thread线程类：负责一个Java NIO Selector选择器的IO事件轮询',
            'Java NIO选择器Selector类'
        ]}
    ]}
]



}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 