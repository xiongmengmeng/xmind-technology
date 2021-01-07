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
'AQS(上)':[
'AbstractQueuedSynchronizer （抽象队列式的同步器）',
    '实现同步器的基础组件，并发包中锁的底层是使用AQS实现的',
    '如常用的ReentrantLock/Semaphore/CountDownLatch',
    {'简介':[
        '一个FIFO的双向队列',
        '内部通过节点head和tail记录队首和队尾元素',
        '队列元素类型为Node'
    ]},
    {'重要元素':[
        {'state':[
            'volatile int state(代表共享资源)'
            'ReentrantLock:state表示当前线程获取锁的可重入次数',
            'ReentrantReadWriteLock:state高16位表示读状态(获取该读锁的次数)，低16位表示写状态',
            'semaphore:state表示当前可用信号个数',
            'CountDownlatch:state表示计数器当前值',
            {'三种访问方式':[
                'getState()',
                'setState()',
                'compareAndSetState()'
            ]}
        ]},
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
            '是条件变量，每个条件变量对应一个条件队列（单向链表）:',
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
    ]},
],
'AQS(下)':[
    
    {'核心方法':[
          {'acquire（int arg）':[
            '1.先使用tryAcquire方法尝试获取资源(设置状态变量state的值)，成功则直接返回',
            '2.失败则将当前线程封装为类型为Node.EXCLUSIVE的Node节点插入到AQS阻塞队列尾部',
            '并调用LockSupport.park（this）方法挂起自己'
        ]},
        {'release（int arg）':[
            '1.尝试使用tryRelease操作释放资源(设置状态变量state的值)',
            '2.调用LockSupport.unpark（thread）方法激活AQS队列里被阻塞的线程（thread）',
            '3.被激活的线程则使用tryAcquire尝试，看当前状态变量state的值是否能满足自己的需要',
            '满足则该线程被激活，然后继续向下运行，否则还是会被放入AQS队列并被挂起'
        ]},
        'tryAcquire和tryRelease由具体的子类实现'
    ]},
    {'常自定义方法':[
        '1.isHeldExclusively():线程是否正在独占资源,只有用到condition才需去实现它',
        '2.tryAquire(int):独占方式,尝试获取资源，成功返回true，失败返回false',
        '3.tryRelease(int):独占方式,尝试释放资源，成功返回true，失败返回false',
        '4.tryAcquireShared(int):共享方式,尝试获取资源,负数表示失败；0表示成功，但没有剩余可用资源；正数表示成功，且有剩余资源',
        '5.tryReleaseShared(int):共享方式,尝试释放资源，如果释放后允许唤醒后续等待结点返回true，否则返回false'
    ]},
    {'两种资源共享方式':[
        'Exclusive（独占，只有一个线程能执行，如ReentrantLock）',
        'Share（共享，多个线程可同时执行，如Semaphore/CountDownLatch）'
    ]},
    {'ReentrantLock为例':[
        'state初始化为0，表示未锁定状态',
        'A线程lock()时，调用tryAcquire()独占该锁并将state+1',
        '其他线程再tryAcquire()会失败，直到A线程unlock()到state=0(释放锁)为止，其他线程才有机会获取该锁',
        '释放锁之前，A线程可以重复获取此锁(state会累加)',
        '注意，获取多少次就要释放多少次，这样才能保证state能回到0'
    ]}
]

}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 