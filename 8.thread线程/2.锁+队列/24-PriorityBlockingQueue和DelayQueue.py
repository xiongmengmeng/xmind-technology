import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="thread"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("PriorityBlockingQueue和DelayQueue")
r2=s2.getRootTopic()
r2.setTitle("PriorityBlockingQueue和DelayQueue")


content={
'PriorityBlockingQueue':[
    {'介绍':[
        '带优先级的无界阻塞队列',
        '使用二叉树堆维护元素优先级',
        '使用数组作为元素存储的数据结构，数组可扩容',
        '出队时始终保证出队元素是堆树的根节点(优先级最高或者最低的元素)',
    ]},
    {'结构':[
        {'数组queue':[
            '存放队列元素,默认容量11,可扩容'
        ]},
        {'size':[
            '存放队列元素个数'
        ]},
        {'allocationSpinLock':[
            '自旋锁，使用CAS操作保证同时只有一个线程扩容队列，状态为0或1'
        ]},
        {'comparator比较器':[
            '比较元素大小,默认使用对象compareTo方法,可自定义'
        ]},
        {'lock独占锁':[
            '控制同时只有一个线程可进行入队、出队操作'
        ]},
        {'notEmpty条件变量':[
            '实现take方法阻塞模式'
        ]},
        {'无notFull条件变量':[
            '无界队列,put操作非阻塞'
        ]}
    ]},
    {'方法':[
        {'offer':[
            '在队列中插入一个元素，由于是无界队列，所以一直返回true'
        ]},
        {'poll':[
            '获取队列内部堆树的根节点元素，如果队列为空，则返回null'
        ]},
        {'put':[
            '内部调用的是offer操作，由于是无界队列，所以不需要阻塞'
        ]},
        {'take':[
            '获取队列内部堆树的根节点元素，如果队列为空则阻塞'
        ]}
    ]},
    '应用：存放有优先级的元素时该队列比较有用'
],
'DelayQueue':[
    {'介绍':[
        '无界阻塞延迟队列',
        '队列中元素都有过期时间，从队列获取元素，只有过期元素才会出队，队列头元素是最快要过期的元素',
        '队列元素要实现Delayed接口，重写方法：获取当前元素到过期剩余时间的方法，元素间比较方法',
    ]},
    {'结构':[
        {'PriorityQueue':[
            '存放数据'
        ]},
        {'ReentrantLock':[
            '实现线程同步'
        ]},
        {'available条件变量':[
            '与lock锁对应的，实现线程间同步'
        ]},
        {'leader':[
            '使用基于Leader-Follower模式的变体，尽量减少不必要的线程等待'
        ]}
    ]},
    {'方法':[
        {'offer':[
            '插入元素到队列，如插入元素为null则抛出异常，否则返回true'
        ]},
        {'take':[
            '获取并移除队列里延迟时间过期的元素，如果队列里面没有过期元素则等待'
        ]},
        {'poll':[
            '获取并移除队头过期元素，如没有过期元素则返回null'
        ]}
    ]}
]





}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 