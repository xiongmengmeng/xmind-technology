import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="thread"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("synchronized特性")
r2=s2.getRootTopic()
r2.setTitle("synchronized特性")


content={
'应用':[
    '共享资源的读写访问需同步，不是共享资源没有同步必要',
    '多个线程访问同一个对象需同步',
    '多个线程访问多个对象，JVM会创建多个锁，无需同步'
],
'特性':[
    {'可重入':[
        '自己可以再次获取自己的锁',
        '支持子类继承',
        '一个synchronized方法/块的内可以调用本类的其他synchronized方法'
    ]},
    '可见性：线程加锁时必须从主内存中获得最新的值，解锁时必须把变量的值刷新到内存中去',
    '异常锁自动释放',
    '不具有继承性:因为子类重写了方法'
],
'死锁':[
    '经典的多线程问题',
    '不同的线程等待不可能被释放的锁，导致线程假死(waiting)'
],
'偏向锁':[
    '目标:在只有一个线程执行同步代码块时提高性能',
    {'过程':[
        '一个线程访问同步代码块:cas操作，用threadId替换mark word',
        '再次访问同步代码快：检查threadID是否是自己(无cas)'
    ]},
    {'锁升级条件':[
        '其他线程尝试竞争偏向锁时',
        '持有偏向锁的线程才会释放锁，线程不会主动释放偏向锁'
    ]}
],
'轻量级锁':[
    '锁是偏向锁时，被另一个线程所访问，偏向锁会升级为轻量级锁,另一线程自旋',
    {'过程':[
        {'加锁':[
            '1.代码进入同步块，如同步对象锁为无锁状态01',
            '2.虚拟机在当前线程的栈帧中建立名为锁记录（Lock Record）的空间',
            '3.让锁记录中Object reference指向锁对象',
            '尝试用cas替换Object的Mark Word,将Mark Word的值存入琐记录',
            '4.cas成功，对象头中存储了锁记录地址和状态00(对象处于轻量级锁定)',
            '5.cas失败，如是自己执行了锁重入，添加一条Lock Record作为重入计数',
            '如其它线程已持有了该Object的轻量级锁，表明有竞争，进入锁膨胀过程',
        ]},
        {'解锁':[
            '1.取值null的锁记录，表示有重入，重置锁记录，表示重入计数减一',
            '2.值不为null，使用cas将Mark Word值恢复给对象头',
            '成功->解锁成功',
            '失败->轻量级锁进行了锁膨胀或已经升级为重量级锁，进入重量级锁解锁流'
        ]}
    ]},
    {'锁膨胀':[
        '1.当Thread-1进行轻量级加锁时，Thread-0 已经对该对象加了轻量级锁',
        '2.Thread-1加轻量级锁失败，进入锁膨胀流程',
        '为Object对象申请Monitor锁',
        '让Object指向重量级锁地址然后自己进入Monitor的EntryList BLOCKED',
        '3.当Thread-0退出同步块解锁时，使用cas将Mark Word的值恢复给对象头，失败',
        '->进入重量级解锁流程，即按照Monitor地址找到Monitor对象',
        '->设置Owner为null，唤醒EntryList中BLOCKED线程'
    ]},
    {'自旋':[
        '好处:减少线程上下文切换的消耗',
        '缺点:循环会消耗CPU'
    ]}
],
'重量级锁':[
    '当锁为轻量级锁时，另一个线程自旋，但不会一直自旋->',
    '自旋一定次数还没有获取到锁，进入阻塞->',
    '该锁膨胀为重量级锁,锁标志的状态值变为10',
    'Mark Word中存储的是指向重量级锁的指针，等待锁的线程都会进入阻塞状态,性能降低'
],
'综上':[
    '通过对象监视器在对象头中的字段来表明的',
    '无锁->偏向锁->轻量级锁->重量级锁,锁状态只能升级不能降级,提高获取锁和释放锁的效率',
    {'总结':[
        '偏向锁通过对比Mark Word解决加锁问题，避免执行CAS操作',
        '轻量级锁是通过用CAS操作和自旋来解决加锁问题，避免线程阻塞和唤醒而影响性能',
        '重量级锁是将除了拥有锁的线程以外的线程都阻塞'
    ]}
],

}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 