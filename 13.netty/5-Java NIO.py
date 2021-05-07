import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="netty"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("Java NIO")
r2=s2.getRootTopic()
r2.setTitle("Java NIO")


content={
'Java NIO组件':[
    '提供了统一的API，为大家屏蔽了底层的不同操作系统的差异'
],
'三个核心组件':[
    'Channel----通道',
    'Buffer----缓冲区',
    'Selector----选择器'
],
'NIO和OIO的对比':[
    'OIO是面向流（Stream Oriented）的，NIO是面向缓冲区（Buffer Oriented）的',
    'OIO操作是阻塞的，NIO操作是非阻塞的',
    'OIO没有选择器（Selector）概念，而NIO有选择器的概念(基于底层的选择器的系统调用)'
],
'Selector,Channel和Butfer的关系':[ 
    '1.每个Channel都会对应一个Buffer',
    '2.Selector对应一个线程，一个线程对应多个Channel(连接) ',
    '3.channel注册到Selector ',
    '4.Selector切换到哪个Channel是由事件决定的，Event是一个重要的概念',
    '5.Selector会根据不同的事件，在各个通道上切换',
    '6.Buffer是一个内存块，底层是一个数组',
    '7.数据的读取写入是通过Buffer(双向流动)',
    '8.channel是双向的，反映底层操作系统的情况(底层的操作系统通道是双向的) ' 
] 

}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 