import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="集合"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("Map集合")
r2=s2.getRootTopic()
r2.setTitle("Map集合")


content={
'Map集合':[
    '一组键值的映射',
    '存储的每个对象都有一个相应的关键字(key)，关键字决定了对象在Map中的存储位置',
],
'HashMap':[
    {'底层':[
        '数组+链表+红黑树'
    ]},
    {'特点':[
        'key不能重复，value可重复',
        '允许一条记录的key为Null,允许多条记录的value为Null',
    ]},
    {'数据结构':[
        '一个数组，然后数组中每个元素是一个单向链表',
        {'Node的四个属性':[
            'key',
            'value',
            'hash 值',
            'Node<K,V> next:用于单向链表的next'
        ]}
    ]},
    {'参数':[
        {'capacity':[
            '当前数组容量，始终保持2^n',
            '可扩容，扩容后数组大小为当前的2倍'
        ]},
        {'loadFactor':[
            '负载因子(默0.75):当散列表中已有75%位置放满，将进行再散列',
            '负载因子越高(越接近1.0)，内存的使用效率越高，元素的寻找时间越长',
            '负载因子越低(越接近0.0)，元素的寻找时间越短，内存浪费越多'
        ]},
        {'threshold':[
            '扩容的阈值，等于capacity*loadFactor'
        ]}
    ]},
    {'覆写equals()和hashCode()注意':[
        '相等的散列码未必是相等的对象',
        '但相等的对象必须有相等的散列码',
    ]},
],
'LinkedHashMap':[
    {'底层':[
        '多了双向链表，记录插入数据的顺序'
    ]}
],
'TreeMap':[
    {'底层':[
        '多了二叉树:每增加一个对象都会进行排序，将对象插入到二叉树指定的位置'
    ]},
    '实现SortedMap接口,根据Key进行排序',
    {'注意':[
        'key须实现Comparable接口||构造TreeMap时传入自定义的Comparator,否运行时抛异常'
    ]}
],
'Hashtable':[
    '继承自Dictionary类',
    '不允许null的键或值',
    'synchronized关键字，对方法加锁，即对对象加锁',
    '线程安全,并发度不如ConcurrentHashMap',
],

}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 