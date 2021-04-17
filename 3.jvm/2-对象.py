import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="jvm"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("对象")
r2=s2.getRootTopic()
r2.setTitle("对象")


content={
'对象创建':[
    {'1.类加载检查':[
        '检查指令参数能否在常量池中定位到【一个类的符号引用】',
        '检查【符号引用代表的类】是否已被加载、解析和初始化过',
        '如果没有，则先进行【类加载】过程'
    ]},
    {'2.分配内存':[
        {'内存的大小':[
            '类加载后可完全确定'
        ]},
        {'内存分配方式':[
            '由垃圾收集器是否带有【空间压缩整理】的能力决定',
            {'内存绝对规整':[
                '指针碰撞'
            ]},
            {'内存不规整':[
                '空闲列表'
            ]}
        ]},
        {'并发分配内存的解决方案':[
            'CAS+失败重试',
            '本地线程分配缓冲'
        ]},
        '分配到的内存空间（不包括对象头）都初始化为零值'
    ]},
    '3.填充额外信息到对象头',
    {'4.对象初始化，执行<init>()方法':[
        '统一赋值对象的属性'
    ]},
    '5.在栈中新建对象引用，并将其指向堆中新建的对象实例'
],
'对象内存布局(三部分)':[
    {'对象头（Header）':[
        {'1.存储对象自身的运行时数据':[
            '如哈希码（HashCode）、GC分代年龄、锁状态标志、线程持有的锁等'
        ]},
        {'2.类型指针':[
            '即对象指向它的类型元数据的指针，可没有'
        ]}
    ]},
    '实例数据（Instance Data）',
    '对齐填充（Padding）'
],
'Person类调用过程':[
    '1.JVM去方法区寻找Person类信息',
    '2.如找不到，Classloader加载Person类信息进内存方法区',
    '3.堆内存中创建Person对象，并持有方法区中Person类的引用',
    '4.person添加到执行main()方法的主线程java调用栈中，指向堆中的内存对象',
    '5.执行person.sayHello()，JVM根据person定位到堆空间的Person实例',
    '6.根据Person实例定位到方法区Person类型信息，获得sayHello()字节码，执行'
],
'对象访问定位':[
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
]


}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 