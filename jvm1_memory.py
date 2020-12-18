import xmind
from xmind.core.markerref import MarkerId
w = xmind.load("c:\\Users\\btr\\Desktop\\jvm_memory.xmind") 
s2=w.createSheet()
s2.setTitle("jvm_memory")
r2=s2.getRootTopic()
r2.setTitle("jvm_memory")


content={
'运行时数据区域':[
    {'程序计数器':[
        '当前线程 所执行字节码的 行号指示器(下一条)',
        '作用：让代码按照代码顺序执行',
        '线程私有:方便线程切换后恢复到正确的执行位置',
        {'值':[
            '执行一个Java方法：记录正在执行的虚拟机字节码指令的地址',
            '执行本地方法：值为空'
        ]},
        '唯一一个没有规定任何OutOfMemoryError情况的区域',
        'Java虚拟机的多线程实现，通过线程轮流切换并分配处理器执行时间实现',
        '任一时刻，一个处理器只会执行一条线程中的指令',
        '程序计数器可保证线程切换后恢复到正确的的执行位置'
    ]},
    {'Java虚拟机栈':[
        '线程私有',
        '方法被调->执行完毕，对应一个栈帧在虚拟机栈的入栈与出栈',
        {'栈帧':[
            {'局部变量表':[
                '编译期可知的各种基本数据类型',
                '内存空间在编译期间完成分配',
                '进入一个方法，方法在帧里分配多少空间是确定的'
            ]},
            '操作数栈',
            '动态连接/方法出口'
        ]},
        '局部变量表'
        '栈通常指虚拟机栈，或者指虚拟机栈中局部变量表'
    ]},
    {'本地方法栈':[
        '为虚拟机使用到的Native方法服务',
        'Navtive方法:Java通过JNI直接调用本地C/C++ 库',
        'StackOverFlowError：栈溢出:递归重现',
        'OutOfMemoryError:循环新增对象'
    ]},
    {'Java堆':[
        '线程共享',
        '几乎所有对象实例都在这里分配内存',
        '特例：栈上分配、标量替换'
    ]},
    {'方法区':[
        '线程共享',
        {'存储':[
            '已被虚拟机加载的类信息',
            '常量',
            '静态变量',
            '即时编译器（JIT）编译后的代码'
        ]},
        '内存回收目标：常量池的回收和对类型的卸载',
        {'运行时常量池':[
            'Class文件有类的版本、字段、方法、接口等描述信息和常量池表',
            '常量池表:存放编译期生成的各种字面量与符号引用',
            '具备动态性,运行期间可以放入新的常量'
        ]},
    ]},
    {'直接内存':[
        'NIO类，一种基于通道与缓冲区的I/O方式，Native函数库直接分配堆外内存',
        '通过一个Java堆里面的DirectByteBuffer对象作为这块内存的引用',
        '避免Java堆和Native堆来回复制数据，提高性能'
    ]}
],
'对象':[
    {'对象创建':[
        {'1.类加载检查':[
            '检查指令参数能否在常量池中定位到一个类的符号引用',
            '检查符号引用代表的类是否已被加载、解析和初始化过'
        ]},
        {'2.分配内存':[
            '内存的大小类加载后可完全确定',
            {'内存分配方式':[
                '由垃圾收集器是否带有空间压缩整理的能力决定',
                '内存绝对规整:指针碰撞',
                '内存不规整:空闲列表'
            ]},
            {'并发分配内存的解决方案':[
                'CAS+失败重试',
                '本地线程分配缓冲'
            ]},
            '分配到的内存空间（但不包括对象头）都初始化为零值'
        ]},
        '3.填充额外信息到对象头',
        '4.对象初始化，执行<init>()方法'
    ]},
    {'对象内存布局':[
        {'三部分':[
            '对象头（Header）',
            '实例数据（Instance Data）',
            '对齐填充（Padding）'
        ]},
        {'对象头':[
            '1.存储对象自身的运行时数据',
            '如哈希码（HashCode）、GC分代年龄、锁状态标志、线程持有的锁等',
            '2.类型指针，即对象指向它的类型元数据的指针',
            '可以没有'
        ]}
    ]},
    {'对象访问定位':[
        '通过栈上的reference数据来操作堆上的具体对象',
        {'两种方式':[
            {'句柄访问':[
                'Java堆中划分出一块内存来作为句柄池',
                'reference中存储对象的句柄地址',
                {'句柄包含':[
                    '对象实例数据的地址信息',
                    '类型数据的地址信息'
                ]},
                {'优势':[
                    'reference中存储的是稳定句柄地址',
                    '对象被移动时只会改变句柄中的实例数据指针'
                ]}
            ]},
            {'直接指针访问':[
                'reference中存储的是对象地址',
                '对象头存储元数据的地址信息',
                {'优势':[
                    '速度快',
                    '访问实例对象节省了一次指针定位的时间'
                ]}
            ]}
        ]}
    ]}
]

}

for key in content:
    t1 = r2.addSubTopic()
    list=key.split(":")
    t1.setTitle(list[0])
    if len(list)>1:
        t1.setPlainNotes(list[1]) 
    # print(content[key])
    for i in content[key]:
        # print(type(i))
        if(type(i).__name__=='dict'):
            for t in i:
                t2 = t1.addSubTopic()
                t2.setTitle(t)
                for j in i[t]:
                    #print(j)
                    if(type(j).__name__=='dict'):
                        for h in j:
                            t3 = t2.addSubTopic()
                            t3.setTitle(h) 
                            for m in j[h]:
                                if(type(m).__name__=='dict'):
                                    for n in m:
                                        t4 = t3.addSubTopic()
                                        t4.setTitle(n) 
                                        for l in m[n]:
                                            if(type(l).__name__=='dict'):
                                                for k in l:
                                                    t5 = t4.addSubTopic()       
                                                    t5.setTitle(k)
                                                    for p in l[k]:
                                                        if(type(p).__name__=='dict'):
                                                            for u in p:
                                                                t6 = t5.addSubTopic()
                                                                t6.setTitle(u)
                                                                for y in p[u]:
                                                                    if(type(y).__name__=='dict'):
                                                                        for a in y:
                                                                            t7 = t6.addSubTopic()
                                                                            t7.setTitle(a)
                                                                            for b in y[a]:
                                                                                t8 = t7.addSubTopic()
                                                                                t8.setTitle(b)
                                                                    else:
                                                                        t7 = t6.addSubTopic()
                                                                        t7.setTitle(y)              
                                                        else:
                                                            t6 = t5.addSubTopic()
                                                            t6.setTitle(p)                                                        
                                            else:
                                                t5 = t4.addSubTopic()
                                                t5.setTitle(l) 
                                else:
                                    t4 = t3.addSubTopic()
                                    t4.setTitle(m) 
                    else:
                        t3 = t2.addSubTopic()
                        t3.setTitle(j) 
        else:
            t2 = t1.addSubTopic()
            t2.setTitle(i) 

topics=r2.getSubTopics()
for topic in topics:
    topic.addMarker(MarkerId.starBlue)

xmind.save(w,"c:\\Users\\btr\\Desktop\\jvm.xmind") 