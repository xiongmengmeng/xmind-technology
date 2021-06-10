import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
xmind_name="jvm"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("G1收集器")
r2=s2.getRootTopic()
r2.setTitle("G1收集器")


content={
'简介':[
    'Garbage First收集器',
    {'目的':[
        '为了适应现在不断扩大的内存和不断增加的处理器数量'
    ]},
    {'作用':[
        '在延迟可控的情况下获得尽可能高的吞吐量'
    ]},
    {'内存布局':[
        '将Java堆划分为多个大小相等的独立区域',
        '每个Region可扮演新生代的Eden空间、Survivor空间，老年代空间',
        '每个Region都是通过指针碰撞来分配空间',
        {'Region大小':[
            '-XX：G1HeapRegionSize，取值范围为1MB～32MB，为2的N次幂'
        ]},
        {'收集停顿时间':[
            '-XX：MaxGCPauseMillis，默认值是200毫秒'
        ]}
    ]},
    {'大对象存放':[
        'Region有特殊的Humongous区域：用来存储大对象（超过Region容量一半的对象）',
        '超过整个Region容量的大对象，放在N个连续的Humongous Region之中,作为老年代的一部分'
    ]},
    {'优先列表':[
        '每次根据允许的收集时间，优先回收价值最大的Region',
        '保证了G1收集器在有限的时间内可以获取尽可能高的收集效率'
    ]},
    {'回收算法':[
        '内存的回收是以region作为基本单位的',
        'Region之间是复制算法，但整体上实际可看作是标记-压缩（Mark-Compact）算法'
    ]},
    {'G1收集器的常见操作步骤':[
        '1.开启G1垃圾收集器',
        '2.设置堆的最大内存',
        '3.设置最大的停顿时间'
    ]} 
],
'与CMS对比':[
    {'G1优点':[
        {'指定最大停顿时间':[
            '相比于CMS GC，G1未必能做到CMS在最好情况下的延时停顿，但是最差情况要好很多'
        ]},
        '分Region的内存布局、按收益动态确定回收集',
        '标记-复制算法'
    ]},
    {'G1缺点':[
        '内存占用,程序运行时的额外执行负载都要比CMS要高'
    ]}
],
'Java不同版本新特性':[
    {'语法层面':[
        'Lambda表达式、switch、自动拆箱装箱、enum、泛型等'
    ]},
    {'API层面':[
        'Stream API、新的日期时间、Optional、String、集合框架'
    ]},
    {'底层优化':[
        'JVM优化、GC的变化、元空间、静态域、字符串常量池位置变化'
    ]}
]
# '四个步骤':[
#     {'初始标记':[
#         '标记一下GC Roots能直接关联到的对象',
#         '修改TAMS指针的值',
#         '需要停顿线程，但耗时很短'
#     ]},
#     {'并发标记':[
#         '从GC Root开始对堆中对象进行可达性分析',
#         '递归扫描整个堆里的对象图，找出回收对象，耗时长',
#         '可与用户程序并发执行',
#         '要重新处理SATB记录下的在并发时有引用变动的对象'
#     ]},
#     {'最终标记':[
#         '需停顿线程',
#         '处理并发阶段结束后遗留下来的少量SATB记录'
#     ]},
#     {'筛选回收':[
#         '更新Region统计数据，对各个Region的回收价值和成本进行排序',
#         '自由选择任意多个Region构成回收集',
#         '把回收Region的存活对象复制到空的Region中',
#         '清理掉整个旧Region空间',
#         '存活对象的移动，须暂停用户线程'
#     ]},
#     {'理念':[
#         '应付应用的内存分配速率，不追求一次把整个Java堆全部清理干净'
#     ]}
# ],

}

#构建xmind
xmind.build(content,r2)

#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 