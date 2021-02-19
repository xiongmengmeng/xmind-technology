import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="thread"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("实践")
r2=s2.getRootTopic()
r2.setTitle("实践")


content={
'ArrayBlockingQueue':[
    'logback中异步日志模型:多生产者-单消费者模型,使用ArrayBlockingQueue实现',
    {'原理':[
        '使用队列把同步日志打印转换为了异步',
        '业务线程: 调用异步appender将日志任务放入队列',
        '日志线程：使用同步appender进行具体日志打印'
    ]},
    'AsyncAppender:实现异步日志的关键',
    {'AsyncAppender':[
        '继承AsyncAppenderBase',
        'ArrayBlockingQueue:有界阻塞队列',
        'queueSize:有界队列元素个数，默认256个',
        'worker:线程，消费者线程',
        'aai:一个appender的装饰器，里面存放同步日志的appender',
        'appenderCount:记录aai里附加的同步appender个数',
        'neverBlock:当队列满时是否阻塞业务线程',
        'discardingThreshold:日志队列空闲元素小于该值，新的某些级别的日志会被丢弃'
    ]},
    {'start()':[
        '1.使用有界队列ArrayBlockingQueue',
        '2.设置discardingThreshold为队列的1/5'
        '3.消费日志队列的worker线程设置为守护线程，设置线程名称',
        '4.启动线程'
    ]},
    {'append()':[
        '1.日志级别<=INFO_INT&&队列剩余容量<discardingThreshold,丢弃日志任务',
        '2.neverBlock为false(默认):是调用阻塞队列put方法,否则调用不阻塞的offer方法'
    ]},
    {'worker的run()':[
        '1.take方法从队列获取一个日志任务，如队列为空线程被阻塞直到队列不为空返回',
        '2.调用AppenderAttachableImpl的aai.appendLoopOnAppenders方法：',
        '循环调用通过addAppender注入的同步日志，appener具体实现把日志打印到磁盘'
    ]},
    {'注意':[
        'ArrayBlockingQueue需合理队列大小免造成OOM',
        '队列将满或满时，根据具体场景制定抛弃策略以免队满时业务线程被阻塞'
    ]}
],
'ConcurrentHashMap':[
    {'put(K key, V value)':[
        '如key已存在，使用value覆盖原值并返回原值',
        '如不存在把value放入返回null'
    ]},
    {'putIfAbsent(K key, V value)':[
        '如key已存在直接返回原值,不使用value覆盖',
        '如key不存在放入value并返回null',
        '注意，判断key是否存在和放入是原子性操作'
    ]}
],
'ScheduledThreadPoolExecutor':[
    'Timer:多线程生产单线程消费,出异常直接清空队列',
    'ScheduledThreadPoolExecutor:可配置',
    '使用定时器功能时优先使用ScheduledThreadPoolExecutor'
],

'ConcurrentLinkedQueue':[
    'Tomcat中NioEndPoint的实现,多生产者-单消费者模型,使用ConcurrentLinkedQueue实现',
    {'NioEndpoint':[
        {'Acceptor':[
            '套接字接受线程(Socket acceptor thread)',
            '接受用户请求并把请求封装为事件任务放入Poller队列',
            '一个Connector里面只有一个Acceptor'
        ]},
        {'Poller':[
            '套接字处理线程(Socket poller thread)，Poller内部有一个队列',
            'Poller线程从自己的队列里获取具体的事件任务，将其交给Worker进行处理',
            'Poller线程的个数与处理器的核数有关'
        ]},
        {'Worker':[
            '实际处理请求的线程',
            'Worker是组件名字',
            '真正任务执行者是SocketProcessor'
        ]}
    ]},
    '使用ConcurrentLinkedQueue队列把接受请求与处理请求操作进行解耦，实现异步处理',
    {'生产者——Acceptor线程':[
        '接受客户端发来的连接请求并将其放入Poller的事件队列:',
        '1.无限循环等待客户端连接',
        '2.控制客户端请求连接数量，如果连接数量达到设置阈值，当前请求会被挂起',
        '3.从TCP缓存获取一个完成三次握手的套接字，如当前没有，线程会被阻塞挂起',
        '4.获取到一个连接套接字后,封装为事件任务，放入poller队列'
    ]},
    {'消费者——Poller线程':[
        '从事件队列里面获取事件并进行处理',
        '1.从事件队列获取事件',
        '2.遍历感兴趣的channel并对感兴趣的事件进行处理'
    ]},
    {'注意':[
        'ConcurrentLinkedQueue是无界队列,需合理队列大小免造成OOM'
    ]}
],

'深浅引用':[
    '引用类型作为集合A元素',
    '如使用集合A作为集合B的构造函数参数',
    '两集合里同一个位置的元素指向的是同一个引用',
    '对引用的修改在两个集合中都可见，此时需对引用元素进行深复制'
],
'FutureTask':[
    '线程池中使用FutureTask，当拒绝策略为DiscardPolicy和DiscardOldestPolicy时',
    '被拒绝任务的FutureTask对象上调get()方法会导致调用线程一直阻塞',
    {'原因':[
        'Future有状态',
        'Future状态>COMPLETING，get()方法返回',
        'future初始值new,上述拒绝策略没有重置future的值'
    ]},
    '建议：尽量使用带超时参数的get方法',
],
'并发编程注意事项':[
    '创建线程和线程池时指定与业务相关的名称',
    '使用线程池后要调用shutdown方法关闭，否则会导致线程池线程资源一直不释放'
],





}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 