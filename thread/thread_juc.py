import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="thread"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("juc")
r2=s2.getRootTopic()
r2.setTitle("并发包")


content={
'ThreadLocalRandom':[
    {'Random类':[
        '1.根据老种子生成新种子',
        '2.根据新种子计算新随机数'
    ]},
    {'问题':[
        '多线程竞争同一个原子变量的更新操作(CAS)',
        '同一时间只有一个线程成功',
        '会造成大量线程自旋重试，降低并发性'
    ]},
    {'ThreadLocalRandom':[
        '类似于ThreadLocal，是个工具类',
        '继承了Random类并重写了nextInt方法',
        '种子:存在调用线程的threadLocalRandomSeed变量',
        '根据线程内维护的种子变量计算新种子，避免了竞争',
        {'current()':[
            '初始化调用线程的threadLocalRandomSeed变量--初始化种子',
            'threadLocalRandomProbe变量--初始化探针'
        ]},
        {'nextInt()':[
            '1.获取当前线程的threadLocalRandomSeed变量作为种子',
            '2.计算新种子并更新到当前线程threadLocalRandomSeed变量',
            '3.根据新种子并使用具体算法计算随机数'
        ]}
    ]}
],
'AtomicLong':[
    {'变量':[
        'Unsafe.getUnsafe（）方法获取到Unsafe类的实例',
        'valueOffset:变量value的偏移量',
        'value被声明为volatile的，这是为了在多线程下保证内存可见性'
    ]},
    {'getAndIncrement':[
        'JDK 7:boolean compareAndSet(long expect, long update)',
        'JDK 8中unsafe.getAndAddLong',
        '内部都是调用：unsafe.compareAndSwapLong'
    ]},
    '高并发下大量线程竞争更新同一个原子变量，失败会不断自旋尝试CAS，浪费CPU资源'
],
'LongAdder':[
    {'类结构':[
        '继承自Striped64类(内部维护着三个变量)',
        'LongAdder的真实值：base的值+Cell数组里面所有Cell元素中的value值的累加',
        {'Striped64类':[
            '1.base:基础值，默认0',
            '2.cellsBusy:实现自旋锁，值有0和1，创建Cell元素，扩容或初始化Cell数组时',
            '使用CAS操作该变量保证同时只有一个线程可以进行其中之一的操作',
            '3.Cell数组:Cell里面有一个初始值为0的long型变量'
        ]},
        '线程争夺一个Cell原子变量失败,在其他Cell变量进行CAS尝试,增加了重试成功的可能',
    ]},
    {'当前线程访问Cell数组哪一个Cell元素':[
        '当前线程变量threadLocalRandomProbe&(cells数组元素个数-1)'
    ]},
    {'初始化Cell数组':[
        '初始化cells数组元素个数为2',
        '计算当前线程应访问celll数组的位置'
    ]},
    {'Cell数组扩容':[
        {'条件':[
            'cells的元素个数<当前机器CPU个数',
            '多线程访问了cells中同一个元素，出现CAS失败'
        ]},
        '容量扩充为之前的2倍，并复制Cell元素到扩容后数组'
    ]}, 
    {'访问Cell元素冲突后':[
        '扩容',
        'CAS失败线程重计算当前线程threadLocalRandomProbe'
    ]},
    {'如何保证线程操作被分配的Cell元素的原子性':[
        'volatile+CAS算法'
    ]}
],
'LongAccumulator':[
    {'构造函数':[
        'LongAccumulator(LongBinaryOperator accumulatorFunction,long identity)',
        'accumulatorFunction:双目运算器接口，根据输入的两个参数返回一个计算值',
        'identity:累加器的初始值'
    ]},
    '优点：初始值可不为0，可指定累加规则',
    'LongAdder类是LongAccumulator的一个特例'
],
'CopyOnWriteArrayList':[
    '有一个array数组对象用来存放具体元素',
    '写时复制的策略来保证list的一致性',
    '增删改的过程使用独占锁',
    '获取，遍历有弱一致性问题，看到的数据是快照'
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