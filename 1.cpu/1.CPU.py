import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
xmind_name="cpu"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("CPU")
r2=s2.getRootTopic()
r2.setTitle("CPU")


content={
'CPU':[
    '【解释】和【运行】【机器语言】的程序内容'
],
'4部分，电流信号相互连通':[
    {'控制器':[
        '把内存上的指令、数据等读入寄存器',
        '根据指令的执行结果来控制整个计算机'
    ]},
    {'运算器':[
        '运算从内存读入寄存器的数据'
    ]},
    {'时钟':[
        '发出CPU开始计时的时钟信号'
    ]},
    {'寄存器':[
        '暂存指令、数据等处理对象，可以看作是内存的一种',
        {'主要种类':[
                '程序计数器：决定程序流程',
                '累加寄存器',
                '标志寄存器',
                '指令寄存器',
                '栈寄存器',
                '基址寄存器',
                '变址寄存器'
            ]}
    ]}
],
'机器语言':[
    {'条件分支和循环机制':[
        '程序计数器的值设定为任意地址'
    ]},
    {'函数的调用机制':[
        '在将函数的入口地址设定到程序计数器之前',
        'call指令会把调用函数后要执行的指令地址存储在名为栈的主存内',
        '函数处理完毕后，再通过函数的出口来执行return命令'
    ]},
    {'机器语言指令的4种主要类型':[
        {'数据传送指令':[
            '寄存器与内存，内存与内存，内存与外围之间数据的读写操作'
        ]},
        {'运算指令':[
            '用累加寄存器执行算术，逻辑，比较，移位运算'
        ]},
        {'跳转指令':[
            '条件分支，循环，强制跳转'
        ]},
        {'call/return指令':[
            '函数调用/返回函数调用前的地址'
        ]}
    ]}
]
}

#构建xmind
xmind.build(content,r2)

#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 