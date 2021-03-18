import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="java"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("map"")
r2=s2.getRootTopic()
r2.setTitle("map")


content={
'Set':[
    'Java 中是一个接口',
    {'HashSet':[
        '采用 Hashmap 的 key 来储存元素',
        '特点是无序的，基本操作都是 O(1) 的时间复杂度，很快'
    ]},
    {'LinkedHashSet':[
        'HashSet + LinkedList 的结构',
        '既拥有了 O(1) 的时间复杂度，又能够保留插入的顺序'
    ]},
    {'TreeSet':[
        '采用红黑树结构',
        '特点是可以有序，可以用自然排序或者自定义比较器来排序',
        '缺点就是查询速度没有 HashSet 快'
    ]}
],
'map':[
    '一个键值对 (Key - Value pairs)，其中 key 是不可以重复的',
    {'HashMap':[
        '与 HashSet 对应，无序，O(1)',
    ]},
    {'LinkedHashMap':[
        'HashMap + 双向链表 的结构',
        '落脚点是 HashMap，所以既拥有 HashMap 的所有特性还能有顺序'
    ]},
    {'TreeMap':[
        '有序的',
        '本质用二叉搜索树来实现的'
    ]}
],
'HashMap 实现原理':[
    '桶用数组来实现',
    'key->经过hash函数计算出一个hash值->模上数组的长度得到它在数组的index',
    {'哈希碰撞':[
        '不同key经过hash函数计算出了相关的hash值',
        '对map来说，不同key经过hash函数+模上数组的长度,计算出相关index'
    ]},
    {'HashMap 中是如何保证元素的唯一性':[
        'hashCode()+equals()'
    ]},
    {'哈希冲突':[
        {'Separate chaining':[
            '在发生碰撞的那个桶后面再加一条“链”来存储',
            '链表，红黑树（超过8）'
        ]},
        {'Open addressing':[
            '顺序查找，如果这个桶里已经被占了，那就按照“某种方式”继续找下一个没有被占的桶，直到找到第一个的',
            ''
        ]}
    ]}
    {'如pairs太多，buckets太少怎么破':[
        'Rehasing:把数组扩容至两倍（默认）',
        '条件：load factor(pair 的数量除以 buckets 的数量)>0.75'
    ]},
    {'与 Hashtable 的区别':[
        'Hashtable 是线程安全的，HashMap 并非线程安全',
        'HashMap 允许 key 中有 null 值，Hashtable 是不允许的'
    ]}
]
}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 