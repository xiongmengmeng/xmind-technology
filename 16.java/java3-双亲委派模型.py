import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="java"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("双亲委派模型")
r2=s2.getRootTopic()
r2.setTitle("双亲委派模型")


content={

'Java一直保持着三层类加载器、双亲委派的类加载架构':[],
'要求':[
    '除了顶层的启动类加载器外，其余的类加载器都应有自己的父类加载器',
    '类加载器之间的父子关系不以继承，而是使用【组合关系】来复用父加载器的代码'
],
'工作过程':[
    '当一个类加载器去加载类时先尝试让父类加载器去加载',
    '如果父类加载器加载不了再尝试自身加载',
    '保证基础类仅加载一次，不会让jvm中存在重名的类'
],
'优点':[
    'Java中的类随着它的类加载器一起具备了一种带有优先级的层次关系'
],
'破坏模型':[
    {'JDBC4.0后,用spi方式注册Driver':[
        'Connection connection = DriverManager.getConnection("jdbc://localhost:3306")',
        {'加载DriverManager类时，会执行静态块':[
            'static {',
            '   loadInitialDrivers();',
            '   println("JDBC DriverManager initialized");',
            '}',
        ]},
        {'loadInitialDrivers()':[
            '内调用Class.forName("com.mysql.jdbc.Driver")',
            'ServiceLoader在java.util下面，使用BootstrapClassLoader，无法加载com.mysql.jdbc包下的类',
            {'使用下面的方式更换类加载器':[
                'ClassLoader cl = Thread.currentThread().getContextClassLoader();',
                'return ServiceLoader.load(service, cl)',
            ]}
        ]},
        {'总结':[
            {'DriverManager':[
                '启动类加载器加载'
            ]},
            {'Driver':[
                '应用类加载器加载'
            ]},
            {'解决':[
                '使用Thread.currentThread().getContextClassLoader()，获得上下文类加载器',
                '线程上下文类加载器让父级类加载器通过调用子级类加载器来加载类，打破了双亲委派模型原则'
            ]}
        ]}
    ]},
    {'热部署':[
        '销毁自定义classloader(被该加载器加载的class也会自动卸载)',
        '更新class',
        '使用新的ClassLoader去加载class'
    ]},
    {'自定义类加载器':[
        '符合双亲委派规范，重写findClass方法（用户自定义类加载逻辑）',
        '破坏:重写loadClass方法(双亲委派的具体逻辑实现)'
    ]},
    # 'https://blog.csdn.net/yusimiao/article/details/99301293'
]


}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 