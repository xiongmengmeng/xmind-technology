import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0,parentdir) 


import xmind
from xmind.core.markerref import MarkerId
xmind_name="springboot"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("刷新应用上下文")
r2=s2.getRootTopic()
r2.setTitle("刷新应用上下文")


content={
'refreshContext(context)':[
        '方法内部最终调用了((AbstractApplicationContext) applicationContext).refresh()',
        'refresh()方法中，初始化Bean前，调用onRefresh()方法'
],
'ServletWebServerApplicationContext':[
    {'onRefresh()':[
        '核心方法：createWebServer()',
        {'内容':[
            {'1.ServletWebServerFactory factory=getWebServerFactory()':[
                '实际返回TomcatServletWebServerFactory'
            ]},
            {'2.factory.getWebServer(getSelfInitializer())':[
                '创建了Tomcat实例,并将context加入其host'
            ]}
        ]}
    ]},
    {'getSelfInitializer()':[
        {'方法内容：this::selfInitialize':[
            'for (ServletContextInitializer beans : getServletContextInitializerBeans()) {',
            '	beans.onStartup(servletContext);',
            '}',
            {'注':[
                'getServletContextInitializerBeans():',
                '获取spring容器中所有的ServletContextInitializer实现'
            ]}
        ]},
        '方法返回值：ServletContextInitializer',
    ]}
],
'TomcatServletWebServerFactory':[
    {'加载方式':[
        'spi方式+EnableAutoConfiguration指定',
        '加载ServletWebServerFactoryAutoConfiguration',
        {'ServletWebServerFactoryAutoConfiguration':[
            '@Import引入ServletWebServerFactoryConfiguration.EmbeddedTomcat.class:',
            '如包含tomcat的jar包,向容器注册TomcatServletWebServerFactory'
        ]}
    ]},
    {'getWebServer(getSelfInitializer())':[
        {'1.创建了Tomcat实例':[
            'Tomcat tomcat = new Tomcat()',
        ]},
        {'2.向Tomcat的Service容器注入Connector':[
            'tomcat.getService().addConnector(connector);'
        ]},
        {'3.将context加入host':[
            'prepareContext(tomcat.getHost(), initializers)'
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
        '3.1.创建了TomcatStarter对象:',
        'TomcatStarter starter=new TomcatStarter(initializers)',
        '3.2.将starter加入context的conainerInitializer列表:',
        'context.addServletContainerInitializer(starter, NO_CLASSES)'

    ]}
],
# '学习':[
#     'https://www.cnblogs.com/zrbcool/p/11480675.html#dispatcherservletregistrationbean',
# ]
}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 