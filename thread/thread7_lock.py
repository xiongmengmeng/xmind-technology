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
    {'lock()':[
        '通过CAS设置状态值为1,CAS成功则表示当前线程获取到了锁',
        '，然后setExclusiveOwnerThread设置该锁持有者是当前线程',
        ''
    ]},
    {'unlock()':[
        '如当前线程持有该锁，该线程持有的AQS状态值减1',
        '如减去1后当前状态值为0，当前线程释放锁',
        '否则仅仅减1',
        '如当前线程没有持有该锁抛出IllegalMonitorStateException异常'
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
    '有两个锁，一个读操作相关锁，共享锁；一个写相关锁，排他锁',
    '内部维护了一个ReadLock和一个WriteLock，依赖Sync(继承自AQS)实现，也提供了公平和非公平的实现',
    'state的高16位表示读状态，也就是获取到读锁的次数；使用低16位表示获取到写锁的线程的可重入次数',
    '读锁：lock.readLock()',
    '写锁：lock.writeLock()',
    '读读共享，读写、写写互斥',
],
'StampedLock':[
    '提供的三种读写模式的锁',
    '调用获取锁的系列函数时，会返回一个long型的变量，我们称之为戳记（stamp），代表锁的状态',
    'try系列获取锁的函数，获取锁失败后会返回为0的stamp值',
    '调用释放锁和转换锁的方法时需要传入获取锁时返回的stamp值',
    '写锁writeLock:排它，不可重入'
    '悲观读锁readLock：共享，不可重入',
    '乐观读锁tryOptimisticRead:操作数据前并没有通过CAS设置锁的状态，仅仅通过位运算测试'
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