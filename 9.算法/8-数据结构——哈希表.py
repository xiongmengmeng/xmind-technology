import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="数据结构"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("哈希表和有序表")
r2=s2.getRootTopic()
r2.setTitle("哈希表和有序表")


content={
'哈希表':[
    '键（key）和值（value）',
    {'增，删，改，查，时间复杂度':[
        'O(1)'
    ]},
    'java中是HashMap',
    {'key':[
        {'基础类型的key':[
            '值传递',
            '占用内存大小,key实际大小',
        ]},
        {'包装类型的key':[
            '值传递',
            '占用内存大小,key实际大小',
        ]},
        {'非基础类型的key':[
            '引用传递',
            '占用内存大小,8节,存的是引用的地址'
        ]},
    ]},
    '哈希值取余后冲突：链表,红黑树解决'
],
'有序表':[
    'java中是TreeMap',
    '增，删，改，查，时间复杂度O(logN)',
    {'底层---平衡二叉树':[
        'AVL',
        'SB',
        '红黑树',
        '跳表'
    ]},
    {'方法':[
        {'firstKey()':[
            '第一个添加的参数'
        ]},
        {'lastKey()':[
            '最后一个添加的参数'
        ]},
        {'floorKey(K key) ':[
            '小于等于key的，离key最近的'
        ]},
        {'ceilingKey(K key) ':[
            '大于等于key的，离key最近的'
        ]},
    ]}
]

}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 