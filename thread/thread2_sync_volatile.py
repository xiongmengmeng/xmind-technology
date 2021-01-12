import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="thread"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("thread_synchronized_volatile")
r2=s2.getRootTopic()
r2.setTitle("对象及变量的并发访问")


content={
'synchronized':[
    '关键字取得的锁都是"对象锁"，不是把一段代码或方法当作锁',
    {'基础':[
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
    ]},
    {'原理':[
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
        ]}
    ]},
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
    ]},
    {'应用':[
        '共享资源的读写访问需同步，不是共享资源没有同步必要',
        '多个线程访问同一个对象需同步',
        '多个线程访问多个对象，JVM会创建多个锁，无需同步'
    ]},
    {'特性':[
        {'可重入':[
            '自己可以再次获取自己的锁',
            '支持子类继承',
            '一个synchronized方法/块的内可以调用本类的其他synchronized方法'
        ]},
        '可见性：线程加锁时必须从主内存中获得最新的值，解锁时必须把变量的值刷新到内存中去',
        '异常锁自动释放',
        '不具有继承性:因为子类重写了方法'
    ]},
    {'死锁':[
        '经典的多线程问题',
        '不同的线程等待不可能被释放的锁，导致线程假死(waiting)'
    ]}
],
'volatile':[
    '强制从公共堆栈中取得变量的值，而不是从线程私有数据栈中取得变量的值',
    {'可见性':[
        {'lock前缀指令':[
            '借助了CPU的lock指令:使变量在多个线程间可见,不具有原子性',
            {'原则':[
                '写volatile时处理器会将缓存写回到主内存',
                '一个处理器的缓存写回到内存会导致其他处理器的缓存失效'
            ]}
            {'MESI':[
                '缓存一致性协议',
                'CPU写数据时，如发现操作变量是共享变量，发出信号通知其他CPU将该变量的缓存行置为无效',
                '当其他CPU需要读取变量时，发现缓存变量的缓存行无效，就会从内存重新读取',
                {'嗅探':[
                    '每个处理器通过嗅探在总线上传播的数据来检查自己缓存的值是否过期',
                    '当处理器发现自己缓存行对应的内存地址被修改，会将缓存行设置成无效',
                    '当处理器对数据进行修改时，会重新从系统内存中把数据读到处理器缓存中'
                ]},
                {'总线风暴':[
                    '由于MESI缓存一致性协议，需不断从主内存嗅探和cas不断循环',
                    '无效交互会导致总线带宽达到峰值'
                ]}
            ]}
        ]},
        {'内存屏障':[
            '内存屏障（memory barriers）：一组处理器指令，用于实现对内存操作的顺序限制',
            '读屏障:读取操作前加入读屏障，让工作内存中的数据失效，重新从主存读取到最新数据',
            '写屏障:写入数据后加入写屏障，让写入到工作内存中的数据更新到主内存，让其他线程可见',
        ]}

    ]},
    {'有序性':[
        {'禁止指令重排序':[
            {'指令重排':[
                '源代码 -> ',
                '编译器优化的重排 -> ',
                '指令并行的重排 ->',
                '指内存系统的重排 ->',
                '最终执行指令'
            ]},
            '多线程环境中线程交替执行，由于编译器优化重排->',
            '两线程中使用变量能否保证一致性无法确定，结果无法预测'
        ]},
        {'内存屏障':[
            '写屏障会确保指令重排序时，不会将写屏障之前的代码排在写屏障之后',
            '读屏障会确保指令重排序时，不会将读屏障之后的代码排在读屏障之前',
            '保证特定操作的顺序:禁止在内存屏障前后的指令执行重排序优化',
            '保证某些变量的内存可见性:刷新CPU缓存'
        ]}
    ]}

],
'synchronized和volatile比较':[
    '1.volatile:线程同步的轻量级实现，性能好，只能修饰变量',
    'synchronized:可修饰方法及代码块,使用面广',
    '2.多线程访问volatile不会发生阻塞，而synchronized会出现阻塞',
    '3.volatile:保证数据的可见性，不保证原子性',
    'synchronized:可保证原子性和可见性（会将私有内存和公共内存数据做同步）',
    '4.volatile解决变量在多个线程之间的可见性',
    'synchronized解决多线程之间访问资源的同步性'
]
}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 