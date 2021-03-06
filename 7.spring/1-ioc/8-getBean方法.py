import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="spring-IOC"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("getBean()")
r2=s2.getRootTopic()
r2.setTitle("getBean()")


content={
'注册bean到容器':[],
'getBean()->doGetBean()->':[
    '1.去singleton缓存中去找实例,如果bean存在于singletonFactories中，为bean生成代理，返回，循环依赖时使用',
    '2.获取该beanFactory父factory，如该beanfactory有父类，用父类去实例化该bean',
    '3.标记目前的bean的正在创建',
    '4.根据beanName去beanDefinitionMap获得BeanDefinition，接着判断bean依赖的bean是否创建，如否，先创建依赖的bean，递归调用',
    '5.如果是单例，调用createBean()'
],
'createBean()':[
    '1.确保该bean的class是真实存在的，也就是该bean是classload可以找到加载的',
    '2.准备方法的重写',
    '3.给beanPostProcessor一个机会去返回一个代理',
    'beanPostProcessor可临时修改bean，它的优先级高于正常实例化bean，如果beanPostProcessor能返回，则直接返回了',
    '4.doCreateBean(beanName, mbd, args)'
],
'doCreateBean(beanName, mbd, args)':[
    {'createBeanInstance()':[
        '1.对bean做安全检查并确定该bean有默认的构造函数',
        '2.instantiateBean(beanName, mbd):通过反射实例化Bean'
    ]},
    {'addSingletonFactory(beanName,()->getEarlyBeanReference(beanName, mbd, bean))':[
        '如果允许循环依赖，执行此方法',
        '将bean放入singletonFactories中(一个map)',
        'key为beanName',
        'value类型为AbstractAutowireCapableBeanFactory'
    ]},
    {'populateBean()':[
        '依赖注入'
    ]},
    {'initializeBean()':[
        {'invokeAwareMethods()':[
            '1.如bean实现了BeanNameAware，执行setBeanName()方法',
            '2.如bean实现了BeanClassLoaderAware，执行setBeanClassLoader()方法',
            '3.如bean实现了BeanFactoryAware，执行setBeanFactory()方法'
        ]},
        {'applyBeanPostProcessorsBeforeInitialization()':[
            '4.执行BeanPostProcessor的postProcessBeforeInitialization()方法'
        ]},
        {'invokeInitMethods()':[
            '5.如果bean实现了InitializingBean，如果实现了先执行afterPropertiesSet这个方法',
            '6.bean又执行了init-method'
        ]},
        {'applyBeanPostProcessorsAfterInitialization()':[
            '7.执行BeanPostProcessor的postProcessAfterInitialization()方法'
        ]}
    ]}
]
}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 