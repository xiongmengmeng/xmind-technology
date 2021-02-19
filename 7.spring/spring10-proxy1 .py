import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="spring"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("JDK动态代理")
r2=s2.getRootTopic()
r2.setTitle("JDK动态代理(上)")


content={
'代理模式':[
    '实现：Java中有静态代理和动态代理',
    '静态代理:代理对象直接持有目标对象的引用',
    {'动态代理':[
        '优点：代理类可作用于多个目标对象，代理对象和目标对象松耦合',
        {'JDK动态代理缺点':[
            '实现比静态代理更加复杂',
            '存在一定限制，如要求需代理的对象必须实现某个接口',
            '不够灵活，会为接口中声明的所有方法添加上相同的代理逻辑'
        ]}
    ]},
],
'JDK动态代理实现机制':[
    'Proxy类的静态方法:',
    'Object newProxyInstance(ClassLoader loader,Class<?>[] interfaces,InvocationHandler h)',
    {'参数':[
        '目标类的类加载器',
        '目标类实现的接口集合',
        'InvocationHandler实例'
    ]},
    {'返回值':[
        '一个Object类型的代理类'
    ]},
    {'具体':[
        '1.Class<?>[] intfs = interfaces.clone():',
        '复制代理类实现的所有接口',
        '2.Class<?> cl = getProxyClass0(loader, intfs):',
        '先从缓存获取代理类, 如果没有再去生成一个代理类',
        '3.Constructor<?> cons = cl.getConstructor(constructorParams):',
        '获取参数类型是InvocationHandler.class的代理类构造器',
        '4.cons.newInstance(new Object[]{h})：',
        '传入InvocationHandler实例去构造一个代理类的实例',
        '代理类都继承自Proxy, 这里会调用Proxy的构造器将InvocationHandler引用传入',
    ]},
    {'getProxyClass0':[
        '通过类加载器和接口集合去缓存里获取，如能找到代理类就直接返回',
        '否则调用ProxyClassFactory这个工厂去生成一个代理类'
    ]}
],
'java两种代理方式':[
    'JDK动态代理：借助Proxy,InvocationHandler',
    'CGLIB动态代理：借助Enhancer,MethodInterceptor'
],
'https://www.cnblogs.com/liuyun1995/p/8144628.html':[]
}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 