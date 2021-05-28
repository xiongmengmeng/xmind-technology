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
        '扩容时,第一个线程生成一个新数组，大小为原数组的两倍，并赋值此字段，方便后续线程协助扩容'
    ]},
    {'volatile int sizeCtl':[
        '用来控制table的初始化和扩容操作(默认0)',
        '-1:代表table正在初始化',
        {'负数':[
            '有线程在扩容',
            {'高16位':[
                '扩容唯一标识戳(值与数组长度有关)',
            ]},
            {'低16位':[
                '参与扩容线程数为N-1',
                '线程进入或退出扩容时更新',
                '最后一个线程-1后，低16位为1,会重新遍历数组，判断 桶结点slot是否为fwt',
                '是,跳过,不是,迁移,一种保障机制,更新sizeCtl值为下次扩容阀值'
            ]}
        ]},
        {'正数':[
            '下次扩容阀值'
        ]}
    ]},
    {'Node':[
        'int hash',
        'K key',
        'volatile V val',
        'volatile Node<K,V> next'
    ]},
    {'ForwardingNode':[
        '在table发生扩容时使用,只放在slot,桶节点的位置',
        '一个特殊的Node节点，hash值为-1，其中存储nextTable的引用',
        '作为一个占位符放在table中表示当前节点为null或则已经被移动',
    ]},
    {'transferIndex':[
        '记录老表的总迁移进度'
    ]}
]
}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 