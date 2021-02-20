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
'IOC':[
    'BeanFactory--DefaultListableBeanFactory',
    'ApplicationContext--AnnotationConfigApplicationContext',
    {'注解':[
        '@SpringBootApplication',
        '@EnableAutoConfiguration',
        '@Configuration',
        '@Component和@ComponentScan',
        '@Import，ImportBeanDefinitionRegistrar和ImportSelector'
    ]},
    {'扩展类':[
        'BeanPostProcessor',
        'BeanFactoryPostProcessor--BeanDefinitionRegistryPostProcessor',
        'FactoryBean',
        'BeanFactoryAware',
        'BeanNameAware'
    ]},
    {'AnnotationConfigApplicationContext启动':[
        'this()',
        'register(componentClasses):Bean注册------实现类AnnotatedBeanDefinitionReader',
        'refresh():Bean的预加载------实现类AbstractApplicationContext'
    ]},
    {'其它':[
        'SpringFactoriesLoader'
    ]}
],
'Bean':[
    'Bean定义:->',
    {'Bean初始化--核心doCreateBean()':[
        '实例化Bean对象：createBeanInstance()--通过反射',
        '依赖注入：populateBean()--思考循环依赖问题',
        '回调方法：initializeBean()--重点'
    ]},
    {'循环依赖解决--缓存':[
        '一级缓存:singletonObjects',
        '二级缓存:earlySingletonObjects',
        '三级缓存:singletonFactories'
    ]}
],
'AOP':[
    {'相关类':[
        'Proxy--ProxyClassFactory--ProxyGenerator',
        'InvocationHandler',
    ]},
    {'基础类':[
        'AdvisedSupport--ProxyCreatorSupport--ProxyFactoryBean',
        'AopProxy--JdkDynamicAopProxy--ObjenesisCglibAopProxy',
        'DefaultAopProxyFactory',
    ]},
    {'入囗类':[
        'DefaultAdvisorAutoProxyCreator--BeanPostProcessor',
        'AnnotationAwareAspectJAutoProxyCreator'
    ]}
],
'Mybatis':[
    'SqlSessionFactoryBean--sqlSessionFactory',
    'MapperFactoryBean',
    'MapperScannerConfigurer--BeanDefinitionRegistryPostProcessorr',
    '@MapperScan->@Import(MapperScannerRegistrar.class):作用同上',
    'MybatisAutoConfiguration：与springboot结合，入囗'
],
'Transaction':[
    {'分类':[
        '编程式：TransactionTemplate',
        '申明式：@Transactional'
    ]},
    {'PlatformTransactionManager--AbstractPlatformTransactionManager':[
        'getTransaction(),返回',
        'commit(TransactionStatus status)',
        'rollback(TransactionStatus status)'
    ]},
    'TransactionAutoConfiguration,：与springboot结合，入囗',
    '@EnableTransactionManagement->@Import(TransactionManagementConfigurationSelector.class)',
    'AutoProxyRegistrar',
    {'ProxyTransactionManagementConfiguration':[
        'TransactionInterceptor：invoke()',
        'TransactionAttributeSource',
        'BeanFactoryTransactionAttributeSourceAdvisor'
    ]},

],
'Redis':[
    'CacheAutoConfiguration->@Import(CacheConfigurationImportSelector.class)',
    'RedisCacheConfiguration->RedisAutoConfiguration',
    {'RedisAutoConfiguration':[
        '@Import({JedisConnectionConfiguration.class }):JedisConnectionConfiguration创建RedisConnectionFactory',
        '创建redisTemplate'
    ]}
]
'Web':[
    'DispatcherServlet',
    'HanlerMapping',
    'HandlerAdapter',
    {'与springboot结合':[
        'TomcatServletWebServerFactor',
        'DispatcherServletRegistrationBean',
        'RegistrationBean'
    ]}
],
}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 