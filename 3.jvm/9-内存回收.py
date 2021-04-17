import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
xmind_name="jvm"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("内存回收")
r2=s2.getRootTopic()
r2.setTitle("内存回收")


content={

'方法或者线程结束，自然回收':[
    '程序计数器',
    '虚拟机栈',
    '本地方法栈'
],
'方法区回收':[
    '废弃的常量:没有对象引用时回收',
    {'不再使用的类型':[
        '类所有的实例都已经被回收',
        '加载该类的类加载器已经被回收',
        '类对应的Class对象没有被引用，无法通过反射访问'
    ]},
    '满足条件的类型，只是允许回收，是否能回收看配置'
],
'对象回收':[
    {'引用计数法':[
        '对象被引用一次，计数器值+1',
        '引用失效，计数器值-1',
        '计数器为0的对象不再被使用',
        '问题：相互引用'
    ]},
    {'可达性分析法':[
        'GC Roots到对象不可达，对象不再被使用',
        {'GC Roots的对象':[
            '虚拟机栈中引用的对象',
            '方法区中类静态属性引用的对象',
            '方法区中常量引用的对象，如字符串常量池（String Table）里的引用',
            '本地方法栈中JNI（即Native方法）引用的对象',
            {'虚拟机内部的引用':[
                '基本数据类型对应的Class对象',
                '常驻异常对象（如NullPointExcepiton）',
                '系统类加载器'
            ]},
            '同步锁（synchronized关键字）持有的对象',
            '反映Java虚拟机内部情况的JMXBean、JVMTI中注册的回调、本地代码缓存'
        ]}
    ]},
    {'四种引用':[
        {'强引用（StronglyReference）':[
            '垃圾收集器永远不会回收掉被引用的对象'
        ]},
        {'软引用（Soft Reference）':[
            '还有用，但非必须的对象',
            '发生内存溢出前，进行回收',
            '对象列进回收范围之中进行第二次回收',
            'SoftReference类来实现'
        ]},
        {'弱引用（Weak Reference）':[
            '非必须对象',
            '弱引用关联的对象只生存到下一次垃圾收集发生为止',
            'WeakReference类来实现',
            'ThreaLocal中的map，继承弱引用WeakReference，防止map中的key引用的对象无法被回收'
        ]},
        {'虚引用（Phantom Reference）':[
            '对象是否有虚引用，不对其生存时间构成影响，不能通过虚引用取得对象实例',
            {'存在目的':[
                '对象被收集器回收时收到一个系统通知'
            ]},
            'PhantomReference类来实现'
        ]}
    ]},
    {'宣告一个对象死亡':[
        '1.标记GC Roots不可达对象',
        '2.筛选对象是否可执行finalize()方法，将对象放置在F-Queue的队列中',
        '3.由低调度优先级的Finalizer线程去执行它们的finalize()方法',
        '4.收集器将对F-Queue中的对象进行第二次小规模的标记',
        '注：finalize()是对象逃脱死亡命运的最后一次机会'
    ]}
]


}

#构建xmind
xmind.build(content,r2)

#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 