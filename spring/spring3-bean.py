import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="spring"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("bean")
r2=s2.getRootTopic()
r2.setTitle("bean")


content={
'装配Bean':[
    {'1.@Component和@ComponentScan':[
        '@Component标明哪个类被扫描进入Spring IoC容器',
        '@ComponentScan标明采用何种策略去扫描装配Bean',
        '配置项basePackages定义扫描的包名，在没有定义的情况下，它只扫描当前包和其子包下的路径'
    ]},
    '2.引入XML配置Bean:xml文件+@ImportResource，通过它可以引入对应的XML文件'
],
'Bean作用域':[
    'Singleton:所有spring应用，默认值，Ioc容器只存在单例',
    'Prototype:所有spring应用，每当从Ioc容器中取出一个Bean，则创建一个新的Bean',
    'request:spring web应用，web工程单次这一次(request)',
    'session:spring web应用，HTTP会话',
    'application:spring web应用，web工程生命周期',
    'globalSession:spring web应用，不常用'
],
'常见类':[
    {'ImportBeanDefinitionRegistrar':[
        '一个接口，该接口的实现类作用于Spring解析Bean的配置阶段',
        '当解析@Configuration注解时，可以向BeanDefinitionRegistry容器中添加额外的BeanDefinition对象',
        '方法：registerBeanDefinitions(AnnotationMetadata importingClassMetadata, BeanDefinitionRegistry registry)',
        'importingClassMetadata参数为@Import所在注解的配置信息',
        'registry参数为BeanDefinition容器'
    ]}
    {'BeanPostProcessor':[
        {'方法':[
            'postProcessBeforeInitialization(Object bean, String beanName)',
            'postProcessAfterInitialization(Object bean, String beanName)'
        ]},
        '通常用于处理Spring Bean对应的Java类中的注解信息或者创建Bean的代理对象',
        '初始化Bean时,"临时"修改Bean属性，注意临时修改'
    ]},
    {'BeanFactoryPostProcessor':[
        '方法：postProcessBeanFactory(ConfigurableListableBeanFactory beanFactory)',
        '因为要修改BeanDefinnition，它存在map中，map存在BeanFactory中,所以传参BeanFactory',
        '修改的是BeanFactory的BeanDefinition，从根本上改',
    ]},
    {'BeanDefinitionRegistryPostProcessor':[
        '一个接口，继承了BeanFactoryPostProcessor',
        '可以向BeanFactory中添加BeanDefinition的',
    ]}
    {'FactoryBean':[
        '一个接口，一个Bean实现这个接口，变成一个Factory，通过getObject()将一个Object暴露出去',
        'factorybean中getObject中返回的对象==beanfactory.getbean返回的bean',
        'Spring中的工厂Bean，通常用于处理Spring中配置较为复杂或者由动态代理生成的Bean实例',
        {'通过beanfactory获取':[
            'beanfactory.getbean("beanFactoryName"),获得factorybean中getObject中返回的对象',
            'beanfactory.getbean("&beanFactoryName"),获得factorybean本身'
        ]}
    ]},
    {'BeanFactoryAware':[
        '方法：setBeanFactory(BeanFactory beanFactory)',
        '实现这个接口的bean知道自己属于哪一个beanfactory'
    ]},
    {'BeanNameAware':[
        '方法：setBeanName(String name)',
        '让实现这个接口的bean知道自己在spring容器里的名字'
    ]},
    {'@Import':[
        '一个注解，在Spring中是用来向Spring容器中导入Bean的',
        '比起在某个类上加上@Component注解，更灵活',
        '@Import注解所指定的类，Spring启动中会对指定的类进行判断，是否实现了比较特殊的接口',
        '比如ImportBeanDefinitionRegistrar，如存在特殊的接口就执行特殊的逻辑',
        '如没有则生成该类对应的BeanDefinition并放入BeanFactory中'
    ]},
    {'ImportBeanDefinitionRegistrar':[
        '动态的注册bean:通过生成BeanDefinition，并且把BeanDefinition放入BeanFactory中'
    ]}
]

}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 