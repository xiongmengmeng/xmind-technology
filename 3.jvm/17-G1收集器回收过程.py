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
'回收过程':[
    {'三个环节':[
        {'年轻代GC（Young GC）':[
            '当年轻代的Eden区用尽时开始年轻代回收过程',
            '收集过程是一个并行的独占式收集器(暂停所有应用程序线程，启动多线程执行年轻代回收)'
        ]},
        {'老年代并发标记过程（Concurrent Marking）':[
            '当堆内存使用达到一定值（默45%）时,开始老年代并发标记过程,标记完成马上开始混合回收过程',     
        ]},
        {'混合回收（Mixed GC）':[
            '涉及到老年代和年轻代的混合回收',
            '一次只需扫描/回收一小部分老年代的Region'
        ]},
        {'备注':[
            '如需要，单线程、独占式、高强度的FullGC是继续存在的',
            '它针对GC的评估失败提供了一种失败保护机制，即强力回收'
        ]}     
    ]},
    '按Young GC->Young GC+Concurrent Mark->Mixed GC顺序,进行垃圾回收,如全满了,执行Full GC',
    {'例子':[
        '一个Web服务器，Java进程最大堆内存为4G，每分钟响应1500个请求，每45秒钟会新分配大约2G的内存',
        'G1会每45秒钟进行一次年轻代回收',
        '每31个小时整个堆的使用率会达到45%，会开始老年代并发标记过程，标记完成后开始四到五次的混合回收'
    ]}
],
'详细回收过程':[
    'JVM启动时，G1先准备好Eden区，程序在运行过程中不断创建对象到Eden区',
    {'Eden耗尽时，触发一次YGC':[
        'G1创建回收集(需要被回收的内存分段的集合),集包含年轻代Eden区和Survivor区所有的内存分段',
        {'过程':[
            {'1.扫描根':[
                '根引用连同RSet记录的外部引用作为扫描存活对象的入口'
            ]},
            {'2.更新RSet':[
                '处理dirty card queue（脏卡表）中的 card，更新RSet',
                '此阶段后，RSet可以准确的反映老年代对所在的内存分段中对象的引用'
            ]},
            {'3.处理RSet':[
                '识别被老年代对象指向的Eden中的对象'
            ]},
            {'4.复制对象':[
                '对象树被遍历，Eden区内存段中存活的对象会被复制到Survivor区中空的内存分段',
                'Survivor区内存段中存活的对象如年龄未达阈值，年龄加1，达到阀值被复制到old区中空的内存分段',
                '如Survivor空间不够，Eden空间的部分数据会直接晋升到老年代空间'
            ]},
            {'5.处理引用':[
                '处理Soft，Weak，Phantom，Final，JNI Weak 等引用',
            ]}
        ]}
    ]},
    {'并发标记':[
        {'1.初始标记阶段':[
            '标记从根节点直接可达的对象,STW,会触发一次年轻代GC',
        ]},
        {'2.根区域扫描':[
            '扫描 Survivor区 直接可达的老年代区域对象，并标记被引用的对象'
        ]},
        {'3.并发标记':[
            '整个堆中进行并发标记，可能被YoungGC中断',
            '过程若发现区域对象中的所有对象都是垃圾，那这个区域会被立即回收（实时回收）',
            '过程会计算每个区域的对象活性（区域中存活对象的比例），用来判断该区域值不值得回收'
        ]},
        {'4.再次标记':[
            '由于应用程序持续进行，需要修正上一次的标记结果，是STW'
        ]},
        {'5.独占清理':[
            '计算各区域的存活对象和GC回收比例,并进行排序，识别可混合回收的区域,是STW'
        ]},
        {'6.并发清理':[
            '识别并清理完全空闲的区域'
        ]}
    ]},
    {'混合回收':[
        '回收整个Young Region，还会回收一部分的Old Region'
    ]},
    {'Full GC':[
        {'条件':[
            '回收的时候没有足够的to-space来存放晋升的对象'
            '并发处理过程完成前空间耗尽'
        ]}
    ]}
],
}

#构建xmind
xmind.build(content,r2)

#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 