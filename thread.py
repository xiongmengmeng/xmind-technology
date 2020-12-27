import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="thread"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("thread")
r2=s2.getRootTopic()
r2.setTitle("多线程")


content={
'Thread类':[
    {'进程':[
        '操作系统管理的基本运行单元',
        '如一个正在操作系统中运行的exe程序'
    ]},
    {'线程':[
        '进程中独立运行的子任务',
        '最大限度地利用CPU空闲时间处理任务'
    ]},
    {'多线程':[
        '异步',
        '代码的运行结果与代码执行顺序或调用顺序无关',
        {'实现方式':[
            '继承Thread类',
            '实现Runnable接口'
        ]},
    ]},
    {'非线程安全':[
        '多个线程对同一个对象中的同一个实例变量进行操作->',
        '出现值被更改、不同步的情况->',
        '影响程序的执行流程'
    ]},
    {'方法':[
        'start():通知“线程规划器”此线程已准备就绪，等待调用线程对象的run（）方法',
        'currentThread():返回代码段正在被哪个线程调用',
        'isAlive():当前的线程是否处于活动状态(正在运行或准备开始运行)',
        'sleep():在指定的毫秒数内让当前“正在执行的线程(this.currentThread())”休眠',
        'getId():线程唯一标识',
        'suspend():暂停线程,resume():恢复线程执行',
        'yield():放弃当前的CPU资源(放弃的时间不确定)',
        'setPriority():设置线程优先级,帮“线程规划器”确定下一次选择哪一个线程优先执行,有继承性',
        {'线程停止':[
            '异常',
            '退出标志:线程正常退出，run方法完成后线程终止',
            'stop方法强行终止(不推荐),可能产生不可预料结果',
            'interrupt方法:在当前线程中打了一个停止的标记，并不是真的停止线程',
            'interrupted法:当前线程是否中断状态，执行后将状态标志置清除',
            'isInterrupted法:线程Thread对象是否中断状态，不清除状态标志'
        ]}
    ]},
    {'Java线程分类 ':[
        '用户线程',
        '守护线程(Daemon):典型---垃圾回收线程'
    ]}
],
'对象及变量的并发访问':[
    {'非线程安全':[
        '问题存在于"实例变量"中',
        '方法内的变量：私有的，是"线程安全"的',
        '线程安全包含原子性和可见性'
    ]},
    {'synchronized':[
        '关键字取得的锁都是"对象锁"，不是把一段代码或方法当作锁',
        {'锁对象':[
            'synchronized 方法',
            'synchronized（this）代码块',
            {'详细':[
                '1.A线程先持有object对象锁，B线程可以异步调用object对象中的非synchronized方法',
                '2.A线程先持有object对象锁，B线程调用object对象中的synchronized类型方法需等待'
            ]}
        ]},
        {'锁非this对象':[
            '不阻塞类中synchronized方法,synchronized（this）代码块,锁的对象不一样'
        ]},
        {'锁类':[
            'synchronized static方法'
            'synchronized（class）代码块',
            'Class锁对类的所有对象实例起作用'
        ]},
        {'锁字符串':[
            '注意常量池带来的一些例外'
        ]},
        {'应用':[
            '共享资源的读写访问需同步，不是共享资源没有同步的必要',
            '多个线程访问同一个对象需同步，多个线程访问多个对象，JVM会创建多个锁，无需同步'
        ]},
        {'特性':[
            {'可重入':[
                '自己可以再次获取自己的锁',
                '支持子类继承',
                '一个synchronized方法/块的内可以调用本类的其他synchronized方法'
            ]},
            '异常锁自动释放',
            '不具有继承性:子类重写了方法'
        ]},
        {'死锁':[
            '经典的多线程问题',
            '不同的线程等待根本不可能被释放的锁，导致线程假死'
        ]}
    ]},
    {'volatile':[
        '使变量在多个线程间可见',
        '强制从公共堆栈中取得变量的值，而不是从线程私有数据栈中取得变量的值',
        '不支持原子性'
    ]},
    {'synchronized和volatile比较':[
        '1.volatile:线程同步的轻量级实现，volatile性能好，只能修饰变量',
        'synchronized:可修饰方法及代码块,使用面广',
        '2.多线程访问volatile不会发生阻塞，而synchronized会出现阻塞',
        '3.volatile:保证数据的=可见性，但不保证原子性',
        'synchronized:可保证原子性和可见性（会将私有内存和公共内存数据做同步）',
        '4.volatile解决变量在多个线程之间的可见性',
        'synchronized解决多线程之间访问资源的同步性'
    ]}

]


}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 