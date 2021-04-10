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
'ReentrantReadWriteLock---读写锁':[
    {'有两个锁':[
        {'读锁':[
            '共享锁',
            'state的高16位表示读状态，获取到读锁次数',
            '获取：ReadLock readLock=lock.readLock()'
        ]},
        {'写锁':[
            '排他锁',
            'state的低16位表示写状态',
            '获取：WriteLock writeLock=lock.writeLock()'
        ]}
    ]},
    '读读共享，读写、写写互斥',
],
'StampedLock':[
    {'三种读写模式的锁':[
        {'写锁writeLock':[
            '排它，不可重入'
        ]},
        {'悲观读锁readLock':[
            '共享，不可重入'
        ]},
        {'乐观读锁tryOptimisticRead':[
            '操作数据前并没有通过CAS设置锁的状态，仅仅通过位运算测试'
        ]},
    ]},
    {'获取锁的系列函数':[
        '返回一个long型的变量，称为戳记（stamp），代表锁的状态',
        '返回0，代表获取锁失败'
    ]},
    '调用释放锁和转换锁的方法时需传入获取锁时返回的stamp值',
],
'分段锁':[
    'ConcurrentHashMap分段锁Segment(继承了ReentrantLock)',
    '内部拥有一个Entry数组,数组中每个元素又是一个链表'
]


}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 