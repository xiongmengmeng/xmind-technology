import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
xmind_name="jvm"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("垃圾收集算法")
r2=s2.getRootTopic()
r2.setTitle("垃圾收集算法")


content={
'名词定义':[
    {'部分收集（Partial GC）':[
        '不是完整收集整个Java堆的垃圾收集'
    ]},
    {'新生代收集（Minor GC/Young GC）':[
        '只是新生代的垃圾收集'
    ]},
    {'老年代收集（Major GC/Old GC）':[
        '只是老年代的垃圾收集(CMS收集器)'
    ]},
    {'混合收集（Mixed GC）':[
        '整个新生代以及部分老年代的垃圾收集(G1收集器)'
    ]},
    {'整堆收集（Full GC）':[
        '整个Java堆和方法区的垃圾收集'
    ]}
],
'标记-清除算法--Mark-Sweep':[
    '标记和清除都需要进行遍历，效率低',
    {'缺点':[
        '执行效率不稳定',
        '内存碎片化,用【分区空闲分配链表】解决内存分配问题，程序吞吐量下降'
    ]}
],
'复制算法--copying':[
    '适用于新生代，每次GC存活对象少',
    '一块Eden，两块较小的Survivor，比例8：1',
    {'过程':[
        '垃圾收集',
        '将Eden和Survivor中存活的对象复制到另外的Survivor上',
        '清理掉Eden和用过的那块Survivor空间',
        'Survivor空间不足时，依赖其他内存区域（大多是老年代）进行分配担保'
    ]},
    {'注':[
        '复制时:需要维护引用对象的地址，如使用句柄访问能提高一定效率'
    ]}   
],
'标记-压缩算法--Mark - Compact':[
    '将存活对象向内存一端移动，然后清理掉边界以外的内存',
    {'缺点':[
        '移动过程中，需要全程暂停用户应用程序,'
        '移动存活对象会更新所有引用这些对象的地方',
        '相比标记-清除算法，多了整理的步骤，停顿时间长',
        
    ]}
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
]


}

#构建xmind
xmind.build(content,r2)

#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 