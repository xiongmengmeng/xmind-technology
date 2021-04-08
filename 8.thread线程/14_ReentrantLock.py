import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="thread"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("ReentrantLock")
r2=s2.getRootTopic()
r2.setTitle("ReentrantLock")


content={
'简介':[
    '可重入锁',
    '底层：AQS (AbstractQueuedSynchronizer)',
    '可代替synchronized关键字，且具有更强的功能'
],
'分类---New ReentrantLock(Boolean isFair)':[
    '公平锁：线程获取锁顺序按线程加锁顺序分配，FIFO先进先出顺序',
    '非公平锁：线程抢占,随机获得锁，可能造成某些线程一直拿不到锁'
],
'方法':[
    'Lock lock=new ReentrantLock()',
    'Condition condition=lock.newCondition()',
    {'lock()---获取锁':[
        '线程持有了对象监视器',
        '1.通过CAS设置状态值为1,CAS成功表示当前线程获得了锁',
        '2.然后setExclusiveOwnerThread设置该锁持有者是当前线程'
    ]},
    {'unlock()---释放锁':[
        '1.如当前线程持有该锁，该线程持有的AQS状态值减1',
        '2.如减去1后当前状态值为0，当前线程释放锁',
        '3.如当前线程没有持有该锁抛出IllegalMonitorStateException异常'
    ]},
    'boolean tryLock():未被另一个线程持有，获取该锁定',
    'boolean isHeldByCurrentThread():当前线程是否保持此锁定',
    'boolean isLocked():此锁定是否由任意线程保持',
    'int getHoldCount():当前线程保持此锁定的个数(即调用lock()方法的次数)',
    'int getQueueLength():正等待获取此锁定的线程估计数',
    'int getWaitQueueLength(Condition conditio):等待与此锁定相关的给定条件Condition的线程估计数'
],
'使用condition实现等待/通知':[
    '可实现"选择性通知"(唤醒指定种类的线程):类似wait()/notify()',
    '生产者/消费者模式,不会出现线程假死',
    'Object类wait()相当于Condition类await()',
    'Object类notify()相当于Condition类signal()',
    '注：condition.await()调用前需调lock.lock()获得同步监视器'
],
'与synchronized对比':[
    'Lock对象中可以创建多个condition(对象监视器)实例',
    'synchronized只有一个对象监视器对象',
    'condition：可以实现选择性通知',
    'notity()：被通知的线程由jvm选择'
],
'扩展':[
    'ConcurrentHashMap(1.7)内部使用的Segment继承ReentrantLock',
    'CopyOnWriteArrayList使用了ReentrantLock'
]



}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 