import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="集合"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("集合")
r2=s2.getRootTopic()
r2.setTitle("集合")


content={
'Java 早期数据结构':[
    {'枚举（Enumeration）':[
    ]},
    {'位集合（BitSet）':[
        '一个Bitset类创建一种特殊类型的数组来保存位值',
        'BitSet中数组大小会随需要增加'
    ]},
    {'向量（Vector）':[
        '和ArrayList相似，该类是同步的，可用在多线程中',
        '允许设置默认的增长长度',
        '默认扩容方式为原来的2倍'
    ]},
    {'栈（Stack）':[
        'Vector的一个子类，实现了一个标准的后进先出的栈',
    ]},
    {'字典（Dictionary）':[
        '一个抽象类',
        '用来存储键/值对，作用和Map类相似',
    ]},
    {'哈希表（Hashtable）':[
        'Dictionary(字典) 的子类'
    ]},
    {'属性（Properties）':[
        '继承于Hashtable',
        '表示一个持久的属性集，属性列表中每个键及其对应值都是一个字符串',
    ]},
    {'缺点':[
        '缺少一个核心的，统一的主题'
    ]}
],
'集合框架':[
    {'包括两种类型的容器':[
        '集合（Collection）:存储一个元素集合',
        '图（Map）:存储键/值对映射'
    ]},
    {'集合框架内容':[
        {'接口':[
            '代表集合的抽象数据类型',
            '如Collection、List、Set、Map等',
            '定义多个接口：为了以不同的方式操作集合对象'
        ]},
        {'实现类':[
            '集合接口的具体实现',
            '从本质上讲，它们是可重复使用的数据结构',
            'ArrayList、LinkedList、HashSet、HashMap'
        ]},
        {'算法':[
            '实现集合接口的对象里的方法执行的一些有用的计算',
            '如搜索和排序',
            '这些算法被称为多态，因为相同的方法可在相似的接口上有着不同的实现'
        ]},
        '几个Map接口和类'
    ]}
]
}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 