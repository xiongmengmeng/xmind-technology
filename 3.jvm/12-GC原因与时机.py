import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
xmind_name="jvm"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("GC原因与时机")
r2=s2.getRootTopic()
r2.setTitle("GC原因与时机")


content={
'GC原因':[
    {'内存溢出':[
        '没有空闲内存，并且垃圾收集器也无法提供更多内存',
        {'原因':[
            '虚拟机的堆内存不够',
            '代码中创建了大量大对象，并且长时间不能被垃圾收集器收集（存在被引用）'
        ]}
    ]},
    {'内存泄漏':[
        '对象不会再被程序用到了，但是GC又不能回收他们的情况',
        '内存泄漏并不会立刻引起程序崩溃，但会逐步耗尽内存，最终出现OutOfMemory异常，导致程序崩溃',
        {'例子':[
            '单例程序中，如果持有对外部对象的引用的话，那么这个外部对象是不能被回收的',
            '一些提供 close 的资源未关闭'
        ]}
    ]}
],
'GC时机':[
    {'安全点':[
        '以【是否具有让程序长时间执行的特征】为原则进行选定',
        {'可能会设置有安全点的位置':[
            '方法调用',
            '循环跳转',
            '异常跳转'
        ]},
        {'可数循环':[
            '使用int类型或范围更小的数据类型作为索引值的循环'
        ]},
        {'不可数循环':[
            '使用long或者范围更大的数据类型作为索引值的循环',
            '虚拟机为了避免安全点过多，对循环做了优化，【不可数循环】才会被放置安全点'
        ]},
        {'两种方案':[
            {'抢先式中断（目前无虚拟机采用）':[
                '所有用户线程都中断',
                '如有用户线程中断不在安全点上，恢复线程，跑到安全点上再中断'
            ]},
            {'主动式中断':{
                '设一个标志位(轮询标志与安全点重合)，线程执行过程不断轮询，标志为真自己在最近安全点中断挂起',
            }}
        ]},
    ]},
    {'安全区域':[
        {'解决问题':[
            '当程序“不执行”时，如用户线程在Sleep或Blocked，线程无法响应中断到安全点挂起自己',
            '确保在某一段代码片段之中，引用关系不会发生变化',
        ]},
        {'执行流程':[
            '1.当线程运行到Safe Region的代码时，首先标识已经进入了Safe Region',
            '如这段时间内发生GC，JVM会忽略标识为Safe Region状态的线程',
            '2.当线程即将离开Safe Region时，会检查JVM是否已经完成GC，',
            '如完成了，继续运行',
            '如没完成，线程必须等待直到收到可以安全离开Safe Region的信号为止'
        ]}
    ]}
],



}

#构建xmind
xmind.build(content,r2)

#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 