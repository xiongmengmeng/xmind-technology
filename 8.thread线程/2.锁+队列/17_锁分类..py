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
r2.setTitle("锁分类")


content={
'公平锁VS非公平锁':[
    {'区别':[
        '多线程竞争锁时要不要排队'
    ]},
    {'公平锁':[
        '通过同步队列实现多线程按照申请锁的顺序来获取锁，实现公平特性',
        '优点:等待锁的线程不会饿死',
        '缺点:整体吞吐效率比非公平锁低，CPU唤醒阻塞线程的开销比非公平锁大'
    ]},
    {'非公平锁':[
        '多线程直接尝试获取锁，如锁刚好可用，线程获取到锁，否则到队列的队尾等待',
        '优点:减少唤起线程的开销，整体的吞吐效率高，因线程有几率不阻塞直接获得锁',
        '缺点:处于等待队列中的线程可能会饿死，或等很久才会获得锁'
    ]}
],
'可重入锁VS非可重入锁':[
    {'区别':[
        '一个线程在多个流程能不能获得同一把锁'
    ]},
    {'可重入锁':[
        'Java中ReentrantLock(AQS中维护了一个同步状态status来计数重入次数)和synchronized',
        '优点：一定程度避免死锁',
    ]},
    {'获取锁':[
        {'可重入锁':[
            '尝试获取并更新status值',
            '如status==0，CAS把status设置为1，当前线程开始执行',
            '如status!=0，判断当前线程是否是获取到这个锁的线程，如是执行status+1'
        ]},
        {'非可重入锁':[
            '尝试获取并更新status值',
            '如status!=0获取锁失败，当前线程阻塞'
        ]}
    ]},
    {'释放锁':[
        {'可重入锁':[
            '当前线程是持有锁的线程&&status-1==0',
            'status置为0,将锁释放'
        ]},
        {'非可重入锁':[
            '当前线程是持有锁的线程,status置为0，将锁释放'
        ]}
    ]}
],
'独享锁VS共享锁':[
    {'区别':[
        '多线程能不能共享一把锁'
    ]},
    {'独享锁':[
        '即排他锁，该锁一次只能被一个线程持有',
        '如线程T对数据A加上排它锁后，其他线程不能再对A加任何类型的锁',
        '获得排它锁的线程即能读数据又能修改数据',
        '如JDK中的synchronized和JUC中的ReentrantLock'
    ]},
    {'共享锁':[
        '锁可被多线程持有',
        '如线程T对数据A加共享锁后，其他线程也可对A再加共享锁，不能加排它锁',
        '获得共享锁的线程只能读数据，不能修改数据',
        '如ReentrantReadWriteLock'
    ]}
]


}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 