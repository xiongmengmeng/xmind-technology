import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="thread"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("Semaphore")
r2=s2.getRootTopic()
r2.setTitle("Semaphore")


content={
'Semaphore':[
    '初始化时可指定计数器一个初始值',
    '不需知道需要同步的线程个数',
    '只需同步的地方调用acquire方法时指定需要同步的线程个数',
    {'acquire(int permits)':[
        '获得一个许可',
        {'内容':[
            '调用了Sync的acquireSharedInterruptibly方法'
        ]},
        '1.对中断进行响应(如当前线程被中断，抛出中断异常)',
        {'2.尝试获取信号量资源,调用tryAcquireShared方法,根据公平策略有两个版本':[
            '获取当前信号量值（available）',
            '减去需要获取的值（acquires）',
            '得到剩余的信号量个数（remaining）',
            '如剩余值<0:当前信号量个数满足不了需求，返回负数',
            '如剩余值>0:使用CAS操作设置当前信号量值为剩余值，然后返回'
        ]},
        '3.返回负数，当前线程会放入AQS的阻塞队列而被挂起'
    ]},
    {'release()':[
        '释放一个许可',
        '把当前Semaphore对象的信号量值增加1',
        '根据公平策略选择一个信号量个数能被满足的线程(AQS的阻塞队列中)进行激活'
    ]},
    '计数器不可自动重置，通过改变aquire方法参数可实现CycleBarrier的功能',
    {'应用':[
        '1.多个共享资源互斥使用',
        '2.并发线程数量控制（限流）'
    ]}
],
'线程同步--实现总结':[
    '1.wait、notify',
    '2.join',
    '3.CountDownLatch',
    '4.CycleBarrier',
    '5.Semaphore'
]



}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 