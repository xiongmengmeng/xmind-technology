import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="netty"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("Java NIO-选择器Selector")
r2=s2.getRootTopic()
r2.setTitle("Java NIO-选择器Selector")


content={
'定义':[
    '通过选择器，一个线程可以查询多个通道的IO事件的就绪状态',
    '选择器和通道的关系，是监控和被监控的关系',
],
'注册':[
    'Channel.register（Selector sel, int ops）',
    {'方法参数':[
        'Selector sel：指定通道注册到的选择器实例',
        'int ops:选择器要监控的IO事件类型',
        {'IO事件类型':[
            '1.可读：SelectionKey.OP_READ',
            '2.可写：SelectionKey.OP_WRITE',
            '3.连接：SelectionKey.OP_CONNECT',
            '4.接收：SelectionKey.OP_ACCEPT'
        ]}
    ]}
],
'SelectableChannel可选择通道':[
    '一条通道若能被选择，必须继承SelectableChannel类'
],
'SelectionKey选择键':[
    '那些被选择器选中的IO事件',
    {'作用':[
        '获得通道的IO事件类型，比方说SelectionKey.OP_READ',
        '获得发生IO事件所在的通道',
        '获得选出选择键的选择器实例'
    ]}
]
}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 