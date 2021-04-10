import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="thread"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("lock_cas")
r2=s2.getRootTopic()
r2.setTitle("CAS")


content={

'定义':[
    'Compare And Swap（比较与交换）',
    '本质：冲突检查+数据更新，无锁算法',
],
'三个操作数':[
    '内存位置（V）',
    '预期原值（A）',
    '新值（B）'
],
'过程':[
    '1.如内存位置V的值与预期原值A匹配,',
    '2.处理器将该位置值更新为新值B',
    '3.否则处理器不做任何操作',
    '4.无论哪种情况，均返回CAS指令前该位置的值',
    {'本质':[
        '借助一个CPU指令完成，属原子操作'
    ]}
],
'效果':[
    '多线程尝试使用CAS同时更新同一个变量，只有一个线程能更新成功',
    '其他线程失败，失败线程不会被挂起，可再次尝试'
],
'存在问题':[
    {'1.ABA':[
        '在变量前加版本号，每次变量更新把版本号加一',
        '实现类：AtomicStampedReference'
    ]},
    '2.循环时间长(一直自旋)开销大',
    {'3.只能保证一个共享变量的原子操作':[
        'AtomicReference类保证引用对象间的原子性',
        '把多变量放在一个对象里来进行CAS操作'
    ]}
],
'扩展':[
    'JDK1.5中新增java.util.concurrent包建立在CAS之上',
    '如AtomicInteger，注:value用volatile修饰，保证可见性'
],
'Unsafe类---CAS的实现类':[
    '类中方法都是native方法，使用JNI方式访问本地C++实现库(提供硬件级别的原子性操作)',
    {'native方法---本地方法':[
        '保存在动态链接库中，即.dll(windows系统)文件中，格式是各个平台专有的'
    ]},
    {'JNI---Java Native Interface':[
        '提供了若干的API实现Java与其它语言的通信'
    ]},
    {'重要方法':[
        {'获得变量地址':[
            'long objectFieldOffset（Field field）',
            '变量在所属类中的内存偏移地址'
        ]},
        {'给变量设值':[
            'long getAndSetLong（Object obj, long offset, long update）',
            '获取对象obj中偏移量为offset的变量volatile语义的当前值,并设置变量volatile语义的值为update',
        ]},
        {'CAS实现方法':[
            'boolean compareAndSwapLong（Object obj, long offset, long expect, long update）',
            '比较对象obj中偏移量为offset的变量值是否与expect相等,相等则使用update值更新，成功返回true',
        ]},

    ]}
]

}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 