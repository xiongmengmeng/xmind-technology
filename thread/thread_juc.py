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
        '首先根据老的种子生成新的种子',
        '然后根据新的种子来计算新的随机数'
    ]},
    {'问题':[
        '多线程竞争同一个原子变量的更新操作(CAS)',
        '同一时间只有一个线程成功',
        '会造成大量线程进行自旋重试，降低并发性能'
    ]},
    '类似于ThreadLocal类，是个工具类',
    '继承了Random类并重写了nextInt方法',
    '种子存放在具体的调用线程threadLocalRandomSeed变量',
    '计算新种子时是根据线程内维护的种子变量进行更新，避免了竞争',
    {'current()':[
        '初始化调用线程的threadLocalRandomSeed变量',
        '即初始化种子'
    ]},
    {'nextInt()':[
        '1.获取当前线程的threadLocalRandomSeed变量作为当前种子',
        '2.计算并更新新的种子到当前线程threadLocalRandomSeed变量',
        '3.根据新种子并使用具体算法计算随机数'
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
    '内部维护多个Cell变量，每个Cell里面有一个初始值为0的long型变量',
    '同等并发量下，争夺单个变量更新操作线程量少，变相减少争夺共享资源的并发量',
    '线程争夺一个Cell原子变量失败,可尝试在其他Cell变量上进行CAS尝试,增加了重试CAS成功的可能',
    '在获取LongAdder当前值时，是把所有Cell变量的value值累加后再加上base返回的'
]





}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 