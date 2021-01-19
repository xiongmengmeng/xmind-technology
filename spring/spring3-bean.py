import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="spring"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("spring")
r2=s2.getRootTopic()
r2.setTitle("spring")


content={
'重要类':[
    'BeanDefinition：表示Bean，描述Bean的配置信息',
    'BeanDefinitionRegistry接口:管理BeanDefinition,提供了向容器注册，删除，获取BeanDefinition对象的方法'

],
'装配Bean':[
    {'1.@Component和@ComponentScan':[
        '@Component标明哪个类被扫描进入Spring IoC容器',
        '@ComponentScan标明采用何种策略去扫描装配Bean',
        '配置项basePackages定义扫描的包名，在没有定义的情况下，它只会扫描当前包和其子包下的路径'
    ]},
    '2.引入XML配置Bean:xml文件+@ImportResource，通过它可以引入对应的XML文件'
],
'Bean生命周期(4个部分)':[
    'Bean定义',
    'Bean的初始化',
    'Bean的生存期',
    'Bean的销毁'
],
'Bean初始化流程':[
    '1.资源定位:如@ComponentScan定义的扫描路径去找到带有@Component的类',
    '2.Bean的定义:找到资源，开始解析，并将定义的信息保存到BeanDefinition实例中(此时没有初始化Bean，也没有Bean的实例)',
    '3.发布Bean定义：IoC容器半截Bean定义。此时，IoC容器也只有Bean的定义，还是没有Bean的实例生成',
    '4.实例化:创建Bean的实例对象',
    '5.依赖注入：如@Autowired注入的各种资源',
    '注：ComponentScan中有配置项lazyInit(Boolean型)，默认值false(不延迟实例化和依赖注入)'
],
'Bean初始化流程,详细':[
    '1.初始化',
    '2.依赖注入',
    '3.setBeanName方法：接囗BeanNameAware',
    '4.setBeanFactory方法：接囗BeanFactoryAware',
    '5.setApplicationContext方法：接囗ApplicationContextAware(需容器实现ApplicationContext接囗才会被调用)',
    '6.postProcessBeforeInitialization方法：BeanPostProcessor的预初始化方法(注：它是针对全部Bean生效)',
    '7.自定义初始化方法：@PostConstruct标方法',
    '8.afterPropertiesSet方法：接囗InitializingBean',
    '9.postProcessAfterInitialization方法：BeanPostProcessor的后初始化方法(注：它是针对全部Bean生效)',
    '10.生存期',
    '11.自定义销毁方法：@PreDestroy标注方法',
    '12.destroy方法：接囗DisposableBean'
],
'Bean作用域':[
    'Singleton:所有spring应用，默认值，Ioc容器只存在单例',
    'Prototype:所有spring应用，每当从Ioc容器中取出一个Bean，则创建一个新的Bean',
    'request:spring web应用，web工程单次这一次(request)',
    'session:spring web应用，HTTP会话',
    'application:spring web应用，web工程生命周期',
    'globalSession:spring web应用，不常用'
],
'其它':[
    {'BeanPostProcessor':[
        '方法：postProcessBeforeInitialization(Object bean, String beanName)',
        'postProcessAfterInitialization(Object bean, String beanName)',
        '初始化Bean时,"临时"修改Bean的属性，注意临时修改'
    ]},
    {'BeanFactoryPostProcessor':[
        '方法：postProcessBeanFactory(ConfigurableListableBeanFactory beanFactory)',
        '修改的是BeanFactory的BeanDefinition，从根本上改',
        ''
    ]},
    {'FactoryBean':[
        '一个接口，一个Bean实现这个接口，变成一个Factory，通过getObject()将一个Object暴露出去',
        'factorybean中getObject中返回的对象==beanfactory.getbean返回的bean',
        {'通过beanfactory获取':[
            'beanfactory.getbean("beanFactoryName"),获得factorybean中getObject中返回的对象',
            'beanfactory.getbean("&beanFactoryName"),获得factorybean本身'
        ]}
    ]},
    {'BeanFactoryAware':[
        '方法：setBeanFactory(BeanFactory beanFactory),
        '实现这个接口的bean其实是希望知道自己属于哪一个beanfactory'
    ]},
    {'BeanNameAware':[
        '方法：setBeanName(String name)',
        '让实现这个接口的bean知道自己在spring容器里的名字'
    ]}
]

}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 