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
'乐观锁VS悲观锁':[
    {'区别':[
        '线程要不要锁住同步资源'
    ]},
    {'悲观锁':[
        '适写操作多场景,在Java中使用，是利用各种锁'
    ]},
    {'乐观锁':[
        '适读操作多场景,在Java中使用，是无锁编程，常用CAS算法'
    ]}
],
'偏向锁VS轻量级锁VS重量级锁':[
    {'偏向锁':[
        '通过对比Mark Word解决加锁问题，避免执行CAS操作'
    ]},
    {'轻量级锁':[
        '通过用CAS操作和自旋来解决加锁问题，避免线程阻塞和唤醒而影响性能'
    ]},
    {'重量级锁':[
        '将除了拥有锁的线程以外的线程都阻塞'
    ]}
],
'自旋锁VS适应性自旋锁 ':[
    {'区别':[
        '自旋时间或次数是否固定'
    ]},
    {'自旋锁':[
        {'适用':[
            '线程挂起和恢复现场的时长>用户代码执行时长'
        ]},
        {'评价':[
            '避免线程切换开销',
            '但占用处理器时间',
            '使用CPU时间换取线程阻塞与调度的开销'
        ]},
        {'实现':[
            'do-while循环',
        ]},
        '注意：自旋等待时间要有限度，没有成功获得锁，应当挂起线程',
        {'三种常见的锁形式':[
            'TicketLock',
            'CLHlock',
            'MCSlock'
        ]}
    ]},
    {'适应性自旋锁':[
        '自旋时间或次数不固定:由前一次在同一个锁上的自旋时间及锁拥有者的状态决定',
        {'情况1':[
            '如在同一个锁对象上',
            '自旋等待刚成功获得过锁，并且持有锁的线程正在运行中',
            '虚拟机认为这次自旋很有可能成功',
            '进而允许自旋等待更长时间'
        ]},
        {'情况2':[
            '如某个锁自旋很少成功获得过',
            '以后尝试获取这个锁将省略自旋',
            '直接阻塞线程，避免浪费处理器资源'
        ]}

    ]}
],
'伪共享':[
    {'前提':[
        '缓存系统中是以缓存行(cache line)为单位存储数据的'
    ]},
    '当多线程修改互相独立的变量时,如果这些变量共享同一个缓存行,会无意中影响彼此的性能(轮番发送RFO消息，占得缓存行的拥有权)',
    {'避免':[
        '缓存填充：让不同线程操作的对象处于不同的缓存行',
        '使用编译指示，强制使每一个变量对齐'
    ]}
],


}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 