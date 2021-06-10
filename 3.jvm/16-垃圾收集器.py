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
        '复制算法'
        '单线程',
        '简单，高效,额外内存消耗最小,适合微服务',
    ]},
    {'ParNew收集器':[
        'Serial收集器的多线程并行版本',
        '除了Serial收集器，只有它能与CMS收集器配合工作',
        '可使用-XX：+/-UseParNewGC选项来强制指定或者禁用它'
    ]},
    {'Parallel Scavenge收集器':[
        '复制算法',
        '目标:达到一个可控制的吞吐量',
        '最大垃圾收集停顿时间:-XX：MaxGCPauseMillis',
        '吞吐量:-XX：GCTimeRatio',
        '垃圾收集的自适应的调节策略:-XX：+UseAdaptiveSizePolicy'
    ]}
],
'老生代收集器':[
    {'Serial Old收集器':[
        '标记-压缩算法'
        '单线程',
        {'两种用途':[
            'JDK 5及之前与Parallel Scavenge收集器搭配使用',
            'CMS收集器失败时的后备预案，并发收集发生Concurrent Mode Failure时使用'
        ]}
    ]},
    {'Parallel Old收集器':[
        '标记-压缩算法'
        '支持多线程并发收集',
    ]},
    {'CMS收集器':[
    ]}
],
'低延迟垃圾收集器':[
    {'垃圾收集器的三项指标':[
        '内存占用（Footprint）',
        {'吞吐量（Throughput）':[
            '运行用户代码时间/(运行用户代码时间+垃圾收集时间)'
        ]},
        {'延迟（Latency）':[
            '最被重视'
        ]},
        {'关系':[
            {'频繁GC':[
                '延迟小，但吞吐量低'
            ]},
            {'少GC':[
                '延迟长，但吞吐量高'
            ]}
        ]}
    ]},
    'ZGC收集器--jdk11',
    'JDK 10,统一了垃圾收集器接口，将内存回收的“行为”与“实现”进行分离'
],




}

#构建xmind
xmind.build(content,r2)

#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 