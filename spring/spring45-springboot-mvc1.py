import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="spring"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("springboot-springmvc1")
r2=s2.getRootTopic()
r2.setTitle("springboot-springmvc")


content={
'SpringApplication.run()':[
    {'1.创建spring主容器':[
        'context = createApplicationContext()',
        '方法内根据具体项目运行时依赖的类来动态选择实现',
        '如是web项目选择AnnotationConfigServletWebServerApplicationContext'
    ]},
    {'2.创建TomcatWebServer':[
        'refreshContext(context)',
        'AbstractApplicationContext类的refresh()方法->',
        'onRefresh()方法，初始化一些特别的类->',
        'ServletWebServerApplicationContext类的onRefresh()->createWebServer()方法'
    ]}
],
'ServletWebServerApplicationContext':[
    {'createWebServer()':[
        {'2.1.从容器中查找ServletWebServerFactory类型的bean':[
            'ServletWebServerFactory factory = getWebServerFactory()',
            '返回TomcatServletWebServerFactory'
        ]},
        {'2.2.创建WebServer':[
            'this.webServer = factory.getWebServer(getSelfInitializer())'
        ]}
    ]},
    {'getSelfInitializer()':[
        '->this::selfInitialize:',
        'for (ServletContextInitializer beans : getServletContextInitializerBeans()) {',
        '   beans.onStartup(servletContext);',
        '}',
        'getServletContextInitializerBeans()->new ServletContextInitializerBeans(getBeanFactory()):',
        '从beanFactory中获取所有ServletContextInitializer实现:addServletContextInitializerBeans(beanFactory);',
        'ServletRegistrationBean类的addRegistration():将DispatchServlet注入到servlet容器中'
    ]}
],
'TomcatServletWebServerFactor':[
    {'getWebServer()':[
        {'1.创建了Tomcat实例作为webServer的内部实现':[
            'Tomcat tomcat = new Tomcat()'
        ]},
        {'2.向Tomcat的Service容器注入Connector':[
            'tomcat.getService().addConnector(connector)'
        ]},
        {'3.准备上下文':[
            'prepareContext(tomcat.getHost(), initializers):',
            {'3.1.找所有ServletContextInitializer实现并合并为一个数组':[
                'ServletContextInitializer[] initializersToUse = mergeInitializers(initializers)'
            ]},
            {'3.2.将context加入host作为host的子容器':[
                'host.addChild(context)'
            ]},
            {'3.3.创建了TomcatStarter对象,并加入onainerInitializer列表':[
                {'configureContext(context, initializersToUse)':[
                    '创建了TomcatStarter对象',
                    'TomcatStarter starter = new TomcatStarter(initializers)',
                    '将starter加入context的conainerInitializer列表',
                    'context.addServletContainerInitializer(starter, NO_CLASSES)'
                ]}
            ]}
        ]}
    ]}
],
'TomcatStarter':[
    '实现ServletContainerInitializer接囗',
    {'初始化':[
        'TomcatStarter(ServletContextInitializer[] initializers) {',
		    'this.initializers = initializers;',
	    '}',
    ]},
    {'启动时加载':[
        'onStartup(Set<Class<?>> classes, ServletContext servletContext){',
        '   for (ServletContextInitializer initializer : this.initializers) {',
        '       initializer.onStartup(servletContext);',
        '   }',
        '}'
    ]}
],
'学习':[
    'https://www.cnblogs.com/zrbcool/p/11480675.html'
]

}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 