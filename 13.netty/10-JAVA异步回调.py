import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="netty"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("java异步回调")
r2=s2.getRootTopic()
r2.setTitle("java异步回调")


content={
# '并发基础中的Future异步回调模式':[],
# 'join异步阻塞':[
#     '应用场景：A线程调用B线程的join方法，等待B线程执行完成；在B线程没有完成前，A线程阻塞',
#     '注意：join调用时，不是线程所指向的目标线程阻塞，而是当前线程阻塞，被合并的线程没有返回值'
# ],
'Runnable接囗':[
    '无返回值',
    {'方法':[
        'void run()'
    ]}
],
'Callable接口':[
    '类似Runnable接口,有返回值',
    {'方法':[
        'V call() throws Exception'
    ]}
],
'FutureTask类':[
    {'背景':[
        'Thread类构造器：Thread(Runnable target)，只接受Runnable做为参数',
        'Runnable接口实例可以作为Thread线程实例的target构造参数，开启一个Thread线程',
        {'解决Callable实例不能做为参数的问题':[
            '搭在Callable实例与Thread线程实例之间的桥->FutureTask'
        ]}
    ]},
    '实现了Future接口,Runnable接囗',
    {'参数':[
        'Callable<V> callable：内部封装一个Callable实例',
        'Object outcome:保存结果'
    ]},
    {'构造方法':[
        'FutureTask(Callable<V> callable)'
    ]},
    {'run()方法':[
        'callable.call()'
    ]},
    {'get()方法':[
        '返回outcome'
    ]},
    {'作用':[
        'FutureTask类能当作Thread线程去执行目标target，被异步执行',
        '如要获取异步执行的结果，需通过FutureTask类的方法去获取，类内部，会将Callable的call方法的真正结果保存起来，以供外部获取',
    ]},
],
'Future接口':[
    {'定义':[
        '对并发任务的执行及获取其结果的一些操作'
    ]},
    {'4个方法':[
        {'boolean cancel(boolean mayInterruptIfRunning)':[
            '取消并发执行中的任务'
        ]},
        {'boolean isCancelled()':[
            '判断任务是否取消'
        ]},
        {'boolean isDone()':[
            '判断并发任务是否执行完成'
        ]},
        {'V get()':[
            '方法是阻塞性的',
            '获取并发的任务完成后的结果'
        ]}
    ]}
]
}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 