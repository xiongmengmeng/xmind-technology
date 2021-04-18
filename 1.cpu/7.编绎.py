import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
xmind_name="cpu"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("编绎")
r2=s2.getRootTopic()
r2.setTitle("编绎")


content={
'基础概念':[
    {'本地语言':[
        'Windows中EXE文件的程序内容,cpu可以运行的语言'
    ]},
    {'编绎':[
        '定义：将高级编程语言编写的源代码转换成本地语言的过程',
        {'编绎器种类由3点决定':[
            '编程语言',
            '电脑的CPU',
            '电脑的操作系统'
        ]}
    ]},
    {'链接':[
        '把多个目标文件结合，生成1个EXE文件的处理'
    ]},
    {'库文件':[
        '把多个目标文件集成保存到一个文件中的形式',
        {'种类':[
            '导入库:存储着两种信息:A函数在某DLL文件，或存储着DLL文件的文件夹信息',
            '静态链接库:存储着目标文件的实体，能直接和EXE文件结合的库文件'
        ]}
    ]},
    {'标准函数':[
        '不是通过源代码形式而是通过库文件形式和编译器一起提供的函数'
    ]},
    {'再配置信息':[
        '在程序运行时，虚拟的内存地址会转换成实际的内存地址',
        '链接器会在EXE文件的开头，追加转换内存地址所需的必要信息'
    ]}
],
'链接后的EXE文件的构造':[
    '再配置信息',
    '变量组和函数组',
    '给变量及函数分配了虚拟的内存地址',
],
'运行后EXE文件的内容':[
    '变量组',
    '函数组',
    {'栈':[
        '存储函数内部的局部变量，以及函数调用时所用的参数的内存区域',
        '对数据进行存储和舍弃（清理处理）的代码，由编译器自动生成',
        '函数被调用时得到申请分配，函数处理完会自动释放'
    ]},
    {'堆':[
        '存储程序运行时的任意数据及对象的内存领域',
        '堆的内存空间，根据程序员的程序，明确进行申请分配或释放'
    ]}
]

}

#构建xmind
xmind.build(content,r2)

#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 