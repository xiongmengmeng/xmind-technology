import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="interview"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("aop")
r2=s2.getRootTopic()
r2.setTitle("aop")


content={
'spring 有哪些主要模块':[
    {'Spring Core':[
        'Core模块是Spring的核心类库',
        'Spring的所有功能都依赖于该类库，Core主要实现IOC功能，Sprign的所有功能都是借助IOC实现的'
    ]},
    {'AOP':[
        'AOP模块是Spring的AOP库，提供了AOP（拦截器）机制，并提供常用的拦截器，供用户自定义和配置'
    ]},
    {'ORM':[
        'Spring 的ORM模块提供对常用的ORM框架的管理和辅助支持',
        'Spring支持常用的Hibernate，ibtas，jdao等框架，Spring并不对ORM进行实现，仅对常见的ORM框架进行封装，并对其进行管理'
    ]},
    {'DAO模块':[
        'Spring 提供对JDBC的支持，对JDBC进行封装，允许JDBC使用Spring资源，并能统一管理JDBC事物，并不对JDBC进行实现'
    ]},
    {'WEB模块':[
        'WEB模块提供对常见框架如Struts1，WEBWORK（Struts 2），JSF的支持，Spring能够管理这些框架，将Spring的资源注入给框架，也能在这些框架的前后插入拦截器'
    ]},
    {'Context模块':[
        'Context模块提供框架式的Bean访问方式，其他程序可以通过Context访问Spring的Bean资源，相当于资源注入'
    ]},
    {'MVC模块':[
        'WEB MVC模块为Spring提供了一套轻量级的MVC实现'
    ]}
],
'Spring 的 AOP 是怎么实现的':[
    '通过一个类实现：AbstractAutoProxyCreator',
    '它实现BeanPostProcessor，重写postProcessAfterInitialization()方法',
    {'方法内容':[
        '1.得到拦截当前bean的advisor、advice、interceptor，封装成advisor',
        '2.将advisor做为参数,创建代理',
    ]},
    '当调用被增强过的bea 时，会走到代理类，触发增强器，本质跟拦截器类似'
],
'多个AOP的顺序怎么定':[
    '通过 Ordered和PriorityOrdered接口(优先级高些)进行排序',
    'order值越小,优先级越高'
],
'Spring 的 AOP 有哪几种创建代理的方式':[
    'JDK 动态代理和 Cglib 代理',
    '如果被代理对象实现了接口，则使用JDK动态代理，否则使用Cglib代理',
    '可通过指定proxyTargetClass=true强制走Cglib代理'
],
'JDK 动态代理和 Cglib 代理的区别':[
    'JDK 动态代理本质上是实现了被代理对象的接口，而 Cglib 本质上是继承了被代理对象，覆盖其中的方法',
    'JDK 动态代理只能对实现了接口的类生成代理，Cglib 则没有这个限制',
    '调用代理方法:JDK通过反射机制调用，Cglib通过FastClass 机制直接调用(使用index入参，直接定位要调用的方法)'
],
'JDK 动态代理为什么只能对实现了接口的类生成代理':[
    'JDK动态代理生成的类已继承Proxy 类，无法再使用继承方式去对类实现代理',
]
}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 