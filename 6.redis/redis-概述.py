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
'Reactor模式':[
    '多个套接字',
    'IO多路复用程序',
    '文件事件分派器',
    '事件处理器'
],
'五种基础类型':[
    '字符串类型',
    '散列类型',
    '列表类型',
    '集合类型',
    '有序集合类型'
],
'LUA脚本':[
    '减少网络开销',
    '原子操作',
    '可复用',
    'RedisScript接口'
],
'过期策略':[
    '定时过期',
    '惰性过期',
    '定期过期'
],
'数据持久化':[
    'RDB',
    'AOF'
],
'主从复制':[
    '多副本',
    '避免单点故障',
    '读写分离，提高服务器负载'
],
'哨兵':[
    '故障自动切换'
],
'分片集群':[
    '横向扩展',
    '支撑更大的写流量'
],
'与spring结合':[
    'RedisTemplate'
],
'缓存异常':[

]

    
}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 