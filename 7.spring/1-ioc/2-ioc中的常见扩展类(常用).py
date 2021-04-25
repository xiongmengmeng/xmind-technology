import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="spring"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("ioc中的常见扩展类")
r2=s2.getRootTopic()
r2.setTitle("ioc中的常见扩展类")


content={
'InitializingBean':[
    {'方法':[
        'afterPropertiesSet()'
    ]},
    {'作用':[
        '初始化Bean时(bean实例已经生成),修改Bean属性(需要类实现此接囗)'
    ]}
],
'BeanPostProcessor':[
    {'方法':[
        'postProcessBeforeInitialization(Object bean, String beanName)',
        'postProcessAfterInitialization(Object bean, String beanName)'
    ]},
    {'作用':[
        '1.处理Bean对应Java类中的注解信息或者创建Bean的代理对象',
        '2.初始化Bean时(bean实例已经生成),修改Bean属性(对所有类都生效)'
    ]},
    {'实际应用':[
        'AOP实现类AbstractAutoProxyCreator，实现了BeanPostProcessor，重写了postProcessAfterInitialization()方法'
    ]}
],
'BeanFactoryPostProcessor':[
    {'方法':[
        'postProcessBeanFactory(ConfigurableListableBeanFactory beanFactory)'
    ]},
    {'作用':[
        '1.修改BeanDefinnition（BeanDefinnition存在于map，而map存在BeanFactory中，所以传参为beanFactory）',
        '2.修改的是BeanFactory的BeanDefinition(bean实例还未生成，此时只有BeanDefinition)，从根本上改'
    ]}
],
'BeanDefinitionRegistryPostProcessor':[
    '一个接口，继承了BeanFactoryPostProcessor',
    {'方法':[
        'postProcessBeanDefinitionRegistry(BeanDefinitionRegistry registry)'
    ]},
    {'作用':[
        '可向BeanFactory中添加BeanDefinition'
    ]},
    {'实际应用':[
        'ConfigurationClassPostProcessor,实现了BeanDefinitionRegistryPostProcessor接囗，重写了postProcessBeanDefinitionRegistry方法',
        '解析加了@Configuration的配置类，还会解析@ComponentScan、@ComponentScans注解扫描的包，以及解析@Import等注解'
    ]}
],
'FactoryBean':[
    '一个接口',
    '一个Bean实现了此接口，会变成一个Factory，通过getObject()将一个Object暴露出去'
    'factorybean中getObject中返回的对象==beanfactory.getbean返回的bean',
    {'方法':[
        'T getObject()'
    ]},
    {'作用':[
        '用于处理配置较为复杂或者由动态代理生成的Bean实例'
    ]},
    {'实际应用':[
        'MyBatis与Spring整合有使用到，用于创建Mapper的代理对象和SqlSessionFactory对象',
        'springAop中有使用到，ProxyFactoryBean用于初始化和返回代理对象'
    ]},
    {'注意':[
        'beanfactory.getbean("beanFactoryName"),获得factorybean中getObject中返回的对象',
        'beanfactory.getbean("&beanFactoryName"),获得factorybean本身'
    ]}
],
'ApplicationContextAware':[
    {'方法':[
         'void setApplicationContext(ApplicationContext applicationContext)'
    ]},
    {'作用':[
        '不交给容器进行管理的模块(如工具类)想要获取bean的一种方式'
    ]}
   
]

}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 