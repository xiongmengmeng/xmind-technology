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

'Redis的键值都使用redisObject结构体保存':[],
'redisObject':[
    'refcount：键值被引用数量',
    {'type':[
        '键值的数据类型',
        'REDIS_STRING 0',
        'REDIS_LIST 1',
        'REDIS_SET 2',
        'REDIS_ZSET 3',
        'REDIS_HASH 4'
    ]},
    {'encoding':[
        '键值的内部编码方式',
        'REDIS_ENCODING_RAW 0',
        'REDIS_ENCODING_INT 1----Encoded as integer',
        'REDIS_ENCODING_HT 2---Encoded as hash table',
        'REDIS_ENCODING_ZIPMAP 3---Encoded as zipmap',
        'REDIS_ENCODING_LINKEDLIST 4---Encoded as regular linked list',
        'REDIS_ENCODING_ZIPLIST 5---Encoded as ziplist',
        'REDIS_ENCODING_INTSET 6---Encoded as intset',
        'REDIS_ENCODING_SKIPLIST 7---Encoded as skiplist'
    ]},
    'lru: lru time',
    'ptr:指向sdshdr类型的变量的地址'
],

    
}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 