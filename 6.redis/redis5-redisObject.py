import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="redis"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("redisObject")
r2=s2.getRootTopic()
r2.setTitle("redisObject")


content={
'作用':[
    '用来存储键值,即value的值'
],
'结构--16byte':[
    'type',
    'encoding',
    'lru',
    'refcount',
    '*ptr'
],
'结构(详细)':[
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
        'object encoding key:查看value对象的编码类型',
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
    {'lru--24bite':[
        '内存淘汰算法设置',
        '记录对象最后一次的访问时间',
        'lru time',
        'lfu data'
    ]},
    {'refcount--4byte':[
        '键值被引用数量',
        'c语言通过引用计数法来管理内存'
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

    
}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 