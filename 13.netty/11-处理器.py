import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="netty"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("处理器")
r2=s2.getRootTopic()
r2.setTitle("处理器")


content={
'涉及环节':[
    '数据包解码',
    '业务处理',
    '目标数据编码',
    '把数据包写到通道中'
],
'分类':[
    '都继承了ChannelHandler处理器接口',
    {'ChannelInboundHandler通道入站处理器':[
        '默认实现为ChannelInboundHandlerAdapter(通道入站处理适配器)',
        'Handler业务处理器的各个方法的执行顺序和生命周期',
        {'主要操作':[
            {'handlerAdded()':[
                '当业务处理器被加入到流水线后，此方法被回调'
            ]},
            {'channelRegistered()':[
                '当通道成功绑定一个NioEventLoop线程后，会通过流水线回调所有业务处理器的channelRegistered()方法'
            ]},
            {'channelActive()':[
                '通道激活成功,所有的业务处理器添加、注册的异步任务完成，并且NioEventLoop线程绑定的异步任务完成'
            ]},
            {'channelRead()':[
                '有数据包入站，通道可读'
            ]},
            {'channelReadComplete()':[
                '流水线完成入站处理后'
            ]},
            {'channelInactive()':[
                '当通道的底层连接已经不是ESTABLISH状态，或者底层连接已经关闭时'
            ]},
            {'channelUnregistered()':[
                '通道和NioEventLoop线程解除绑定，移除掉对这条通道的事件处理之后'
            ]},
            {'handlerRemoved()':[
                'Netty会移除掉通道上所有的业务处理器后'
            ]} 
        ]}
    ]},
    {'ChannelOutboundHandler通道出站处理器':[
        '默认实现为ChanneloutBoundHandlerAdapter(通道出站处理适配器)',
        {'出站处理的方向':[
            '通过上层Netty通道，去操作底层Java IO通道'
        ]},
        {'主要操作':[
            {'bind()':[
                '监听地址（IP+端口）绑定：完成底层Java IO通道的IP地址绑定,用于服务器端'
            ]},
            {'connect()':[
                '连接服务端：完成底层Java IO通道的服务器端的连接操作,用于客户端'
            ]},
            {'write()':[
                '写数据到底层：完成Netty通道向底层Java IO通道的数据写入操作'
            ]},
            {'flush()':[
                '腾空缓冲区中的数据，把这些数据写到对端'
            ]},
            {'read()':[
                '从底层读数据：完成Netty通道从Java IO通道的数据读取'
            ]},
            {'disConnect()':[
                '断开服务器连接：断开底层Java IO通道的服务器端连接,主要用于客户端'
            ]},
            {'close()':[
                '主动关闭通道：关闭底层的通道，例如服务器端的新连接监听通道'

            ]}
        ]}
    ]},
    {'ChannelInitializer通道初始化处理器':[
        '属于入站处理器的类型,向流水线中装配业务处理器',
        {'initChannel()方法':[
            '新连接通道作为参数，往它的流水线中装配Handler业务处理器'
        ]}
    ]}
]

}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 