import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
xmind_name="jvm"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("JVM性能监控与调优")
r2=s2.getRootTopic()
r2.setTitle("JVM性能监控与调优")


content={

'基础工具':[
    {'JHSDB':[
        '一款基于服务性代理实现的进程外调试工具'
    ]},
    {'JConsole':[
        '一款基于JMX的可视化监视、管理工具',
        '主要功能是通过JMX的MBean（Managed Bean）对系统进行信息收集和参数动态调整'
    ]},
    {'VisualVM':[
        '功能最强大的运行监视和故障处理程序之一',
        {'jvisualvm.exe':[
            ':图形化工具，提供内存，CPU,堆转储分析，内存泄漏检测'
        ]}
    ]},
    {'Java Mission Control':[
        '可持续在线的监控工具'
    ]}
],
'HotSpot虚拟机插件HSDIS':[
    '一个被官方推荐的HotSpot虚拟机即时编译代码的反汇编插件',
    '-XX：+PrintAssembly指令：把即时编译器动态生成的本地代码->汇编代码',
    {'JITWatch':[
        'HSDIS经常搭配使用的可视化的编译日志分析工具'
    ]}
],
'案例':[
    {'大内存硬件上的程序部署策略':[
        {'1.单虚拟机管理大内存':[
            'a.用G1收集器,Shenandoah、ZGC等，可控制延迟',
            {'b.用Parallel Scavenge/Old等':[
                '需把Full GC频率控制得足够低,低到不会在用户使用过程中发生，如一天不出现一次Full GC',
                '可深夜以定时任务方式触发Full GC或自动重启应用服务器',
                {'控制Full GC频率关键':[
                    '老年代的相对稳定',
                    '大多数对象能否符合“朝生夕灭”的原则'
                ]},
                '发生堆内存溢出，几乎无法产生堆转储快照,即使有分析也很困难'
            ]}
        ]},
        {'2.多虚拟机，逻辑集群':[
            '一台物理机器启动多个应用服务器进程，每个服务器进程配不同端口,前端搭建一个负载均衡器，反向代理方式分配访问请求',
            {'无Session复制的亲合式集群':[
                '均衡器按一定的规则算法将一个用户请求永远分配到一个固定集群节点',
                '程序开发阶段就几乎不必为集群环境做任何特别的考虑'
            ]}
        ]}
    ]},
    '集群间同步导致的内存溢出',
    {'堆外内存导致的溢出错误':[
        {'直接内存':[
            '-XX：MaxDirectMemorySize调整大小',
            '内存不足时抛出OutOf-MemoryError,或OutOfMemoryError：Direct buffer memory'
        ]},
        {'线程堆栈':[
            '通过-Xss调整大小',
            '内存不足时抛出StackOverflowError（线程请求的栈深度>虚拟机允许深度）',
            'OutOfMemoryError（栈扩展时无法申请到足够的内存）'
        ]},
        {'Socket缓存区':[
            '每个Socket连接都Receive和Send两个缓存区，分别占大约37KB和25KB内存',
            '连接多的话,如无法分配，抛出IOException：Too many open files异常'
        ]},
        {'JNI代码':[
            '代码中使用JNI调用本地库',
            '本地库用的是本地方法栈和本地内存，不是堆内存'
        ]}
    ]},
    '外部命令导致系统缓慢',
    {'服务器虚拟机进程崩溃':[
        'http请求响应超时->等待线程和Socket连接越来越多',
        '->超过虚拟机承受能力->虚拟机进程崩溃',
        {'解决':[
            '异步调用可改为消息模式'
        ]}
    ]},
    {'不恰当数据结构导致内存占用过大':[
        '以HashMap<Long，Long>Entry为例'
    ]},
    {'Windows虚拟内存导致的长时间停顿':[
        '程序在最小化时它的工作内存被自动交换到磁盘的页面文件之中',
        '垃圾收集时因为恢复页面文件的操作导致不正常的垃圾收集停顿',
        '加入参数“-Dsun.awt.keepWorkingSetOnMinimize=true”'
    ]},
    # {'安全点导致长时间停顿':[
    #     '可数循环没有放置安全点->循环很慢导致停顿',
    #     '循环索引的数据类型int改为long，可数循环变为不可数循环'
    # ]}
]
}

#构建xmind
xmind.build(content,r2)

#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 