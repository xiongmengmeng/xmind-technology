import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="netty"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("ChannelPipeline")
r2=s2.getRootTopic()
r2.setTitle("ChannelPipeline")


content={
'ChannelInboundInvoker':[
    '针对出站方法，在出站handler的外层再包装一层，达到在方法前后拦截并做一些特定操作的目的'
],
'ChannelOutboundInvoker':[
    '针对入站方法，在入站handler的外层再包装一层，达到在方法前后拦截并做一些特定操作的目的'
],
'ChannelPipeline':[
    '实现ChannelInboundInvoker, ChannelOutboundInvoker接囗',
    {'addLast(EventExecutorGroup group, String name, ChannelHandler handler)':[
        '如handler是耗时操作，可将其放入一个线程池group中执行'
    ]}
],
'DefaultChannelPipeline':[
    {'DefaultChannelPipeline(Channel channel)':[
        '将channel赋值给channel字段，用于pipeline操作channel',
        '创建一个future和promise，用于异步回调使用',
        '创建一个inbound的tailContext，创建一个既是inbound类型又是outbound类型的 headContext',
        '最后，将两个Context互相连接，形成双向链表',
    ]},
    {'bind(java.net.SocketAddress, io.netty.channel.ChannelPromise)':[
        'tail.bind(localAddress, promise)'
    ]},
    {'bind(ChannelHandlerContext ctx, SocketAddress localAddress, ChannelPromise promise)':[
        'unsafe.bind(localAddress, promise);',
        'unsafe为内部类HeadContext的属性，值为pipeline.channel().unsafe()',
        '此处为AbstractNioMessageChannel'
    ]},
    {'fireChannelRead(Object msg)':[
        'AbstractChannelHandlerContext.invokeChannelRead(head, msg);'
    ]},
    {'channelRead(ChannelHandlerContext ctx, Object msg)':[
        'ctx.fireChannelRead(msg)'
    ]},
    {'addLast(ChannelHandler handler)':[
        'addLast(null, handler)->',
        'addLast(null, name, handler)'
    ]},
    {'addLast(EventExecutorGroup group, String name, ChannelHandler handler)':[
        {'newCtx=newContext(group,filterName(name, handler),handler)':[
            '创建一个 Context'
        ]},
        {'addLast0(newCtx)':[
            '将Context追加到链表中'
        ]}
    ]}
],
'ChannelPipeline|ChannelHandler|ChannelHandlerContext创建过程':[
    {'Socket创建的时候创建pipeline':[
        '具体在AbstractChannel的构造器中'
    ]},
    {'add**添加处理器的时候创建Context**':[
        'DefaultChannelPipeline的addLast(ChannelHandler handler)方法'
    ]}
]


}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 