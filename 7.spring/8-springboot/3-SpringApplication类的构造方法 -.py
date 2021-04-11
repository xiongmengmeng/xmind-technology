import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0,parentdir) 


import xmind
from xmind.core.markerref import MarkerId
xmind_name="springboot"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("SpringApplication类的构造方法")
r2=s2.getRootTopic()
r2.setTitle("SpringApplication类的构造方法")


content={
'构造方法':[
    {'推断应用类型':[
        'this.webApplicationType = deduceWebApplicationType();',
        '根据类型初始化对应的环境,常用的一般是servlet环境'
    ]},
    {'初始化classpath下META-INF/spring.factories中已配置的ApplicationContextInitializer':[
        'setInitializers((Collection) getSpringFactoriesInstances(ApplicationContextInitializer.class))'
    ]},
    {'初始化classpath下所有已配置的 ApplicationListener':[
        'setListeners((Collection) getSpringFactoriesInstances(ApplicationListener.class))'
    ]},
    {'根据调用栈，推断出 main 方法的类名':[
        'this.mainApplicationClass = deduceMainApplicationClass()'
    ]}
],
'deduceWebApplicationType()':[
    '推断应用的类型',
    'WebApplicationType.REACTIVE:classpath下存在org.springframework.web.reactive.DispatcherHandler',
    'WebApplicationType.SERVLET:classpath下存在javax.servlet.Servlet或者org.springframework.web.context.ConfigurableWebApplicationContext',
    'WebApplicationType.NONE:不满足以上条件'
],
'setInitializers(...)':[
    '通过指定的classloader从META-INF/spring.factories获取指定的Spring的工厂实例,共6个',
    {'spring-boot-autoconfigure包下':[
        'org.springframework.context.ApplicationContextInitializer=',
        'org.springframework.boot.autoconfigure.SharedMetadataReaderFactoryContextInitializer,',
        'org.springframework.boot.autoconfigure.logging.ConditionEvaluationReportLoggingListener'
    ]},
    {'spring-boot-autoconfigure包下':[
        'org.springframework.context.ApplicationContextInitializer=',
        'org.springframework.boot.context.ConfigurationWarningsApplicationContextInitializer,',
        'org.springframework.boot.context.ContextIdApplicationContextInitializer,',
        'org.springframework.boot.context.config.DelegatingApplicationContextInitializer,',
        'org.springframework.boot.rsocket.context.RSocketPortInfoApplicationContextInitializer,',
        'org.springframework.boot.web.context.ServerPortInfoApplicationContextInitializer'
    ]},
    {'getSpringFactoriesInstances()':[
        {'1.从spring.factories中加载Bean':[
            '1.SpringFactoriesLoader.loadFactoryNames(type, classLoader)',
        ]},
        {'2.反射实例化bean':[
            '2.createSpringFactoriesInstances(type, parameterTypes,classLoader, args, names)',
        ]},
    ]},
    {'ApplicationContextInitializer ':[
        '在ConfigurableApplicationContext调用refresh()方法之前，回调这个类的initialize方法',
        '通过ConfigurableApplicationContext实例获取容器的环境Environment，从而实现对配置文件的修改完善等工作'
    ]}

],
'setListeners(...)':[
    '加载过程同上',
    {'ApplicationListener':[
        'spring的事件监听器，典型的观察者模式',
        '通过ApplicationEvent类和ApplicationListener接口，实现对spring容器全生命周期的监听，当然也可以自定义监听事件'
    ]}
]
}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 