import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="netty"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("Netty:Pipeline流水线")
r2=s2.getRootTopic()
r2.setTitle("Netty:Pipeline流水线")


content={

'ChannelPipeline':[
    '一个Handler的集合，负责拦截inbound和outbound事件和操作',
    '像一条管道，将绑定到一个通道的多个Handler处理器实例，串在一起，形成一条流水线',
    '基于【责任链设计模式】设计，内部是一个【双向链表】，支持动态地添加和删除Handler业务处理器',
    {'细节':[
        '入站事件和出站事件在一个双向链表中',
        '入站事件会从链表head往后传递到最后一个入站的handler'
        '出站事件从会链表tail往前传递到最前一个出站的handler',
        '两种类型的handler互不干扰'
    ]},
    {'方法':[
        {'addFirst(String name, ChannelHandler handler)':[
            '把一个业务处理类添加到链中的第一个位置'
        ]},
        {'addLast(String name, ChannelHandler handler)':[
            '把一个业务处理类添加到链中的最后一个位置'
        ]}
    ]},
    {'截断流水线':[
        {'入站':[
            '在channelRead方法中，不再调用父类的channelRead入站方法或不调用ctx.fireChannelXxx()'
        ]},
        {'出站':[
            '流程只要开始执行，就不能被截断',
            '强行截断话，Netty会抛出异常',
            '如果业务条件不满足，可以不启动出站处理'
        ]}
    ]},
],
'ChannelHandlerContext上下文':[
    '在Handler处理器被添加到流水线时创建，代表了ChannelHandler通道处理器和ChannelPipeline通道流水线之间的关联',
    {'作用':[
        {'1.获取上下文所关联的Netty组件实例':[
            '如所关联的通道、所关联的流水线、上下文内部Handler业务处理器实例等'
        ]},
        {'2.入站和出站处理方法':[
            '只会从当前的节点开始执行Handler业务处理器，并传播到同类型处理器的下一节点'
        ]}
    ]},
    {'方法':[
        {'close()':[
            '关闭通道'
        ]},
        {'flush()':[
            '刷新'
        ]},
        {'writeAndFlush(Object msg)':[
            '将数据写入到ChannelPipeline中',
            '当前ChannelHandler的下一个ChannelHandler开始处理(出站)'
        ]}
    ]}
],
'Channel、Handler、ChannelHandlerContext三者关系':[
    'Channel通道拥有一条ChannelPipeline通道流水线',
    '每一个流水线节点为一个ChannelHandlerContext通道处理器上下文对象',
    '每一个上下文中包裹了一个ChannelHandler通道处理器',
    '在ChannelHandler通道处理器的入站/出站处理方法中，Netty都会传递一个Context上下文实例作为实际参数',
    '通过Context实例的实参,可获取ChannelPipeline通道流水线的实例或Channel通道的实例'
],




}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 