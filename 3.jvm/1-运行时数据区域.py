import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="jvm"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("运行时数据区域")
r2=s2.getRootTopic()
r2.setTitle("运行时数据区域")


content={
'程序计数器':[
    '当前线程 所执行字节码的 行号指示器(下一条)',
    {'作用':[
        '让程序按照代码顺序执行',
    ]},
    {'线程私有':[
        '方便线程切换后恢复到正确的执行位置',
        '多线程实现是通过线程轮流切换并分配处理器执行时间实现的',
        {'CPU资源分配————时间片轮转策略':[
            '给每个线程分配一个时间片，线程在时间片内占用CPU,执行任务'
        ]},
        {'线程上下文切换时机':[
            '1.当前线程CPU时间片用完处于就绪状态',
            '2.当前线程被其他线程中断'
        ]}
    ]},
    {'值':[
        {'执行一个Java方法':[
            '记录正在执行的虚拟机字节码指令的地址'
        ]},
        {'执行本地方法':[
            '值为空'
        ]}
    ]},
    '唯一一个没有规定任何OutOfMemoryError情况的区域',
],
'Java虚拟机栈':[
    '线程私有',
    '方法被调用->执行完毕，对应一个栈帧在虚拟机栈的入栈与出栈',
    {'栈帧':[
        {'局部变量表':[
            '编译期可知的各种基本数据类型',
            '内存空间在编译期间完成分配',
            '进入一个方法，方法在帧里分配多少空间是确定的'
        ]},
        '操作数栈',
        '动态连接/方法出口'
    ]}
],
'本地方法栈':[
    '为虚拟机使用到的Native方法(Java通过JNI直接调用本地C/C++库)服务',
    {'StackOverFlowError':[
        '栈溢出:递归重现'
    ]},
    {'OutOfMemoryError':[
        '循环新增对象'
    ]}
],
'Java堆':[
    '线程共享,几乎所有对象实例都在这里分配内存',
    {'特例':[
        '栈上分配、标量替换'
    ]}
],
'方法区':[
    '线程共享',
    {'存储':[
        '已被虚拟机加载的类信息',
        '常量',
        '静态变量',
        '即时编译器（JIT）编译后的代码'
    ]},
    {'内存回收目标':[
        '常量池的回收和对类型的卸载'
    ]},
    {'运行时常量池':[
        'Class文件有类的版本、字段、方法、接口等描述信息和常量池表',
        {'常量池表':[
            '存放编译期生成的各种字面量与符号引用'
        ]},
        '具备动态性,运行期间可以放入新的常量'
    ]},
],
'直接内存':[
    {'NIO类':[
        '一种基于通道与缓冲区的I/O方式',
        'Native函数库直接分配堆外内存'
    ]},
    '通过一个Java堆里面的DirectByteBuffer对象作为这块内存的引用',
    '避免Java堆和Native堆来回复制数据，提高性能'
]


}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 