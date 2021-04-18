import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
xmind_name="cpu"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("内存")
r2=s2.getRootTopic()
r2.setTitle("内存")


content={
'物理模型':[
    {'内存IC构造':[
        'VCC和GND是电源',
        'A0～A9是地址信号的引脚',
        'D0～D7是数据信号的引脚',
        'RD和WR是控制信号的引脚'
    ]},
    {'内存IC大小估算':[
        {'数据信号引脚8个':[
            '一次可以输入输出8位（=1字节）的数据'
        ]},
        {'地址信号引脚10个':[
            '可指定0000000000～1111111111共1024个地址'
        ]},
        {'地址':[
            '表示数据的存储场所'
        ]},
        '这个内存IC可存储1024个1字节数据，1024=1K,该内存IC容量为1KB'
    ]}
],
'逻辑模型':[
    '楼房:1层可以存储1个字节的数据，楼层号表示的就是地址'
],
'指针':[
    '一种变量，不表示数据的值，而表示存储着数据的内存地址',
    '通过指针，可以对任意指定地址的数据进行读写',
    '指针的数据类型表示一次可以读写的长度'
],
'数组':[
    '定义：多个同样数据类型的数据在内存中连续排列的形式',
    {'分类':[
        {'栈':[
            '使用LIFO（LastInput First Out，后入先出）方式'
        ]},
        {'队列':[
            '使用FIFO（First Input First Out，先入先出）方式'
        ]},
        {'链表':[
            '更加高效地对数组数据（元素）进行追加和删除处理'
        ]},
        {'二叉查找树':[
            '使数据的搜索更有效率'
        ]}
    ]}
]
}


#构建xmind
xmind.build(content,r2)

#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 