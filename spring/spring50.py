import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="spring"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("@EnableTransactionManagement")
r2=s2.getRootTopic()
r2.setTitle("@EnableTransactionManagement")


content={
'@RestController vs @Controller':[
    '@Controller不加 @ResponseBody:返回一个视图，对应于前后端不分离的情况',
    '@RestController 返回JSON 或 XML 形式数据'
],
'IoC':[
    'Inverse of Control:控制反转,一种设计思想 ',
    '将原本在程序中手动创建对象的控制权，交由Spring框架来管理',
    'IoC容器:Spring用来实现IoC的载体，实际上是个Map（key，value）,Map中存放的是各种对象',
    '将对象之间的相互依赖关系交给 IoC 容器来管理，并由 IoC 容器完成对象的注入',
    '简化应用的开发，把应用从复杂的依赖关系中解放出来'
],
'AOP':[
    '面向切面编程,将那些与业务无关，却为业务模块所共同调用的逻辑或责任（例如事务处理、日志管理、权限控制等）封装起来',
    '减少系统的重复代码，降低模块间的耦合度，并有利于未来的可拓展性和可维护性',
    'Spring AOP基于动态代理',
    '如要代理的对象，实现某个接口，Spring AOP使用JDK Proxy，去创建代理对象',
    '对于没有实现接口的对象，Spring AOP会使用Cglib,生成一个被代理对象的子类来作为代理 ',
    {'Spring AOP 和 AspectJ AOP 有什么区别':[
        'Spring AOP 属于运行时增强，而 AspectJ 是编译时增强',
        'Spring AOP 基于代理(Proxying)，而 AspectJ 基于字节码操作(Bytecode Manipulation)',
        '当切面太多的话，最好选择 AspectJ ，它比Spring AOP 快很多'
    ]}
],
'bean':[
    'bean作用域',
    {'@Component 和 @Bean 的区别':[
        '作用对象不同: @Component 注解作用于类，而@Bean注解作用于方法',
        '@Component需要配合 @ComponentScan使用，将类装配到bean容器，@Bean在使用方法时加载到bean容器',
        '@Bean 注解比 Component 注解的自定义性更强，更灵活'
    ]},
    {'将一个类声明为Spring的 bean 的注解':[
        '@Component：通用注解，可标注任意类为Spring 组件',
        '@Repository：对应持久层即 Dao 层，主要用于数据库相关操作',
        '@Service：对应服务层，主要涉及一些复杂的逻辑，需要用到Dao层',
        '@Controller：对应Spring MVC控制层，主要用户接受用户请求并调用Service层返回数据给前端页面'
    ]},
    'bean生命周期',
    '',
    '',
    ''
],
'Spring MVC':[
    '',
    '',
    '',
    '',
    ''
],
'':[
    '',
    '',
    '',
    '',
    ''
],
'':[
    '',
    '',
    '',
    '',
    ''
],
'':[
    '',
    '',
    '',
    '',
    ''
],
}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 