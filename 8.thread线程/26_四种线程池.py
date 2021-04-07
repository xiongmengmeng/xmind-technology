import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="thread"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("ThreadPoolExecutor2")
r2=s2.getRootTopic()
r2.setTitle("四种线程池")


content={
'四种线程池':[
    {'FixedThreadExecutor':[
        '固定数量线程池,比较常用',
        '核心线程和最大线程个数都为nThreads',
        '阻塞队列LinkedBlockingQueue长度为Integer.MAX_VALUE',
        'keeyAliveTime=0：线程个数比核心线程个数多并且当前空闲则回收'
    ]},
    {'CachedThreadExecutor':[
        '缓存线程池,比较常用',
        '按需创建线程的线程池，初始线程个数为0，最多线程个数为Integer.MAX_VALUE',
        '阻塞队列为同步队列,最多只有一个任务,加入同步队列的任务会被马上执行',
        'keeyAliveTime=60=:当前线程在60s内空闲则回收'
    ]},
    {'SingleThreadExecutor':[
        '固定数量线程池,比较常用',
        '核心线程和最大线程个数都为1',
        '阻塞队列长度为Integer.MAX_VALUE',
        'keeyAliveTime=0：线程个数比核心线程个数多并且当前空闲则回'
    ]}, 
    {'ScheduledThreadExecutor':[
        '定时调度线程池,一般很少使用'
    ]},
    'ThreadPoolExecutor:自定义线程池'
],
'ScheduledThreadPoolExecutor':[
    '可指定一定延迟时间后或定时进行任务调度执行的线程池',
    {'类图':[
        'DelayedWorkQueue:一个延迟的线程池队列，其和DelayedQueue类似',
        'period:任务的类型，0：一次性，负数：fixed-delay任务，正数：fixed-rate任务',
        'ScheduledFutureTask:继承自FutureTask,具有返回值的任务',
        {'ScheduledFutureTask':[
            'state:用来表示任务的状态，一开始状态为NEW',
            'callable'
        ]}
    ]},
    {'period=0':[
        'schedule(Runnable command,long delay,TimeUnit unit)',
        '提交一个延迟执行的任务',
        '任务从提交时间算起延迟单位为unit的delay时间后开始执行',
        '任务只会执行一次',
    ]},
    {'period 负数':[
        'scheduleWithFixedDelay(Runnable command,long initialDelay,long delay,TimeUnitunit)',
        '当任务执行完毕后，让其延迟固定时间后再次运行（fixed-delay任务）',
        'initialDelay:提交任务后延迟多少时间开始执行任务command',
        'delay:当任务执行完毕后延长多少时间后再次运行command任务',
        'unit:initialDelay和delay的时间单位',
        {'过程':[
            '当添加一个任务到延迟队列后，等待initialDelay时间，任务过期从队列移除，并执行',
            '执行完毕，重新设置任务的延迟时间，再把任务放入延迟队列，循环往复'
        ]}
    ]},
    {'period 正数':[
        'scheduleAtFixedRate(Runnable command,long initialDelay,long period,TimeUnitunit)',
        '同上',
        '时间为initdelday+n*period时启动任务',
        '如当前任务没执行完，下一次任务时间到了，不会并发执行，而要等到当前任务执行完毕后再执行'
    ]}
]

}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 