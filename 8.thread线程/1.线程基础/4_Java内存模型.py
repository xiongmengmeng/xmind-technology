import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) 
sys.path.insert(0,parentdir) 


import xmind
xmind_name="thread"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("Java内存模型")
r2=s2.getRootTopic()
r2.setTitle("Java内存模型")


content={
'目的':[
    '定义程序中各种变量的访问规则'
],
'内存':[
    {'与CPU的矛盾':[
        '速度差距大，时间花费在磁盘I/O、网络通信或者数据库访问上',
        {'解决方案':[
            '高速缓存-------作为内存与CPU间的缓冲',
            '读写速度接近CPU运算速度',
        ]}
    ]},
    {'主内存':[
        '所有的变量都存储其上（类比物理硬件内存）',
    ]},
    {'工作内存':[
        '每条线程一份（类比CPU缓存），保存线程使用变量的主内存副本'
    ]},
    '线程对变量的操作在工作内存进行，不直接读写主内存中数据'

],
'内存间交互操作(8种)':[
    {'lock（锁定）':[
        '作用于主内存变量',
        '标识一条线程独占的状态'
    ]},
    {'unlock（解锁）':[
        '作用于主内存变量',
        '把一个处于锁定状态的变量释放出来'
    ]},
    {'read（读取）':[
        '作用于主内存变量',
        '把变量值从主内存传输到线程的工作内存，以便load动作使用'
    ]},
    {'load（载入）':[
        '作用于工作内存变量',
        '把read操作从主内存中得到的变量值放入工作内存中'
    ]},
    {'use（使用）':[
        '作用于工作内存变量',
        '把工作内存中的变量值传递给执行引擎',
        '虚拟机遇到使用变量值的字节码指令时执行此操作'
    ]},
    {'assign（赋值）':[
        '作用于工作内存变量',
        '把从执行引擎接收的值赋给变量',
        '虚拟机遇到给变量赋值的字节码指令时执行此操作'
    ]},
    {'store（存储）':[
        '作用于工作内存变量',
        '把工作内存中变量的值传送到主内存，以便write操作使用'
    ]},
    {'write（写入）':[
        '作用于主内存变量',
        '把store操作从工作内存中得到的变量值放入主内存的变量'
    ]}
],
'内存间操作规则限定':[
    '一个新的变量只能在主内存中诞生',
    '变量从主内存拷贝到工作内存:要按顺序执行read和load操作',
    '变量从工作内存同步回主内存:要按顺序执行store和write操作',
    '对一个变量执行unlock操作前，需要把变量同步回主内存中（执行store、write操作）'
],
# '先行发生规则':[
#     '程序次序规则',
#     '管程锁定和volatile变量规则',
#     '线程启动,终止,中断，终结规则',
#     '传递性规则',
#     '时间顺序与先行发生原则无因果关系，衡量并发安全问题以先行发生原则为准'
# ]

}

#构建xmind
xmind.build(content,r2)

#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 