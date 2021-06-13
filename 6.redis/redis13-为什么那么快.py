import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="redis"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("redis为什么那么快")
r2=s2.getRootTopic()
r2.setTitle("redis为什么那么快")


content={
'应用维度':[
    '缓存使用',
    '集群运用',
    '数据结构的巧妙使用'
],
'系统维度':[
    {'高性能':[
        '线程模型',
        '网络IO模型',
        '数据结构',
        
    ]},
    {'高可用':[
        '持久化机制'
        '主从复制',
        '哨兵集群',
        'Cluster分片集群'
    ]},
    {'高拓展':[
        '负载均衡'
    ]}
],
'redis为什么那么快':[
    {'1.基于内存操作':[
        '一般是简单的存取操作'
    ]},
    {'2.IO多路复用':[
        '非阻塞IO',
        '单线程轮询描述符，将数据库的开、关、读、写都转换成了事件',
        'Redis采用自己实现的事件分离器，效率较高'
    ]},
    {'3.单线程':[
        '保证每个操作的原子性，也减少了线程的上下文切换和竞争'
    ]},
    {'4.高效的数据结构':[
        {'redisDB主体数据结构':[
            '一个全局哈希表，查找时间复杂度是O(1)'
        ]},
        {'rehash':[
            '防止哈希冲突导致链表过长',
            '扩充哈希桶数量，减少哈希冲突'
        ]},
        {'渐进式rehash':[
            '防止一次性重新映射数据过大导致线程阻塞',
            '将一次性拷贝分摊到多次请求过程，避免阻塞'
        ]},
        {'特殊的数据结构，对数据存储进行优化':[
            '如压缩表，对短数据进行压缩存储',
            '如跳表，使用有序的数据结构加快读取的速度',
            '根据实际存储的数据类型选择不同编码'
        ]}
    ]}
]
}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 