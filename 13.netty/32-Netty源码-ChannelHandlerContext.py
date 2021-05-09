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
        '找出栈的ctx'     
    ]},
    {'invokeChannelRead(final AbstractChannelHandlerContext next, Object msg)':[
        {'得到通道所在的eventloop':[
            'EventExecutor executor = next.executor()'
        ]},
        {'判executor线程与eventloop是否在同一线程':[
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
],
'异步处理handler':[
    {'两种方式':[
        'handler中加入线程池',
        'Context中添加线程池'
    ]},
    {'handler中加入线程池':[
        '在handler的channelRead方法进行异步', 
        '将耗时操作放入线程池',
        '执行完耗时任务',
        'context的write方法,此任务会交给IO线程'
    ]},
    {'Context中添加线程池':[
        '在添加pipeline中的handler时候，添加一个业务线程池',
        '创建ctx时,属性executor为封装后的线程池',
        '后续执行ctx，使用业务线程池'
    ]},
    {'两种方式比较':[
        {'handler中加入线程池':[
            '更自由,比如访问数据库,就异步,不需要,就不异步,异步会拖长接口响应时间',
            '因需要将任务放进mpscTask中,如IO时间短,task多,会导致响应时间达不到指标'
        ]},
        {'Context中添加线程池':[
            'Netty 标准方式(即加入到队列)',
            '将整个handler交给业务线程池,不论耗时不耗时,都加入到队列里,不够灵活'
        ]}
    ]}
]


}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 