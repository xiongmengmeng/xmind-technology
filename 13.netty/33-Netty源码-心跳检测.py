import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="netty"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("心跳检测")
r2=s2.getRootTopic()
r2.setTitle("心跳检测")


content={
'IdleStateHandler':[
    '处理空闲状态的处理器',
    {'属性':[
        {'boolean observeOutput':[
            '是否考虑出站时较慢的情况, 默认false'
        ]},
        {'long readerIdleTimeNanos':[
            '读事件空闲时间，0则禁用事件'
        ]},
        {'long writerIdleTimeNanos':[
            '写事件空闲时间，0则禁用事件'
        ]},
        {'long allIdleTimeNanos':[
            '读或写空闲时间，0则禁用事件'
        ]}
    ]},
    {'IdleStateHandler(long readerIdleTime, long writerIdleTime, long allIdleTime,TimeUnit unit)':[
        {'long readerIdleTime':[
            '表示多长时间没有读, 会发送一个心跳检测包检测是否连接'
        ]},
        {'long writerIdleTime':[
            '表示多长时间没有写, 会发送一个心跳检测包检测是否连接'
        ]},
        {'long allIdleTime':[
            '表示多长时间没有读写, 会发送一个心跳检测包检测是否连接'
        ]},
        '当IdleStateEvent触发后,会传递给管道的下一个handler去处理',
        '通过调用(触发)下一个handler的userEventTiggered()',
        '在该方法中去处理IdleStateEvent(读空闲，写空闲，读写空闲)'
    ]},
    {'handlerAdded(ChannelHandlerContext ctx)':[
        'initialize(ctx)'
    ]},
    {'initialize(ChannelHandlerContext ctx)':[
        'System.nanoTime()//纳秒，十亿分之一',
        '给定的参数大于 0， 就创建一个定时任务， 每个事件都创建'
    ]},
    {'3个定时任务类':[
        '对应读,写，读或写事件,共有一个父类(AbstractIdleTask)',
        {'AbstractIdleTask':[
            '提供一个模板方法run(ChannelHandlerContext ctx)'
        ]},
        {'ReaderIdleTimeoutTask':[
            {'run(ChannelHandlerContext ctx)':[
                '1.得到用户设置的超时时间',
                {'2.判断读间隔时间是否超过设定时间':[
                    {'超过':[
                        '放入队列',
                        '创建一个IdleStateEvent类型的事件对象',
                        '将此对象传递下个handler的UserEventTriggered方法'
                    ]},
                    {'不超过':[
                        '放入队列'
                    ]}
                ]},
            ]}
        ]}
    ]},
    {'实现基于EventLoop的定时任务':[
        '每次读写都会记录一个值',
        '在定时任务运行时，计算当前时间-设置时间-上次事件发生时间的结果，来判断是否空闲'
    ]}
]




}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 