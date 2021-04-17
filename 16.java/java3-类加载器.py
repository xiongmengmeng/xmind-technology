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
    {'作用':[
        '通过一个类的全限定名来获取描述此类的二进制字节流'
    ]},
    {'实现环境':[
        'Java虚拟机外部实现，以便让应用程序自己决定如何去获取所需要的类'
    ]},
    {'类在Java虚拟机中的唯一性':[
        '由加载它的类加载器+类本身共同确立'
    ]},
    '每一个类加载器，都拥有一个独立的类名称空间'
],
'三种类加载器':[
    {'BootstrapClassLoader---启动类类加载器':[
        '加载<JAVA_HOME>/jre/lib路径',
        'C++语言实现，虚拟机自身的一部分'
    ]},
    {'ExtClassLoader---拓展类类加载器':[
        '加载<JAVA_HOME>/jre/lib/ext路径以及java.ext.dirs系统变量指定的类路径下的类',
        'Java语言实现',
        '继承自抽象类java.lang.ClassLoader',
        '独立存在于虚拟机外部'
    ]},
    {'AppClassLoader---应用程序类类加载器':[
        '加载应用程序ClassPath下的类（包含jar包中的类）',
        'java应用程序默认的类加载器'
    ]},
    {'其它':[
        {'自定义ClassLoader':[
            '继承ClassLoader类，后覆盖findClass（String name）方法',
            '注意parent需自己设置，可以放在构造函数中',
            {'没有继承AppClassLoader原因':[
                'AppClassLoader和ExtClassLoader都是Launcher的内部类，都是包访问路径权限'
            ]}
        ]},
        {'ThreadContextClassLoader':[
            '线程上下文加载器',
            '不是一个新的类型，更像一个类加载器的角色',
            '可以是上述类加载器的任意一种，通常是AppClassLoader'
        ]},
        '自定义：解密加密后的.class文件，防止代码被反编译'
    ]}
],
'类加载器的加载':[
    '1.虚拟机启动的时候会初始化BootstrapClassLoader',
    '2.然后在Launcher类(JRE中用于启动程序入口main()的类)中加载ExtClassLoader、AppClassLoader',
    '3.并将AppClassLoader的parent设置为ExtClassLoader,并设置线程上下文类加载器',
    'ExtClassLoader没有设置parent:BootstrapClassLoader是由c++实现的，并不存在一个Java的类'
],
# '双亲委派模型':[
#     'Java一直保持着三层类加载器、双亲委派的类加载架构',
#     {'要求':[
#         '除了顶层的启动类加载器外，其余的类加载器都应有自己的父类加载器',
#         '类加载器之间的父子关系不以继承，而是使用【组合关系】来复用父加载器的代码'
#     ]},
#     {'工作过程':[
#         '当一个类加载器去加载类时先尝试让父类加载器去加载',
#         '如果父类加载器加载不了再尝试自身加载',
#         '保证基础类仅加载一次，不会让jvm中存在重名的类'
#     ]},
#     {'优点':[
#         'Java中的类随着它的类加载器一起具备了一种带有优先级的层次关系'
#     ]},
#     {'破坏模型':[
#         {'JDBC4.0后,用spi方式注册Driver':[
#             'Connection connection = DriverManager.getConnection("jdbc://localhost:3306")',
#             {'加载DriverManager类时，会执行静态块':[
#                 'static {',
#                 '   loadInitialDrivers();',
#                 '   println("JDBC DriverManager initialized");',
#                 '}',
#             ]},
#             {'loadInitialDrivers()':[
#                 '内调用Class.forName("com.mysql.jdbc.Driver")',
#                 'ServiceLoader在java.util下面，使用BootstrapClassLoader，无法加载com.mysql.jdbc包下的类',
#                 {'使用下面的方式更换类加载器':[
#                     'ClassLoader cl = Thread.currentThread().getContextClassLoader();',
#                     'return ServiceLoader.load(service, cl)',
#                 ]}
#             ]},
#             {'总结':[
#                 {'DriverManager':[
#                     '启动类加载器加载'
#                 ]},
#                 {'Driver':[
#                     '应用类加载器加载'
#                 ]},
#                 {'解决':[
#                     '使用Thread.currentThread().getContextClassLoader()，获得上下文类加载器',
#                     '线程上下文类加载器让父级类加载器通过调用子级类加载器来加载类，打破了双亲委派模型原则'
#                 ]}
#             ]}
#         ]},
#         {'热部署':[
#             '销毁自定义classloader(被该加载器加载的class也会自动卸载)',
#             '更新class',
#             '使用新的ClassLoader去加载class'
#         ]},
#         {'自定义类加载器':[
#             '符合双亲委派规范，重写findClass方法（用户自定义类加载逻辑）',
#             '破坏:重写loadClass方法(双亲委派的具体逻辑实现)'
#         ]},
#         # 'https://blog.csdn.net/yusimiao/article/details/99301293'
#         ]}
#     ]}
# ]

}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 