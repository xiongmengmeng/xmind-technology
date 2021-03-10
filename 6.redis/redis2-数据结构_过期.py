import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="redis"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("数据结构")
r2=s2.getRootTopic()
r2.setTitle("数据结构")


content={
'数据结构':[
    'Redis的键值都使用redisObject结构体保存',
    {'redisObject':[
        'refcount：键值被引用数量',
        'type字：键值的数据类型',
        'encoding：键值的内部编码方式',
        'lru: lru time',
        'ptr:指向sdshdr类型的变量的地址'
    ]},
    {'sdshdr类型的变量':[
        '来存储字符串',
        'len：字符串的长度',
        'free：buf中的剩余空间',
        'buf：字符串的内容'
    ]}
],
'LUA脚本':[
    '减少网络开销（一个脚本只发送一个请求）',
    '原子操作',
    '可复用',
    'https://blog.csdn.net/qq_39172525/article/details/105779727'
],
'过期':[
    {'过期策略':[
        '定时过期：每个设置过期时间的key需创建一个定时器，过期立即清除，占用cpu',
        '惰性过期：当访问一个key时，才判断key是否过期，过期则清除,占用内存',
        '定期过期：隔段时间，扫描一定数量的expires字典中一定数量的key，清除其中已过期key'
    ]},
    'Redis中同时使用了惰性过期和定期过期两种过期策略',
    {'Redis内存淘汰策略':[
        '内存不足时，怎么处理需要新写入且需要申请额外空间的数据',
        {'全局的键空间选择性移除':[
            'noeviction：内存不足时，新写入操作会报错',
            'allkeys-lru：内存不足时，在键空间中，移除最近最少使用的key(最常用)',
            'allkeys-random：内存不足时，在键空间中，随机移除某个key'
        ]},
        {'设置过期时间的键空间选择性移除':[
            'volatile-lru：内存不足时，在设置了过期时间的键空间中，移除最近最少使用的key',
            'volatile-random：内存不足时，在设置了过期时间的键空间中，随机移除某个key',
            'volatile-ttl：内存不足时，在设置了过期时间的键空间中，有更早过期时间的key优先移除'
        ]}
    ]}
]
    
}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 