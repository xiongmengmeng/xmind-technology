import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="redis"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("数据类型内部编码规则")
r2=s2.getRootTopic()
r2.setTitle("数据类型内部编码规则")


content={

'字符串类型':[
    {'sdshdr类型变量':[
        '存储字符串',
        'int len:字符串长度',
        'int free:buf中剩余空间',
        'char buf[]:字符串内容'
    ]},
    'redisObject的ptr字段指向sdshdr类型变量的地址',
    'SET key foobar:sizeof(redisObject)+sizeof(sdshdr)+strlen("foobar") = 30字节'
    
],
'散列类型':[
    'hash-max-ziplist-entries:512',
    'hash-max-ziplist-value:64',
    {'内部编码方式':[
        {'REDIS_ENCODING_ZIPLIST':[
            '字段个数<hash-max-ziplist-entries&&字段名和值长度<hash-max-ziplist-value',
            '紧凑的编码格式，牺牲了部分读取性能以换取极高的空间利用率，适合在元素少时使用',
            {'结构':[
                'zlbytes:uint32_t类型,整个结构占用的空间',
                'zltail：uint32_t类型,到最后一个元素的偏移，程序可直接定位到尾部元素',
                'zllen：uint16_t类型，存储元素的数量',
                {'元素(4部分组成)':[
                    '存储前一个元素的大小(可实现倒序查找)',
                    '元素编码类型',
                    '元素大小',
                    '元素的实际内容',
                ]},
                'zlend：一个单字节标识，标记结构的末尾，值永远是255',
            ]}
        ]},
        {'REDIS_ENCODING_HT':[
            '散列表',
            'O(1)时间复杂度的赋值取值',
        ]}
    ]}
],
'列表类型':[
    '内部编码方式可能是REDIS_ENCODING_LINKEDLIST或REDISENCODING_ZIPLIST',
    '转换方式和散列类型一样',
    {'REDIS_ENCODING_LINKEDLIST':[
        '双向链表，链表中的每个元素用redisObject存储的',
    ]}
],
'集合类型':[
    '内部编码方式可能是REDIS_ENCODING_HT或REDIS_ENCODING_INTSET',
    {'REDIS_ENCODING_INTSET':[
        '集合中所有元素都是整数且元素个数<set-max-intset-entries(默512)'
    ]}
],
'有序集合类型':[
    '内部编码方式可能是REDIS_ENCODING_SKIPLIST或REDIS_ENCODING_ZIPLIST',
    '转换方式和散列类型一样',
    {'REDIS_ENCODING_SKIPLIST':[
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