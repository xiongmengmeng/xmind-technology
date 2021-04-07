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
    '等待线程对象销毁，使线程排队运行作用，类似同步的运行效果',
    '使所属的线程对象x正常执行run()中任务，使当前线程z进行无限期阻塞，等待线程x销毁后再继续执行线程z后面代码',
    'join(long)：参数是设定等待的时间',
    {'原理':[
        'while (isAlive()) {',
        '   wait(0);',
        '}',
        'join(),一个synchronized方法，内部调用wait()，目的是让持有这个对象锁(线程x)的线程z进入等待',
        '子线程x执行完毕后，JVM会调用lock.notify_all()',
        '唤醒持有对象锁(线程x)的线程，也就是主线程，继续执行'
    ]},
    {'与synchronized区别':[
        'join在内部使用wait()方法进行等待，synchronized使用对象监视器'
    ]},
    '陷阱:同步代码块中，join()，设备时间的情况下，后面的代码提前运行',
],
'LockSupport':[
    '作用:挂起和唤醒线程，是创建锁和其他同步类的基础',
    'LockSupport类与每个使用它的线程都会关联一个许可证',
    '默认情况下调用LockSupport类方法的线程不持有许可证',
    {'方法':[
        'park()：如调用线程已经拿到与LockSupport关联的许可证，直接返回，否则调用线程被挂起',
        'unpark(Thread thread)：thread线程持有与LockSupport类关联的许可证',
        {'park(Object blocker)':[
            'Thread类里有变量volatile Object parkBlocker',
            '存放park方法传递的blocker对象'
        ]}
    ]}
]


}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 