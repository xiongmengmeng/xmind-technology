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

'Service Provider Interface':[
    '服务提供接口,jdk内置的一种服务动态扩展机制',
    {'实现类':[
        'java的spi机制:ServiceLoader',
        'spring的SPI机制:SpringFactoriesLoader'
    ]},
    {'目的':[
        '解耦'
    ]},
    {'一种规则':[
        '1.META-INF/services/下',
        '2.创建文件：文件名为binary name(接囗，抽象类的全量限定名)',
        '3.文件内容：实现类的全是限定名',
        {'4.使用:ServiceLoader.load(A.class)':[
            '4.1.ServiceLoader中定义了变量="META-INF/services/"',
            '4.2.class.getClassName:定位文件',
            '4.3.ServiceLoader实现Iterable接囗，可遍历文件，拿到类的全量限定名',
            '4.4.反射加载类',
        ]}
    ]}
],
'ServiceLoader':[
    '实现了Iterable接口，注意iterator()方法的实现',
    'ServiceLoader依赖于类加载器实例进行类加载，核心属性LazyIterator是就是用来实现iterator()方法的',
    {'参数':[
        'PREFIX = "META-INF/services/":需要加载的资源的路径的目录',
        'Class<S> service:ServiceLoader需要加载的类或者接口',
        'ClassLoader loader:进行类加载的时候使用的类加载器引用',
        'LazyIterator lookupIterator:"懒查找"迭代器，ServiceLoader的核心',
    ]},
    {'构造器':[
        'private ServiceLoader(Class<S> svc, ClassLoader cl)',
        '1、判断传入的接口或者类的Class实例不能为null，否则抛异常',
        '2、如果传入的ClassLoader实例为null，使用应用类加载器(Application ClassLoader)',
        '3、实例化访问控制上下文',
        '4、调用实例方法reload()，清空目标加载类的实现类实例的缓存并且构造LazyIterator实例'
    ]},
    {'静态方法':[
        'static <S> ServiceLoader<S> load(Class<S> service)',
        '构造ServiceLoader实例:调用ServiceLoader的私有构造器进行实例化'
    ]},
    {'iterator()':[
        {'hasNext()和next()':[
            '优先判断缓存中是否已经存在实现类的实例',
            '如存在则直接从缓存中返回，否则调用懒加载迭代器LazyIterator的实例去获取'
        ]},
        {'LazyIterator':[
            '一个Iterator接口的实现，是ServiceLoader的一个私有内部类',
            {'hasNextService()':[
                '查询实现类的全是限定名',
                '1.String fullName=PREFIX+service.getName():前缀+要查找的类的全限定名',
                '2.configs=loader.getResources(fullName):使用ClassLoader的getResource方法查询资源'
            ]},
            {'nextService()':[
                '反射创建类，创建实例'
            ]}
        ]}
    ]}
]
}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 