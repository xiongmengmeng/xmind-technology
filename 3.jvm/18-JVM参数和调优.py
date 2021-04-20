import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
xmind_name="jvm"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("JVM参数和调优")
r2=s2.getRootTopic()
r2.setTitle("JVM参数和调优")


content={
'JVM参数':[
    {'-Xms4096m':[
    '堆区的起始内存'
    ]},
    {'-Xmx4096m':[
    '堆区的最大内存',
    '-Xms和-Xmx两参数配置相同值，则Java垃圾回收机制清理完堆区后不需重新分隔计算堆区大小，可提高性能'
    ]},
    {'-XX:NewRatio=2 ':[
    '新生代占1，老年代占2，新生代占整个堆的1/3'
    ]},
    {'-XX:SurvivorRatio=8':[
    'Eden空间和另外两个Survivor空间缺省所占的比例是 8：1：1'
    ]},
    {'-XX:+PrintGCDetails ':[
    'OOM时打印堆栈信息'
    ]},
    {'-XX:+HeapDumpBeforeFullGC':[
        '-XX:+HeapDumpOnOutOfMemoryError ',
        '-XX:HeapDumpPath=/home/logs/tms-service/ ',
        'FullGC或OutOfMemory时下dump快照文件',
    ]}
],
'调优':[
    {'Minor GC':[
        '新生代的GC，等价于 YGC',
        {'触发条件':[
            'Eden区满，Survivor满不会引发GC'
        ]}
    ]},
    {'Major GC':[
        '老年代的GC',
        {'触发条件':[
            '老年代空间不足'
        ]},
        '出现了MajorGC，经常会伴随至少一次的Minor GC(不是绝对)'
    ]},
    {'Full GC':[
        '整堆收集，收集整个Java堆和方法区的垃圾收集',
        {'触发条件':[
            '调用System.gc()时，系统建议执行Full GC，但是不必然执行',
            '老年代空间不足',
            '方法区空间不足',
            '通过Minor GC进入老年代的平均大小>老年代的可用内存',
            'Minor GC时，生活对象大于To Space可用内存，把对象转到老年代，且老年代的可用内存小于该对象大小'
        ]},
    ]},
    {'分析':[
        'GC过程会出现Stop The World',
        '而Major GC和Full GC出现STW时间，是Minor GC的10倍以上->尽量避免'
    ]}
],
'TLAB':[
    'JVM在Eden空间内，为每个线程分配了一个私有缓存区域',
    {'优势':[
        '这种内存分配方式称之为快速分配策略',
        '可避免一系列非线程安全问题，同时够提升内存分配的吞吐量'
    ]},
    {'参数开启':[
        '-XX:[+/-]UseTLAB:是否开启TLAB空间'
    ]},
    {'分配过程':[
        '对象首先是通过TLAB开辟空间，如不能放入（如对象太大TLAB空间不足等），需通过Eden来进行分配'
    ]},
    {'注':[
        '堆空间不都是共享的,有TLAB这个概念，在堆中划分出一块区域，为每个线程所独占'
    ]}
],
'分析dump下的hprof文件':[
    {'分析工具':[
        'Eclipse Memory Analyzer'
    ]},
    '将hprof文件导入',
    {'分析':[
        {'1.Dominator Tree':[
            '可以列出占用内存最大的线程，以及线程下面的那些对象占用的空间'
        ]},
        {' 2.Leak Suspects':[
            'MA分析出的可能导致内存溢出的地方'
        ]}
    ]}
]


}

#构建xmind
xmind.build(content,r2)

#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 