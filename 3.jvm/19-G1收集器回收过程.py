import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
xmind_name="jvm"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("G1收集器回收过程")
r2=s2.getRootTopic()
r2.setTitle("G1收集器回收过程")


content={
'收集分类':[
    {'年轻代GC（Young GC）':[
        '现有Eden区放满不会马上触发，G1会计算下现在Eden区回收大概要多久时间',
        '如回收时间远小于参数-XX:MaxGCPauseMills值，增加年轻代region，继续给新对象存放，不会马上做YoungGC',
        '直到下一次Eden区放满，G1计算回收时间接近参数-XX:MaxGCPauseMills设定的值，触发Young GC'
    ]},
    {'混合回收（Mixed GC）':[
        '老年代的堆占有率达到参数(-XX:InitiatingHeapOccupancyPercent)设定的值则触发',
        '回收所有Young和部分Old以及大对象区，正常情况G1的垃圾收集是先做MixedGC',
        '主要使用复制算法，需把各个region中存活的对象拷贝到别的region里去',
        '拷贝过程中如果发现没有足够的空region能够承载拷贝对象就会触发一次Full GC'
    ]},
    {'Full GC':[
        '停止系统程序，采用单线程进行标记、清理和压缩整理',
        '好空闲出来一批Region供下一次MixedGC使用，这个过程非常耗时'
    ]},  
    '按Young GC->Mixed GC顺序,进行垃圾回收,如全满了,执行Full GC',
    {'例子':[
        '一个Web服务器，Java进程最大堆内存为4G，每分钟响应1500个请求，每45秒钟会新分配大约2G的内存',
        'G1会每45秒钟进行一次年轻代回收',
        '每31个小时整个堆的使用率会达到45%，会开始老年代并发标记过程，标记完成后开始四到五次的混合回收'
    ]}
],
'参数设置':[
    {'-XX:+UseG1GC':[
        '使用G1收集器'
    ]},
    # {'-XX:ParallelGCThreads':[
    #     '指定GC工作的线程数量'
    # ]},
    {'-XX:G1HeapRegionSize':[
        '指定分区大小(1MB~32MB，且必须是2的N次幂)，默认将整堆划分为2048个分区'
    ]},
    {'-XX:MaxGCPauseMillis':[
        '目标暂停时间(默认200ms)',
        {'过大':[
            '导致年轻代可能占用了堆内存的60%，才触发年轻代gc',
            '存活对象多，Survivor区域放不下那么多对象，直接进入老年代中'
        ]},
        {'过小':[
            '年轻代gc频繁,垃圾回收速度跟不上内存分配速度，新对象进入老年代'
        ]}
    ]},
    {'-XX:G1NewSizePercent':[
        '新生代内存初始空间(默认整堆5%)'
    ]},
    {'-XX:G1MaxNewSizePercent':[
        '新生代内存最大空间'
    ]},
    {'-XX:TargetSurvivorRatio':[
        'Survivor区的填充容量(默认50%)，Survivor区域里的一批对象(年龄1+年龄2+年龄n的多个',
        '年龄对象)总和超过了Survivor区域的50%，此时就会把年龄n(含)以上的对象都放入老年代'
    ]},
    {'-XX:MaxTenuringThreshold':[
        '最大年龄阈值(默认15)'
    ]},
    {'-XX:InitiatingHeapOccupancyPercent':[
        '老年代占用空间达到整堆内存阈值(默认45%)，则执行新生代和老年代的混合收集(MixedGC)',
    ]},
    {'-XX:G1MixedGCLiveThresholdPercent':[
        '(默认85%) region中的存活对象低于这个值时才会回收该region',
        '如果超过这个值，存活对象过多，回收意义不大'
    ]},
    {'-XX:G1MixedGCCountTarget':[
        '一次回收过程中指定做几次筛选回收(默认8次)',
        '在筛选回收阶段可以回收一会，然后暂停回收，恢复系统运行，再开始回收，让系统不至于单次停顿时间过长'
    ]},
],
'详细回收过程':[
    # 'JVM启动时，G1先准备好Eden区，程序在运行过程中不断创建对象到Eden区',
    # {'Eden耗尽时，触发一次YGC':[
    #     'G1创建回收集(需要被回收的内存分段的集合),集包含年轻代Eden区和Survivor区所有的内存分段',
    #     {'过程':[
    #         {'1.扫描根':[
    #             '根引用连同RSet记录的外部引用作为扫描存活对象的入口'
    #         ]},
    #         {'2.更新RSet':[
    #             '处理dirty card queue（脏卡表）中的 card，更新RSet',
    #             '此阶段后，RSet可以准确的反映老年代对所在的内存分段中对象的引用'
    #         ]},
    #         {'3.处理RSet':[
    #             '识别被老年代对象指向的Eden中的对象'
    #         ]},
    #         {'4.复制对象':[
    #             '对象树被遍历，Eden区内存段中存活的对象会被复制到Survivor区中空的内存分段',
    #             'Survivor区内存段中存活的对象如年龄未达阈值，年龄加1，达到阀值被复制到old区中空的内存分段',
    #             '如Survivor空间不够，Eden空间的部分数据会直接晋升到老年代空间'
    #         ]},
    #         {'5.处理引用':[
    #             '处理Soft，Weak，Phantom，Final，JNI Weak 等引用',
    #         ]}
    #     ]}
    # ]},
    {'1.初始标记(initial mark，STW)':[
        '暂停所有的其他线程，并记录下gc roots直接能引用的对象，速度很快'
    ]},
    {'2.并发标记':[
        '同CMS的并发标记',
        '过程若发现区域对象中的所有对象都是垃圾，那这个区域会被立即回收（实时回收）',
        '过程会计算每个区域的对象活性（区域中存活对象的比例），用来判断该区域值不值得回收'
    ]},
    {'3.最终标记（Remark，STW）':[
        '同CMS的重新标记'
    ]},
    {'4.筛选回收（Cleanup，STW）':[
        '首先对各个Region的回收价值和成本进行排序',
        '根据用户所期望的GC停顿时间(JVM参数 -XX:MaxGCPauseMillis指定)来制定回收计划'
    ]},
],
}

#构建xmind
xmind.build(content,r2)

#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 