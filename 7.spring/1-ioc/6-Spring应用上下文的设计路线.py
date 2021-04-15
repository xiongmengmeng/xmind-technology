import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0,parentdir) 


import xmind
from xmind.core.markerref import MarkerId
xmind_name="springboot"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("Spring应用上下文的设计路线")
r2=s2.getRootTopic()
r2.setTitle("Spring应用上下文的设计路线")


content={
'上下文对容器不仅是扩展关系，更重要是持有关系，上下文是以属性形式持有了容器':[],
'ApplicationContext':[
    'MessageSource，支持不同的信息源。具备支持国际化的实现，为开发多语言版本的应用提供服务',
    'ResourcePatternResolver，访问数据源。具备了从不同地方得到Bean定义资源的能力，比如：xml，java config，注解等等',
    'ApplicationEventPublisher，发布事件。使应用上下文具备了事件机制。事件机制为Bean声明周期的管理提供了便利'
],
'ConfigurableApplicationContext':[
    'refresh()：IoC容器的初始化过程，标志着IoC容器的正式启动'
],
'AbstractApplicationContext':[
    {'实现refresh()方法':[
        {'invokeBeanFactoryPostProcessors(beanFactory)':[
            '在IoC容器中建立BeanDefinition数据映射'
        ]},
        {'finishBeanFactoryInitialization(beanFactory)':[
            '初始化bean'
        ]}
    }
],
'GenericApplicationContext':[
    '属性DefaultListableBeanFactory beanFactory'
],
'AnnotationConfigServletWebServerApplicationContext':[
    '属性beanFactory是IoC容器(DefaultListableBeanFactory)'
]

}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 