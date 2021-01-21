import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="spring"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("IoC容器")
r2=s2.getRootTopic()
r2.setTitle("IoC容器")


content={
'简介':[
    'Spring IoC容器是一个管理Bean的容器',
    {'两个基本功能':[
       '通过描述管理Bean，包括发布和获取Bean',
       '通过描述完成Bean间的依赖关系'
    ]}
],
'BeanFactory':[
    '一个顶级容器接口,spring所有的IoC容器都要实现它',
    {'方法':[
        '多个getBean方法:按类型（by type）/名称（byname）获取Bean',
        'isSingleton:Bean是否为单例,默认Bean都是单例的，即用getBean方法返回的都是同一个对象',
        'isPrototype:true，使用getBean获取Bean时，Spring IoC容器会创建一个新的Bean返回'
    ]},
],
'ApplicationContext':[
    {'实现接囗和继承类':[
        'BeanFactory',
        '消息国际化接口（MessageSource）',
        '环境可配置接口（EnvironmentCapable）',
        '应用事件发布接口（ApplicationEventPublisher）',
        '资源模式解析接口（ResourcePatternResolver）'
    ]},
    '现实中我们使用的大部分Spring IoC容器是ApplicationContext接口的实现类',
    '如AnnotationConfigApplicationContext，基于注解的IoC容器'
],
'AnnotationConfigApplicationContext':[
    '继承GenericApplicationContext',
    'GenericApplicationContext实现了BeanDefinitionRegistry',
    {'参数':[
        'AnnotatedBeanDefinitionReader:一个读取注解的Bean读取器,初始化时，会加载class类型的配置',
        'ClassPathBeanDefinitionScanner：一个扫描指定类路径中注解Bean的扫描器，它初始化时，会初始化一些需被扫描的注解'
    ]},
    {'register()':[
        'AnnotatedBeanDefinitionReader,持有BeanDefinitionRegistry'
    ]},
    {'refresh()':[
        'AbstractApplicationContext'
    ]}
],
'AnnotatedBeanDefinitionReader初始化':[
    'AnnotationConfigUtils.registerAnnotationConfigProcessors(this.registry)',
    '会把一些自动注解处理器加入到AnnotationConfigApplicationContext下的BeanFactory的BeanDefinitions中',
    '1.ConfigurationClassPostProcessor:处理@Configuration，@Import，@ImportResource和类内部的@Bean',
    '2.AutowiredAnnotationBeanPostProcessor:处理@Autowired注解和@Value注解的',
    '3.RequiredAnnotationBeanPostProcessor:处理@Required注解',
    '4.CommonAnnotationBeanPostProcessor:支持@Resource、@PostConstruct和@.PreDestroy',
    '5.PersistenceAnnotationBeanPostProcessor:提供@PersistenceContext的支持',
    '6.EventListenerMethodProcessor:提供@EventListener的支持'
],
'DefaultListableBeanFactory':[
    {'BeanDefinitionRegistry':[
        '定义对BeanDefinition的各种增删改操作:',
        '注册（registerBeanDefinition）',
        '消除注册（removeBeanDefinition）',
        '获取注册（getBeanDefinition）',
        '查看是否有此注册（containsBeanDefinition）',
        '获取所有的名称（getBeanDefinitionNames）',
        '获取名片的个数（getBeanDefinitionCount）'
    ]},
    'AliasRegistry：定义对alias的简单增删改等操作',
    'SimpleAliasRegistry：主要使用map作为alias的缓存，并对接口AliasRegistry进行实现',
    'SingletonBeanRegistry：定义对单例的注册及获取。',
    'BeanFactory：定义获取bean及bean的各种属性',
    'DefaultSingletonBeanRegistry：对接口SingletonBeanRegistry各函数的实现',
    'HierarchicalBeanFactory：继承BeanFactory，也就是在BeanFactory定义的功能的基础上增加了对parentFactory的支持',
    'FactoryBeanRegistrySupport：在DefaultSingletonBeanRegistry基础上增加了对FactoryBean的特殊处理功能',
    'ConfigurableBeanFactory：提供配置Factory的各种方法',
    'ListableBeanFactory：根据各种条件获取bean的配置清单',
    'AbstractBeanFactory：综合FactoryBeanRegistrySupport和ConfigurableBeanFactory的功能',
    'AutowireCapableBeanFactory：提供创建bean、自动注入、初始化以及应用bean的后处理器',
    'AbstractAutowireCapableBeanFactory：综合AbstractBeanFactory并对接口AutowireCapable BeanFactory进行实现',
    'ConfigurableListableBeanFactory：BeanFactory配置清单，指定忽略类型及接口等',
    'DefaultListableBeanFactory：综合上面所有功能，主要是对Bean注册后的处理'
]


}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 