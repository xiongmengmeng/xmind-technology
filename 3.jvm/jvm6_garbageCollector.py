import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
xmind_name="jvm"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("jvm_garbageCollector")
r2=s2.getRootTopic()
r2.setTitle("jvm_垃圾收集器")


content={



'新生代收集器':[
    {'Serial收集器':[
        '单线程',
        '简单，高效',
        '额外内存消耗最小,适合微服务',
        '标记复制算法'
    ]},
    {'ParNew收集器':[
        'Serial收集器的多线程并行版本',
        '除了Serial收集器，只有它能与CMS收集器配合工作',
        'ParNew收集器是激活CMS（使用-XX：+UseConcMarkSweepGC选项）的默认新生代收集器',
        '可以使用-XX：+/-UseParNewGC选项来强制指定或者禁用它'
    ]},
    {'Parallel Scavenge收集器':[
        '标记-复制算法',
        '目标是达到一个可控制的吞吐量',
        '最大垃圾收集停顿时间:-XX：MaxGCPauseMillis',
        '吞吐量:-XX：GCTimeRatio',
        '垃圾收集的自适应的调节策略:-XX：+UseAdaptiveSizePolicy'
    ]}
],
'老生代收集器':[
    {'Serial Old收集器':[
        '单线程',
        '标记-整理',
        {'两种用途':[
            'JDK 5及之前与Parallel Scavenge收集器搭配使用',
            'CMS收集器失败时的后备预案，并发收集发生Concurrent Mode Failure时使用'
        ]}
    ]},
    {'Parallel Old收集器':[
        '支持多线程并发收集',
        '标记-整理算法'
    ]},
    {'CMS收集器':[
        '目标：获取最短回收停顿时间',
        '标记-清除算法',
        '并发收集、低停顿',
        {'四个步骤':[
            '初始标记（CMS initial mark）：标记GC Roots能直接关联到的对象',
            '并发标记（CMS concurrent mark）：从GC Roots的直接关联对象开始遍历整个对象图',
            '重新标记（CMS remark）：修正并发标记期间，因用户程序运作导致标记产生变动的对象标记记录',
            '并发清除（CMS concurrent sweep）：清理删除掉标记阶段判断已经死亡的对象'
        ]},
        '初始标记、重新标记两个步骤需要“Stop The World”',
        {'缺点':[
            '占用部分线程导致应用程序变慢，降低总吞吐量',
            '无法处理“浮动垃圾”：并发标记和并发清理阶段产生的',
            '空间碎片过多'
        ]}
    ]}
],
'Garbage First收集器':[
    {'基于Region的内存布局形式':[
        '将Java堆划分为多个大小相等的独立区域',
        '每个Region可以扮演新生代的Eden空间、Survivor空间，老年代空间',
        'Region大小:-XX：G1HeapRegionSize，取值范围为1MB～32MB，为2的N次幂',
        '收集停顿时间:-XX：MaxGCPauseMillis，默认值是200毫秒'
    ]},
    {'大对象回收':[
        'Region有特殊的Humongous区域，用来存储大对象（超过了Region容量一半的对象）',
        '超过整个Region容量的大对象，放在N个连续的Humongous Region之中,作为老年代的一部分'
    ]},
    'JDK 10,统一了垃圾收集器接口，将内存回收的“行为”与“实现”进行分离',
    '跟踪Region里面的垃圾堆积的大小，在后台维护一个优先级列表,优先处理回收价值大的Region',
    {'四个步骤':[
        {'初始标记':[
            '标记一下GC Roots能直接关联到的对象',
            '修改TAMS指针的值',
            '需要停顿线程，但耗时很短'
        ]},
        {'并发标记':[
            '从GC Root开始对堆中对象进行可达性分析',
            '递归扫描整个堆里的对象图，找出回收对象，耗时长',
            '可与用户程序并发执行',
            '要重新处理SATB记录下的在并发时有引用变动的对象'
        ]},
        {'最终标记':[
            '需停顿线程',
            '处理并发阶段结束后遗留下来的少量SATB记录'
        ]},
        {'筛选回收':[
            '更新Region统计数据，对各个Region的回收价值和成本进行排序',
            '自由选择任意多个Region构成回收集',
            '把回收Region的存活对象复制到空的Region中',
            '清理掉整个旧Region空间',
            '存活对象的移动，须暂停用户线程'
        ]},
        '理念：应付应用的内存分配速率，不追求一次把整个Java堆全部清理干净'
    ]},
    {'与CMS对比':[
        'G1优点:指定最大停顿时间、分Region的内存布局、按收益动态确定回收集,标记-复制算法',
        'G1缺点:内存占用,程序运行时的额外执行负载都要比CMS要高'
    ]}
],
'低延迟垃圾收集器':[
    {'垃圾收集器的三项指标':[
        '内存占用（Footprint）',
        '吞吐量（Throughput）',
        '延迟（Latency）:最被重视'
    ]},
    'ZGC收集器'
],
'垃圾收集器工作':[
    '对象优先在Eden分配',
    {'大对象直接进入老年代':[
        '-XX：PretenureSizeThreshold:大于该值的对象直接在老年代分配',
        '上述参数只对Serial和ParNew两款新生代收集器有效',
        '避免在Eden区及两个Survivor区之间来回复制，产生大量的内存复制操作'
    ]},
    {'长期存活的对象将进入老年代':[
        'XX：MaxTenuringThreshold:对象晋升老年代的年龄阈值,默15'
    ]},
    {'动态对象年龄判定':[
        'Survivor中相同年龄所有对象大小>Survivor的一半',
        '年龄>=该年龄的对象直接进入老年代'
    ]},
    {'空间分配担保':[
        '老年代的连续空间>新生代对象总大小or历次晋升的平均大小，进行Minor GC，否则进行Full GC'
    ]}
],


}

#构建xmind
xmind.build(content,r2)

#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 