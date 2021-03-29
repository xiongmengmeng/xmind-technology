import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="interview"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("IoC容器")
r2=s2.getRootTopic()
r2.setTitle("IoC容器")


content={
'Spring IoC 的容器构建流程':[
    'refresh 方法的核心内容'
],
'Spring bean 的生命周期':[],
'BeanFactory 和 FactoryBean 的区别':[
    {'BeanFactory':[
        'Spring 容器最核心,最基础的接口',
        '本质是个工厂类，用于管理 bean 的工厂',
        '最核心的功能是加载 bean，也就是 getBean 方法',
        '通常我们不会直接使用该接口，而是使用其子接口',
    ]},
    {'FactoryBean':[
        '该接口以bean样式定义，但它不是一种普通的bean，它是个工厂bean',
        '实现该接口的类可以自己定义要创建的bean实例，只需实现它的getObject方法',
        '广泛应用于 Java 相关的中间件中,通过 FactoryBean#getObject 来返回一个代理类',
    ]}
],
'Spring 怎么解决循环依赖的问题':[],
'Spring 能解决构造函数循环依赖吗':[
    '不行',
    '使用三级缓存的前提是：使用构造函数创建一个“不完整”的bean实例”',
    '当构造函数出现循环依赖，“不完整”的bean实例是无法构建的'
],
'Spring 三级缓存':[],
'@PostConstruct修饰的方法里用到了其他bean实例，会有问题吗':[
    '1.属性的依赖注入在populateBean方法里，属于属性填充阶段',
    '2.@PostConstruct注解被封装在CommonAnnotationBeanPostProcessor中',
    '具体触发时间在postProcessBeforeInitialization方法，即initializeBean方法里，属于初始化bean阶段',
    '3.属性填充阶段位于初始化之前,没问题',
    'bean的init-method属性指定的方法里用到了其他bean实例,也没问题'
],
'要在Spring IoC容器构建完毕后执行一些逻辑，怎么实现':[
    '1.使用事件监听器，实现 ApplicationListener 接口，监听 ContextRefreshedEvent 事件',
    '2.实现 SmartLifecycle 接口，并且 isAutoStartup 方法返回 true',
    '两种方式都是在 finishRefresh 中被触发，SmartLifecycle在ApplicationListener之前'
],


}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 