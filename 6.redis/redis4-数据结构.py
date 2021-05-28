import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="redis"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("数据结构")
r2=s2.getRootTopic()
r2.setTitle("数据结构")


content={
'redis':[
    '1.二进制安全的数据结构',
    {'2.内存预分配，避免了频繁的内存分配':[
        '内存不超过1M,扩容为使用容量的两倍',
        '内存超过1M,扩容:使用空间+1M'
    ]},
    '3.兼容c语言函数库，charp[]数组末尾加\0'
],
'键值':[
    {'redisObject--16byte':[
        'type',
        'encoding',
        'lru',
        'refcount',
        '*ptr'
    ]},
    {'type--4bit':[
        '键值的数据类型',
        'type key:查看具体数据类型',
        {'详细':[
            'string:0000(0)',
            'list:0001(1)',
            'set:0010(2)',
            'zset:0011(3)',
            'hash:0100(4)'
        ]},
    ]},
    {'encoding--4bit':[
        '键值的内部编码方式',
        'object encoding key:使用此命令可查看value对象的编码类型',
        {'详细':[
            'raw 0',
            'int 1',
            'ht(hash table) 2',
            'zipmap 3',
            'linked list 4',
            'ziplist 5',
            'intset 6',
            'skiplist 7'
        ]}

    ]},
    {'lru--23bite':[
        '内存淘汰算法设置',
        '记录对象最后一次的访问时间',
        'lru time',
        'lfu data'
    ]},
    {'refcount--4byte':[
        '键值被引用数量',
        'c语言自己开辟内存空间，自己释放，通过引用计数法来管理内存'
    ]},
    {'*ptr--8byte':[
        '指针(8字节，64bit)，指向数据的位置',
        {'优化':[
            {'1.如value<=20个字节':[
                '尝试将其转为int类型,ptr直接存放value值',
                '此时value的编码格式为int'
            ]},
            {'2.如value<=44个字节':[
                '在ptr后使用连续空间来存放数据,可减少一次内存io',
                '此时value的编码格式为embstr',
                {'原理':[
                    'cpu读取数据时是按行来读取数据的，一个缓存行64字节',
                    '如数据<44字节（redisObject占用16字节,sds8中其余部分占用4字节)',
                ]}
            ]},
            {'3.如value>44个字节':[
                '开辟另外一个内存空间来存储,ptr指针指向一个sds',
                '此时value的编码格式为raw',
            ]}
        ]}
    ]}
],
'string的数据结构':[
    '字符串最大容量512M',
    {'redis3.2以前':[
        {'struct sdshdr':[
            'int len',
            'int free',
            'char buf[]'
        ]},
        'sds(Simple Dynamic String)的结构，hdr意思为描述空间',
        '没有直接使用c语言的字符串结构，而是封装了一层',
        {'有空间浪费问题':[
            {'int len/free':[
                'int为4字节,32位，可表示42亿数据',
                '用不完'
            ]}
        ]},
    ]},
    {'redis3.2以后':[
        {'struct sdshdr5':[
            'unsigned char flags',
            'char buf[]'
        ]},
        '5:用5个bit位来表示数据长度，2^5-1=32位，表示长度在32位以内的数据',
        {'flags':[
            '占用一个字节，8位',
            '前三位用来存数据类型type,5为0，8为1，16为2，32为3，64为4',
            '后五位用来存数据长度,当数据结构为sdshdrX，这里闲置'
        ]},
        {'struct sdshdrX':[
            'unsigned char flags',
            'uintX_t len',
            'uintX_t alloc',
            'char buf[]'
        ]},
        'x为8，16，32，64:表示用x个bit位来表示数据范围',
        {'len':[
            '已用的字节长度',
            'x=8,len使用一个字节',
            'x=16,len使用二个字节',
            'x=16,len使用二个字节'
        ]},
        {'alloc':[
            '字符串最大字节长度'
        ]},
        {'char buf[]':[
            '真正有效的字符串数据，长度由alloc控制'
        ]}
       
    ]},
     '总之,不同的数据长度用不同的数据类型来对数据进行表示'

]

    
}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 