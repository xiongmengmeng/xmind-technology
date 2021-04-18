import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
xmind_name="cpu"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("运行环境")
r2=s2.getRootTopic()
r2.setTitle("运行环境")


content={
'运行环境=操作系统 + 硬件':[],
'硬件':[
    'CPU',
    '存储程序指令和数据的内存',
    '通过I/O连接的键盘、显示器、硬盘、打印机等外围设备'
],
'CPU':[
    '负责解析并运行本地代码',
    '机器语言的程序称为本地代码（native code）',
    '源代码:程序员用C语言等编写的程序，在编写阶段仅仅是文本文件',
    '通过对源代码进行编译，就可以得到本地代码'
],
'Windows操作系统':[
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
],
'源代码的运行方案':[
    'Unix系列操作系统FreeBSD中Ports的机制,能结合当前硬件环境编译应用源代码，得到本地代码',
    '利用虚拟机获得其他操作系统环境',
    {'JAVA':[
        '提供不依赖于特定硬件及操作系统的程序运行环境',
        'Java编译器:将程序员编写的源代码（sample.java）转换成字节码（sample.class）',
        'Java虚拟机（java.exe）:把字节代码变换成x86系列CPU适用的本地代码',
        '由x86系列CPU负责实际的处理',
        '从操作系统看，Java虚拟机是一个应用，从Java应用看，Java虚拟机是运行环境'
    ]}
]
}

#构建xmind
xmind.build(content,r2)

#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 