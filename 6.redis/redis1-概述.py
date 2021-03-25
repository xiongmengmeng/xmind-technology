import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="redis"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("概述")
r2=s2.getRootTopic()
r2.setTitle("概述")


content={

'redis是什么':[
    '一个高性能的key-value数据库(非关系型)',
    '为了解决高并发、高扩展，大数据存储等一系列的问题而产生的数据库解决方案',
],
'特点':[
    {'单线程':[
        '避免了不必要的上下文切换和竞争条件,队列技术将并发访问变为串行访问'
    ]},
    {'数据类型丰富':[
        '键的类型只能为字符串，值支持5种数据类型：字符串、列表、集合、散列表、有序集合',
        '单个value的最大限制是1GB'
    ]},
    {'基于内存':[
        'CPU不是Redis的瓶颈，瓶颈可能是内存大小或网络带宽，类似于HashMap，查找和操作的时间复杂度都是O(1)'
    ]}
],
'Memcache与Redis的区别':[
    '1.Memecache把数据全部存在内存之中，断电后会挂掉，数据不能超过内存大小',
    'Redis有部份存在硬盘上，这样能保证数据的持久性',
    '2.数据支持类型 Memcache对数据类型支持相对简单。Redis有复杂的数据类型',
    '3.底层模型不同：Redis直接自己构建了VM 机制 ，因为一般的系统调用系统函数的话，会浪费一定的时间去移动和请求',

],
'redis适用于的场景':[
    '会话缓存（Session Cache），优势快且可持久化',
    '队列: list 和 set 操作,可做为broker',
    '排行榜/计数器:集合（Set）和有序集合（Sorted Set）',
    '分布式锁:Redis自带的SETNX 命令',
    {'实现延时队列':[
        '使用sortedset，拿时间戳作为score,消息内容作为key调用zadd来生产消息',
        '消费者用zrangebyscore指令获取N秒之前的数据轮询进行处理'
    ]}
],
'实际应用':[
    'id自增',
    '缓存：四级地址',
    '分布式锁'
]
'主键失效和淘汰策略':[
    '适用场景:去重、赞、踩、共同好友',
    '内部使用值为空的散列表实现',
    '增加/删除元素:sadd key member1 member2',
    'srem key member1 member2',
    '获得集合中的所有元素:smembers key'
],
'Redis分布式锁':[

]


    
}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 