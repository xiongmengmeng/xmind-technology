import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="redis"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("hash内部编码规则")
r2=s2.getRootTopic()
r2.setTitle("hash内部编码规则")


content={

'内部编码方式':[
    'ziplist',
    'dict'
],
'ziplist':[
    '紧凑的编码格式，牺牲了部分读取性能以换取极高的空间利用率，适合在元素少时使用',
    {'结构':[
        {'zlbytes':[
            '4字节',
            '记录压缩列表总共占用的字节数'
        ]},
        {'zltail':[
            '4字节',
            '定位list的末尾节点',
            '最后一项（entry）在ziplist中的偏移字节数',
            '方便尾端快速地执行push或pop操作'
        ]},
        {'zllen':[
            '2字节',
            '记录ziplist中数据项（entry）的个数'
        ]},
        {'zlentry':[
            '存放真实数据，长度不定',
            {'4部分':[
                'prerawlen:前一个entry的数据长度',
                'len:entry中数据的长度)',
                'data:真实数据存储',
            ]}
        ]},
        {'zlend':[
            '1字节',
            '结束标记，值固定为255'
        ]}
    ]}
],
'dict':[
    '散列表,redis中哈希表称为dict',
    'O(1)时间复杂度的赋值取值',
    {'dict':[
        {'type':[
        ]},
        {'privdata':[
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
        ]}
    ]},
    {'dictEntry':[
        'key',
        'value',
        'next'
    ]}
],
'ziplist转为dict的条件':[
    {'hash-max-ziplist-entries=512':[
        'ziplist元素个数超过512'
    ]},
    {'hash-max-ziplist-value=64':[
        '单个元素大小超过64byte'
    ]}
]


    
}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 