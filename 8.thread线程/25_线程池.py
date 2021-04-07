import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="thread"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("ThreadPoolExecutor")
r2=s2.getRootTopic()
r2.setTitle("线程池-基础")


content={
'状态':[
    'RUNNING：接受新任务并且处理阻塞队列里的任务',
    'STOP：中断正在处理的任务,拒绝新任务并且抛弃阻塞队列里的任务',
    'TIDYING：所有任务都执行完（包含阻塞队列的）,线程池活动线程数为0，调用terminated方法',
    'TERMINATED：终止状态,terminated方法调用完成以后的状态',
    {'转换':[
        'RUNNING -> SHUTDOWN:显式调用shutdown()，或隐式调用finalize()里的shutdown()',
        'RUNNING或SHUTDOWN-> STOP:显式调用shutdownNow()时',
        'SHUTDOWN -> TIDYING:当线程池和任务队列都为空时',
        'STOP -> TIDYING:当线程池为空时',
        'TIDYING -> TERMINATED:当terminated()执行完成时'
    ]}
],
'参数':[
    'corePoolSize：核心线程数',
    'maximunPoolSize：最大线程数',
    'workQueue：等待执行任务的阻塞队列',
    'threadFactory：创建线程的工厂',
    'keeyAliveTime：如 线程数量 > corePoolSize，多出线程在keepAliveTime后释放',
    'TimeUnit：keepAliveTime的时间单位',
    'RejectedExecutionHandler：拒绝策略，队列满且线程个数达到maximunPoolSize后采取的策略',
    {'详细':[
        'AbortPolicy（抛出异常）',
        'CallerRunsPolicy（使用调用者所在线程来运行任务）',
        'DiscardOldestPolicy（调用poll丢弃一个任务，执行当前任务）',
        'DiscardPolicy（默默丢弃，不抛出异常）'
    ]}
],
'工作原理':[
    {'举例：':[
        'corePoolSize：1',
        'mamximumPoolSize：3',
        'keepAliveTime：60s',
        'workQueue：ArrayBlockingQueue，有界阻塞队列，队列大小4',
        'handler：默认策略，抛ThreadPoolRejectException'
    ]},
    '1.开始有一个线程变量poolSize维护当前线程数量.poolSize=0',
    '2.来一个任务.需创建线程.poolSize(0) < corePoolSize(1),直接创建线程',
    '3.来一个任务.需创建线程.poolSize(1) >= corePoolSize(1),队列没满,丢到队列中',
    '4.如队列满了,但是poolSize < mamximumPoolSize,继续创建线程',
    '5.如poolSize==maximumPoolSize,再提交任务,执行handler,默认抛异常',
    '6.如线程池有3个线程处于空闲状态,corePoolSize=1,超出的2个空闲线程,空闲超过60s,会给回收掉'
],
'类图':[
    'ctl:Integer的原子变量，记录线程池状态和线程池中线程个数',
    'mainLock:独占锁，控制新增Worker线程操作的原子性',
    'termination:锁对应的条件队列，在线程调用awaitTermination时存放阻塞的线程',
    'Worker:继承AQS和Runnable接口，具体承载任务的对象,实现了简单不可重入独占锁',
    {'Worker':[
        'state:锁状态，0-锁未被获取，1-锁已被获取，-1-创建Worker时默认的状态',
        'firstTask：工作线程执行的第一个任务',
        'thread：具体执行任务的线程'
    ]},
    {'DefaultThreadFactory线程工厂':[
        'newThread方法是对线程的一个修饰',
        'poolNumber：静态的原子变量，统计线程工厂的个数',
        'threadNumber：记录每个线程工厂创建了多少线程'
    ]}
]
}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 