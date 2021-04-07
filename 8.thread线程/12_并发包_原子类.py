import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="thread"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("并发包_原子类")
r2=s2.getRootTopic()
r2.setTitle("并发包_原子类")


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
]





}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 