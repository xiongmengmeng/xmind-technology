import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="集合"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("Set集合")
r2=s2.getRootTopic()
r2.setTitle("Set集合")


content={
'Set集合':[
    '无序集合，不允许存放重复的元素',
    '允许存储null元素',
    '对add()、equals()和hashCode() 方法添加了限制',
],
'HashSet':[
    {'底层':[
        '采用 Hashmap 的 key 来储存元素',
        '哈希表'
    ]},
    {'特点':[
        '存储的数据是无序的',
        '采用HashCode算法来存取元素，具有比较好的查找性能'
        '非线程安全'
    ]},
    {'存储':[
        '通过hashCode值来确定元素在内存中的位置',
        '一个hashCode位置上可以存放多个元素'
    ]},
    {'过滤重复元素':[
        '1.调用元素HashCode获得哈希码',
        {'2.判断哈希码是否相等':[
            '不相等:录入',
            {'相等:判断equals()后是否相等':[
                '不相等:进行hashcode录入',
                '相等:不录入'
            ]}
        ]}
    ]}
],
'LinkedHashSet':[
    {'底层':[
        'HashSet + LinkedList 的结构',
        '一个链表:维护元素的插入顺序'
    ]},
    {'特点':[
        '存储的数据是有序的'
    ]},
    {'内容':[
        '没有定义任何方法，只有四个构造函数',
        '所有方法都继承自HashSet',
        '维持元素插入顺序的性质继承自LinkedHashMap'
    ]},
    {'插入':[
        '计算hashCode+维护链表,插入性能比HashSet低',
    ]},
    {'遍历':[
        '只需要按链表来访问元素,遍历时性能更高'
    ]},
],
'TreeSet':[
    {'底层':[
        '二叉树:每增加一个对象都会进行排序，将对象插入到二叉树指定的位置'
    ]},
    {'特点':[
        '实现了SortedSet接口',
        '提供了一些额外的按排序位置访问元素的方法'
    ]},
    {'排序有两种':[
        {'自然排序':[
            '调用compareTo方法比较元素大小，然后按升序排序',
            '元素对象必须实现Comparable接口，否则抛异常',
            {'Comparable接口':[
                '提供自然排序顺序'
            ]}
        ]},
        {'定制排序':[
            '关联一个Comparator对象，由Comparator提供排序逻辑',
            {'Comparator接口':[
                '自定义排序函数,适用于没有自然顺序的类、或想要不同于自然顺序的顺序',
                '将Comparator传递给Collections.sort或Arrays.sort，实现排序',
                '如：Collections.sort(lst,new Comparator<TaskPrintSchemeVO>()'
            ]}
        ]}
    ]}
]
}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 