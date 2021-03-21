import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="netty"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("前言")
r2=s2.getRootTopic()
r2.setTitle("前言")


content={

'netty':[
    '一个提供异步的、事件驱动的网络应用程序框架，所有IO操作都是异步非阻塞的',
    '通过Future-Listener机制，用户可以方便地主动获取或者通过通知机制获得IO操作结果'
],
'redis':[
    'Remote Dictionary Server（远程字典服务器）'
],
'ZooKeeper':[
    '分布式协调工具'
],
'高并发IM':[
    '一切高实时性通信、消息推送的应用场景',
    '如：私信、聊天、大规模推送、视频会议、抽奖、互动游戏、基于位置的应用（Uber、滴滴司机位置）、在线教育' 
]

}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 