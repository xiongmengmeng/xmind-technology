import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="redis"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("redis")
r2=s2.getRootTopic()
r2.setTitle("redis")


content={
'是什么':[],
'使用场景':[],
'5种数据类型':[
    '字符串类型',
    '散列类型',
    '列表类型',
    '集合类型',
    '有序集合类型'
],
'其它数据类型':[
    'bitmap',
    'Geospatial',
    'Hyperloglog'
],
'数据结构':[
    'redisObject'
],
'LUA脚本':[],
'过期删除策略':[
    '定时过期',
    '惰性过期',
    '定期过期'
],
'内存淘汰策略(8种)':[],
'reactor模式':[
    '多个套接字',
    'IO多路复用程序',
    '文件事件分派器',
    '事件处理器'
],
'持久化':[
    'RDB',
    'AOF'
],
'集群':[
    '主从复制',
    '哨兵',
    '分片集群'
],
'缓存使用':[
    '更新'
],
'缓存异常':[
    '缓存击穿',
    '缓存穿透',
    '缓存雪崩'
],
'代码使用':[
    '与spring结合:RedisTemplate',
    {'分布式锁':[
        'setnx',
        'redissionLock'
    ]}
],
'集群元数据维护':[
    '集中式',
    'gossip协议'
],
'分布式寻址算法':[
    'hash算法',
    '一致性hash算法+虚拟节点',
    'hash slot算法',
],
'redis cluster':[
    '集群伸缩',
    '客户端路由:直连'
],
'集群选举':[
    '哨兵模式',
    'cluster模式'
]


    
}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 