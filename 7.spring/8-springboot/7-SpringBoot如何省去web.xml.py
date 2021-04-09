import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0,parentdir) 


import xmind
from xmind.core.markerref import MarkerId
xmind_name="springboot"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("springBoot如何省去web.xml")
r2=s2.getRootTopic()
r2.setTitle("springBoot如何省去web.xml")


content={
'存在web.xml时':[
    'Servlet容器根据web.xml中的配置初始化jar包',
    'web.xml是jar包和Servlet联系的中介'
],
'Servlet3.0容器':[
    'javax.servlet.ServletContainerInitializer中的实现替代了web.xml的作用',
    '@HandlesTypes注解中指定的感兴趣的类，可理解为具体实现了web.xml的功能',
    {'容器启动时':[
        '1.通过SPI扩展机制自动扫描所有已添加的jar包下的META-INF/services/javax.servlet.ServletContainerInitializer中指定的类，并实例化该类',
        '2.回调ServletContainerInitializer的实现类的onStartup方法',
        '3.如该类存在@HandlesTypes注解，且在注解中指定类，调用注解指定类的onStartup方法'
    ]},
    'org.springframework:spring-web工程下，META-INF/services/javax.servlet.ServletContainerInitializer文件中:',
    'org.springframework.web.SpringServletContainerInitializer'

],
'SpringServletContainerInitializer':[
    '@HandlesTypes(WebApplicationInitializer.class)',
    '实现ServletContainerInitializer接囗',
    {'重写onStartup()方法':[
        '调用webapplicationinitializer所有实现类的onStartup方法'
    ]}
],
'WebApplicationInitializer':[
    '接口的实现类:实现了web.xml中配置文件中配置DispatcherServlet的内容'
],
'SpringBootServletInitializer':[
    'WebApplicationInitializer的实现类',
    {'onStartup':[
        {'createRootApplicationContext(servletContext)':[
            '返回值WebApplicationContext类型',
            '1.SpringApplication application = builder.build()',
            '2.application.run()'
        ]}
    ]}
],
'学习':[
    'https://www.cnblogs.com/hello-shf/p/10926271.html',
    'https://www.cnblogs.com/hello-shf/p/10952362.html'
]
}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 