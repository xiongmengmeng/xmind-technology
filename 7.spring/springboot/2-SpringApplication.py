import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0,parentdir) 


import xmind
from xmind.core.markerref import MarkerId
xmind_name="springboot"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("SpringApplication")
r2=s2.getRootTopic()
r2.setTitle("SpringApplication")


content={
'SpringApplication#run(java.lang.String...)':[
    {'创建spring主容器':[
        'context = createApplicationContext()',
        '根据WebApplicationType webApplicationType决定加载什么类型的容器',
        'webApplicationType：在SpringApplication初始化时，据具体项目运行时依赖的类来动态选择实现',
        '如果是web项目会选择AnnotationConfigServletWebServerApplicationContext'
    ]},
    {'初始化Bean':[
        'refreshContext(context)方法',
        '方法内部最终调用了((AbstractApplicationContext) applicationContext).refresh()',
        'refresh()方法中，初始化Bean前，调用onRefresh()方法'
    ]}
],
'ServletWebServerApplicationContext的onRefresh()':[
    {'createWebServer()':[
        '1.ServletWebServerFactory factory = getWebServerFactory():',
        {'详细':[
            '实际返回TomcatServletWebServerFactory',
            {'加载TomcatServletWebServerFactory':[
                'org.springframework.boot.autoconfigure.EnableAutoConfiguration=',
                'org.springframework.boot.autoconfigure.web.servlet.ServletWebServerFactoryAutoConfiguration',
                {'ServletWebServerFactoryAutoConfiguration':[
                    '@Import部分引入了ServletWebServerFactoryConfiguration.EmbeddedTomcat.class:',
                    '包含了tomcat的jar包,向容器注册TomcatServletWebServerFactory'
                ]}
            ]}
        ]},
        '2.this.webServer = factory.getWebServer(getSelfInitializer())',
        {'详细':[
            {'factory.getWebServer(...)':[
                '实现类：org.springframework.boot.web.embedded.tomcat.TomcatServletWebServerFactory',
                {'1.创建了Tomcat实例作为webServer的内部实现':[
                    'Tomcat tomcat = new Tomcat()',
                    'tomcat.setBaseDir(baseDir.getAbsolutePath());'
                ]},
                {'2.向Tomcat的Service容器注入Connector':[
                    'tomcat.getService().addConnector(connector);'
                ]},
                {'3.设置默认Host容器的AutoDeploy属性等':[
                    'tomcat.getHost().setAutoDeploy(false);',
                ]},
                {'4.prepareContext(tomcat.getHost(), initializers)':[
                ]}
            ]}
        ]}
    ]}
],
'ServletWebServerApplicationContext.getSelfInitializer()':[
    {'方法内容：this::selfInitialize':[
        'for (ServletContextInitializer beans : getServletContextInitializerBeans()) {',
        '	beans.onStartup(servletContext);',
        '}'
    ]},
    '方法返回值：ServletContextInitializer',
    {'getServletContextInitializerBeans()':[
        'new ServletContextInitializerBeans(getBeanFactory()):',
        {'内容':[
            {'addServletContextInitializerBeans(beanFactory)':[
                '获取spring容器中所有的ServletContextInitializer实现'
            ]}

        ]}
    ]}
],
'prepareContext(tomcat.getHost(), initializers)':[
    {'1.将context加入host作为host的子容器':[
        'host.addChild(context)',
    ]},
    {'2.查找所有ServletContextInitializer实现并合并为一个数组':[
        'ServletContextInitializer[] initializersToUse = mergeInitializers(initializers)'
    ]},
    {'3.configureContext(context, initializersToUse);':[
        '创建了TomcatStarter对象:TomcatStarter starter = new TomcatStarter(initializers)',
        '将starter加入context的conainerInitializer列表:context.addServletContainerInitializer(starter, NO_CLASSES);'
    ]}
],
'学习':[
    'https://www.cnblogs.com/zrbcool/p/11480675.html#dispatcherservletregistrationbean',
]
}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 