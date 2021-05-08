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
    {'handlerAdded(ChannelHandlerContext ctx)':[
        'initialize(ctx)'
    ]},
    {'initialize(ChannelHandlerContext ctx)':[
        'System.nanoTime()//纳秒，十亿分之一'
    ]}
]




}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 