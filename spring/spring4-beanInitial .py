import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="spring"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("Bean源码")
r2=s2.getRootTopic()
r2.setTitle("Bean源码")


content={

'入囗：AnnotationConfigApplicationContext':[],
'1.this():AnnotationConfigApplicationContext初始化':[
    '在执行子类的无参构造函数时，会优先执行父类GenericApplicationContext的无参构造函数：创建一个DefaultListableBeanFactory'
    '初始化参数：AnnotatedBeanDefinitionReader reader,会初始化类加载器AppClassLoader，然后加载DefaultListableBeanFactory',
    '初始化参数：ClassPathBeanDefinitionScanner scanner'
],
'2.register(componentClasses):Bean注册':[
    {'简化':[
        '1.将类转化为AnnotatedGenericBeanDefinition，里面只有beanClass',
        '2.填充作用域',
        '3.封装BeanDefinitionHolder，有参数BeanDefinition，beanClass，aliases',
        '4.注册:先验证，然后把BeanDefinition放到beanDefinitionMap，beanDefinitionNames中'
    ]},
    '1.new AnnotatedGenericBeanDefinition(beanClass):将类转化为AnnotatedGenericBeanDefinition',
    '2.conditionEvaluator.shouldSkip():判断@Conditional是否被启用,如类没有被@Conditional注解修饰，不会skip',
    '3.this.scopeMetadataResolver.resolveScopeMetadata(abd):查作用域',
    '4.this.beanNameGenerator.generateBeanName(abd, this.registry))：获得beanName',
    '5.AnnotationConfigUtils.processCommonDefinitionAnnotations(abd):处理注解Bean定义类中通用的注解,@lazy注解->@primary-> @DependsOn->@Role-> @Description',
    '6.针对@Qualifier注解:配置自动依赖注入装配的限定条件',
    '7.customizer.customize(abd):允许使用lambda 表达式来自定义注册一个bean',
    '8.new BeanDefinitionHolder(abd, beanName):把BeanDefination简单的封装为BeanDefinitionHolder',
    '9.AnnotationConfigUtils.applyScopedProxyMode():通过判断proxyMode的值为注册的Bean创建相应模式的代理对象',
    '10.BeanDefinitionReaderUtils.registerBeanDefinition(definitionHolder, this.registry):',
    {'注册BeanDefinition':[
        '方法：registerBeanDefinition(String beanName, BeanDefinition beanDefinition)',
        '1.对BeanDefiniton的校验:对AbstractBeanDefinition属性中的methodOverrides效验',
        '效验methodOverrides 是否与工厂方法并存或者methodOverrides对应的方法根本不存在',
        '2.对容器中已经存在了一个同名bean的处理方法,报错或覆盖',
        '3.将beanName和beanDefinition放到beanDefinitionMap'
    ]},
    '11.registry.registerAlias(beanName, alias):给bean注册别名',
],
'3.refresh():Bean的预加载':[
    '1.synchronized (this.startupShutdownMonitor):startupShutdownMonitor,refresh方法和destory方法公用的一个监视器，避免两方法同时执行',
    '2.prepareRefresh():设置容器启动时间和启动标志字段',
    '3.obtainFreshBeanFactory():获得BeanFactory，BeanFactory在AbstractApplicationContext类初始化的时候已经初始化为DefaultListableBeanFactory',
    '4.prepareBeanFactory(beanFactory):设置 BeanFactory 的类加载器，添加几个 BeanPostProcessor，手动注册几个特殊的 bean',
    '5.postProcessBeanFactory(beanFactory):提供给子类的扩展点,具体的子类可以在这步的时候添加一些特殊的 BeanFactoryPostProcessor 的实现类或做点什么事',
    '6.invokeBeanFactoryPostProcessors(beanFactory):调用 BeanFactoryPostProcessor 各个实现类的 postProcessBeanFactory(factory) 回调方法',
    '7.registerBeanPostProcessors(beanFactory):注册 BeanPostProcessor 的实现类,仅注册，之后会看到回调这两方法的时机',
    '8.initMessageSource()：初始化当前 ApplicationContext 的 MessageSource，国际化',
    '9.initApplicationEventMulticaster：初始化当前 ApplicationContext 的事件广播器',  
    '10.onRefresh():钩子方法,具体的子类可以在这里初始化一些特殊的 Bean（在初始化 singleton beans 之前）',
    '11.registerListeners: 注册事件监听器，监听器需要实现 ApplicationListener 接口',
    '12.finishBeanFactoryInitialization(beanFactory):初始化所有的 singleton beans,（lazy-init 的除外）',
    {'doCreateBean()':[
        '实例化Bean对象：createBeanInstance()',
        '依赖注入：populateBean()',
        '回调方法：initializeBean()'
    ]},
    '13.finishRefresh():广播事件'
]
}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 