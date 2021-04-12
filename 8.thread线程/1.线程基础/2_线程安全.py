import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) 
sys.path.insert(0,parentdir) 


import xmind
xmind_name="thread"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("线程安全")
r2=s2.getRootTopic()
r2.setTitle("线程安全")


content={
'定义':[
    {'多线程【同时】访问【一个对象】':[
        '不考虑线程在运行时环境下的调度和交替执行',
        '不需进行额外的同步',
        '不需调用方进行任何其他的协调操作',
    ]},
    '调用对象的行为都可获得正确结果'
],
'程度分类(5类)':[
    {'不可变':[
        '一定是线程安全',
        '方法实现或方法的调用者，均不需进行任何线程安全保障措施',
        '对象：其行为(方法)不会对其状态(成员变量)产生影响',
        {'途径':[
            '把对象的成员变量声明为final',
            '对象的成员变量是基本数据类型，声明为final'
        ]}
    ]},
    {'绝对线程安全':[
        'Java API中标注线程安全的类，大多都不是绝对线程安全',
        '如java.util.Vector'
    ]},
    {'相对线程安全':[
        '对对象单次操作是线程安全的，调用时不需额外保障措施',
        '对连续调用，调用端要使用额外同步手段',
        '如Vector、HashTable等'
    ]},
    {'线程兼容':[
        '对象本身并不是线程安全的，调用端可使用同步手段保证其并发安全',
        'ArrayList和HashMap'
    ]},
    {'线程对立':[
        '调用端是否采取措施，都无法在多线程环境中并发使用',
        'System.setIn()、Sytem.setOut()和System.runFinalizersOnExit()等'
    ]}
],
'原子性、可见性与有序性':[
    {'原子性':[
        'read、load、assign、use、store和write六个',
        '基本数据类型访问、读写都具备原子性',
        '更大范围原子性保证:lock和unlock'
    ]},
    {'可见性':[
        '实现可见性的关键字：synchronized，final和volatile',
        {'synchronized':[
            '对变量执行unlock操作前，须先把此变量同步回主内存中'
        ]},
        {'final':[
            '字段在构造器中一旦被初始化完成，其他线程中就能看见final字段的值'
        ]},
        {'volatile':[
            '新值能立即同步到主内存，以及每次使用前立即从主内存刷新'
        ]}
    ]},
    {'有序性':[
        '在本线程内观察，所有操作都是有序的:线程内似表现为串行',
        '在A线程中观察B线程，所有操作都是无序的:指令重排序和工作内存与主内存同步延迟'
    ]}
],
'线程安全实现方法':[
    '互斥同步',
    '非阻塞同步',
    '无同步方案'
]



}

#构建xmind
xmind.build(content,r2)

#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 