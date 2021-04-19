import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
xmind_name="jvm"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("GC回收区域")
r2=s2.getRootTopic()
r2.setTitle("GC回收区域")


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
            {'虚拟机栈':[
                '栈中引用的对象'
            ]},
            {'方法区':[
                '类静态属性引用的对象',
                '常量引用的对象，如字符串常量池（String Table）里的引用'
            ]},
            {'本地方法栈':[
                'JNI（即Native方法）引用的对象'
            ]},
            {'虚拟机内部':[
                '基本数据类型对应的Class对象',
                '常驻异常对象（如NullPointExcepiton）',
                '系统类加载器'
            ]},
            '同步锁（synchronized关键字）持有的对象',
            '反映Java虚拟机内部情况的JMXBean、JVMTI中注册的回调、本地代码缓存'
        ]},
        {'根节点枚举---加速':[
            'HotSpot使用一组称为【OopMap】的数据结构,减少STW(需要一致性快照)时间',
            {'类加载完成时':[
                '把对象内什么偏移量上是什么类型的数据计算出来'
            ]},
            {'即时编译过程中':[
                '在特定的位置记录下栈里和寄存器里哪些位置是引用'
            ]}
        ]}
    ]},
],
'宣告一个对象死亡(至少要经历两次标记过程)':[
    '1.标记GC Roots不可达对象,进行第一次标记',
    '2.筛选对象是否可执行finalize()方法，将对象放置在F-Queue的队列中',
    '3.由低调度优先级的Finalizer线程去执行它们的finalize()方法',
    '4.收集器将对F-Queue中的对象进行第二次小规模的标记',
    '注：finalize()是对象逃脱死亡命运的最后一次机会'
]


}

#构建xmind
xmind.build(content,r2)

#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 