import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
xmind_name="jvm"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("后端编译器")
r2=s2.getRootTopic()
r2.setTitle("后端编译器")


content={
'目标':[
    '将【程序代码】翻译为【本地机器码】',
    '优化代码'
],
'解释器':[
    'Java程序最初都是通过解释器进行解释执行的'
],
'即时编译器':[
    {'编译器编译的目标：热点代码':[
        '被多次调用的方法',
        '被多次执行的循环体'
    ]},
    {'编译的目标对象':[
        '整个方法体,对于循环体,执行入口会稍有不同',
    ]},
    {'即时编译器':[
        '运行时，将代码编译成本地机器码,并尽可能优化代码,提高热点代码执行效率'
    ]},
    {'HotSpot虚拟机内置的个即时编译器':[
        '客户端编译器”（Client Compiler）',
        '服务端编译器”（Server Compiler）',
        'Graal编译器'
    ]},
    {'触发条件:热点探测':[
        '基于采样',
        {'基于计数器':[
            '方法调用计数器',
            '回边计数器,回边:在循环边界往回跳转',
            '方法调用计数器热度衰减'
        ]},
        '两计数器有明确阈值，阈值一旦溢出，会触发即时编译'
    ]},
    {'编译过程':[
        '1.字节码->HIR(优化：方法内联，常量传播等）',
        '2.HIR->LIR(优化：空值检查消除，范围检查消除等）',
        '3.LIR->本地代码(寄存器分配，窥孔优化，机器码生成）'
    ]},
    {'优点':[
        '性能分析制导优化',
        '激进预测性优化:不行就回退',
        '链接时优化'
    ]},
    {'缺点':[
        '占用程序运行时间和运算资源'
    ]},
],
'提前编译器':[
    '传统的静态提前编译',
    '做即时编译的缓存'
]

}

#构建xmind
xmind.build(content,r2)

#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 