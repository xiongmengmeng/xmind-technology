import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="netty"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("异步处理handler")
r2=s2.getRootTopic()
r2.setTitle("异步处理handler")


content={
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