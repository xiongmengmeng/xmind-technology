import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="java"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("ProxyClassFactory工厂类")
r2=s2.getRootTopic()
r2.setTitle("ProxyClassFactory工厂类")


content={
'Class<?> apply(ClassLoader loader, Class<?>[] interfaces)':[
    {'1.确定代理类名称前缀':[
        '$Proxy'
    ]},
    {'2.用原子类来生成代理类的序号':[
    ]},
    {'3.遍历interfaces数组进行验证':[
        'intf是否可以由指定的类加载进行加载',
        'intf是否是一个接口',
        'intf在数组中是否有重复'
    ]},
    {'4.得出代理类的全限定名':[
        '包名+前缀+序号, 如：com.sun.proxy.$Proxy0'
    ]},
    {'5.用ProxyGenerator来生成字节码':[
        'ProxyGenerator.generateProxyClass(proxyName,interfaces, accessFlags)'
    ]},
    {'6.根据二进制文件生成相应的Class实例':[
        'defineClass0(loader, proxyName, proxyClassFile, 0, proxyClassFile.length)'
    ]}
],
'ProxyGenerator来生成字节码':[
    '1.收集要生成的代理方法，将其包装成ProxyMethod对象并注册到Map集合中',
    '2.收集要为Class文件生成的字段信息和方法信息',
    {'详细':[
        '1.为代理类生成一个带参构造器，传入InvocationHandler实例的引用并调用父类的带参构造器',
        'protected Proxy0(InvocationHandler h) {',
        '   super(h);',
        '}',
        '2.遍历代理方法Map集合，为每个代理方法生成对应的Method类型静态域，并将其添加到fields集合中',
        '3.遍历代理方法Map集合，为每个代理方法生成对应的MethodInfo对象，并将其添加到methods集合中',
        'public boolean equals(Object obj) {',
        '  try {',
        '      Object[] args = new Object[] {obj};',
        '      return (boolean) h.invoke(this, m2, args);',
        '   } catch (Throwable e) {',
        '      throw new UndeclaredThrowableException(e);',
        '   }',
        ' }',
        '4.为代理类生成静态初始化方法，该静态初始化方法主要是将每个代理方法的引用赋值给对应的静态字段'
    ]},
    '3.完成了上面的工作后，开始组装Class文件',
]

}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 