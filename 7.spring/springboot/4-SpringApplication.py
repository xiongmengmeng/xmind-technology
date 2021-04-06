import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0,parentdir) 


import xmind
from xmind.core.markerref import MarkerId
xmind_name="springboot"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("SpringApplication类的run方法")
r2=s2.getRootTopic()
r2.setTitle("SpringApplication类的run方法")


content={
'run方法':[
    {'1.获取并启动监听器':[
        'SpringApplicationRunListeners listeners = getRunListeners(args);',
        'listeners.starting()'
    ]},
    {'2.构造应用上下文环境':[
        'ConfigurableEnvironment environment = prepareEnvironment(listeners, applicationArguments)'
    ]},
    {'3.初始化应用上下文':[
        'context = createApplicationContext()'
    ]},
    {'4.刷新应用上下文前的准备阶段':[
        'prepareContext(context, environment, listeners, applicationArguments, printedBanner);'
    ]},
    {'5.刷新应用上下文':[
        'refreshContext(context);'
    ]},
    {'6.刷新应用上下文后的扩展接口':[
        'afterRefresh(context, applicationArguments);'
    ]},
],
'获取并启动监听器---getRunListeners(args)':[
    'getSpringFactoriesInstances():',
    '获取META-INF/spring.factories中的指定key的value，然后实例化',
    'org.springframework.boot.SpringApplicationRunListener=',
    'org.springframework.boot.context.event.EventPublishingRunListener(Spring容器的启动监听器)',
    'listeners.starting():开启监听事件'
],
'构造应用上下文环境---prepareEnvironment()':[
    {'上下文环境':[
        '计算机的环境',
        'Java环境',
        'Spring的运行环境',
        'Spring项目的配置（在SpringBoot中就是那个熟悉的application.properties/yml）'
    ]},
    {'1.创建并配置相应的环境':[
        'ConfigurableEnvironment environment = getOrCreateEnvironment();'
    ]},
    {'2.根据用户配置，配置environment系统环境':[
        'configureEnvironment(environment, applicationArguments.getSourceArgs());'
    ]},
    {'3.启动相应的监听器':[
        '其中一个重要的监听器 ConfigFileApplicationListener 就是加载项目配置文件的监听器',
        'listeners.environmentPrepared(environment);'
    ]}

],

}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 