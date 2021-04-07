import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="thread"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("ReentrantReadWriteLock")
r2=s2.getRootTopic()
r2.setTitle("ReentrantReadWriteLock")


content={
'ReentrantReadWriteLock':[
    '读写锁',
    '有两个锁，一个读操作相关锁，共享锁；一个写相关锁，排他锁',
    '内部维护了一个ReadLock和一个WriteLock，依赖Sync(继承自AQS)实现，有公平和非公平的实现',
    'state的高16位表示读状态，获取到读锁次数,低16位表示写状态',
    '读锁：lock.readLock()',
    '写锁：lock.writeLock()',
    '读读共享，读写、写写互斥',
],
'StampedLock':[
    '提供的三种读写模式的锁',
    '调用获取锁的系列函数时，会返回一个long型的变量，我们称之为戳记（stamp），代表锁的状态',
    'try系列获取锁的函数，获取锁失败后会返回为0的stamp值',
    '调用释放锁和转换锁的方法时需要传入获取锁时返回的stamp值',
    '写锁writeLock:排它，不可重入',
    '悲观读锁readLock：共享，不可重入',
    '乐观读锁tryOptimisticRead:操作数据前并没有通过CAS设置锁的状态，仅仅通过位运算测试'
],
'分段锁':[
    'ConcurrentHashMap分段锁Segment(继承了ReentrantLock)',
    '内部拥有一个Entry数组->',
    '数组中每个元素又是一个链表,同时是一个ReentrantLock'
]


}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 