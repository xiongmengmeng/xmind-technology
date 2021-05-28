import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="redis"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("数据类型----内部编码规则")
r2=s2.getRootTopic()
r2.setTitle("数据类型---内部编码规则")


content={
'字符串类型':[
    {'sdshdr类型变量':[
        '存储字符串',
        'int len:字符串长度',
        'int free:buf中剩余空间',
        'char buf[]:字符串内容'
    ]},
    'redisObject的ptr字段指向sdshdr类型变量的地址',
],
'散列类型':[
    'hash-max-ziplist-entries:512',
    'hash-max-ziplist-value:64',
    {'内部编码方式':[
        {'ziplist':[
            '字段个数<hash-max-ziplist-entries&&字段名和值长度<hash-max-ziplist-value',
            '紧凑的编码格式，牺牲了部分读取性能以换取极高的空间利用率，适合在元素少时使用',
            {'结构':[
                {'zlbytes':[
                    '4字节',
                    '记录压缩列表总共占用的字节数'
                ]},
                {'zltail':[
                    '4字节',
                    '定位list的末尾节点'
                ]},
                {'zllen':[
                    '2字节',
                    '记录共有多少个entry'
                ]},
                {'zlentry':[
                    '存放真实数据',
                    {'4部分':[
                        'prevrawlensize:存储前一个元素的大小(可实现倒序查找)',
                        'prevrawlen:存储前一个元素的大小(可实现倒序查找)',
                        'lensize:',
                        'len:当前节点占用长度',
                        'headersize:prevrawlensize+lensize',
                        'encoding:元素编码类型,两种zipstr,zipint',
                        '*p:元素指针',
                    ]}
                ]},
                {'zlend':[
                    '1字节',
                    '结束标记，值固定为255'
                ]}
            ]}
        ]},
        {'hashtable':[
            '散列表,redis中哈希表称为dict',
            'O(1)时间复杂度的赋值取值',
            {'dict':[
                {'type':[
                    ''
                ]},
                {'privdata':[
                    ''
                ]},
                {'ht[2]':[
                    '采用双哈希表，用来扩容',
                    {'dictht[0]':[
                        'table：数组，数组的节点为dictEntry',
                        'size:数组长度',
                        'sizemask:数组长度-1',
                        'used:已存节点'
                    ]}
                ]},
                {'rehashidx':[
                    ''
                ]}
            ]},
            {'dictEntry':[
                'key',
                'value',
                'next'
            ]}
        ]}
    ]}
],
'列表类型':[
    'quicklist,只有一种数据结构',
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
],
'集合类型':[
    'hashtable和intset',
    {'intset':[
        '集合中所有元素都是整数且元素个数<set-max-intset-entries(默512)',
        {'结构':[
            'encoding:整数类型，三种，int-16,int-32,int-64',
            'length:集合元素个数',
            'contents[]:整数数组，从小到大排序'
        ]}
    ]}
],
'有序集合类型':[
    'skiplist或ziplist',
    '转换方式和散列类型一样',
    {'skiplist':[
        '散列表和跳跃列表（skip list）两种数据结构来存储有序集合类型键值',
        '散列表:存储元素值与元素分数的映射关系,实现O(1)时间复杂度的ZSCORE命令',
        '跳跃列表:存储元素的分数及其到元素值的映射以实现排序功能',
        {'Redis对跳跃列表的实现':[
            '允许跳跃列表中的元素（即分数）相同',
            '为跳跃链表每个节点增加了指向前一个元素的指针以实现倒序查找'
        ]}
    ]}
]

    
}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 