import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
xmind_name="jvm"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("jvm总结-垃圾回收")
r2=s2.getRootTopic()
r2.setTitle("jvm总结-垃圾回收")


content={
'回收区域':[
    {'方法或者线程结束，自然回收':[
        '程序计数器',
        '虚拟机栈',
        '本地方法栈'
    ]},
    {'方法区回收':[
        '废弃的常量',
        '不再使用的Class对象'
    ]},
    {'对象回收':[
        {'判断对象是否可达':[
            '引用计数法',
            '可达性分析法'
        ]},
        {'对象分配过程':[
            '1.对象优先在Eden分配',
            '2.大对象直接进入老年代',
            '3.长期存活的对象将进入老年代',
            '4.动态对象年龄判定',
            '4.空间分配担保'
        ]},
        {'对象回收过程':[
            '至少经历两次标记过程'
        ]}
    ]}
],
'回收开始节点':[
    {'GC Roots的对象':[
        {'虚拟机栈':[
            '栈中引用的对象'
        ]},
        {'方法区':[
            '类静态属性引用的对象,常量引用的对象',
        ]},
        {'本地方法栈':[
            'JNI（即Native方法）引用的对象'
        ]},
        {'虚拟机内部':[
            '常驻异常对象（如NullPointExcepiton）,系统类加载器',
        ]},
        '同步锁（synchronized关键字）持有的对象',
        '反映Java虚拟机内部情况的JMXBean、JVMTI中注册的回调、本地代码缓存'
    ]},
    {'根节点枚举---加速':[
        'OopMap',
    ]},
],
'回收开始时间':[
    '安全点---主动式中断',
    '安全区域'
],
'回收算法':[
    '标记-清除算法--Mark-Sweep',
    '复制算法--copying',
    '标记-压缩算法--Mark - Compact'
],
'回收分类':[
    'Minor GC',
    'Major GC',
    'Full GC'
],
'回收其它':[
    '记忆集与卡表',
    'TLAB',
    'JVM参数',
    '分析dump下的hprof文件'
],
'垃圾收集器':[
    {'新生代收集器':[
        'Serial收集器',
        'ParNew收集器',
        'Parallel Scavenge收集器'
    ]},
    {'老生代收集器':[
        'Serial Old收集器',
        'Parallel Old收集器',
        'CMS收集器'
    ]},
    'G1收集器',
    {'三项指标':[
        '内存占用（Footprint）',
        '吞吐量（Throughput）',
        '延迟（Latency）'
    ]}
],





}

#构建xmind
xmind.build(content,r2)

#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 