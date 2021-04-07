import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="thread"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("并发包_队列")
r2=s2.getRootTopic()
r2.setTitle("并发包_队列")


content={
'ConcurrentLinkedQueue':[
    '使用CAS算法实现的无界非阻塞队列,入队和出队使用CAS',
    '入队时：新元素被插入队列末尾，出队时：从队列头部获取一个元素',
    '第一次执行peek或者first操作把head指向第一个真正的队列元素',
    {'结构':[
        '单向链表,每个元素包装成一个Node节点',
        '两个volatile类型的Node节点用来存放队列的首、尾节点',
        '默认头、尾节点都是指向item为null的哨兵节点',
        {'Node':[
            'item(volatile):存放节点的值',
            'next:存放链表的下一个节点'
        ]}
    ]},
    {'方法':[
        'offer:在队列末尾添加一个元素,使用CAS无阻塞算法',
        'add:在链表末尾添加一个元素，内部调用offer操作',
        'poll:在队列头部获取并移除一个元素，如队列为空则返回null',
        'peek:获取队列头部一个元素（只获取不移除），如队列为空则返回null',
        'size:计算当前队列元素个数，在并发环境下不是很有用，因为CAS没有加锁',
        'remove:如队列里存在该元素则删除,存在多个删除第一个并返回true，否则返回false'
    ]}
],
'LinkedBlockingQueue':[
    '用独占锁实现的有界阻塞队列',
    {'结构':[
        '单向链表',
        '使用头、尾节点进行入队和出队,出队和入队可同时进行',
        'count原子变量:初始值为0，记录队列元素个数',
        '两个ReentrantLock的实例，分别用来控制元素入队和出队的原子性',
        'takeLock:控制元素出队原子性,同时只有一个线程可从队头获取元素',
        'putLock:控制元素入队队原子性,同时只有一个线程可在队尾添加元素',
        'notEmpty和notFull:条件变量，内部都有一个条件队列存放进队和出队时被阻塞的线程',
        '默认队列容量为0x7fffffff'
    ]},
    {'方法':[
        'offer:向队尾插入一个元素，如队列有空闲则插入成功返回true，如队列已满则丢弃返false',
        'put:向队尾插入一个元素，如队空闲插后返回，如队满则阻塞当前线程，直到空闲插入成功返回',
        'poll:从队头获取并移除一个元素，如队列为空则返回null，不阻塞',
        'peek:获取队头元素但是不从队列里移除它，如队列为空则返回null,不阻塞',
        'take:获取当前队头元素并从队里移除,如队空则阻塞当前线程直到队不为空然后返回元素',
        'remove:删除队列里面指定元素，有则删除并返回true，没有则返回false'
    ]},
    '对头、尾节点操作分别使用单独的独占锁保证原子性',
    '独占锁都配备一个条件队列，存放被阻塞线程，结合入队、出队操作实现一个生产消费模型',
    {'ConcurrentLinkedQueue无原子变量count':[
        '原子变量保存队列元素个数需保证入队、出队操作和原子变量是原子性操作',
        '而ConcurrentLinkedQueue使用的CAS无锁算法，不是原子性的'
    ]}
]


}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 