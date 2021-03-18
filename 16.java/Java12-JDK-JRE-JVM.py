import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="java"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("JDK-JRE-JVM")
r2=s2.getRootTopic()
r2.setTitle("JDK-JRE-JVM")


content={
'Oracle有两个Java平台标准的产品，Java SE 开发工具包(JDK) 和 Java SE 运行时环境(JRE)':[
],
'JDK':[
    'Java Development Kit:Java开发工具包',
    '提供给Java开发人员使用的，包含java开发工具和JRE',
    {'目录结构和作用':[
        {'bin':[
            '一堆EXE可执行文件',
            'java.exe:运行工具，运行.class 的字节码',
            'javac.exe:编译工具，将.java的源代码编译成为.class的字节码',
            'jar.exe:打包工具',
            'javap.exe: 反编译程序'
        ]},
        {'db':[
            '内置Derby数据库，体积小，免安装'
        ]},
        {'include':[
            'Java和JVM交互的头文件',
            '如JVMTI写C++工程时，需把这个include包引入进jvmti.h'
        ]},
        {'jre':[
            'Java运行环境,包含了运行时需要的可执行文件',
            '以及运行时需要依赖的 Java 类库和动态链接库 .so .dll .dylib'
        ]},
        {'lib':[
            'Java 类库，如dt.jar、tools.jar',
        ]}
    ]}
],
'JRE':[
    'Java Runtime Environment:Java运行环境',
    'JDK 的子集',
    '提供了库、Java 虚拟机（JVM）和其他组件，用于运行Java编程语言、小程序、应用程序',
    {'作用':[
        '一个运行在 CPU 上的程序，用于解释执行 Java 代码'
    ]},
    {'目录结构和作用':[
        'bin：有java.exe但无javac.exe(无法编译Java程序，但可运行Java程序)',
        'lib：Java基础&核心类库，包含JVM 运行时需要的类库和rt.jar',
    ]}
],
'JVM':[
    'Java Virtual Machine:Java虚拟机',
    '可理解为一个虚拟出来的计算机，具备基本运算方式:',
    '把Java程序生成的字节码文件，解释成具体系统平台上的机器指令，让其在各个平台运行',
    '是一种规范，各个供应商都可以实现自己 JVM虚拟机',
    {'两种启动模式':[
        'Client模式：加载速度较快,可用于运行GUI交互程序',
        'Server模式：加载速度较慢但运行起来较快,可用于运行服务器后台程序'
    ]},
    'jvm.dll:在jre\bin\server目录下，解释class文件时需要调用jre\lib下类库'
]
}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 