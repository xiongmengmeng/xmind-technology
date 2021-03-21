import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="netty"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("并发基础中的Future异步回调模式")
r2=s2.getRootTopic()
r2.setTitle("并发基础中的Future异步回调模式")


content={
'并发基础中的Future异步回调模式':[],
'join异步阻塞':[
    '应用场景：A线程调用B线程的join方法，等待B线程执行完成；在B线程没有完成前，A线程阻塞',
    '注意：join调用时，不是线程所指向的目标线程阻塞，而是当前线程阻塞，被合并的线程没有返回值'
],
'FutureTask异步阻塞':[
    {'Callable接口':[
        '类似Runnable接口,更强大，有返回值'
    ]},
    {'Future接口':[
        {'定义':[
            '对并发任务的执行及获取其结果的一些操作'
        ]},
        {'3大功能':[
            '判断并发任务是否执行完成。',
            '获取并发的任务完成后的结果。',
            '取消并发执行中的任务'
        ]}
    ]},
    {'FutureTask类':[
        '实现了Future接口，提供了外部操作异步任务的能力',
        '内部封装一个Callable实例',
        '自身作为Thread线程的target',
        '一座搭在Callable实例与Thread线程实例之间的桥' 
    ]}
],
'Guava的异步回调':[
    {'增强':[
        '1.引入接口ListenableFuture，继承了Java的Future接口，使得Java的Future异步任务在Guava中能被监控和获得非阻塞异步执行的结果',
        '2.引入接口FutureCallback，这是一个独立的新接口,目的是在异步任务执行完成后，根据异步结果，完成不同的回调处理，并且可以处理异步结果'
    ]},
    {'FutureCallback':[
        {'作用':[
            '用来填写异步任务执行完后的监听逻辑'
        ]},
        {'两个回调方法':[
            'onSuccess方法，在异步任务执行成功后被回调',
            'onFailure方法，在异步任务执行过程中，抛出异常时被回调'
        ]}
    ]},
    {'ListenableFuture':[
        'ListenableFuture异步任务实例获取：向Guava自己定制的线程池（ThreadPool）提交Callable任务的方式',
        {'Guava异步回调的流程':[
            '1.实现Java的Callable接口，创建异步执行逻辑',
            '2.创建Guava线程池(它是对Java线程池的一种装饰）',
            '3.将第1步创建的Callable/Runnable异步执行逻辑的实例，通过submit提交到Guava线程池，从而获取ListenableFuture异步任务实例',
            '4.创建FutureCallback回调实例，通过Futures.addCallback将回调实例绑定到ListenableFuture异步任务上'
        ]}
    ]},
    {'Futures工具类':[
        'addCallback静态方法:将FutureCallback的回调实例绑定到ListenableFuture异步任务'
    ]},
    {'与Java的FutureTask异步回调对比':[
        'Guava是非阻塞的异步回调，调用线程是不阻塞的，可以继续执行自己的业务逻辑',
        'FutureTask是阻塞的异步回调，调用线程是阻塞的，在获取异步结果的过程中，一直阻塞，等待异步线程返回结果'
    ]}
],
'Netty的异步回调模式':[
    {'增强':[
        'Netty的Future接口,对Java的Future接口进行了增强',
        'GenericFutureListener接口，用于表示异步执行完成的监听器'
    ]},
    {'GenericFutureListener接口':[
        '回调方法：operationComplete,异步任务操作完成,Future异步任务执行完成后，将回调此方法'
    ]},
    {'Netty的Future接口':[
        'addListener():增加异步任务执行完成与否的监听器listener',
        '对执行的过程的进行监控，对异步回调完成事件进行监听（Listen）',
        'ChannelFuture的使用'
    ]}
]
}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 