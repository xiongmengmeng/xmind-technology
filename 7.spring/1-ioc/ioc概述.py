import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="spring"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("IOC")
r2=s2.getRootTopic()
r2.setTitle("IOC")


content={
'Bean基础内容':[
    'Bean生命周期',
    'BeanDefinition',
    'Bean作用域',
    'Bean初始化流程'
],
'IOC中的常见扩展类':[
    'InitializingBean',
    'BeanPostProcessor',
    'BeanFactoryPostProcessor',
    'BeanDefinitionRegistryPostProcessor',
    'FactoryBean'
],
'IoC容器基础内容':[
    {'IoC容器的设计路线':[
        'BeanDefinitionRegistry接口',
        'SingletonBeanRegistry接口--DefaultSingletonBeanRegistry',
        'BeanFactory接口',
        'AbstractBeanFactory抽象类',
        'AutowireCapableBeanFactory接口',
        'AbstractAutowireCapableBeanFactory抽象类',
        'DefaultListableBeanFactory'
    ]},
    {'Spring应用上下文的设计路线':[
        'ApplicationContext',
        'ConfigurableApplicationContext',
        'AbstractApplicationContext',
        'GenericApplicationContext',
        'AnnotationConfigServletWebServerApplicationContext'
    ]}
],
'IOC过程':[
    {'入囗':[
        'AbstractApplicationContext.refresh()'
    ]},
    {'Bean的注册(注解方式)':[
        'invokeBeanFactoryPostProcessors(beanFactory)'
    ]},
    {'Bean的加载':[
        'finishBeanFactoryInitialization(beanFactory)'
    ]}
],
'Bean的注册(注解方式)---核心类':[
    'ConfigurationClassPostProcessor',
    'ConfigurationClassParser',
    'SpringFactoriesLoader'
],
'Bean的加载---核心方法':[
    {'doCreateBean(beanName, mbd, args)':[
        {'1.反射创建bean':[
            'createBeanInstance()'
        ]},
        {'2.依赖注入':[
            'populateBean()'
        ]},
        {'3.初始化bean':[
            'initializeBean()'
        ]}
    ]},
    {'getBean()':[
        '可通过sping解决依赖注入的方式来学习'
    ]}
]
}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 