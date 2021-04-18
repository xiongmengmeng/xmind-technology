import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
xmind_name="jvm"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("垃圾收集器")
r2=s2.getRootTopic()
r2.setTitle("垃圾收集器")


content={
'新生代收集器':[
    {'Serial收集器':[
        '标记复制算法'
        '单线程',
        '简单，高效',
        '额外内存消耗最小,适合微服务',
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
        '标记-整理算法'
        '单线程',
        {'两种用途':[
            'JDK 5及之前与Parallel Scavenge收集器搭配使用',
            'CMS收集器失败时的后备预案，并发收集发生Concurrent Mode Failure时使用'
        ]}
    ]},
    {'Parallel Old收集器':[
        '标记-整理算法'
        '支持多线程并发收集',
    ]},
    {'CMS收集器':[
        {'标记-清除算法':[
            '并发收集(第一次实现了让垃圾收集线程与用户线程同时工作)、低停顿'
        ]},
        {'目标':[
            '获取最短回收停顿时间'
        ]},
        {'四个步骤':[
            {'初始标记（CMS initial mark）':[
                '标记GC Roots能直接关联到的对象',
                'stop-the-world,很快'
            ]},
            {'并发标记（CMS concurrent mark）':[
                '从GC Roots的直接关联对象开始遍历整个对象图',
                '耗时较长,但不需要停顿用户线程（可与垃圾收集线程一起并发运行)',
                'stop-the-world,很快'
            ]},
            {'重新标记（CMS remark）':[
                '修正并发标记期间，因用户程序运作导致标记产生变动的对象标记记录'
            ]},
            {'并发清除（CMS concurrent sweep）':[
                '清理删除掉标记阶段判断已经死亡的对象',
                '因为使用标记-清除算法，只清除不移动，不需要停顿用户线程'
            ]},         
        ]},
        '初始标记、重新标记两个步骤需要“Stop The World”',
        {'缺点':[
            '占用部分线程导致应用程序变慢，降低总吞吐量',
            {'无法处理“浮动垃圾”':[
                '并发标记和并发清理阶段产生的'
            ]},
            '空间碎片过多'
        ]}
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
'JDK 10,统一了垃圾收集器接口，将内存回收的“行为”与“实现”进行分离':[],



}

#构建xmind
xmind.build(content,r2)

#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 