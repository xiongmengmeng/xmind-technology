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
        '如:一个正在运行的exe程序'
    ]},
    {'线程':[
        '进程中独立运行的子任务',
        '最大限度地利用CPU空闲时间处理任务'
    ]},
    {'多线程':[
        '异步',
        '代码运行结果与代码执行或调用顺序无关',
        {'实现方式':[
            '继承Thread类',
            '实现Runnable接口',
            '实现Callable接囗（有返回值）'
        ]},
    ]},
    {'非线程安全':[
        '多个线程对同一个对象中的同一个实例变量进行操作->',
        '出现值被更改、不同步的情况->',
        '影响程序的执行流程'
    ]},
    {'方法':[
        'start():通知"线程规划器"此线程已准备就绪，等待调用线程对象的run()方法',
        'currentThread():代码段正在被哪个线程调用',
        'isAlive():当前线程是否处于活动状态(正在运行或准备开始运行)',
        'sleep():在指定毫秒数内让"正在执行的线程(this.currentThread())"休眠',
        'getId():线程唯一标识',
        'suspend():暂停线程,resume():恢复线程执行',
        'yield():放弃当前的CPU资源(放弃的时间不确定)',
        'setPriority():设置线程优先级,有继承性',
        {'线程停止':[
            '1.抛异常',
            '2.使用退出标志，线程正常退出:run方法完成后线程终止',
            '3.stop():强行终止(不推荐),可能产生不可预料结果',
            '4.interrupt+return:在当前线程中打了一个停止标记，并不是真的停止线程',
            'interrupted():判断当前线程是否中断，执行后将状态标志为清除',
            'isInterrupted():判断当前线程是否中断，不清除状态标志'
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
        {'原理':[
            {'synchronized（this）':[
                '通过javap生成的字节码中包含monitorenter和monitorexit两个指令',
                '进入锁时执行monitorenter指令，会获取对象的monitor',
                'wait/notify方法也依赖于monitor对象',
                '所以只有在同步块或方法中才能调用wait/notify，否则抛java.lang.IllegalMonitorStateException',
            ]},
            {'synchronized 方法':[
                '相对普通方法，常量池中多了ACC_SYNCHRONIZED标示符,JVM根据标示符来实现方法同步',
                '方法调用时，调用指令检查方法的ACC_SYNCHRONIZED访问标志是否被设置',
                '如设置了，执行线程先获取monitor，获取成功后执行方法体，方法执行完后释放monitor',
                '在方法执行期间，其他任何线程都无法再获得同一个monitor对象',
                '本质与synchronized（this）没有区别，只是用一种隐式的方式来实现，无需通过字节码'
            ]}
        ]},
        {'锁对象':[
            'synchronized 方法',
            'synchronized（this）代码块',
            {'详细':[
                '1.A线程先持有对象锁，B线程可异步调用对象中的非synchronized方法',
                '2.A线程先持有对象锁，B线程调用对象中synchronized类型方法需等待'
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
            '共享资源的读写访问需同步，不是共享资源没有同步必要',
            '多个线程访问同一个对象需同步',
            '多个线程访问多个对象，JVM会创建多个锁，无需同步'
        ]},
        {'特性':[
            {'可重入':[
                '自己可以再次获取自己的锁',
                '支持子类继承',
                '一个synchronized方法/块的内可以调用本类的其他synchronized方法'
            ]},
            '可见性：线程加锁时必须从主内存中获得最新的值，解锁时必须把变量的值刷新到内存中去',
            '异常锁自动释放',
            '不具有继承性:因为子类重写了方法'
        ]},
        {'死锁':[
            '经典的多线程问题',
            '不同的线程等待不可能被释放的锁，导致线程假死(waiting)'
        ]}
    ]},
    {'volatile':[
        '强制从公共堆栈中取得变量的值，而不是从线程私有数据栈中取得变量的值',
        '使变量在多个线程间可见,不具有原子性',
        {'MESI':[
            '缓存一致性协议',
            'CPU写数据时，如发现操作变量是共享变量，发出信号通知其他CPU将该变量的缓存行置为无效',
            '当其他CPU需要读取变量时，发现缓存变量的缓存行无效，就会从内存重新读取',
            {'嗅探':[
                '每个处理器通过嗅探在总线上传播的数据来检查自己缓存的值是否过期',
                '当处理器发现自己缓存行对应的内存地址被修改，会将缓存行设置成无效',
                '当处理器对数据进行修改时，会重新从系统内存中把数据读到处理器缓存中'
            ]},
            {'总线风暴':[
                '由于MESI缓存一致性协议，需不断从主内存嗅探和cas不断循环，无效交互会导致总线带宽达到峰值'
            ]}
        ]},
        {'禁止指令重排序':[
            '指令重排:源代码 -> 编译器优化的重排 -> 指令并行的重排 -> 内存系统的重排 -> 最终执行指令',
            '多线程环境中线程交替执行，由于编译器优化重排，两线程中使用的变量能否保证一致性无法确定，结果无法预测',
            {'使用内存屏障':[
                '一个CPU指令',
                '保证特定操作的顺序:禁止在内存屏障前后的指令执行重排序优化',
                '保证某些变量的内存可见性:刷新CPU缓存'
            ]}
        ]}
    ]},
    {'synchronized和volatile比较':[
        '1.volatile:线程同步的轻量级实现，性能好，只能修饰变量',
        'synchronized:可修饰方法及代码块,使用面广',
        '2.多线程访问volatile不会发生阻塞，而synchronized会出现阻塞',
        '3.volatile:保证数据的可见性，不保证原子性',
        'synchronized:可保证原子性和可见性（会将私有内存和公共内存数据做同步）',
        '4.volatile解决变量在多个线程之间的可见性',
        'synchronized解决多线程之间访问资源的同步性'
    ]}

],
'线程间通信':[
    {'等待/通知机制':[
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
                '重量级锁模式时对象头是一个指向互斥量的指针，实际上互斥量就是一个监视器锁（ObjectMonitor）的数据结构',
                '此时对象的hashCode、分代年龄等信息都会保存到对应的ObjectMonitor中',
                {'ObjectMonitor属性':[
                    'recursion记录本锁被重入的次数',
                    'EntrySet：处于等待锁block状态的线程',
                    'WaitSet：处于wait状态的线程',
                    'TheOwner记录拥有本锁的线程对象'
                ]}

            ]},
            '几个线程一起竞争对象的锁（EntrySet），只有一个能成功（acquire），成功的线程记录在The Owner中',
            {'调用wait、notify运行流程':[
                '有一个对象o，锁被线程t1持有，调用wait()后，线程t1将会被放到Wait Set 结构中',
                '然后另一个线程t2获取到锁，The Owner记录的变成t2线程',
                't2 线程不需要o锁时，调用o.notify()，对象o告诉 Wait Set中的线程：你们又可以来竞争我啦，我的锁现在没被人持有',
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
    ]},
    {'join()':[
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
    ]},
    {'ThreadLocal类':[
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
            '3.在Entry内部使用ThreadLocal作为key，我们设置的value作为value'
            '4.ThreadLocal创建的副本是存储在自己的threadLocals中的，也就是自己的ThreadLocalMap',
            '5.ThreadLocalMap的键值为ThreadLocal对象，可以有多个threadLocal变量',
            '6.进行get前，必须先set，否则报空指针异常，也可以初始化一个(重写initialValue()方法)',
            '7.ThreadLocal本身并不存储值，它作为一个key来让线程从ThreadLocalMap获取value',
            '8.通过threadLocalHashCode来标识每一个ThreadLocal的唯一性',
            {'ThreadLocalMap中key为ThreadLocal的弱引用':[
                '如此对象只存在弱引用，下一次垃圾回收的时必被清理掉->',
                'ThreadLocalMap中ThreadLocal的key会被清理掉',
                '但value是强引用，不会被清理，会出现key为null的value',
                '优化是在调用 set()、get()、remove() 方法时，会清理掉key为null的记录',
                '建议回收自定义的ThreadLocal变量',
                '尤其在线程池场景下，线程经常会被复用，不清理可能会影响后续业务逻辑和造成内存泄露',
                '尽量在代理中使用try-finally块进行回收',

            ]}
        ]}
    ]}
],
'Lock':[
    {'ReentrantLock':[
        '可重入锁',
        {'分类':[
            'New ReentrantLock(Boolean isFair)',
            '公平锁：线程获取锁顺序按线程加锁顺序分配，FIFO先进先出顺序',
            '非公平锁：线程抢占,随机获得锁，可能造成某些线程一直拿不到锁'
        ]},
        {'方法':[
            'Lock lock=new ReentrantLock()',
            'Condition condition=lock.newCondition()'
            'lock():获取锁,线程是持有了对象监视器',
            'unlock():释放锁',
            'boolean tryLock():未被另一个线程持有，获取该锁定',
            'boolean tryLock(long timeout，TimeUnit unit)：给定时间内未被另一个线程锁定，获取该锁定',
            'boolean isHeldByCurrentThread():当前线程是否保持此锁定',
            'boolean isLocked():此锁定是否由任意线程保持',
            'int getHoldCount():当前线程保持此锁定的个数(即调用lock()方法的次数)',
            'int getQueueLength():正等待获取此锁定的线程估计数',
            'int getWaitQueueLength(Condition conditio):等待与此锁定相关的给定条件Condition的线程估计数'
        ]},
        {'与synchronized对比':[
            '一个Lock对象中以创建多个condition(对象监视器)实例',
            'synchronized只有一个对象监视器对象',
            'condition可以实现选择性通知',
            'notity()中被通知的线程是由jvm选择的'
        ]},
        {'使用condition实现等待/通知':[
            '可实现"选择性通知"(唤醒指定种类的线程):类似wait()/notify()',
            '生产者/消费者模式,不会出现线程假死',
            'Object类wait()相当于Condition类await()',
            'Object类notify()相当于Condition类signal()',
            '注：condition.await()调用前需调lock.lock()获得同步监视器'
        ]},
    ]},
    {'ReentrantReadWriteLock':[
        '读写锁',
        '有两个锁，一个读操作相关锁，共享锁；一个写相关锁，排他锁',
        '读锁：lock.readLock()',
        '写锁：lock.writeLock()',
        '读读共享，读写、写写互斥'
    ]},
    'Lock可代替synchronized关键字，且具有更强的功能'
],
'Timer定时器类':[
    'Timer类：设置计划任务，TimeTask类：封闭计划任务',
    'Schedule(TimeTask timeTask,Date time)在指定时间执行一次某任务',
    '一个timer可运行多个TimeTask，TimeTask以队列方式一个一个被顺序执行，执行的时间可能跟预计不一致（单线程执行）',
    '3.Schedule(TimeTask timeTask,Date firstTime,long period)：指定日期后，按指定间隔周期性无限循环地执行某一任务'
],
'多线程下的单例':[
    '立即加载：使用类时已将对象创建完毕，不存在线程安全问题',
    '类加载的准备阶段为类变量分配空间，设初始值，初始化阶段为类变量赋值',
    '延迟加载：兼顾效率与线程安全性，使用DCL双检查锁机制：volatile+synchronized',
    'private volatile static MyObject myObject;'
    '....'
    'synchronized (MyObject.class) {',
    '   if (object == null) {',
    '       object = new MyObject();',
    '   }',
    '}',
    '静态内置类实现:类加载的初始化阶段会执行类的静态语句块',
],
'其它':[
    {'线程的状态':[
        '状态枚举：Thread.State',
        'NEW：尚未启动的线程，未执行start()',
        'RUNNABLE：正在java虚拟机中执行的线程',
        'BLOCKED：受阻塞，等待某个监视器锁的线程',
        'WAITING：无限期等待另一线程来执行某一特定操作',
        'TIMED_WAITING：有限期等待另一线程来执行某一特定操作',
        'TERMINATED：已退出'
    ]},
    {'线程组':[
        '线程组中可以有线程对象，也可以有线程组',
        '作用:批量管理线程或线程组对象'
    ]},
    {'SimpleDateFormat非线程安全,解决方式':[
        '1.建了多个SimpleDateFormat类的实例',
        '2.ThreadLocal类能使线程绑定到指定的对象'
    ]}
]



}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 