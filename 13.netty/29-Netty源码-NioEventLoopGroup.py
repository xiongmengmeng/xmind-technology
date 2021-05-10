import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="netty"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("NioEventLoopGroup")
r2=s2.getRootTopic()
r2.setTitle("NioEventLoopGroup")


content={
'MultithreadEventExecutorGroup':[
    {'属性':[
        {'EventExecutorChooserFactory.EventExecutorChooser chooser':[
            'NioEventLoop选择器'
        ]},
        {'EventExecutor[] children':[
            '存放创建的NioEventLoop'
        ]}
    ]},
    {'MultithreadEventExecutorGroup(int nThreads, Executor executor, Object... args)':[
        'this(nThreads, executor, DefaultEventExecutorChooserFactory.INSTANCE, args)->',
        {'详细':[
            {'1.创建指定线程数的执行器数组':[
                'children = new EventExecutor[nThreads]'
            ]},
            {'2.创建new NioEventLoop':[
                'children[i] = newChild(executor, args)'
            ]},
            {'3.为每一个单例线程池添加一个关闭监听器':[
                'e.terminationFuture().addListener(terminationListener)'
            ]},
            {'4.将所有的单例线程池添加到一个HashSet中':[
                'Collections.addAll(childrenSet, children)'
            ]}
        ]}
    ]},
    {'next()':[
        'chooser.next()'
    ]}
],
'MultithreadEventLoopGroup':[
    {'MultithreadEventLoopGroup(int nThreads, Executor executor, Object... args)':[
        'super(nThreads == 0 ? DEFAULT_EVENT_LOOP_THREADS : nThreads, executor, args);',
        {'DEFAULT_EVENT_LOOP_THREADS':[
            '默认线程数:CPU核数的2倍',
            'Runtime.getRuntime().availableProcessors()*2'
        ]}
    ]},
    {'next()':[
        '(EventLoop) super.next()'
    ]},
    {'register(Channel channel)':[
        'next().register(channel)'
    ]}
],
'NioEventLoopGroup':[
    {'属性':[
        {'EventExecutor[] children':[
            '继承自父类MultithreadEventExecutorGroup'
        ]}
    ]},
    {'构造器':[
        {'NioEventLoopGroup()':[
            'this(0)->',
            'this(nThreads, (Executor) null)->',
            'this(nThreads, executor, SelectorProvider.provider())->',
            'this(nThreads, executor, selectorProvider, DefaultSelectStrategyFactory.INSTANCE)->',
            'super(nThreads, executor, selectorProvider, selectStrategyFactory, RejectedExecutionHandlers.reject());'
        ]},
        {'NioEventLoopGroup(int nThreads)':[
            'this(nThreads, (Executor) null)'
        ]}
    ]},
    {'newChild(Executor executor, Object... args)':[
        'new NioEventLoop(...)->',
        {'详细':[
            {'1.初始化任务队列(默16)':[
                'Queue<Runnable> tailTasks = newTaskQueue(maxPendingTasks)->',
                'new LinkedBlockingQueue<Runnable>(maxPendingTasks)'
            ]},
            {'2.初始化选择器，类型为WindowsSelectorImpl':[
                'selector = openSelector()'
            ]}
        ]}
    ]}
],






}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 