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
    {'属性':[
        {'EventExecutor executor':[
            '将ctx添加到别的线程池中时，此值不空，为线程池'
        ]}
    ]},
    {'executor()':[
        {'executor是否为空':[
            'executor == null',
            {'是':[
                '返回eventloop',
                'return channel().eventLoop()'
            ]},
            {'否':[
                'return executor;'
            ]}
        ]}
    ]},
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
        '找入栈的ctx'     
    ]},
    {'invokeChannelRead(final AbstractChannelHandlerContext next, Object msg)':[
        {'得到通道所在的eventloop':[
            'EventExecutor executor = next.executor()'
        ]},
        {'判当前线程与eventloop是否在同一线程':[
            'executor.inEventLoop()',
            {'是':[
                'next.invokeChannelRead(m);'
            ]},
            {'否':[
                'executor.execute(()->next.invokeChannelRead(m))'
            ]}
        ]}
    ]},
    {'invokeChannelRead(Object msg)':[
        '((ChannelInboundHandler) handler()).channelRead(this, msg)',
        '调用实际的hanler的channelRead方法',
        '方法内可能会调用ctx.fireChannelRead(msg),进行循环'
    ]},
    {'writeAndFlush(Object msg)':[
        'writeAndFlush(msg, newPromise())->write(msg, true, promise)'
    ]},
    {'write(Object msg, boolean flush, ChannelPromise promise)':[
        {'判定下个outbound的executor线程是否是当前线程':[
            'EventExecutor executor = next.executor()',
            'executor.inEventLoop()',
            {'是':[
                '调用next.invokeWriteAndFlush(m, promise);'
            ]},
            {'否':[
                '当前的工作封装成task,然后放入mpsc队列，等待IO任务执行完后执行队列中的任务',
                'AbstractWriteTask task=WriteAndFlushTask.newInstance(next, m, promise)',
                'safeExecute(executor, task, promise, m)'
            ]}
        ]}
    ]},
    {'safeExecute(EventExecutor executor, Runnable runnable, ChannelPromise promise, Object msg)':[
        '将任务提交到mpsc队列',
        'executor.execute(runnable)'
    ]}
],



}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 