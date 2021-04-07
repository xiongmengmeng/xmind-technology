import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0,parentdir) 


import xmind
from xmind.core.markerref import MarkerId
xmind_name="springboot"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("IoC容器的设计路线")
r2=s2.getRootTopic()
r2.setTitle("IoC容器的设计路线")


content={
'BeanFactory接口':[
    '定义IoC容器的基本规范',
    'getBean(String name):按名称的获取Bean'
],
'HierarchicalBeanFactory接口':[
    'getParentBeanFactory():使BeanFactory具备了双亲IoC容器管理的功能'
],
'ConfigurableBeanFactory接口':[
    '提供了配置BeanFactory的各种方法',
    'setParentBeanFactory():配置上面提到的双亲IoC容器',
    'addBeanPostProcessor():配置Bean后置处理器'
],
'ConfigurableListableBeanFactory接口':[
    '增加指定忽略类型和接口'
],
'AutowireCapableBeanFactory接口':[
    'autowireBean():自动注入bean',
    'createBean():创建bean()',
    'initializeBean():初始化bean'
],
'AbstractBeanFactory抽象类':[
    '常用注解@Autowired @Resource(name = "xxx")一个是按类查找，一个是按名获取,通过以下方法实现',
    'getBean(String name):实现了BeanFactory中定义的方法',
    'getBean(String name, Class<T> requiredType):实现了BeanFactory中定义的方法'
],
'AbstractAutowireCapableBeanFactory抽象类':[
    '实现了AutowireCapableBeanFactory接口定义的方法',
    '在此基础上通过继承AbstractBeanFactory具备了操作Bean的能力'
],
'AbstractAutowireCapableBeanFactory 抽象类':[
    '实现了Bean的创建方法',
    '完成了一个Bean从createBean()==>createInstance()==>init(invokeInitMethods())的所有工作'
],
'DefaultListableBeanFactory ':[
    '除以上父类所具有功能外,加入了对BeanDefinition的管理和维护',
    {'Map<String, BeanDefinition> beanDefinitionMap':[
        '缓存 beanName到BeanDefinition的映射关系',
        'ean name --> BeanDefinition'
    ]},
]


}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 