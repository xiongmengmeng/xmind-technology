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
r2.setTitle("线程池")


content={
'ThreadPoolExecutor':[
    {'好处':[
        '1.执行大量异步任务时提供更好的性能:线程的创建和销毁需要开销,线程池里线程可复用',
        '2.提供一种资源限制和管理的手段，如可限制线程的个数，动态新增线程等',
    ]},
    'Executors:工具类，有很多静态方法，根据用户选择返回不同的线程池实例'
],
'线程池':[
    {'状态':[
        'RUNNING：接受新任务并且处理阻塞队列里的任务',
        'STOP：中断正在处理的任务,拒绝新任务并且抛弃阻塞队列里的任务',
        'TIDYING：所有任务都执行完（包含阻塞队列的）当前线程池活动线程数为0，调用terminated方法',
        'TERMINATED：终止状态,terminated方法调用完成以后的状态'
    ]},
    {'状态转换':[
        'RUNNING -> SHUTDOWN:显式调用shutdown()方法，或隐式调用finalize()方法里的shutdown()方法',
        'RUNNING或SHUTDOWN-> STOP:显式调用shutdownNow()方法时',
        'SHUTDOWN -> TIDYING:当线程池和任务队列都为空时',
        'STOP -> TIDYING:当线程池为空时',
        'TIDYING -> TERMINATED:当terminated()hook方法执行完成时'
    ]},
    {'参数':[
        'corePoolSize：线程池核心线程个数',
        'maximunPoolSize：线程池最大线程数量',
        'workQueue：等待执行的任务的阻塞队列',

        'threadFactory：创建线程的工厂',

        'keeyAliveTime：如 当前线程数量 > corePoolSize，多出线程会在keepAliveTime后释放掉',
        'TimeUnit：keepAliveTime的时间单位',
                'RejectedExecutionHandler：饱和策略，当队列满并且线程个数达到maximunPoolSize后采取的策略',
        '如AbortPolicy（抛出异常）、CallerRunsPolicy（使用调用者所在线程来运行任务）、DiscardOldestPolicy（调用poll丢弃一个任务，执行当前任务）及DiscardPolicy（默默丢弃，不抛出异常）',
    ]},
    {'工作原理':[
        {'举例：':[
            'corePoolSize：1',
            'mamximumPoolSize：3',
            'keepAliveTime：60s',
            'workQueue：ArrayBlockingQueue，有界阻塞队列，队列大小是4',
            'handler：默认的策略，抛出来一个ThreadPoolRejectException'
        ]},
        '1.一开始有一个线程变量poolSize维护当前线程数量.poolSize=0',
        '2.来一个任务.需创建线程.poolSize(0) < corePoolSize(1),直接创建线程',
        '3.来一个任务.需创建线程.poolSize(1) >= corePoolSize(1),队列没满,丢到队列中',
        '4.如队列满了,但是poolSize < mamximumPoolSize,继续创建线程',
        '5.如poolSize == maximumPoolSize,再提交任务,就要执行handler,默认抛出异常',
        '6.如线程池有3个线程处于空闲状态,corePoolSize=1,(3-1 =2),超出的2个空闲线程,空闲超过60s,会给回收掉'

    ]},
    {'类图':[
        'ctl:Integer的原子变量，记录线程池状态和线程池中线程个数',
        'mainLock:独占锁，控制新增Worker线程操作的原子性',
        'termination:锁对应的条件队列，在线程调用awaitTermination时用来存放阻塞的线程',
        'Worker:继承AQS和Runnable接口，是具体承载任务的对象,实现了简单不可重入独占锁',
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
    ]}
],
'线程池':[
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
'线程池方法':[
    {'execute(Runnable command)':[
        '1.线程池线程个数<corePoolSize，向workers里新增一个核心线程执行该任务',
        '2.线程池线程个数>=corePoolSize',
        {'2.1判断线程池状态':[
            '2.1.1 RUNNING:添加当前任务到任务队列',
            {'二次检查线程池状态':[
                'RUNNING:判断当前线程池里是否有线程，没有则新增一个',
                '不是RUNNING:把任务从任务队列移除，移除后执行拒绝策略'
            ]},
            '2.1.2 非RUNNING:抛弃新任务'
        ]},
        {'3.尝试开启线程来执行该任务,判断线程池线程个数>maximumPoolSize':[
            '否：开启线程来执行该任务'
            '是：执行拒绝策略'
        ]}
    ]}, 
    {'addWorkder():新增线程':[
        '1.双重循环通过CAS操作增加线程数',
        '2.把并发安全的任务添加到workers里，并且启动任务执行'
    ]},
    {'shutdown()':[
        '检查权限',
        '设置当前线程池状态为STOP:如当前线程池状态>=SHUTDOWN则直接返回，否则设置为SHUTDOWN状态',
        {'设置所有空闲线程的中断标志':[
            '加了全局锁，同时只有一个线程可以调用shutdown方法设置中断标志',
            '尝试获取Worker自己的锁，获取成功则设置中断标志',
            '由于正在执行的任务已经获取了锁，所以正在执行的任务没有被中断',
            '中断的是阻塞到getTask（）方法并企图从队列里面获取任务的线程，也就是空闲线程'
        ]}
    ]},
    {'shutdownNow()':[
        '检查权限',
        '设置当前线程池状态为STOP',
        '中断所有的工作线程(包含空闲线程和正在执行任务的线程)',
        '返回值为这时候队列里面被丢弃的任务列表'
    ]},
    {'awaitTermination()':[
        '获取独占锁，然后在无限循环内判断当前线程池状态是否至少是TERMINATED状态',
        '是,直接返回',
        '否,说明线程池里还有线程在执行，看超时时间nanos是否小于0，是说明不需要等待，直接返回',
        '大于0调用条件变量termination的awaitNanos方法等待nanos时间'
    ]}
],
'工作线程Worker':[
    {'runWorker':[
        '1.task==null或者调用getTask从任务队列获取的任务返回null,跳3',
        {'2.执行任务':[
            '2.1获取工作线程内持有的独占锁',
            '2.2执行扩展接口代码',
            '2.3执行任务',
            '2.4任务执行完毕后做一些事情',
            '2.5统计当前Worker完成了多少个任务',
            '2.6释放锁'
        ]},
        {'3.执行清理任务':[
            {'统计信息':[
                '加全局锁',
                '统计线程池完成任务个数',
                '把当前工作线程中完成任务累加到全局计数器',
                '然后从工作集中删除当前Worker',
                '释放锁'
            ]},
            '尝试设置线程池状态为TERMINATED',
            '判断当前线程池里面线程个数<核心线程个数，如果是则新增一个线程',
        ]}
    ]}
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
        'schedule（Runnable command, long delay, TimeUnit unit）',
        '提交一个延迟执行的任务',
        '任务从提交时间算起延迟单位为unit的delay时间后开始执行',
        '任务只会执行一次',
    ]},
    {'period 负数':[
        'scheduleWithFixedDelay（Runnable command, long initialDelay, long delay, TimeUnitunit）',
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
        'scheduleAtFixedRate（Runnable command, long initialDelay, long period, TimeUnitunit）',
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