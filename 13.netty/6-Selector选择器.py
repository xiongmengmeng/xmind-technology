import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="netty"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("选择器Selector")
r2=s2.getRootTopic()
r2.setTitle("选择器Selector")


content={

'定义':[
    '通过选择器，一个线程可以查询多个通道的IO事件的就绪状态',
    '选择器和通道的关系，是监控和被监控的关系',
],
'注册':[
    '通道和选择器之间的关系，通过Channel.register（Selector sel, int ops）方法完成注册',
    'register方法有两个参数：第一个参数，指定通道注册到的选择器实例；第二个参数，指定选择器要监控的IO事件类型'
],
'SelectableChannel可选择通道':[
    '必须继承SelectableChannel类(提供了实现通道的可选择性所需要的公共方法)'
],
'SelectionKey选择键':[
    '定义：那些被选择器选中的IO事件',
    {'作用':[
        '可以获得通道的IO事件类型，比方说SelectionKey.OP_READ',
        '获得发生IO事件所在的通道',
        '可以获得选出选择键的选择器实例'
    ]}
],
'选择器使用流程':[
    {'1.获取选择器实例':[
        '选择器实例是通过调用静态工厂方法open()来获取的'
    ]},
    {'2.将通道注册到选择器中':[
        '调用通道的register()方法，将通道注册到了一个选择器上'
    ]},
    {'3.轮询感兴趣的IO就绪事件（选择键集合）':[
        '1.通过Selector选择器的select()方法，选出已经注册的、已经就绪的IO事件，保存到SelectionKey选择键集合中',
        '2.SelectionKey集合保存在选择器实例内部，是一个元素为SelectionKey类型的集合（Set）,调用选择器的selectedKeys()方法，可以取得选择键集合',
        '3.处理完成后，需要将选择键从这个SelectionKey集合中移除，防止下一次循环的时候，被重复的处理'
    ]}
]

}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 