import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="interview"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("IoC容器")
r2=s2.getRootTopic()
r2.setTitle("IoC容器")


content={
'Spring 中的常见扩展点有哪些':[
    {'ApplicationContextInitializer':[
        'initialize方法，在Spring容器刷新前触发，也就是 refresh 方法前被触发'
    ]},
    {'BeanFactoryPostProcessor':[
        'postProcessBeanFactory方法，在加载完Bean定义后，创建Bean实例之前被触发，通常使用该扩展点来加载一些自己的bean定义'
    ]},
    {'BeanPostProcessor':[
        'postProcessBeforeInitialization方法，执行bean的初始化方法前被触发',
        'postProcessAfterInitialization 方法，执行bean的初始化方法后被触发'
    ]},
    {'@PostConstruct':[
        '该注解被封装在 CommonAnnotationBeanPostProcessor 中，具体触发时间是在 postProcessBeforeInitialization方法'
    ]},
    {'InitializingBean':[
        'afterPropertiesSet 方法，在bean的属性填充之后，初始化方法（init-method）之前被触发，作用基本等同于init-method'
    ]},
    {'ApplicationListener，事件监听器':[
        'onApplicationEvent 方法，根据事件类型触发时间不同',
        '通常使用的ContextRefreshedEvent触发时间为上下文刷新完毕，通常用于IoC容器构建结束后处理一些自定义逻辑'
    ]},
    {'@PreDestroy':[
        '该注解被封装在DestructionAwareBeanPostProcessor中，具体触发时间是在postProcessBeforeDestruction方法，是在销毁对象之前触发'
    ]},
    {'DisposableBean':[
        'destroy 方法，在 bean 的销毁阶段被触发，该方法的作用基本等同于destroy-method，主用用于执行销毁相关操作'
    ]}
],
'Spring中如何让两个bean按顺序加载':[
    '1.使用 @DependsOn、depends-on',
    '2.后加载的类依赖先加载的类',
    '3.使用扩展点提前加载，例如：BeanFactoryPostProcessor'
],
'@Autowire和@Resource注解的区别':[
    '都是Spring支持的注解方式动态装配bea',
    {'@Autowire':[
        '1.默认按照类型(by-type)装配，要求依赖对象必须存在',
        '2.@Autowire(required=false):允许依赖对象为null',
        '3.@Autowire + @qualifier("") = @Resource(name=""):按名字装配',
        {'前提':[
            '在Spring配置文件进行配置，<context:annotation-config />'
        ]},
        {'原理':[
            '启动spring IoC时，容器自动装载了一个AutowiredAnnotationBeanPostProcessor后置处理器',
            '当容器扫描到@Autowied、@Resource或@Inject时，会在IoC容器自动查找需要的bean，并装配给该对象的属性'
        ]}
    ]},
    {'@Resource':[
        '1.默认按照名称(by-name)装配，名称可通过name属性指定',
        '2.当按名称未匹配时，按照类型(by-type)装配',
    ]}
],
'Spring 框架中都用到了哪些设计模式':[
    '1.工厂模式：Spring使用工厂模式，通过BeanFactory和ApplicationContext来创建对象',
    '2.单例模式：Bean默认为单例模式',
    '3.策略模式：例如Resource的实现类，针对不同的资源文件，实现了不同方式的资源获取策略',
    '4.代理模式：Spring的AOP功能用到了JDK的动态代理和CGLIB字节码生成技术',
    '5.模板方法：可以将相同部分的代码放在父类中，而将不同的代码放入不同的子类中，用来解决代码重复的问题。比如RestTemplate, JmsTemplate, JpaTemplate',
    '6.适配器模式：Spring AOP的增强或通知（Advice）使用到了适配器模式，Spring MVC中也是用到了适配器模式适配Controller',
    '7.观察者模式：Spring事件驱动模型就是观察者模式的一个经典应用',
    '8.桥接模式：可以根据客户的需求能够动态切换不同的数据源。比如我们的项目需要连接多个数据库，客户在每次访问中根据需要会去访问不同的数据库',
    '详细：https://blog.csdn.net/a745233700/article/details/112598471'
],
}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 