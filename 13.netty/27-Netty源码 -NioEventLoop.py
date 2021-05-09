import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="netty"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("NioEventLoop")
r2=s2.getRootTopic()
r2.setTitle("NioEventLoop")


content={
'ScheduledExecutorService':[
    '一个定时任务接口'
],
'EventExecutor接囗':[
    'next()',
    'boolean inEventLoop()',
    'boolean inEventLoop(Thread thread)'
],
'AbstractEventExecutor':[
    {'next()':[
        'return this;'
    ]},
    {'inEventLoop()':[
        'return inEventLoop(Thread.currentThread())'
    ]}
],
'SingleThreadEventExecutor':[
    '一个单个线程的线程池',
    {'属性':[
        {'Queue<Runnable> taskQueue':[
            '任务队列'
        ]},
        {'Thread thread':[
            ''
        ]}
    ]},
    {'方法':[
        {'inEventLoop(Thread thread)':[
            'return thread == this.thread'
        ]},
        {'execute(Runnable task)':[
            '将任务加到任务队列',
            {'判断该 EventLoop 的线程是否是当前线程':[
                {'是':[
                    '将任务添加到队列中去',
                    {'addTask(task)':[
                        'taskQueue.offer(task)'
                    ]}
                ]},
                {'不是':[
                    '尝试启动线程,随后再将任务添加到队列中去',
                    {'startThread()':[
                        'state状态判断是否启动过了，保证 EventLoop 只有一个线程',
                        '如没启动过，尝试使cas更新state为ST_STARTED(已启动),然后调用doStartThread方法'
                    ]},
                    'addTask(task)'
                ]}
            ]}

        ]},
        {'doStartThread()':[
            'executor.execute(()->SingleThreadEventExecutor.this.run())',
            {'ThreadPerTaskExecutor':[
                '继承Executor类，重写execute(Runnable command)方法',
                {'execute(Runnable command)':[
                    'threadFactory.newThread(command).start()'
                ]}
            ]}
        ]}
        {'runAllTasks(long timeoutNanos)':[
            '无限循环执行任务',
            {'safeExecute(Runnable task)':[
                'task.run();'
            ]}
        ]}
    ]}
],
'SingleThreadEventLoop':[
    {'register(io.netty.channel.Channel)':[
        'register(new DefaultChannelPromise(channel, this))'
    ]},
    {'register(final ChannelPromise promise)':[
        'promise.channel().unsafe().register(this, promise)'
    ]}
],
'NioEventLoop':[
    {'属性':[
        {'Selector selector;':[
            '选择器'
        ]},
        {'SelectedSelectionKeySet selectedKeys':[
            'SelectionKey[] keys',
            'int size;'
        ]}
    ]},
    {'run()':[
        {'select(boolean oldWakenUp)':[
            '有条件的等待 Nio 事件',
            '默认阻塞一秒,如有定时任务,在定时任务剩余时间的基础上在加0.5秒进行阻塞',
            '当执行execute()方法时,即添加任务时，唤醒selecor，防止selecot阻塞时间过长',
        ]},
        {'processSelectedKeys()':[
            '处理Nio事件',
            {'processSelectedKeysOptimized();':[
                'Object a = k.attachment()',
                {'a是否是AbstractNioChannel类型':[
                    '是，执行processSelectedKey(k, (AbstractNioChannel) a)',
                    '否，执行processSelectedKey(k, task)'
                ]}
            ]},
            {'processSelectedKey(SelectionKey k, AbstractNioChannel ch)':[
                {'readyOps=16':[
                    '连接事件',
                    'AbstractNioMessageChannel.NioMessageUnsafe#read'
                ]},
            ]}
        ]},
        {'runAllTasks()':[
            '处理队列中的任务'
        ]}
    ]}
]
}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 