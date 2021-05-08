import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="netty"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("ChannelHandlerContext")
r2=s2.getRootTopic()
r2.setTitle("ChannelHandlerContext")


content={
'ChannelHandlerContext':[
    '实现ChannelInboundInvoker, ChannelOutboundInvoker接囗,继承了其方法',
    '定义自己的方法:获取Context上下文环境中对应的如channel,executor,handler,pipeline,内存分配器',
    '包装了handler相关的一切：方便Context在pipeline中操作handler',
],
'AbstractChannelHandlerContext':[
    {'bind(final SocketAddress localAddress, final ChannelPromise promise)':[
        'next.invokeBind(localAddress, promise);',
        {'invokeBind(localAddress, promise)':[
            '((ChannelOutboundHandler) handler()).bind(this, localAddress, promise);'
        ]}
    ]},
    {'fireChannelRead(final Object msg)':[
        'invokeChannelRead(findContextInbound(), msg);'
    ]},
    {'findContextInbound()':[
        'do {',
        '   ctx = ctx.next;',
        '} while (!ctx.inbound);',
        'return ctx;',
        '找出栈的ctx'     
    ]},
    {'invokeChannelRead(final AbstractChannelHandlerContext next, Object msg)':[
        'EventExecutor executor = next.executor();',
        'next.invokeChannelRead(m);'
    ]},
    {'invokeChannelRead(Object msg)':[
        '((ChannelInboundHandler) handler()).channelRead(this, msg)',
        '调用实际的hanler的channelRead方法',
        '方法内可能会调用ctx.fireChannelRead(msg),进行循环'
    ]},
],
'ChannelHandler':[
    '作用就是处理IO事件或拦截IO事件，并将其转发给下一个处理程序ChannelHandler',
    {'handlerAdded(ChannelHandlerContext ctx)':[
        '把 ChannelHandler 添加到 pipeline 时被调用'
    ]},
    {'handlerRemoved(ChannelHandlerContext ctx)':[
        '从 pipeline 中移除时调用'
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