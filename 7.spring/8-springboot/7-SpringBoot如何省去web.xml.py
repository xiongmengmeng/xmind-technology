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
    'ContextLoaderLisenter:创建ioc容器',
    'DispatcherServlet:创建派发器'
],
'注解':[
    '@WebServlet',
    '@WebFilter',
    '@WebListenter'
],
'SPI方式':[
    '文件名：META-INF/services/javax.servlet.ServletContainerInitializer',
    '文件内容：org.springframework.web.SpringServletContainerInitializer'
],
'Servlet3.0---tomcat.start()':[
    '1.tomcat启动',
    '2.调用SpringServletContainerInitializer.onStartup()方法',
    '3.将@HandlesTypes标注的类，加载到内存，传入onStartup的值参'
],
'SpringServletContainerInitializer':[
    '类注解:@HandlesTypes(WebApplicationInitializer.class)',
    '实现ServletContainerInitializer接囗',
    {'重写onStartup()方法':[
        '1.过滤webapplicationinitializer实现类为接囗，抽象类的',
        '2.反射创建实例，加入集合',
        '3.排序',
        '4.调用实例的onStartup方法'
    ]}
],
'SpringBootServletInitializer':[
    'WebApplicationInitializer的实现类',
    {'onStartup()':[
        'createRootApplicationContext(servletContext),返回WebApplicationContext类型:',
        '1.SpringApplication application = builder.build()',
        '2.application.run()'

    ]}
]
}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 