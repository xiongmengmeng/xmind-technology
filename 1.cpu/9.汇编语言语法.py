import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
xmind_name="cpu"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("汇编语言")
r2=s2.getRootTopic()
r2.setTitle("汇编语言")


content={
'操作码+操作数':[],
'操作码':[
    {'mov A,B':[
        '把B值赋给A'
    ]},
    {'add A,B':[
        'A与B的值相加，结果赋值给A'
    ]},
    {'push A':[
        '把A的值存储在栈中'
    ]},
    {'pop A':[
    '从栈中读取出值，赋给A'
    ]},
    {'cmp A,B':[
        '对A跟B的值进行比较，比较结果会自动存入标志寄存器'
    ]},
    {'jge/jl/jle 标签名':[
        '和cmp命令组合使用，跳转到标签行'
    ]},
    {'inc A':[
    'A的值加1'
    ]},
    {'jmp 标签名':[
        '将控制无条件跳转到指定标签行'
    ]},
    {'call A':[
        '调用函数A'
    ]},
    {'ret 无':[
        '将处理返回到函数的调用源'
    ]},
    {'xor A,B':[
        'A和B的位进行异或比较，并将结果存入A中'
    ]},
],
'操作数':[
    '内存地址',
    '常数',
    {'寄存器名':[
        'eax 累加寄存器  运算',
        'ebx 基址寄存器  存储内存地址',
        'ecx 计数寄存器  计算循环次数',
        'edx 数据寄存器  存储数据',
        'esi 源基址寄存器   存储数据发送源的内存地址',
        'edi 目标基址寄存器 存储数据发送目标的内存地址',
        'ebp 扩展基址指针寄存器 存储数据存储领域基点内存地址',
        'esp 扩展栈指针寄存器   存储栈中最高位数据的内存地址'
    ]}
],
'函数':[
    '函数调用机制',
    {'函数内部处理':[
        '参数通过【栈】来传递',
        '返回值通过【寄存器】来返回'
    ]}
],
'其它':[
    '全局变量',
    {'循环处理的实现方法':[
        'xor inc com jl'
    ]},
    {'条件分支的实现方法':[
        'com jle jge jmp'
    ]}
]
}



#构建xmind
xmind.build(content,r2)

#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 