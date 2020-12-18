import xmind
from xmind.core.markerref import MarkerId
w = xmind.load("c:\\Users\\btr\\Desktop\\cpu.xmind") 
s2=w.createSheet()
s2.setTitle("cpu3_operateSystem")
r2=s2.getRootTopic()
r2.setTitle("计算机基础")


content={
'运行环境':[
    '运行环境=操作系统 + 硬件',
    {'硬件':[
        'CPU',
        '存储程序指令和数据的内存',
        '通过I/O连接的键盘、显示器、硬盘、打印机等外围设备'
    ]},
    {'CPU':[
        '负责解析并运行本地代码',
        '机器语言的程序称为本地代码（native code）',
        '源代码:程序员用C语言等编写的程序，在编写阶段仅仅是文本文件',
        '通过对源代码进行编译，就可以得到本地代码']},
    {'Windows操作系统':[
        '前身是监控程序:加载和运行程序',
         {'3部分':[
            '硬件控制程序:硬件控制，程序运行控制',
            '编程语言处理器（汇编、编译、解析）',
            '各种实用程序：调试工具，dump程序，文本编辑器'
         ]},
         {'特征':[
            '克服了除CPU以外的硬件差异',
            '应用通过操作系统API间接控制硬件',
            {'详细':[
                '键盘输入、显示器输出等是通过向Windows发送指令间接实现向硬件发送指令',
                '系统调用（system call）:操作系统通过函数来控制硬件的形为',
                '使硬件抽象化:文件是操作系统对磁盘媒介空间的抽象化',
                '通过API函数集来提供系统调用,API通过多个DLL文件来提供',
            ]},
            'GUI（Graphical User Interface，图形用户界面）',
            '多任务:Windows是通过时钟分割技术来实现同时运行多个程序的功能'
        ]}  
    ]},
    {'源代码的运行方案':[
        'Unix系列操作系统FreeBSD中Ports的机制,能结合当前硬件环境编译应用源代码，得到本地代码',
        '利用虚拟机获得其他操作系统环境',
        {'JAVA':[
            '提供不依赖于特定硬件及操作系统的程序运行环境',
            'Java编译器:将程序员编写的源代码（sample.java）转换成字节码（sample.class）',
            'Java虚拟机（java.exe）:把字节代码变换成x86系列CPU适用的本地代码',
            '由x86系列CPU负责实际的处理',
            '从操作系统看，Java虚拟机是一个应用，从Java应用看，Java虚拟机是运行环境'
        ]}
    ]}],
'外围设备控制':[
    {'3种识别方式':[
        {'I/O端口号':[
            {'计算机主机':[
                '计算机主机中，附带用来连接显示器等外围设备的连接器',
                '连接器内部，有计算机主机同外围设备间交换数据的IC'
            ]},
            {'I/O 控制器':[
                'Input/Output的缩写',
                '显示器、键盘等外围设备有各自专用的I/O控制器',
                'I/O控制器中有用于临时保存输入输出数据的内存',
                '这个内存就是端口'
            ]},
            {'对比':[
                'CPU内部的寄存器用来进行数据运算',
                'I/O寄存器用来临时存储数据'
            ]}
        ]},
        {'IRQ':[
            'Interrupt Request 中断处理',
            '定义：用来暂停正在运行的程序，并跳转到其他程序的必要机制',
            '实施中断请求的是----连接外围设备的I/O控制器',
            '实施中断处理的是----CPU',
            '中断控制器会把从多个外围设备发出的中断请求有序传给CPU',
            '实时处理从外围设备输入的数据',
            {'中断请求过程':[
                '1.寄存器的备份：把CPU所有寄存器的数值保存到内存的栈中',
                '2.外围设备控制：在中断处理程序中完成外围设备的输入输出',
                '3.寄存器的还原：把栈中保存的数值还原到CPU寄存器中',
                '4.主程序的处理']}
        ]},
        {'DMA':[
            'Direct Memory Access',
            '不通过CPU，外围设备直接和主内存进行数据传送',
            '可实现短时间内传送大量数据,因CPU作为中介的时间被节省了',
            '像磁盘这样用来处理大量数据的外围设备都具有DMA功能'
        ]}
    ]},
    {'例子':[
            '显示器中显示的信息一直存储在某内存中，该内存称VRAM（VideoRAM）',
            '在程序中，往VRAM中写入数据，数据就会在显示器中显示，借助中断进行处理',
            '显卡中一般都配置有与主内存相独立的VRAM和GPU（图形处理器）'
    ]}]
}

for key in content:
    t1 = r2.addSubTopic()
    t1.setTopicHyperlink(s2.getID()) 
    list=key.split(":")
    t1.setTitle(list[0])
    if len(list)>1:
        t1.setPlainNotes(list[1]) 
    # print(content[key])
    for i in content[key]:
        # print(type(i))
        if(type(i).__name__=='dict'):
            for t in i:
                t2 = t1.addSubTopic()
                t2.setTopicHyperlink(t1.getID()) 
                t2.setTitle(t)
                for j in i[t]:
                    #print(j)
                    if(type(j).__name__=='dict'):
                        for h in j:
                            t3 = t2.addSubTopic()
                            t3.setTopicHyperlink(t2.getID()) 
                            t3.setTitle(h) 
                            for m in j[h]:
                                if(type(m).__name__=='dict'):
                                    for n in m:
                                        t4 = t3.addSubTopic()
                                        t4.setTitle(n) 
                                        for l in m[n]:
                                            if(type(l).__name__=='dict'):
                                                for k in l:
                                                    t5 = t4.addSubTopic()       
                                                    t5.setTitle(k)
                                                    for p in l[k]:
                                                        if(type(p).__name__=='dict'):
                                                            for u in p:
                                                                t6 = t5.addSubTopic()
                                                                t6.setTitle(u)
                                                                for y in p[u]:
                                                                    if(type(y).__name__=='dict'):
                                                                        for a in y:
                                                                            t7 = t6.addSubTopic()
                                                                            t7.setTitle(a)
                                                                            for b in y[a]:
                                                                                t8 = t7.addSubTopic()
                                                                                t8.setTitle(b)
                                                                    else:
                                                                        t7 = t6.addSubTopic()
                                                                        t7.setTopicHyperlink(t2.getID()) 
                                                                        t7.setTitle(y)              
                                                        else:
                                                            t6 = t5.addSubTopic()
                                                            t6.setTopicHyperlink(t2.getID()) 
                                                            t6.setTitle(p)                                                        
                                            else:
                                                t5 = t4.addSubTopic()
                                                t5.setTopicHyperlink(t3.getID()) 
                                                t5.setTitle(l) 
                                else:
                                    t4 = t3.addSubTopic()
                                    t4.setTopicHyperlink(t3.getID()) 
                                    t4.setTitle(m) 
                    else:
                        t3 = t2.addSubTopic()
                        t3.setTopicHyperlink(t2.getID()) 
                        t3.setTitle(j) 
        else:
            t2 = t1.addSubTopic()
            t2.setTopicHyperlink(t1.getID()) 
            t2.setTitle(i) 



topics=r2.getSubTopics()
for topic in topics:
    topic.addMarker(MarkerId.starBlue)

xmind.save(w,"c:\\Users\\btr\\Desktop\\cpu.xmind") 