import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="java"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("类加载器")
r2=s2.getRootTopic()
r2.setTitle("类加载器")


content={
'类加载器':[
    '通过一个类的全限定名来获取描述此类的二进制字节流',
    '这个动作放到Java虚拟机外部实现',
    '以便让应用程序自己决定如何去获取所需要的类',
    '实现这个动作的代码模块称为“类加载器”'
],
'类加载器种类，各自职责，关系':[
    {'三种类加载器':[
        {'BootstrapClassLoader':[
            '启动类类加载器',
            '加载<JAVA_HOME>/jre/lib路径',
            '由c++实现'
        ]},
        {'ExtClassLoader':[
            '拓展类类加载器',
            '加载<JAVA_HOME>/jre/lib/ext路径以及java.ext.dirs系统变量指定的类路径下的类'
        ]},
        {'AppClassLoader':[
            '应用程序类类加载器',
            '加载应用程序ClassPath下的类（包含jar包中的类）',
            'java应用程序默认的类加载器'
        ]}
    ]},
    {'其它':[
        {'用户自定义类加载器':[
            '用户根据自定义需求，自由的定制加载的逻辑',
            '继承AppClassLoader，仅仅覆盖findClass（）即将继续遵守双亲委派模型'
        ]},
        {'ThreadContextClassLoader':[
            '线程上下文加载器',
            '不是一个新的类型，更像一个类加载器的角色',
            '可以是上述类加载器的任意一种，通常是AppClassLoader'
        ]}
    ]},
    {'类加载器的加载':[
        '1.在虚拟机启动的时候会初始化BootstrapClassLoader',
        '2.然后在Launcher类(JRE中用于启动程序入口main()的类)中去加载ExtClassLoader、AppClassLoader',
        '3.并将AppClassLoader的parent设置为ExtClassLoader,并设置线程上下文类加载器',
        'ExtClassLoader没有设置parent:BootstrapClassLoader是由c++实现的，并不存在一个Java的类'
    ]},
    {'遵循双亲委派模型':[
        '当一个类加载器去加载类时先尝试让父类加载器去加载',
        '如果父类加载器加载不了再尝试自身加载',
        '保证基础类仅加载一次，不会让jvm中存在重名的类'
    ]},
    {'破坏了双亲委派模型的情况':[
        {'jdbc':[
            'jdk1.6后加载驱动:Connection connection = DriverManager.getConnection("jdbc://localhost:3306")--BootstrapClassLoader加载的类',
            '方法内调用Class.forName("com.mysql.jdbc.Driver")--ThreadContextClassLoader加载的类'
        ]}
    ]}
],
'自定义ClassLoader':[
    '继承ClassLoader类，后覆盖findClass（String name）方法',
    '注意parent需自己设置，可以放在构造函数中',
    {'没有继承AppClassLoader原因':[
        'AppClassLoader和ExtClassLoader都是Launcher的内部类，都是包访问路径权限'
    ]}
],
'ServiceLoader.load原理':[
    '1.String fullName=PREFIX+service.getName():前缀+要查找的类的全限定名 ',
    '2.configs=loader.getResources(fullName):使用ClassLoader的getResource方法查询资源',
    '备：PREFIX = "META-INF/services/"'
],
'SPI机制':[
    'Service Provider Interface:服务提供接口,jdk内置的一种服务发现机制',
    '核心就是ClassLoader的getResource系列方法',
    'jdk提供了一个工具类:ServiceLoader',
    'Spring实现了自己的SPI机制:SpringFactoriesLoader'
]
}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 