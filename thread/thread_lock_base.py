import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="thread"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("lock_base")
r2=s2.getRootTopic()
r2.setTitle("锁基础")


content={
'AQS':[
    'AbstractQueuedSynchronized 抽象队列式的同步器',
    '定义一套多线程访问共享资源的同步器框架，许多同步类实现都依赖于它',
    '如常用的ReentrantLock/Semaphore/CountDownLatch',
    {'重要元素':[
        '一个volatile int state(代表共享资源)',
        '一个FIFO线程等待队列（多线程争用资源被阻塞时会进入此队列）'
    ]},
    {'state三种访问方式':[
        'getState()',
        'setState()',
        'compareAndSetState()'
    ]},
    {'两种资源共享方式':[
        'Exclusive（独占，只有一个线程能执行，如ReentrantLock）',
        'Share（共享，多个线程可同时执行，如Semaphore/CountDownLatch）'
    ]},
    {'自定义同步器':[
        '只需要实现共享资源state的获取与释放方式即可',
        '具体线程等待队列的维护(如获取资源失败入队/唤醒出队等),AQS已经在顶层实现好'
    ]},
    {'常自定义方法':[
        '1.isHeldExclusively():线程是否正在独占资源,只有用到condition才需去实现它',
        '2.tryAquire(int):独占方式,尝试获取资源，成功返回true，失败返回false',
        '3.tryRelease(int):独占方式,尝试释放资源，成功返回true，失败返回false',
        '4.tryAcquireShared(int):共享方式,尝试获取资源,负数表示失败；0表示成功，但没有剩余可用资源；正数表示成功，且有剩余资源',
        '5.tryReleaseShared(int):共享方式,尝试释放资源，如果释放后允许唤醒后续等待结点返回true，否则返回false'
    ]},
    {'ReentrantLock为例':[
        'state初始化为0，表示未锁定状态',
        'A线程lock()时，调用tryAcquire()独占该锁并将state+1',
        '其他线程再tryAcquire()会失败，直到A线程unlock()到state=0(释放锁)为止，其他线程才有机会获取该锁',
        '释放锁之前，A线程自己是可以重复获取此锁的(state会累加)，这就是可重入的概念',
        '注意，获取多少次就要释放多少次，这样才能保证state能回到0'
    ]}
],
'乐观锁/悲观锁':[
    '悲观锁适合写操作多的场景，乐观锁适合读操作多的场景，不加锁会带来性能提升',
    '悲观锁在Java中使用，是利用各种锁',
    '乐观锁在Java中使用，是无锁编程，常采用CAS算法，典型例子是原子类，通过CAS自旋实现原子操作的更新'
],
'CAS':[
    '一种乐观锁：冲突检查+数据更新',
    'Compare And Swap（比较与交换）:是一种无锁算法',
    '多个线程尝试使用CAS同时更新同一个变量时，只有其中一个线程能更新变量的值',
    '其他线程都失败，失败线程并不会被挂起，而是被告知这次竞争中失败，可以再次尝试',
    {'三个操作数':[
        '需要读写的内存位置（V）',
        '进行比较的预期原值（A）',
        '拟写入的新值（B）'
    ]},
    {'过程':[
        '如内存位置V的值与预期原值A匹配，处理器自动将该位置值更新为新值B',
        '否则处理器不做任何操作',
        '无论哪种情况，它都会在CAS指令之前返回该位置的值'
    ]},
    '过程在JNI里借助一个CPU指令完成，属原子操作，保证多线程都能够看到同一个变量的修改值',
    {'特性':[
        '通过调用 JNI 的代码实现',
        '非阻塞算法',
        '非独占锁'
    ]},
    {'存在问题':[
        {'ABA':[
            '可在变量前面加版本号，每次变量更新时把版本号加一',
            'AtomicStampedReference类'
        ]},
        '循环时间长(一直自旋)开销大',
        {'只能保证一个共享变量的原子操作':[
            'AtomicReference类保证引用对象间的原子性',
            '可把多变量放在一个对象里来进行CAS操作'
        ]}
    ]},
    'JDK1.5中新增java.util.concurrent包就是建立在CAS之上',
    '如AtomicInteger，注意其值value用volatile修饰，保证可见性'
],
'偏向锁/轻量级锁/重量级锁':[
    '偏向锁:一段同步代码一直被一个线程所访问，该线程会自动获取锁',
    {'轻量级锁':[
        '当锁是偏向锁时，被另一个线程所访问，偏向锁会升级为轻量级锁',
        '其他线程会通过自旋的形式尝试获取锁，不会阻塞，提高性能',
        {'自旋':[
            '好处:减少线程上下文切换的消耗',
            '缺点:循环会消耗CPU'
        ]}
    ]},
    {'重量级锁':[
        '当锁为轻量级锁时，另一个线程自旋，但不会一直自旋->',
        '自旋一定次数还没有获取到锁，会进入阻塞->',
        '该锁膨胀为重量级锁',
        '重量级锁会让他申请的线程进入阻塞，性能降低'
    ]},
    '通过对象监视器在对象头中的字段来表明的',
    '可以升级但是不可以降级，目的是提高获取锁和释放锁的效率'
]



}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 