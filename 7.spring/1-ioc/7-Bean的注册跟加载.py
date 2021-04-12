import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="spring"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("Bean的注册跟加载")
r2=s2.getRootTopic()
r2.setTitle("Bean的注册跟加载")


content={
'入囗：AnnotationConfigApplicationContext':[],
'1.this():AnnotationConfigApplicationContext初始化':[
    '先执行父类GenericApplicationContext的无参构造函数：创建一个DefaultListableBeanFactory',
    {'再执行子类的无参构造函数':[
        '初始化参数：AnnotatedBeanDefinitionReader reader,会初始化类加载器AppClassLoader',
        '初始化参数：ClassPathBeanDefinitionScanner scanner'
    ]}
],
'2.register(componentClasses):Bean注册':[
    '实现类，AnnotatedBeanDefinitionReader，持有BeanDefinitionRegistry',
    {'简化':[
        '1.将类转化为AnnotatedGenericBeanDefinition，里面只有beanClass,填充作用域',
        '2.封装成BeanDefinitionHolder，有参数BeanDefinition，beanClass，aliases',
        '3.注册:先验证，然后把BeanDefinition放到beanDefinitionMap，beanDefinitionNames中',
    ]},
    '1.new AnnotatedGenericBeanDefinition(beanClass):将类转化为AnnotatedGenericBeanDefinition',
    '2.conditionEvaluator.shouldSkip():判断@Conditional是否被启用,如类没有被@Conditional注解修饰',
    '3.this.scopeMetadataResolver.resolveScopeMetadata(abd):查作用域',
    '4.this.beanNameGenerator.generateBeanName(abd, this.registry))：获得beanName',
    '5.AnnotationConfigUtils.processCommonDefinitionAnnotations(abd):处理Bean定义类中通用注解:@lazy注解->@primary-> @DependsOn->@Role-> @Description',
    '6.针对@Qualifier注解:配置自动依赖注入装配的限定条件',
    '7.customizer.customize(abd):允许使用lambda 表达式来自定义注册一个bean',
    '8.new BeanDefinitionHolder(abd, beanName):把BeanDefination简单的封装为BeanDefinitionHolder',
    '9.AnnotationConfigUtils.applyScopedProxyMode():通过判断proxyMode的值为注册的Bean创建相应模式的代理对象',
    {'10.BeanDefinitionReaderUtils.registerBeanDefinition(definitionHolder, this.registry):注册BeanDefinition':[
        '1.对BeanDefiniton的校验:对AbstractBeanDefinition属性中的methodOverrides效验',
        '2.对容器中已经存在了一个同名bean的处理方法,报错或覆盖',
        '3.将beanName和beanDefinition放到beanDefinitionMap'
    ]},
    '11.registry.registerAlias(beanName, alias):给bean注册别名',
],
'3.refresh():Bean的预加载':[
    '实现类，AbstractApplicationContext',
    '1.synchronized (this.startupShutdownMonitor):refresh方法和destory方法公用的一个监视器startupShutdownMonitor，避免两方法同时执行',
    '2.prepareRefresh():设置容器启动时间和启动标志字段',
    '3.obtainFreshBeanFactory():获得BeanFactory，BeanFactory在AbstractApplicationContext类初始化的时候已经初始化为DefaultListableBeanFactory',
    '4.prepareBeanFactory(beanFactory):设置BeanFactory的类加载器，添加几个BeanPostProcessor，手动注册几个特殊的bean',
    '5.postProcessBeanFactory(beanFactory):提供给子类的扩展点,具体的子类可以在这步添加一些特殊的BeanFactoryPostProcessor实现类',
    '6.invokeBeanFactoryPostProcessors(beanFactory):处理实现BeanFactoryPostProcessor的bean,说明BeanFactoryPostProcessor实例化的优先级最高',
    '7.registerBeanPostProcessors(beanFactory):注册BeanPostProcessor的实现类,仅注册，之后会看到回调这两方法的时机',
    '8.initMessageSource()：初始化当前 ApplicationContext 的 MessageSource，国际化',
    '9.initApplicationEventMulticaster：初始化当前 ApplicationContext 的事件广播器',  
    '10.onRefresh():钩子方法,具体的子类可以在这里初始化一些特殊Bean（在初始化singleton beans之前）',
    '11.registerListeners: 注册事件监听器，监听器需要实现ApplicationListener接口',
    {'12.finishBeanFactoryInitialization(beanFactory):初始化所有singleton beans（lazy-init的除外）,核心doCreateBean()':[
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