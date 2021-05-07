import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="netty"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("Netty:Channel通道")
r2=s2.getRootTopic()
r2.setTitle("Netty:Channel通道")


content={
'定义':[
    '反应器的查询和分发的IO事件的来源',
    '每一种通信连接协议，Netty都实现了自己的通道'
],
'抽象类AbstractChannel':[
    {'构造器':[
        {'parent属性':[
            '对于每一条传输通道（如NioSocketChannel实例）',
            'parent属性的值为接收到该连接的服务器连接监听通道'
        ]},
        {'pipeline属性':[
            '一条通道，一条流水线,实际类型为DefaultChannelPipeline'
        ]}
    ]},
    {'几个重要方法':[
        {'ChannelFuture connect(SocketAddress address)':[
            '连接远程服务器,在客户端的传输通道使用'
        ]},
        {'ChannelFuture bind（SocketAddress address）':[
            '绑定监听地址，监听新的客户端连接,在服务器的新连接监听和接收通道使用'
        ]},
        {'ChannelFuture close()':[
            '关闭通道连接，返回连接关闭的ChannelFuture异步任务'
        ]},
        {'Channel read()':[
            '读取通道数据，并启动入站处理'
        ]},
        {'ChannelFuture write（Object o）':[
            '启程出站流水处理'
        ]},
        {'Channel flush()':[
            '将缓冲区中的数据立即写出到对端'
        ]}
    ]}
],
'AbstractNioChannel':[
    '属性SelectableChannel ch'
],
'NioSocketChannel类':[
    'TCP协议对应的传输通道类型',
    '对映服务器监听类NioServerSocketChannel'
]





}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 