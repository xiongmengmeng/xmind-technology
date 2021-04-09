import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="thread"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("线程间通信")
r2=s2.getRootTopic()
r2.setTitle("线程间通信")


content={
'join()':[
    'Thread类的方法',
    {'作用':[
        '将两个交替执行的线程合并为顺序执行的线程',
        '如在主线程A中调用了线程B的Join()方法，直到线程B执行完毕后，才会继续执行主线程A',
    ]},
    {'解释':[
        '当主线程A调用B.join时候，主线程A会获得线程对象B的锁，然后进入其wait等待队列',
        '直到线程B执行完方法，JVM会调用lock.notify_all()',
        '唤醒持有线程B对象锁的线程A，线程继续执行',
        {'注意':[
            '线程A调用B.join时，必须能够拿到线程B对象的锁'
        ]}
    ]},
    {'原理':[
        'join(),一个synchronized方法，内部调用wait()',
        {'内部':[
            'while (isAlive()) {',
            '   wait(0);',
            '}',
        ]}
    ]},
    {'与synchronized区别':[
        'join在内部使用wait()方法进行等待，synchronized使用对象监视器'
    ]},
    '陷阱:同步代码块中，join()，设置时间的情况下，后面的代码提前运行',
],
'LockSupport':[
    {'作用':[
        '挂起和唤醒线程，是创建锁和其他同步类的基础'
    ]},
    {'方法':[
        {'park()':[
            '阻塞线程',
        ]},
        {'park(Object blocker)':[
            'blocker:记录线程被阻塞时被谁阻塞的,用于线程监控和分析工具来定位原因的'
        ]},
        {'unpark(Thread thread)':[
            '启动唤醒线程'
        ]}
    ]},
    {'与wait/notify对比':[
        {'不用获取对象锁，便可锁住线程':[
            'wait和notify都是Object的方法,在调用这两个方法前必须先获得锁对象',
            'park不需要获取某个对象的锁就可以锁住线程',
        ]},
        {'可唤醒指定线程':[
            'notify只能随机选择一个线程唤醒，无法唤醒指定的线程',
            'unpark可以唤醒一个指定的线程'
        ]}
    ]}
],
'线程状态切换图':[],
'通过管道进行线程间通信':[
    '管道流',
    'PipedInputStream和PipedOutputStream',
    'PipedReader和PipedWriter'
]

}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 