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
r2.setTitle("线程")


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
'Timer定时器类':[
    '1.Timer类：设置计划任务，TimeTask类：封闭计划任务',
    '2.Schedule(TimeTask timeTask,Date time)在指定时间执行一次某任务',
    '一个timer可运行多个TimeTask',
    'TimeTask以队列方式一个一个被顺序执行',
    '执行的时间可能跟预计不一致（单线程执行）',
    '3.Schedule(TimeTask timeTask,Date firstTime,long period)',
    '指定日期后，按指定间隔周期性无限循环地执行某一任务'
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
],
'ThreadLocalRandom':[
    {'Random类':[
        '首先根据老的种子生成新的种子',
        '然后根据新的种子来计算新的随机数'
    ]},
    {'问题':[
        '多线程竞争同一个原子变量的更新操作(CAS)',
        '同一时间只有一个线程成功',
        '会造成大量线程进行自旋重试，降低并发性能'
    ]},
    '类似于ThreadLocal类，是个工具类',
    '继承了Random类并重写了nextInt方法'
    '种子存放在具体的调用线程threadLocalRandomSeed变量',
    '计算新种子时是根据线程内维护的种子变量进行更新，避免了竞争',
    {'current()':[
        '初始化调用线程的threadLocalRandomSeed变量',
        '即初始化种子'
    ]},
    {'nextInt()':[
        '1.获取当前线程的threadLocalRandomSeed变量作为当前种子',
        '2.计算并更新新的种子到当前线程threadLocalRandomSeed变量',
        '3.根据新种子并使用具体算法计算随机数'
    ]}
],
'AtomicLong':[
    {'变量':[
        'Unsafe.getUnsafe（）方法获取到Unsafe类的实例',
        'valueOffset:变量value的偏移量',
        'value被声明为volatile的，这是为了在多线程下保证内存可见性'
    ]},
    {'getAndIncrement':[
        'JDK 7:boolean compareAndSet(long expect, long update)',
        'JDK 8中unsafe.getAndAddLong',
        '内部都是调用：unsafe.compareAndSwapLong'
    ]},
    '高并发下大量线程竞争更新同一个原子变量，失败会不断自旋尝试CAS，浪费CPU资源'
],
'LongAdder':[
    '内部维护多个Cell变量，每个Cell里面有一个初始值为0的long型变量',
    '同等并发量下，争夺单个变量更新操作线程量少，变相减少争夺共享资源的并发量',
    '线程争夺一个Cell原子变量失败，可尝试在其他Cell的变量上进行CAS尝试，增加了重试CAS成功的可能性',
    '在获取LongAdder当前值时，是把所有Cell变量的value值累加后再加上base返回的'
]



}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 