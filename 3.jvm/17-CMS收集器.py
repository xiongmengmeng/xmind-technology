import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
xmind_name="jvm"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("CMS收集器")
r2=s2.getRootTopic()
r2.setTitle("CMS收集器")


content={
'标记-清除算法':[
    '并发收集(第一次实现了让垃圾收集线程与用户线程同时工作)、低停顿'
],
'目标':[
    '获取最短回收停顿时间'
],
'四个步骤':[
    {'初始标记（CMS initial mark）':[
        '需STW,暂停所有的其他线程',
        '标记GC Roots能直接关联到的对象',
    ]},
    {'并发标记（CMS concurrent mark）':[
        '从GC Roots的直接关联对象开始遍历整个对象图',
        '耗时较长,但不需要停顿用户线程（可与垃圾收集线程一起并发运行)',
    ]},
    {'重新标记（CMS remark）':[
        '需STW,暂停所有的其他线程',
        '修正并发标记期间，因用户程序运作导致标记产生变动的对象标记记录',
        '停顿时间一般会比初始标记阶段的时间稍长，远远比并发标记阶段时间短',
        '用到三色标记里的增量更新算法做重新标记'
    ]},
    {'并发清除（CMS concurrent sweep）':[
        '清理删除掉标记阶段判断已经死亡的对象',
        '段如果有新增对象会被标记为黑色不做任何处理',
        '因为使用标记-清除算法，只清除不移动，不需要停顿用户线程'
    ]},  
    {'并发重置':[
        '重置本次GC过程中的标记数据'
    ]},
    {'注':[
        '初始标记、重新标记两个步骤需要“Stop The World”'
    ]}      
],
'缺点':[
    {'对CPU资源敏感（会和服务抢资源）':[
        '占用部分线程导致应用程序变慢，降低总吞吐量'
    ]},
    {'无法处理“浮动垃圾”':[
        '并发标记和并发清理阶段产生的'
    ]},
    {'空间碎片过多':[
        'XX:+UseCMSCompactAtFullCollection可让jvm在执行完标记清除后再做整理'
    ]},
    {'执行过程中的不确定性':[
        '存在上一次垃圾回收还没执行完，然后垃圾回收又被触发的情况',
        '即是"concurrentmode failure"，此时会进入STW，用serial old垃圾收集器来回收'
    ]}
],
'CMS的相关核心参数':[
    {'1.-XX:+UseConcMarkSweepGC':[
        '启用cms'
    ]},
    {'2.-XX:ConcGCThreads':[
        '并发的GC线程数'
    ]},
    {'3.-XX:+UseCMSCompactAtFullCollection':[
        'FullGC之后做压缩整理（减少碎片）'
    ]},
    {'4.-XX:CMSFullGCsBeforeCompaction':[
        '多少次FullGC之后压缩一次，默认是0，代表每次FullGC后都会压缩一次',
    ]},
    {'5.-XX:CMSInitiatingOccupancyFraction':[
        '当老年代使用达到该比例时会触发FullGC（默认是92，这是百分比）'
    ]},
    {'6.-XX:+UseCMSInitiatingOccupancyOnly':[
        '只使用设定的回收阈值，如果不指定，JVM仅在第一次使用设定值，后续则会自动调整'
    ]},
    {'7.-XX:+CMSScavengeBeforeRemark':[
        '在CMS GC前启动一次minor gc,',
        '目的在减少老年代对年轻代的引用，降低CMS GC的标记阶段时的开销，一般CMS的GC耗时80%都在标记阶段'
    ]},
    {'8. -XX:+CMSParallellnitialMarkEnabled':[
        '在初始标记的时候多线程执行，缩短STW'
    ]},
    {'9.-XX:+CMSParallelRemarkEnabled':[
        '在重新标记的时候多线程执行，缩短STW'
    ]}
]




}

#构建xmind
xmind.build(content,r2)

#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 