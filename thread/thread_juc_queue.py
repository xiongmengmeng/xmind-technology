import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="thread"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("juc")
r2=s2.getRootTopic()
r2.setTitle("并发包_基础类")


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
        'remove:如队列里存在该元素则删除，如果存在多个则删除第一个，并返回true，否则返回false'
    ]}
],
'LinkedBlockingQueue':[
    '用独占锁实现的阻塞队列',
    {'':[
        '单向链表实现',
        '使用头、尾节点来进行入队和出队操作',
        ''
    ]},
    '入队操作都是对尾节点进行操作，出队操作都是对头节点进行操作',
    '对头、尾节点的操作分别使用了单独的独占锁从而保证了原子性',
    '所以出队和入队操作是可以同时进行的',
    '对头、尾节点的独占锁都配备了一个条件队列，用来存放被阻塞的线程，并结合入队、出队操作实现了一个生产消费模型'
]

}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 