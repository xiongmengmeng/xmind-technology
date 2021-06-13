import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="redis"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("SDS")
r2=s2.getRootTopic()
r2.setTitle("SDS")


content={
'string的数据结构':[
    'sds(simple dynamic string)',
    '不同的数据长度用不同的数据类型来对数据进行表示',
    {'优点':[
        {'1.二进制安全的数据结构':[
            'redis的字符串，以\0结尾，如遇到这种字符，会导致字符串被截断'
        ]},
        {'2.内存预分配，避免了频繁的内存分配':[
            '内存不超过1M,扩容为使用容量的两倍',
            '内存超过1M,扩容:使用空间+1M'
        ]},
        {'3.兼容c语言函数库':[
            '自动在char[]数组末尾加\0'
        ]}
    ]},
    '字符串最大容量512M',
],   
'redis3.2以前':[
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
],
'redis3.2以后':[
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
    
]

    
}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 