import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="netty"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("Guava异步回调")
r2=s2.getRootTopic()
r2.setTitle("Guava异步回调")


content={
# '并发基础中的Future异步回调模式':[],
# 'join异步阻塞':[
#     '应用场景：A线程调用B线程的join方法，等待B线程执行完成；在B线程没有完成前，A线程阻塞',
#     '注意：join调用时，不是线程所指向的目标线程阻塞，而是当前线程阻塞，被合并的线程没有返回值'
# ],
'Guava异步回调':[
    {'增强':[
        {'1.引入ListenableFuture接口':[
            '继承了Java的Future接口',
            '使得Java的Future异步任务在Guava中能被监控和获得非阻塞异步执行的结果',
            {'方法':[
                'addListener(Runnable listener, Executor executor)',
                '将FutureCallback善后回调工作，封装成一个内部的Runnable异步回调任务->',
                '在Callable异步任务完成后，回调FutureCallback进行善后处理'
            ]},
            {'ListenableFuture异步任务实例获取':[
                '向Guava自己定制的线程池（ThreadPool）提交Callable任务的方式'
            ]}
        ]},
        {'2.引入FutureCallback接口':[
            '一个独立的新接口',
            '目的:在异步任务执行完成后，根据异步结果，完成不同的回调处理，并且可以处理异步结果',
            {'作用':[
                '用来填写异步任务执行完后的监听逻辑'
            ]},
            {'两个回调方法':[
                {'onSuccess(@Nullable V result)':[
                    '在异步任务执行成功后被回调'
                ]},
                {'onFailure(Throwable t)':[
                    '在异步任务执行过程中，抛出异常时被回调'
                ]}
            ]}
        ]}
    ]},
    {'Futures工具类':[
        {'addCallback静态方法':[
            '将FutureCallback的回调实例绑定到ListenableFuture异步任务',
        ]}
    ]},
    {'Guava异步回调流程':[
        {'1.实现Java的Callable接口，创建异步执行逻辑':[
            'XXXJob implement Callable ...',
            'XXXJob job =new XXXJob()'
        ]},
        {'2.创建Guava线程池(它是对Java线程池的一种装饰）':[
            'ExecutorServicejPool=  Executors.newFixedThreadPool(10)',
            'ListeningExecutorServicegPool=  MoreExecutors.listeningDecorator(jPool)'
        ]},
        {'3.将第1步创建的Callable实例，通过submit提交到Guava线程池，从而获取ListenableFuture异步任务实例':[
            'ListenableFuture<Boolean>hFuture = gPool.submit(job);',
        ]},
        {'4.创建FutureCallback回调实例，通过Futures.addCallback将其绑定到ListenableFuture':[
            'Futures.addCallback(listenableFuture,newFutureCallback<Boolean>(){',
            '   //实现回调方法，有两个});',
            '}'
        ]}
    ]},
    {'与Java的FutureTask异步回调对比':[
        'Guava是非阻塞的异步回调，调用线程是不阻塞的(可判断是否执行完)，可以继续执行自己的业务逻辑',
        'FutureTask是阻塞的异步回调，调用线程是阻塞的，在获取异步结果的过程中，一直阻塞，等待异步线程返回结果'
    ]}
],
'Netty异步回调':[
    {'增强':[
        {'Netty的Future接口':[
            '对Java的Future接口进行了增强',
            '对应到Guava的ListenableFuture接口',
            {'addListener(GenericFutureListener listener)':[
                '增加异步任务执行完成与否的监听器listener',
                '对执行的过程的进行监控，对异步回调完成事件进行监听（Listen）'
            ]},
            '一般使用其子接口，有一系列，代表不同类型的异步任务，如ChannelFuture接口'
        ]},
        {'GenericFutureListener接口':[
            '表示异步执行完成的监听器',
            '对应到Guava的FutureCallback接口(回调改监听)',
            {'operationComplete()':[
                '民步任务操作完成,Future异步任务执行完成后，将回调此方法'
            ]}
        ]}
    ]},
    {'Future-Listener机制':[
        '当Futrue对象刚创建时，处于非完成状态，调用者可通过返回的ChannelFuture来获取操作执行的状态，注册监听函数来执行完成后的操作'
    ]}
]
}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 