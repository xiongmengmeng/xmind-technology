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
    ]},
    '@sun.misc.Contended注解对cell类进行字节填充，防止数组中多元素共享一个缓存行，可提升性能'
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
    '获取，遍历有弱一致性问题，看到的数据是快照',
    {'问题':[
        '写操作时，内存有两个对象，占用空间',
        '元素较多时，复制开销大，占用CPU'
    ]}
]





}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 