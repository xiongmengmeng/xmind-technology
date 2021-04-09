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
'原理,版本1.8':[
    '保证并发更新的安全：CAS+synchronized:',
    '数据结构：数组+链表+红黑树'
],
'重要成员变量':[
    'volatile Node<K,V>[] table:默认null，初始化发生在第一次插入（默认大小16的数组），用来存储Node节点，大小总是2的幂次方',
    'volatile Node<K,V>[] nextTable:默认null，扩容时新生成的数组，大小为原数组的两倍',
    {'volatile int sizeCtl':[
        '默认0:用来控制table的初始化和扩容操作',
        '-1:代表table正在初始化 ',
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
        '只有table发生扩容时，它才发挥作用',
        '作为一个占位符放在table中表示当前节点为null或则已经被移动',
        '一个特殊的Node节点，hash值为-1，其中存储nextTable的引用'
    ]},
],
'实例初始化':[
    'initTable()',
    '延缓到第一put操作再进行，并且初始化只会执行一次',
    '防止初始化后的首次操作就需要扩容（比如putAll），从而影响效率'
],
'put()':[
    '1.table为空，对table进行初始化',
    {'2.table不为空，通过key的hash值定位的bucket':[
        {'bucket为空':[
            '使用CAS操作，将Node放入对应的bucket中',
        ]},
        {'bucket不为空,当前map是否在扩容f.hash == MOVED':[
            '是：则跟其他线程一起进行扩容',
            {'否':[
                '说明出现hash冲突，采用synchronized关键字',
                '若当前节点是链表的头节点，遍历链表，更新或增加节点',
                '若当前节点是红黑树的根节点，在树结构上遍历元素，更新或增加节点'
            ]}
        ]}
    ]},
    '3.链表节点超过8，链表转为红黑树:treeifyBin()',
    '4.统计节点个数，检查是否需要resize:addCount()'
],
'table 扩容':[
    {'treeifyBin()':[
        {'tab的长度<MIN_TREEIFY_CAPACITY(默64)':[
            '是：将数组长度扩大到原来的两倍,触发transfer，调整节点位置',
            '否：将链表转为红黑树'
        ]}
    ]},
    {'addCount()':[
        '利用CAS更新baseCount',
        '统计tab中的节点个数大于阈值（sizeCtl），会触发transfer，重新调整节点位置'
    ]},
    {'transfer':[
        '构建一个nextTable，大小为table的两倍',
        '通过for自循环处理每个槽位中的链表元素',
        '如所有的节点都已完成复制，把nextTable赋值给table，清空临时对象nextTable',
        {'扩容时，并发地复制与插入':[
            '1.遍历整个table，当前节点为空，采用CAS的方式在当前位置放入fwd',
            '2.当前节点已为fwd(with hash field “MOVED”)，则已有线程处理完，直接跳过，这里是控制并发扩容的核心',
            {'3.当前节点为链表节点或红黑树':[
                '重新计算链表节点的hash值，移动到nextTable相应位置',
                '移动完成后，用Unsafe.putObjectVolatile在tab的原位置赋为为fwd, 表示当前节点已经完成扩容'
            ]}
        ]}
    ]}
],
'get()':[
    '不需要同步控制，较简单',
    '1.空tab，直接返回null',
    '2.计算hash值，找到相应的bucket位置，为node节点直接返回，否则返回null'
],
'版本对比':[
    'JDK1.7:Segment + HashEntry',
    'JDK1.8:Node + CAS + Synchronized'
]
}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 