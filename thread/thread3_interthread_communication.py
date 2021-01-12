import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="thread"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("inter_thread_communication")
r2=s2.getRootTopic()
r2.setTitle("线程间通信")


content={

'等待/通知机制':[
    {'wait()':[
        'Object类的方法',
        '方法调用前:线程须获得该对象的对象级别锁，即在同步方法或块中调用方法',
        '调用方法未持有锁，抛IllegalMonitorStateException(RuntimeException的子类，不需try-catch捕捉异常)',
        '方法调用后:当前线程释放锁,从运行状态退出，进入等待队列，直到被再次唤醒',
        'wait()返回前，线程与其他线程竞争重新获得锁',
        'wait(long):long时间内如未未被唤醒，超过long时间自动唤醒',
        {'每个锁对象都有两个队列':[
            '就绪队列：存储将要获得锁的线程，如线程被唤醒后进入，等待CPU的调度',
            '阻塞队列：存储被阻塞的线程,如线程被wait后进入，等待下一次被唤醒'
        ]},
        {'对象锁的本质':[
            '重量级锁模式时对象头是一个指向互斥量的指针',
            '实际上互斥量是一个监视器锁（ObjectMonitor）的数据结构',
            '此时对象的hashCode、分代年龄等信息都会保存到对应的ObjectMonitor中',
            {'ObjectMonitor属性':[
                'recursion记录本锁被重入的次数',
                'EntrySet：处于等待锁block状态的线程',
                'WaitSet：处于wait状态的线程',
                'TheOwner记录拥有本锁的线程对象'
            ]}

        ]},
        '几个线程一起竞争对象的锁（EntrySet），只有一个能成功（acquire），成功的线程记录在The Owner中',
        {'wait/notify运行流程':[
            '有一个对象o，锁被线程t1持有，调用wait()后，线程t1将会被放到Wait Set结构中',
            '-->另一个线程t2获取到锁，The Owner记录变成t2线程',
            '-->t2不需要o锁时，调用o.notify()',
            '-->对象o告诉Wait Set中线程:你们可以来竞争我啦，我的锁现在没被人持有',
        ]}
    ]},
    {'notify()':[
        '调用前:线程须获得该对象的对象级别锁,如无，抛异常',
        {'调用后':[
            '不会马上释放锁：',
            '需等线程将程序执行完，即退出synchronized代码块后，线程才会释放锁',
            '会通知等待该对象锁的其他线程:',
            '如有多个线程等待,由线程规划器随机挑选一个对其发出通知，使它获取对象锁',
            '获得锁的wait线程执行完，释放锁，但其它wait状态的线程由于没有得到通知也无法执行'
        ]},
        '多次调用notify()唤醒了全部WAITING中的线程'    
    ]},
    {'notifyAll()':[
        '可使所有正在等待队列中等待同一共享资源的“全部”线程从等待状态退出，进入可运行状态'
    ]},
    {'总结':[
        'wait使线程停止运行，notify使停止的线程继续运行',
        '方法wait()锁释放与notify()锁不释放'
    ]},
    '线程状态切换图'
    '案例:"生产者/消费者"模式',
    {'通过管道进行线程间通信':[
        '管道流',
        'PipedInputStream和PipedOutputStream',
        'PipedReader和PipedWriter'
    ]}
],
'join()':[
    '等待线程对象销毁，使线程排队运行作用，类似同步的运行效果',
    '使所属的线程对象x正常执行run()中任务，使当前线程z进行无限期阻塞，等待线程x销毁后再继续执行线程z后面代码',
    'join(long)：参数是设定等待的时间',
    {'原理':[
        'while (isAlive()) {wait(0);}',
        'join(),一个synchronized方法，里面调用了wait()，目的是让持有这个对象锁(线程x)的线程z进入等待',
        '子线程x执行完毕后，JVM会调用lock.notify_all()',
        '唤醒持有对象锁(线程x)的线程，也就是主线程，继续执行'
    ]},
    {'与synchronized区别':[
        'join在内部使用wait()方法进行等待，synchronized使用对象监视器'
    ]},
    '陷阱:同步代码块中，join()后面的代码提前运行',
],
'LockSupport':[
    '作用:挂起和唤醒线程，是创建锁和其他同步类的基础',
    'LockSupport类与每个使用它的线程都会关联一个许可证',
    '默认情况下调用LockSupport类方法的线程不持有许可证',
    {'方法':[
        'park()：如调用线程已经拿到与LockSupport关联的许可证，直接返回，否则调用线程被挂起',
        'unpark(Thread thread)：thread线程持有与LockSupport类关联的许可证',
        {'park(Object blocker)':[
            'Thread类里有变量volatile Object parkBlocker',
            '存放park方法传递的blocker对象'
        ]}
    ]}
],
'ThreadLocal':[
    '每个线程有自己的共享变量，解决变量在不同线程间的隔离性',
    '通过覆盖initialValue()方法具有初始值',
    '使用类InheritableThreadLocal可在子线路中取得父线程继承下来的值',
    {'应用场景':[
        '变量在线程间隔离而在方法或类间共享的场景',
        '进行事务操作，用于存储线程事务信息',
        '数据库连接，Session会话管理',
        '全链路追踪中的 traceId 或者流程引擎中上下文的传递一般采用 ThreadLocal',
        'Spring 事务管理器采用了 ThreadLocal',
        'Spring MVC 的 RequestContextHolder 的实现使用了 ThreadLoca'
    ]},
    {'源码':[
        '1.每个Thread维护着一个ThreadLocalMap的引用',
        '2.ThreadLocalMap是ThreadLocal的内部类，用Entry（继承的弱引用）来存储数据',
        '3.在Entry内部使用ThreadLocal作为key，我们设置的value作为value',
        '4.ThreadLocal创建的副本是存储在自己的threadLocals中的，也就是自己的ThreadLocalMap',
        '5.ThreadLocalMap的键值为ThreadLocal对象，可以有多个threadLocal变量',
        '6.进行get前，必须先set，否则报空指针异常，也可以初始化一个(重写initialValue()方法)',
        '7.ThreadLocal本身并不存储值，它作为一个key来让线程从ThreadLocalMap获取value',
        '8.通过threadLocalHashCode来标识每一个ThreadLocal的唯一性',
        {'ThreadLocalMap中key':[
            '为ThreadLocal的弱引用',
            '->',
            'ThreadLocalMap中ThreadLocal的key会被清理掉',
            '但value是强引用，不会被清理，会出现key为null的value',
            '优化是在调用 set()、get()、remove()方法时，清理掉key为null的记录',
            '建议回收自定义的ThreadLocal变量',
            '尤其在线程池场景下，线程经常被复用，不清理会影响后续业务逻辑和造成内存泄露',
            '尽量在代理中使用try-finally块进行回收'
        ]}
    ]},
    {'ThreadLocalMap中key要用弱引用':[
        {'现象':[
            '业务代码中使用完ThreadLocal, ThreadLocal ref被回收',
            'threadLocalMap的Entry弱引用了threadLocal',
            '->threadLocal下次GC时被回收'
        ]},
        ''
        '弱引用:如对象只存在弱引用，下一次垃圾回收的时必被清理掉',
        '实际：key使用哪种类型引用都无法完全避免内存泄漏',
        '意义：set()、get()、remove()方法时，清理掉key为null的记录',
        ''
    ]}

]


}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 