import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
xmind_name="jvm"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("jvm_lock")
r2=s2.getRootTopic()
r2.setTitle("锁优化")


content={


'自旋锁':[
    '两个及以上cpu，能让多线程同时并行执行',
    '后请求锁的线程自旋,不放弃处理器的执行时间'
],
'自适应自旋':[
    '自旋时间不固定',
    '由前一次同一个锁上的自旋时间及锁的拥有者的状态来决定的'
],
'锁消除':[
    '代码中，堆上的数据不会逃逸出去被其他线程访问到',
    '可当作栈上数据对待，认为它们线程私有,不用加锁',
    '如：三个字符串相加,转化为StringBuilder对象的连续append()操作',
    '解释执行时加锁，经过编译器的即时编译后，代码会忽略同步措施'
],
'锁粗化':[
    '一串零碎的操作都对同一个对象加锁，把加锁同步的范围扩展到外部'
],
'轻量级锁':[
    {'加锁过程':[
        '1.代码将进入同步块，同步对象未被锁定（锁标志位01）',
        '在当前线程的栈帧中建立名为锁记录的空间,存储锁对象Mark Word的拷贝',
        '2.CAS操作把对象的Mark Word更新为指向Lock Record的指针',
        '3.更新成功：线程拥有对象的锁，对象Mark Word的锁标志位变为00（轻量级锁定状态）',
        '4.更新失败，检查对象Mark Word是否指向当前线程的栈帧',
        '是：当前线程已经拥有对象锁，直接进入同步块继续执行',
        '否：锁对象被其他线程抢占，轻量级锁膨胀为重量级锁，锁标志变为10，Mark Word指向互斥锁指针'
    ]},
    {'解锁过程':[
        '对象Mark Word指向线程的锁记录',
        'CAS操作把对象当前的Mark Word和线程中复制的Mark Word替换回来',
        '成功替换:同步过程就顺利完成',
        '替换失败:其他线程尝试过获取锁，要在释放锁的同时，唤醒被挂起线程'
    ]}
],
'偏向锁':[
    {'目的':[
        '消除数据在无竞争情况下的同步，提高程序运行性能'
    ]},
    {'过程':[
        '锁对象第一次被线程获取时，把对象头中的标志位变为01、偏向模式变为1',
        'CAS操作把获取到锁的线程ID记录在对象Mark Word中',
        'CAS操作成功:持有偏向锁的线程以后进入锁相关的同步块，不再进行同步操作（如加锁、解锁，Mark Word的更新）'
    ]},
    {'失效':[
        '另外一个线程尝试获取锁，偏向模式马上结束',
        '根据锁对象目前是否处于被锁定的状态决定是否撤销偏向',
        '撤销后标志位恢复到未锁定01或轻量级锁定00',
        '后续的同步操作按照轻量级锁执行'
    ]},
    {'失败情况':[
        '对象计算过哈希码了，没位置存线程id'
    ]}
],
'轻量级锁，偏向锁对比':[
    '轻量级锁:在无竞争的情况下,使用CAS操作去消除同步使用的互斥量',
    '偏向锁:在无竞争的情况下,把整个同步都消除掉',
]

}

#构建xmind
xmind.build(content,r2)

#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 