import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="thread"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("synchronized原理")
r2=s2.getRootTopic()
r2.setTitle("synchronized原理")


content={
'基础':[
    {'Mark Word':[
        'java对象组成：普通和数组',
        '它们都包括Mark Word对象头'
    ]},
    {'Monitor':[
        '是操作系统的对象；Mark Word是java的对象',
        'Monitor 被翻译为监视器或管程',
        '每个Java对象都可以关联一个操作系统Monitor对象',
        'synchronized给对象上锁（重量级）后，对象头的Mark Word指向操作系统Monitor对象',
        {'结构':[
            'owner:monitor的所有者，只有一个',
            'entrylist:处于blocked状态的线程',
            'waitset:获得过锁，但条件不满足进入waiting状态的线程'
        ]},
        'blocked线程在owner线程释放时唤醒',
        'waiting线程在owner线程调用notify()时,进入entrylist'
    ]}
],
'原理':[
    {'synchronized（this）':[
        '通过javap生成的字节码中包含monitorenter和monitorexit两个指令',
        '进入锁时执行monitorenter指令：将lock对象markword置为monitor指针',
        '退出锁时执行monitorexit指令：将lock对象markword重置，唤醒entrylist'
    ]},
    {'synchronized 方法':[
        '相对普通方法，常量池中多了ACC_SYNCHRONIZED标示符,JVM根据标示符来实现方法同步',
        '方法调用时，调用指令检查方法的ACC_SYNCHRONIZED访问标志是否被设置',
        '如设置了，执行线程先获取monitor，获取成功后执行方法体，方法执行完后释放monitor',
        '在方法执行期间，其他任何线程都无法再获得同一个monitor对象',
        '本质与synchronized（this）没有区别，只是用一种隐式的方式来实现，无需通过字节码'
    ]},
    '关键字取得的锁都是"对象锁"，不是把一段代码或方法当作锁',
],
'锁的内容':[
    {'锁对象':[
        'synchronized 方法',
        'synchronized（this）代码块',
        {'详细':[
            '1.A线程先持有对象锁，B线程可异步调用对象中的非synchronized方法',
            '2.A线程先持有对象锁，B线程调用对象中synchronized类型方法需等待'
        ]}
    ]},
    {'锁非this对象':[
        '不阻塞类中synchronized方法,synchronized（this）代码块,锁的对象不一样'
    ]},
    {'锁类':[
        'synchronized static方法'
        'synchronized（class）代码块',
        'Class锁对类的所有对象实例起作用'
    ]},
    {'锁字符串':[
        '注意常量池带来的一些例外'
    ]}
],
'应用':[
    '共享资源的读写访问需同步，不是共享资源没有同步必要',
    '多个线程访问同一个对象需同步',
    '多个线程访问多个对象，JVM会创建多个锁，无需同步'
],

}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 