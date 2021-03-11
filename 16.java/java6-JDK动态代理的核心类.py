import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="java"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("JDK动态代理的核心类")
r2=s2.getRootTopic()
r2.setTitle("JDK动态代理的核心类")


content={

'JDK动态代理有两大核心类，它们都在Java的反射包下（java.lang.reflect）':[],
'InvocationHandler':[
    '每一个代理实例都要有一个关联的InvocationHandler',
    '调用代理实例的方法时，会被转到InvocationHandler的invoke方法上',
    {'作用':[
        '用于方法调用的约束与增强'
    ]},
    {'Object invoke(Object proxy, Method method, Object[] args)':[
        '作用：处理代理实例上的方法调用并返回结果'
    ]}
],
'Proxy':[
    '创建动态代理类及其实例',
    '是动态代理类的超类',
    {'作用':[
        '获取动态代理对象'
    ]},
    {'Proxy(InvocationHandler h)':[
        '构造函数',
        '接受一个参数:接口InvocationHandler的实现',
        '作用：用于设置代理实例的调用处理器'
    ]},
    {'Class<?> getProxyClass(ClassLoader loader, Class<?>... interfaces)':[
        '返回代理Class对象',
        '本质：以Class造Class',
        '1.从传入的接口Class中，“拷贝”类结构信息到一个新的Class对象中',
        '2.但新的Class对象带有构造器，可以创建对象'
    ]},
    {'Object newProxyInstance(ClassLoader loader,Class<?>[] interfaces,InvocationHandler h)':[
        {'参数':[
            '目标类的类加载器',
            '目标类实现的接口集合',
            'InvocationHandler实例'
        ]},
        {'返回值':[
            '一个Object类型的代理类'
        ]},
        {'具体':[
            {'1.Class<?>[] intfs = interfaces.clone()':[
                '复制代理类实现的所有接口'
            ]},
            {'2.Class<?> cl = getProxyClass0(loader, intfs)':[
                '先通过类加载器和接口集合去缓存里获取，如能找到代理类就直接返回',
                '否则调用ProxyClassFactory这个工厂去生成一个代理类'
            ]},
            {'3.Constructor<?> cons = cl.getConstructor(constructorParams)':[
                '获取参数类型是InvocationHandler.class的代理类构造器'
            ]},
            {'4.cons.newInstance(new Object[]{h})':[
                '传入InvocationHandler实例去构造一个代理类的实例',
                '代理类都继承自Proxy, 这里会调用Proxy的构造器将InvocationHandler引用传入'
            ]}
        ]}
    ]},
    {'ProxyClassFactory':[
        '静态内部类',
        '作用：生成静态代理',
        {'ProxyGenerator.generateProxyClass':[
            '用来生成代理类的.class文件'
        ]},
        {'defineClass0':[
            '一个native方法，负责字节码加载的实现，并返回对应的Class对象'
        ]}
    ]}
]


}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 