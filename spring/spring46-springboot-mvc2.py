import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="spring"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("组件初始化")
r2=s2.getRootTopic()
r2.setTitle("组件初始化")


content={
'自动加载开始':[
    '来源：spring-boot-autoconfigure/META-INF/spring.factories',
    {'spring.factories':[
        'org.springframework.boot.autoconfigure.EnableAutoConfiguration',
        'org.springframework.boot.autoconfigure.web.servlet.ServletWebServerFactoryAutoConfiguration',
        'org.springframework.boot.autoconfigure.web.servlet.DispatcherServletAutoConfiguration'
    ]},
],
'ServletWebServerFactoryAutoConfiguration':[
    {'类注解':[
        '@Import({ ServletWebServerFactoryAutoConfiguration.BeanPostProcessorsRegistrar.class,',
        'ServletWebServerFactoryConfiguration.EmbeddedTomcat.class,',
        'ServletWebServerFactoryConfiguration.EmbeddedJetty.class,',
        'ServletWebServerFactoryConfiguration.EmbeddedUndertow.class})',
    ]},
],
'ServletWebServerFactoryConfiguration.EmbeddedTomcat':[
    {'tomcatServletWebServerFactory()':[
        '向容器注入TomcatServletWebServerFactory的Bean实例',
    ]}
],
'DispatcherServletAutoConfiguration':[
    {'dispatcherServletRegistration()':[
        '向容器注入DispatcherServletRegistrationBean的Bean实例',
    ]}
],
'RegistrationBean':[
    '实现ServletContextInitializer接囗',
    {'重写onStartup(ServletContext servletContext)方法':[
        'SpringApplication.run()方法的流程中被调用到',
        {'register(description, servletContext)':[
            '子类DynamicRegistrationBean实现'
        ]}
    ]},
    {'子类DynamicRegistrationBean':[
        {'register(description, servletContext)':[
            'D registration = addRegistration(description, servletContext)',
            '子类ServletRegistrationBean实现'
        ]}
    ]},
    {'子类ServletRegistrationBean':[
        'String name = getServletName();',
        'return servletContext.addServlet(name, this.servlet);',
        '将DispatchServlet加入到Servlet容器'
    ]}
]
}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 