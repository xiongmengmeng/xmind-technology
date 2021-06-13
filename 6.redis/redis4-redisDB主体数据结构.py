import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="redis"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("redisDB主体数据结构")
r2=s2.getRootTopic()
r2.setTitle("redisDB主体数据结构")


content={
'redis':[
    {'数组结构--hash':[
        '数据：O(1)',
        '链表：O(n)'
    ]},
    {'使用':[
        '创建一个大的数组',
        'hash(key)/(arr.size-1):确定数据存放位置',
        'hash冲突：使用头插法来解决，形成链表'
    ]}
],
'redisDB':[
    {'dict *dict':[
        '字典'
    ]},
    {'expires':[
    ]},
    {'blocking_keys':[
    ]},
    {'ready_keys':[
    ]},
    {'watched_keys':[
    ]},
    {'id':[
    ]},
    {'avg_ttl':[
    ]},
],
'dict':[
    {'type':[
    ]},
    {'privdata':[
    ]},
    {'dictht ht[2]':[
        '两个hashtable',
        'ht[0]:正常使用的hashtable',
        'ht[1]:扩容时的hashtable，渐进式rehash'
    ]},
    {'rehashidx':[
    ]},
    {'iterators':[
    ]}, 
],
'扩容时，数据访问':[
    'ht[0]结点不存入，访问ht[1]',
    'ht[0]结点存在:搬相映桶的数据到ht[1]',
    '定时任务，每次搬部分数据'
],
'dictht':[
    {'dictEntry **table':[
        '一个数组'
    ]},
    {'long size':[
        'hashtable中的数组容量'
    ]},
    {'long sizemask':[
        'size-1',
        '插入数据时，key的hash&sizemask:位运算确定数据存入位置'
    ]},
    {'long used':[
        'hashtable中存储的数据量'
    ]},
],
'dictEntry':[
    {'void *key':[
        'key值的指针'
    ]},
    {'union':[
        {'void *val':[
            '指向一个数据结构是redisObject的指针'
        ]},
        {'uint64_t u64':[
        ]},
        {'int64_t s64':[
        ]},
        {'double d':[
        ]},
    ]},
    {'dictEntry *next':[
        'hash冲突时，下一个节点的指针(使用链表解决)'
    ]},
]

    
}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 