import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="thread"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("lock")
r2=s2.getRootTopic()
r2.setTitle("锁")


content={

'ReentrantLock':[
    '可重入锁',
    'AbstractQueuedSynchronizer (AQS)',
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
    {'很多类的基础':[
        'ConcurrentHashMap内部使用的Segment是继承ReentrantLock',
        'CopyOnWriteArrayList也使用了ReentrantLock'
    ]},
    'Lock可代替synchronized关键字，且具有更强的功能'
],
'ReentrantReadWriteLock':[
    '读写锁',
    'AbstractQueuedSynchronizer (AQS)',
    '有两个锁，一个读操作相关锁，共享锁；一个写相关锁，排他锁',
    '读锁：lock.readLock()',
    '写锁：lock.writeLock()',
    '读读共享，读写、写写互斥'
],
'并发工具类':[
    {'Semaphore':[
        '共享锁:该锁可被多个线程所持有',
        '可指定多个线程同时访问某个资源',
        '适用于限制访问某些资源的线程数目，可以用它来做限流',
        '不会实现数据的同步'
    ]},
    {'CountDownLatch':[
        '共享锁:该锁可被多个线程所持有',
        '可看成一个倒计数器，允许一个或多个线程等待其他线程完成操作',
        'countDown():将计数器减1',
        'await():会阻塞当前线程直到计数器变为0'
    ]},
    'CyclicBarrier'
],
'分段锁':[
    'ConcurrentHashMap分段锁Segment(继承了ReentrantLock)',
    '内部拥有一个Entry数组->',
    '数组中每个元素又是一个链表,同时是一个ReentrantLock'
],
'分布式锁':[
    'RLock'
]


}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 