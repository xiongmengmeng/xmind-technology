import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
xmind_name="cpu"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("外围设备控制")
r2=s2.getRootTopic()
r2.setTitle("外围设备控制")


content={

'3种识别方式':[
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
],
'例子':[
        '显示器中显示的信息一直存储在某内存中，该内存称VRAM（VideoRAM）',
        '在程序中，往VRAM中写入数据，数据就会在显示器中显示，借助中断进行处理',
        '显卡中一般都配置有与主内存相独立的VRAM和GPU（图形处理器）'
]
}

#构建xmind
xmind.build(content,r2)

#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 