import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
xmind_name="jvm"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("jvm总结-内存模型")
r2=s2.getRootTopic()
r2.setTitle("jvm总结-内存模型")


content={

'运行时数据区域':[
    '程序计数器',
    'Java虚拟机栈',
    '本地方法栈',
    'Java堆',
    '方法区',
    '直接内存'
],
'对象':[
    {'对象创建':[
        '类加载检查',
        '分配内存',
        '填充额外信息到对象头',
        '对象初始化，执行<init>()方法',
        '在栈中新建对象引用，并将其指向堆中新建的对象实例'
    ]},
    {'对象内存布局':[
        '对象头（Header）',
        '实例数据（Instance Data）',
        '对齐填充（Padding）'
    ]},
    {'对象访问定位':[
        '句柄访问',
        '直接指针访问'
    ]},
    {'四种引用':[
        '强引用（StronglyReference）',
        '软引用（Soft Reference）',
        '弱引用（Weak Reference）',
        '虚引用（Phantom Reference）'
    ]},
]





}

#构建xmind
xmind.build(content,r2)

#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 