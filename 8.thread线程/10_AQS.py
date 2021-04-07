import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="thread"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("lock_aqs")
r2=s2.getRootTopic()
r2.setTitle("AQS")


content={
'简介':[
    'AbstractQueuedSynchronizer （抽象队列式的同步器）',
    '实现同步器的基础组件，并发包中锁的底层是使用AQS实现的',
    '如常用的ReentrantLock/Semaphore/CountDownLatch',
],
'结构':[
    '一个FIFO的双向队列',
    '内部通过节点head和tail记录队首和队尾元素',
    '队列元素类型为Node'
],
'重要元素':[
    {'state':[
        'volatile int state(代表共享资源)',
        'ReentrantLock:state表示当前线程获取锁的可重入次数',
        'ReentrantReadWriteLock:state高16位--读状态(获取读锁次数)，低16位--写状态',
        'semaphore:state表示当前可用信号个数',
        'CountDownlatch:state表示计数器当前值'
    ]},
    'ExclusiveOwnerThread:记录当前加锁的是哪个线程',
    'FIFO线程等待队列（多线程争用资源被阻塞时进入此队列）',
    {'Node':[
        'thread：存放进入AQS队列里面的线程',
        'SHARED：标记该线程是获取共享资源时被阻塞挂起后放入AQS队列',
        'EXCLUSIVE：标记线程是获取独占资源时被挂起后放入AQS队列',
        {'waitStatus':[
            '记录当前线程等待状态',
            'CANCELLED（线程被取消了）',
            'SIGNAL（线程需要被唤醒）',
            'CONDITION（线程在条件队列里等待）',
            'PROPAGATE（释放共享资源时需通知其他节点）'
        ]},
        'prev:记录当前节点的前驱节点',
        'next:记录当前节点的后继节点'
    ]},
    {'内部类ConditionObject':[
        '结合锁实现线程同步',
        '可直接访问AQS对象内部的变量，如state状态值和AQS队列',
        '是条件变量，每个条件变量对应一个条件队列（单向链表）,类比monitor中的waitSet:',
        '用来存放调用条件变量的await方法后被阻塞的线程',
        {'await()':[
            '1.构造一个类型为Node.CONDITION的node节点，然后将该节点插入条件队列末尾',
            '2.之后当前线程会释放获取的锁（操作锁对应的state变量的值），并被阻塞挂起'
        ]},
        {'signal()':[
            '1.把条件队列里队头的一个线程节点从条件队列里移除并放入AQS的阻塞队列里面',
            '2.然后激活这个线程'
        ]}
    ]},
    '一个锁对应一个AQS阻塞队列，对应多个条件变量，每个条件变量有自己的一个条件队列'
]


}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 