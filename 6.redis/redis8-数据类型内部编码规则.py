import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="redis"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("内部编码规则")
r2=s2.getRootTopic()
r2.setTitle("内部编码规则")


content={
'list':[
    {'内部编码方式':[
        'quicklist(双端链表)+ziplist'
    ]},
    {'quicklist':[
        '双向链表，每个节点存放ziplist',
        {'结构':[
            'quickListNode head',
            'quickListNode tail',
            'long count:ziplist中的entry的总和',
            'int fill:ziplist大小设置',
            'int compress:节点压缩深度设置'
        ]},
        {'quickListNode':[
            'quickListNode *prev',
            'quickListNode *next',
            'zl:ziplist的指针',
            'count:ziplist中的数据个数'
        ]}
    ]},
    {'提升数据存取效率':[
        {'设置每个ziplist的最大容量':[
            'list-max-ziplist-size=-2',
            '单ziplist节点最大能存储8kb,超过则分裂,将数据存储在新的ziplist节点中'
        ]},
        {'quicklist的数据压缩范围':[
            'list-compress-depth=1',
            '0:所有节点都不进行压缩',
            '1:从头节点往后走一个，尾节点往前走一个不用压缩，其他的全部压缩',
            '2，3，4 ... 以此类推'
        ]}
    ]}
],
'set':[
    {'内部编码方式':[
        'intset',
        'hashtable'
    ]},
    {'intset':[
        '整数集合是一个有序的，存储整型数据的结构',
        {'结构':[
            'encoding:编码类型，三种，int-16,int-32,int-64',
            'length:元素个数',
            'contents[]:元素存储，从小到大排序'
        ]}
    ]},
    {'intset转为hashtable的条件':[
        {'set-max-intset-entries=512':[
            'intset能存储的最大元素个数'
        ]},
        '添加了一个非int类型的数据'
    ]},
],
'zset':[
    {'内部编码方式':[
        'ziplist',
        'hashtable+skiplist'
    ]},
    {'hashtable+skiplist':[
        {'hashtable':[
            '存储【元素值】->【元素分数】的映射关系',
            '实现O(1)时间复杂度的ZSCORE命令'
        ]},
        {'skiplist':[
            '存储【元素分数】->【元素值】的映射关系'
        ]},
        {'Redis对跳跃列表的实现':[
            '允许跳跃列表中的元素（即分数）相同',
            '为跳跃链表每个节点增加了指向前一个元素的指针以实现倒序查找'
        ]}
    ]},
    {'ziplist转为hashtable+skiplist的条件':[
        {'zset-max-ziplist-entries=128':[
            '元素个数超过128'
        ]},
        {'zset-max-ziplist-value=64':[
            '单个元素大小超过64byte'
        ]}
    ]},
]

    
}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 