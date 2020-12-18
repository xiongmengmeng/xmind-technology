import xmind
from xmind.core.markerref import MarkerId
w = xmind.load("c:\\Users\\btr\\Desktop\\cpu.xmind") 
s2=w.createSheet()
s2.setTitle("cpu1_cpu")
r2=s2.getRootTopic()
r2.setTitle("计算机基础")


content={
'CPU':[
    '解释和运行机器语言的程序内容',
    {'4部分，电流信号相互连通':[
        {'控制器':[
            '把内存上的指令、数据等读入寄存器',
            '根据指令的执行结果来控制整个计算机'
        ]},
        '运算器：运算从内存读入寄存器的数据',
        '时钟：发出CPU开始计时的时钟信号',
        {'寄存器':[
            '定义：暂存指令、数据等处理对象，可以看作是内存的一种',
            {'主要种类':[
                    '程序计数器：决定程序流程',
                    '累加寄存器',
                    '标志寄存器',
                    '指令寄存器',
                    '栈寄存器',
                    '基址寄存器',
                    '变址寄存器'
                ]}
        ]}]},
    {'机器语言':[
        {'条件分支和循环机制':[
            '程序计数器的值设定为任意地址'
        ]},
        {'函数的调用机制':[
            '在将函数的入口地址设定到程序计数器之前',
            'call指令会把调用函数后要执行的指令地址存储在名为栈的主存内',
            '函数处理完毕后，再通过函数的出口来执行return命令']},
        {'机器语言指令的4种主要类型':[
            '数据传送指令：寄存器与内存，内存与内存，内存与外围之间数据的读写操作',
            '运算指令：用累加寄存器执行算术，逻辑，比较，移位运算',
            '跳转指令：条件分支，循环，强制跳转',
            'call/return指令：函数调用/返回函数调用前的地址'
        ]}
    ]}],
'二进制':[
    {'基础定义':[
        '二进制数表示计算机信息',
        {'为什么':[
            '计算机内部是由IC这种电子部件构成的',
            'IC的一个引脚，只能表示两个状态'
        ]},
        '字节：信息的基本单位，8位二进制数被称为一个字节',
        '位权：数字的位数不同，位权也不同',
    ]},
    {'运算':[
        {'移位运算':[
            '定义：将二进制数值的各数位进行左右移位的运算'
            '<<表示左移，>>表示右移',
            '<<和>>运算符的左侧是被移位的值，右侧表示要移位的位数',
            '数位移动可以代替乘法运算和除法运算',
            '补数：用正数来表示负数',
            '补数求解：取反+ 1',
            '溢出的位,计算机会直接忽略掉',
            '左移：在空出来的低位补0',
            {'右移区分逻辑位移和算术位移':[
                '逻辑位移在最高位补0',
                '算术位移:用移位前符号位的值补足'
            ]},
            '符号扩充：用符号位的值（0或者1）填充高位']},
        {'逻辑运算':[
            '逻辑非（NOT运算）',
            '逻辑与（AND运算）',
            '逻辑或（OR运算）',
            '逻辑异或（XOR运算）']}

    ]},
    {'缺点':[
        '小数运算时出错：一些十进制数的小数无法转换成二进制数',
        {'浮点数':[
            '定义：用符号、尾数、基数和指数这四部分来表示的小数',
            '双精度浮点数--64位',
            '单精度浮点数--32位来表示全体小数'
        ]}
    ]}]
}

for key in content:
    t1 = r2.addSubTopic()
    t1.setTopicHyperlink(s2.getID()) 
    t1.setTitle(key)
    for i in content[key]:
        # print(type(i))
        if(type(i).__name__=='dict'):
            for t in i:
                t11 = t1.addSubTopic()
                t11.setTopicHyperlink(t1.getID()) 
                t11.setTitle(t)
                for j in i[t]:
                    if(type(j).__name__=='dict'):
                        for h in j:
                            t111 = t11.addSubTopic()
                            t111.setTopicHyperlink(t11.getID()) 
                            t111.setTitle(h) 
                            for m in j[h]:
                                if(type(m).__name__=='dict'):
                                    for n in m:
                                        t1111 = t111.addSubTopic()
                                        t1111.setTopicHyperlink(t111.getID()) 
                                        t1111.setTitle(n) 
                                        for l in m[n]:
                                            t11111 = t1111.addSubTopic()
                                            t11111.setTopicHyperlink(t111.getID()) 
                                            t11111.setTitle(l) 
                                else:
                                    t1111 = t111.addSubTopic()
                                    t1111.setTopicHyperlink(t111.getID()) 
                                    t1111.setTitle(m) 
                    else:
                        t111 = t11.addSubTopic()
                        t111.setTopicHyperlink(t11.getID()) 
                        t111.setTitle(j) 
        else:
            t11 = t1.addSubTopic()
            t11.setTopicHyperlink(t1.getID()) 
            t11.setTitle(i) 



topics=r2.getSubTopics()
for topic in topics:
    topic.addMarker(MarkerId.starBlue)

xmind.save(w,"c:\\Users\\btr\\Desktop\\cpu.xmind") 