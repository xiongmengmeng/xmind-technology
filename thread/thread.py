import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="thread"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("thread")
r2=s2.getRootTopic()
r2.setTitle("多线程")


content={
'基础':[
    '非线程安全',
    'Thread方法',
    'Thread状态'
],
'关键字':[
    'synchronized',
    'volatile',
    '对比'
],
'线程间通信':[
    'wait()/notify()',
    'join()',
    'ThreadLocal',
    'CountDownLatch',
    'CycleBarrier',
    'Semaphore'
],
'锁基础':[
    {'CAS':[
        'java使用:Unsafe',
        {'应用':[
            'ThreadLocalRandom',
            'AtomicLong',
            'LongAdder',
            'LongAccumulator'
        ]}
    ]},
    'AQS'
],
'常见锁':[
    'ReentrantLock',
    'ReentrantReadWriteLock',
    'StampedLock'
],
'锁应用--队列':[
    'ConcurrentLinkedQueue',
    'LinkedBlockingQueue',
    'ArrayBlockingQueue',
    'PriorityBlockingQueue',
    'DelayQueue'
],
'线程池':[
    '参数',
    '状态',
    '工作原理'
]
}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 