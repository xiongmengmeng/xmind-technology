import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
xmind_name="jvm"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("字节码指令")
r2=s2.getRootTopic()
r2.setTitle("字节码指令")


content={
'重要概念':[
    'JVM采用【面向操作数栈】的架构(区别面向寄存器）',
    {'指令大多':[
        '只一个操作码，指令参数放在操作数栈中'
    ]},
    {'操作码长度':[
        '一个字节（即0～255）'
    ]},
    {'指令集的操作码总数':[
        '<=256条'
    ]},
    '处理超过一个字节数据时，运行时从字节中重建出具体数据结构'
],
'字节码与数据类型':[
    {'iload指令':[
        '从局部变量表中加载int型的数据到操作数栈中',
        'fload指令加载的是float类型数据'
    ]},
    {'两条指令区别':[
        'JVM内部可能是同一段代码',
        'Class文件中它们必须拥有各自独立的操作码'
    ]},
    '大部分与数据类型相关的字节码指令，其【操作码助记符】都有【特殊字符】表明为哪种【数据类型】服务'
],
'加载和存储指令':[
    {'作用':[
        '将数据在栈帧中的【局部变量表】和【操作数栈】之间来回传输'
    ]},
    {'iload':[
        '将一个局部变量加载到操作栈'
    ]},
    {'istore':[
        '将一个数值从操作数栈存储到局部变量表'
    ]},
    {'bipush':[
        '将一个常量加载到操作数栈'
    ]},
    {'wide':[
        '扩充局部变量表的访问索引的指令'
    ]}
],
'运算指令':[
    {'作用':[
        '对两个【操作数栈】上的值进行特定运算，并把结果重存入到【操作栈顶】'
    ]},
    {'iadd':[
        '加法指令'
    ]},
    {'isub':[
        '减法指令'
    ]},
    {'imul':[
        '乘法指令'
    ]},
    {'idiv':[
        '除法指令'
    ]},
    {'irem':[
        '求余指令'
    ]},
    {'ineg':[
        '取反指令'
    ]},
    {'ishl':[
        '位移指令'
    ]},
    {'ior':[
        '按位或指令'
    ]},
    {'iand':[
        '按位与指令'
    ]},
    {'dcmpg':[
        '比较指令'
    ]}
]
}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 