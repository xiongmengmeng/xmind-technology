import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="spring"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("BeanFactoryPostProcessor")
r2=s2.getRootTopic()
r2.setTitle("BeanFactoryPostProcessor初始化")


content={
'invokeBeanFactoryPostProcessors(beanFactory)':[
    '将BeanFactoryPostProcessor作为bean注册到容器',
    '1.先执行BeanDefinitionRegistryPostProcessors',
    '2.在beanFactory中获取实现BeanFactoryPostProcessor这个接口的bean的名称',
    '3.将获取到的BeanFactoryPostProcessors的bean分类，根据bean是否实现PriorityOrdered，Ordered这些接口',
    '4.实例化实现BeanFactoryPostProcessor的bean:getBean()方法---',
    '5.将实例化后的bean放入List<BeanFactoryPostProcessor> nonOrderedPostProcessors',
    '6.批量执行nonOrderedPostProcessors中的BeanFactoryPostProcessor',
],
'getBean()->doGetBean()->':[
    '将BeanFactoryPostProcessor作为bean注册到容器',
    '1.去singleton缓存中去找实例',
    '2.获取该beanFactory父factory，希望从这些factory中获取，如果该beanfactory有父类，则希望用父类去实例化该bean',
    '3.标记目前的bean的正在创建',
    '4.根据beanName去beanDefinitionMap获得BeanDefinition，接着bean依赖的bean，如依赖的bean还没创建，先创建依赖的bean，递归调用',
    '5.如果是单例，调用createBean()'
],
'createBean()':[
    '1.确保该bean的class是真实存在的，也就是该bean是可以classload可以找到加载的',
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
    {'populateBean()':[
        '',
        '',
        '',
        ''
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