import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="thread"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("线程基本概念")
r2=s2.getRootTopic()
r2.setTitle("线程基本概念")


content={
'进程':[
    '操作系统管理的基本运行单元',
    '当一个程序被运行，从磁盘加载程序的代码到内存，就开启了一个进程'
    '如:一个正在运行的exe程序'
],
'线程':[
    '一个指令流，将指令流中的一条条指令以一定的顺序交给CPU处理',
    '进程中独立运行的子任务',
    '最大限度地利用CPU空闲时间处理任务'
],
'并行与并发':[
    '单核CPU下，线程串行执行',
    {'任务调度器':[
        '将cpu的时间片(15毫秒)分给不同的程序使用',
        '由于cpu在线程间(时间片)的切换很快，感觉是同时运行的'
    ]},
    {'并发':[
        '线程轮流使用cpu,实际是串行的'
    ]},
    {'并行':[
        '多核cpu下，每个核都可调试运行线程'
    ]}
],
'多线程':[
    {'异步':[
        '代码运行结果与代码执行或调用顺序无关'
    ]},
    {'实现方式':[
        '继承Thread类',
        '实现Runnable接口',
        '实现Callable接囗（FutureTask接收返回值）'
    ]},
    {'Future接口':[
        '获取异步计算结果',
    ]},
    {'FutureTask类':[
        'Future接口的实现类',
    ]}
],
'非线程安全':[
    '多个线程对同一个对象中的同一个实例变量进行操作->出现值被更改、不同步的情况->影响程序的执行流程',
    {'分类':[
        '成员变量：共享的,有读写操作的',
        '局部变量：引用对象逃离方法作用范围'
    ]},
    '线程安全包含原子性和可见性'
],
# 'Timer定时器类':[
#     {'1.Timer类':[
#         '设置计划任务，TimeTask类：封闭计划任务'
#     ]},
#     {'2.Schedule(TimeTask timeTask,Date time)在指定时间执行一次某任务':[
#         '一个timer可运行多个TimeTask',
#         'TimeTask以队列方式一个一个被顺序执行',
#         '执行的时间可能跟预计不一致（单线程执行）'
#     ]},
#     {'3.Schedule(TimeTask timeTask,Date firstTime,long period)':[
#         '指定日期后，按指定间隔周期性无限循环地执行某一任务'
#     ]}
# ],
'多线程下的单例':[
    {'立即加载':[
        '使用类时已将对象创建完毕，不存在线程安全问题',
        '类加载的准备阶段为类变量分配空间，设初始值，初始化阶段为类变量赋值'
    ]},
    {'延迟加载':[
        '兼顾效率与线程安全性，使用DCL双检查锁机制：volatile+synchronized',
        'private volatile static MyObject myObject;'
        '....',
        'synchronized (MyObject.class) {',
        '   if (object == null) {',
        '       object = new MyObject();',
        '   }',
        '}',
        {'静态内置类实现':[
            '类加载的初始化阶段会执行类的静态语句块'
        ]}
    ]}
]
}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 