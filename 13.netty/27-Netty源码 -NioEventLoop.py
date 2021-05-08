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
'SingleThreadEventExecutor':[

],
'SingleThreadEventExecutor':[
    {'属性':[
        {'Queue<Runnable> taskQueue':[
            '任务队列'
        ]},
        {'Thread thread':[
            ''
        ]}
    ]},
    {'方法':[
        {'execute(Runnable task)':[
            '将任务加到任务队列',
            {'addTask(task);':[
                'taskQueue.offer(task)'
            ]}
        ]},
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
        {'select()':[
            '有条件的等待 Nio 事件'
        ]},
        {'processSelectedKeys()':[
            '处理 Nio 事件',
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
            '处理消息队列中的任务,父类方法'
        ]}
    ]}
]
}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 