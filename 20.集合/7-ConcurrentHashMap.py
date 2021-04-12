import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="集合"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("ConcurrentHashMap")
r2=s2.getRootTopic()
r2.setTitle("ConcurrentHashMap")


content={
'原理,版本1.7':[
    {'保证并发更新的安全':[
        'Segment(继承ReentrantLock) + HashEntry'
    ]},
    '一个Segment数组',
    {'Segment':[
        '继承ReentrantLock,实现对key加锁',
        '内部类似一个HashMap'
    ]},
    {'concurrencyLevel':[
        '并发数，Segment数(默16)',
        '可以初始化时设置，但初始化后，不可扩容'
    ]}
],
'原理,版本1.8':[
    {'保证并发更新的安全':[
        'Node + CAS + Synchronized'
    ]},
    {'数据结构':[
        '数组+链表+红黑树'
    ]}
],
'重要成员变量':[
    {'volatile Node<K,V>[] table':[
        '默认null',
        '初始化发生在第一次插入（默认大小16的数组）',
        '用来存储Node节点，大小总是2的幂次方'
    ]},
    {'volatile Node<K,V>[] nextTable':[
        '默认null',
        '扩容时新生成的数组，大小为原数组的两倍'
    ]},
    {'volatile int sizeCtl':[
        '默认0',
        '用来控制table的初始化和扩容操作',
        '-1:代表table正在初始化',
        'N:表示有N-1个线程正在进行扩容操作 ',
        '如table未初始化，表示table需要初始化的大小',
        '如table初始化完成，表示table的容量，默认table大小的0.75倍，公式0.75（n - (n >>> 2)'
    ]},
    {'Node':[
        'int hash',
        'K key',
        'volatile V val',
        'volatile Node<K,V> next'
    ]},
    {'ForwardingNode':[
        '在table发生扩容时使用',
        '一个特殊的Node节点，hash值为-1，其中存储nextTable的引用',
        '作为一个占位符放在table中表示当前节点为null或则已经被移动',
    ]},
]
}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 