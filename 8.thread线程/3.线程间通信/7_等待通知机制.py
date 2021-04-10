import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="thread"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("等待/通知机制")
r2=s2.getRootTopic()
r2.setTitle("等待/通知机制")


content={
'wait()':[
    'Object类的方法',
    {'方法调用前':[
        '线程须获得该对象的对象级别锁，即在同步方法或块中调用方法',
        '调用方法未持有锁，抛IllegalMonitorStateException(RuntimeException的子类，不需try-catch捕捉异常)',
    ]},
    {'方法调用后':[
        '当前线程释放锁,从运行状态退出，进入等待队列，直到被再次唤醒',
        '线程与其他线程竞争重新获得锁',
    ]},
    'wait(long):long时间内如未未被唤醒，超过long时间自动唤醒',
    {'每个锁对象都有两个队列':[
        {'就绪队列':[
            '存储将要获得锁的线程，如线程被唤醒后进入，等待CPU的调度'
        ]},
        {'阻塞队列':[
            '存储被阻塞的线程,如线程被wait后进入，等待下一次被唤醒'
        ]}
    ]},
    {'对象锁的本质':[
        '重量级锁模式时对象头是一个指向互斥量的指针(一个监视器锁（ObjectMonitor）的数据结构)',
        '此时对象的hashCode、分代年龄等信息都会保存到对应的ObjectMonitor中',
        {'ObjectMonitor属性':[
            'TheOwner:记录拥有本锁的线程对象'
            'EntrySet：处于等待锁block状态的线程',
            'WaitSet：处于wait状态的线程',
            'recursion:记录本锁被重入的次数',
            
        ]},
        '几个线程一起竞争对象的锁，成功的线程记录在The Owner，失败的记录在EntrySet队列',
    ]}
],
'notify()':[
    {'调用前':[
        '线程须获得该对象的对象级别锁,如无，抛异常'
    ]},
    {'调用后':[
        {'不会马上释放锁':[
            '等线程将程序执行完，即退出synchronized代码块后，线程才会释放锁'
        ]},
        {'通知等待该对象锁的其他线程':[
            '如有多个线程等待,由线程规划器随机挑选一个对其发出通知，使它获取对象锁',
            '注：获得锁的wait线程执行完，释放锁，但其它wait状态的线程由于没有得到通知也无法执行',
            '可多次调用notify()唤醒了全部WAITING中的线程' 
        ]}
    ]}, 
],
'notifyAll()':[
    '可使所有正在等待队列中等待同一共享资源的“全部”线程从等待状态退出，进入可运行状态'
],
'wait/notify运行流程':[
    '有一个对象o，锁被线程t1持有，调用wait()后，线程t1将会被放到Wait Set结构中',
    '-->另一个线程t2获取到锁，The Owner记录变成t2线程',
    '-->t2不需要o锁时，调用o.notify()',
    '-->对象o告诉Wait Set中线程:你们可以来竞争我啦，我的锁现在没被人持有',
],
'总结':[
    'wait使线程停止运行，notify使停止的线程继续运行',
    '方法：wait()锁释放与notify()锁不释放'
],



}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 