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
    '一个java开源框架',
    '一个提供【异步】的、【事件驱动】的【网络通信框架】，所有IO操作都是【异步非阻塞】的',
    '主要针对TCP协议，面向客户端的高并发应用',
    '本质是一个NIO框架，适用于服务器通讯相关的各种场景'
    '通过Future-Listener机制，用户可方便地主动获取或者通过通知机制获得IO操作结果',
    {'应用(高并发网络通讯)':[
        'Kafka、RocketMQ等消息中间件',
        'ElasticSearch开源搜索引擎',
        '大数据处理Hadoop的RPC框架Avro',
        '主流的分布式通信框架Dubbo'
    ]},
    {'学习方向':[
        'TCP/IP',
        'JDK原生包(java io,网络编程)',
        'java NIO',
        'netty'
    ]},
    {'学习书籍':[
        'Netty In Action'
    ]}
],
'redis':[
    'Remote Dictionary Server（远程字典服务器）',
    {'应用':[
        '缓存（数据查询、短连接、新闻内容、商品内容等',
        '分布式会话（Session）',
        '聊天室的在线好友列表',
        '任务队列（秒杀、抢购、12306等）',
        '应用排行榜',
        '访问统计',
        '数据过期处理（可以精确到毫秒）'
    ]}
],
'ZooKeeper':[
    '分布式协调工具',
    {'实现了分布式环境的数据一致性':[
        '每时每刻我们访问ZooKeeper的树结构时，不同的节点返回的数据都是一致的'
    ]}
],
'高并发IM':[
    '适用一切高实时性通信、消息推送的应用场景',
    {'应用':[
        '私信、聊天',
        '大规模推送',
        '视频会议',
        '抽奖,互动游戏',
        '基于位置的应用（Uber、滴滴司机位置）',
        '在线教育'
    ]}
]

}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 