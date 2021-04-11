import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="集合"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("集合接囗")
r2=s2.getRootTopic()
r2.setTitle("集合接囗")


content={
'Collection接口':[
    '最基本的集合接口',
    '一个Collection代表一组Object',
    '存储一组不唯一，无序的对象'
],
'List接口':[
    '一个有序的Collection',
    '能精确的控制每个元素插入的位置，能通过索引(元素在List中位置，类似于数组的下标)来访问List中的元素',
    '第一个元素的索引为 0，允许有相同的元素',
    '存储一组不唯一，有序（插入顺序）的对象'
],
'Set':[
    '与Collection完全一样的接口，只是行为上不同，Set不保存重复的元素',
    'Set接口存储一组唯一，无序的对象',
],
'SortedSet':[
    '继承于Set保存有序的集合',
],
'Map':[
    '存储一组键值对象，提供key（键）到value（值）的映射',
    {'Map.Entry':[
        'Map的内部接口',
        '描述在一个Map中的一个元素（键/值对）',
        
    ]},
    {'SortedMap':[
        '继承于Map，使Key保持升序排列',
    ]}
],
'Enumeration':[
    '一个传统的接口和定义的方法，已被迭代器取代',
    '通过它可以枚举（一次获得一个）对象集合中的元素',
],
'数据结构':[
    {'ArrayXxx':[
        '底层数据结构是数组',
        '查询快，增删慢'
    ]},
    {'LinkedXxx':[
        '底层数据结构是链表',
        '查询慢，增删快'
    ]},
    {'HashXxx':[
        '底层数据结构是哈希表',
        '依赖两个方法：hashCode()和equals()'
    ]},
    {'TreeXxx':[
        '底层数据结构是二叉树',
        '两种方式排序：自然排序和比较器排序'
    ]}
]
}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 