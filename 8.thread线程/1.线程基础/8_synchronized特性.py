import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) 
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
'特性':[
    {'可重入':[
        '自己可以再次获取自己的锁,支持子类继承',
        '一个synchronized方法/块的内可以调用本类的其他synchronized方法'
    ]},
    '可见性：线程加锁时必须从主内存中获得最新的值，解锁时必须把变量的值刷新到内存中去',
    '异常锁自动释放',
],
'死锁':[
    '不同的线程等待不可能被释放的锁，导致线程假死(waiting)'
],
'偏向锁':[
    {'目标':[
        '消除数据在无竞争情况下的同步，提高程序运行性能'
    ]},
    {'过程':[
        {'线程第一次访问同步代码块':[
            '把对象头中的标志位变为01、偏向模式变为1',
            'CAS操作把获取到锁的线程ID记录在对象Mark Word中',
        ]},
        {'线程再次访问同步代码块':[
            '检查threadID是否是自己',
            '不再进行同步操作（如加锁、解锁，Mark Word的更新）'
        ]}
    ]},
    {'锁升级条件':[
        '另外一个线程尝试获取锁，偏向模式马上结束',
        '根据锁对象目前是否处于被锁定的状态决定是否撤销偏向,撤销后标志位恢复到未锁定01或轻量级锁定00',

    ]}
],
'轻量级锁':[
    '锁是偏向锁时，被另一个线程所访问，偏向锁会升级为轻量级锁,另一线程自旋',
    {'过程':[
        {'加锁':[
            '1.代码将进入同步块，同步对象未被锁定（锁标志位01）',
            '2.虚拟机在当前线程的栈帧中建立名为锁记录(Lock Record)的空间,存储锁对象Mark Word的拷贝',
            {'3.cas把对象的Mark Word更新为指向Lock Record的指针':[
                '成功：线程拥有对象锁，对象Mark Word的锁标志位变为00（轻量级锁定状态）,对象头中存储了锁记录地址',
                {'失败':[
                    '检查对象Mark Word是否指向当前线程的栈帧',
                    '是：自己执行了锁重入，添加一条Lock Record作为重入计数',
                    '否：锁对象被其他线程抢占，轻量级锁膨胀为重量级锁，锁标志变为10，Mark Word指向互斥锁指针'
                ]}
            ]}
        ]},
        {'解锁':[
            '对象Mark Word指向线程的锁记录',
            {'cas将对象当前的Mark Word和线程中复制的Mark Word替换回来':[
                '成功->解锁成功',
                '失败->其他线程尝试过获取锁，要在释放锁的同时，唤醒被挂起线程'
            ]},
        ]}
    ]},
    {'锁膨胀':[
        '1.当Thread-1进行轻量级加锁时，Thread-0 已经对该对象加了轻量级锁',
        {'2.Thread-1加轻量级锁失败，进入锁膨胀流程':[
            '为Object对象申请Monitor锁',
            '让Object指向重量级锁地址然后自己进入Monitor的EntryList BLOCKED'
        ]},
        {'当Thread-0退出同步块解锁时，使用cas将Mark Word的值恢复给对象头，失败':[
            '进入重量级解锁流程，即按照Monitor地址找到Monitor对象',
            '设置Owner为null，唤醒EntryList中BLOCKED线程'
        ]}
    ]},
    {'自旋':[
        '好处:减少线程上下文切换的消耗',
        '缺点:循环会消耗CPU'
    ]}
],
'重量级锁':[
    '当锁为轻量级锁时，另一个线程自旋，但不会一直自旋->自旋一定次数还没有获取到锁，进入阻塞->',
    '锁膨胀为重量级锁,锁标志的状态值变为10',
    'Mark Word中存储的是指向重量级锁的指针，等待锁的线程都会进入阻塞状态',
    '性能差：阻塞或唤醒线程，需操作系统帮忙，用户态与核心态切换耗cpu时间'

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