import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="集合"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("HashMap")
r2=s2.getRootTopic()
r2.setTitle("HashMap")


content={
'HashMap1.7':[
    {'数据结构':[
        '数组+单向链表',
        {'Entry':[
            'key',
            'value',
            'hash 值',
            '用于单向链表的 next'
        ]}
    ]},
    {'put':[
        '1.执行hash(Object key)得到一个int类型的hash值,根据hash值找到Node节点的位置',
        '(n - 1) & hash 即通过key的hash值来取对应的数组下标,并非是对table的size进行取余操作',
        {'table是否为空':[
            {'2.是':[
                '表明这是第一个元素插入，使用resize()进行扩容，初始大小默认16',
                '没有产生hash碰撞,直接插入node节点,调到第5步,否则进行下一步'
            ]},
            {'否':[
                '3.遍历对应下标处的链表，看是否有重复key存在，如有，直接覆盖，put方法返回旧值',
                '4.不存在重复key，将entry添加到链表中（先判断是否满足扩容条件，满足先扩容再插入数据）',
            ]}
        ]},
        {'数组扩容':[
            {'触发条件':[
                '当前size>=阈值threshold',
                '插入的数组位置上已有元素'
            ]},
            {'操作':[
                '1.建一个新的数组（旧数组的2倍），将旧数组中的值迁移到新数组中',
                '原table[i]中的链表的所有节点，分拆到新的数组的newTable[i]和 newTable[i + oldLength]位置上',
                '如原数组长16，扩容后，原table[0]处链表中的所有元素会被分配到新数组中newTable[0]和newTable[16]两个位置'
            ]} 
        ]}
    ]},
    {'get':[
        '根据key计算hash值',
        '对数组长度进行取模,找到相应的数组下标：hash & (length - 1)',
        '遍历该数组位置处的链表，直到找到相等(==或equals)的 key'
    ]}
],
'HashMap1.8':[
    {'数据结构':[
        '一个数组，然后数组中每个元素是一个单向链表或红黑树',
        {'Node的四个属性':[
            'key',
            'value',
            'hash 值',
            'Node<K,V> next:用于单向链表的next'
        ]}
    ]},
    {'hash(Object key)':[
        '(h = key.hashCode()) ^ (h >>> 16)',
        'key的hashCode，将它的高16位与低16位做了一个异或操作'
    ]},
    {'put':[
        '1.执行hash(Object key)得到一个int类型的hash值,根据hash值找到Node节点的位置',
        {'table是否为空':[
            {'2.是':[
                '表明这是第一个元素插入，使用resize()进行扩容，初始大小默认16',
                '不会产生hash碰撞,直接插入node节点,调到第6步,否则进行下一步'
            ]},
            {'否':[
                '3.桶中第一个元素(数组中的结点)的hash值相等，key相等,赋值给node节点e',
                '4.hash值不相等,说明key不相等,为红黑树,放入树中,赋值给node节点e',
                '5.hash值不相等,说明key不相等,为链表,遍历链表,赋值给最后一个节点,并返回node节点e',
                '当链表长度大于8之后需要将链表转化为红黑树进行存储'
            ]},
        ]},
        '6.判断新插入这个值是否导致size已经超过了阈值，是则进行扩容'
    ]}
]
}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 