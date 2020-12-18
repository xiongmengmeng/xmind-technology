import xmind
from xmind.core.markerref import MarkerId
w = xmind.load("c:\\Users\\btr\\Desktop\\cpu.xmind") 
s2=w.createSheet()
s2.setTitle("cpu4_compile")
r2=s2.getRootTopic()
r2.setTitle("计算机基础")


content={
'编绎':[
    {'基础概念':[
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
    ]},
    {'链接后的EXE文件的构造':[
        '再配置信息',
        '变量组和函数组',
        '给变量及函数分配了虚拟的内存地址',
    ]},
    {'运行后EXE文件的内容':[
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
    ]}],
'汇编语言(上)':[
    {'基础概念':[
        '助记符',
        {'汇编语言':[
            '使用助记符的编程语言，文件的扩展名.asm',
            '汇编语言编写的源代码，和本地代码是一一对应',
            'C语言源代码同本地代码不一一对应，反编译后的代码和源代码可能不一样'
        ]},
        {'段定义':[
            '定义：给构成程序的命令和数据的集合体加上一个名字',
            '由伪指令segment和ends围起来',
            '_TEXT：指令的段定义',
            '_DATA：被初始化（有初始值）的数据的段定义',
            '_BSS：尚未初始化的数据的段定义',
            'group：把_BSS和_DATA这两个段定义汇总为名为DGROUP的组',
            '伪指令proc和endp围起来的部分:过程（procedure）的范围',
            'end:源代码的结束'
        ]}
    ]},
],
'汇编语言(下）':[
    {'语法:操作码+操作数':[
        {'操作码':[
            'mov A,B:把B值赋给A',
            'add A,B:A与B的值相加，结果赋值给A',
            'push A:把A的值存储在栈中',
            'pop A:从栈中读取出值，赋给A',
            'cmp A,B:对A跟B的值进行比较，比较结果会自动存入标志寄存器',
            'jge/jl/jle 标签名：和cmp命令组合使用，跳转到标签行'
            'inc A:A的值加1',
            'jmp 标签名：将控制无条件跳转到指定标签行',
            'call A:调用函数A',
            'ret 无：将处理返回到函数的调用源',
            'xor A,B:A和B的位进行异或比较，并将结果存入A中'
        ]},
        {'操作数':[
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
        ]},
        {'函数':[
            '函数调用机制',
            '函数内部处理：参数通过栈来传递，返回值通过寄存器来返回'
        ]},
        {'其它':[
            '全局变量',
            '循环处理的实现方法:xor inc com jl',
            '条件分支的实现方法:com jle jge jmp'
        ]}
    ]},
    {'流程':[
        '加载本地代码到内存，内存中存储着构成本地代码的指令和数据',
        '程序运行时：CPU从内存中把指令和数据读出，将其存储在CPU内部的寄存器中进行处理'
    ]}
]
}

for key in content:
    t1 = r2.addSubTopic()
    t1.setTopicHyperlink(s2.getID()) 
    list=key.split("：")
    t1.setTitle(list[0])
    if len(list)>1:
        t1.setPlainNotes(list[1]) 
    # print(content[key])
    for i in content[key]:
        # print(type(i))
        if(type(i).__name__=='dict'):
            for t in i:
                t11 = t1.addSubTopic()
                t11.setTitle(t)
                for j in i[t]:
                    if(type(j).__name__=='dict'):
                        for h in j:
                            t111 = t11.addSubTopic()
                            t111.setTitle(h) 
                            for m in j[h]:
                                if(type(m).__name__=='dict'):
                                    for n in m:
                                        t1111 = t111.addSubTopic()
                                        t1111.setTitle(n) 
                                        for l in m[n]:
                                            t11111 = t1111.addSubTopic()
                                            t11111.setTitle(l) 
                                else:
                                    t1111 = t111.addSubTopic()
                                    t1111.setTitle(m) 
                    else:
                        t111 = t11.addSubTopic()
                        t111.setTitle(j) 
        else:
            t11 = t1.addSubTopic()
            t11.setTitle(i) 



topics=r2.getSubTopics()
for topic in topics:
    topic.addMarker(MarkerId.starBlue)

xmind.save(w,"c:\\Users\\btr\\Desktop\\cpu.xmind") 