import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
xmind_name="cpu"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("各种语言")
r2=s2.getRootTopic()
r2.setTitle("各种语言")


content={
'机器码':[
    '各种用【二进制编码方式】表示的指令，叫做【机器指令码】',
    '它编写的程序，CPU可直接读取运行，相比其他语言编的程序，执行速度最快',
    '不同种类的CPU所对应的机器指令不同'
],
'机器指令':[
    '把机器码中特定的0和1序列，简化成对应的指令',
    '不同的硬件平台的同一种指令（比如mov），对应的机器码也可能不同'
],
'汇编语言':[
    {'助记符（Mnemonics）':[
        '代替机器指令的操作码'
    ]},
    {'地址符号（Symbo1）或标号（Labe1）':[
        '代替指令或操作数的地址'
    ]},
    {'定义':[
        '使用【助记符】的编程语言，文件的扩展名.asm',
        '在不同的硬件平台，汇编语言对应着不同的机器语言指令集',
        '汇编语言编写的程序必须翻译成机器指令码，计算机才能识别和执行',
        '汇编语言编写的源代码，和本地代码是一一对应',
    ]},
    {'段定义':[
        '定义：给构成程序的命令和数据的集合体加上一个名字',
        'segment：源代码的开始',
        '_TEXT：指令的段定义',
        '_DATA：被初始化（有初始值）的数据的段定义',
        '_BSS：尚未初始化的数据的段定义',
        'group：把_BSS和_DATA这两个段定义汇总为名为DGROUP的组',
        'proc和endp围起来的部分:过程（procedure）的范围',
        'end:源代码的结束'
    ]},
    {'流程':[
        '加载本地代码到内存，内存中存储着构成本地代码的指令和数据',
        {'程序运行时':[
            'CPU从内存中把指令和数据读出',
            '将其存储在CPU内部的寄存器中进行处理'
        ]}
    ]}
],
'高级语言':[
    '比机器语言和汇编语言更接近人的语言',
    '计算机执行高级语言编写的程序时，仍然需要把程序解释和编译成【机器指令】'
],
'C、C++源程序执行过程':[
    {'两个阶段':[
        {'编译':[
            '读取源程序（字符流），对之进行词法和语法分析，将【高级语言】转换为等效的【汇编代码】'
        ]},
        {'汇编':[
            '把【汇编语言】代码翻译成目标【机器指令】的过程'
        ]}
    ]}
]

}

#构建xmind
xmind.build(content,r2)

#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 