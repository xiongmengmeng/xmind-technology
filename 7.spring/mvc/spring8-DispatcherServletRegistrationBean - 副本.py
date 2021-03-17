import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0,parentdir) 


import xmind
from xmind.core.markerref import MarkerId
xmind_name="springMVC"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("TomcatServletWebServerFactory")
r2=s2.getRootTopic()
r2.setTitle("TomcatServletWebServerFactory")


content={
'加载':[
    'org.springframework.boot.autoconfigure.EnableAutoConfiguration=',
    'org.springframework.boot.autoconfigure.web.servlet.ServletWebServerFactoryAutoConfiguration',
    {'ServletWebServerFactoryAutoConfiguration':[
        '@Import部分引入了ServletWebServerFactoryConfiguration.EmbeddedTomcat.class:',
        '向容器注册TomcatServletWebServerFactory'
    ]}
],
'ServletContextInitializer接囗':[
    'onStartup(ServletContext servletContext)'
],
'RegistrationBean':[
    {'重写onStartup(ServletContext servletContext)方法':[
        'register(description, servletContext)模版方法'
    ]}
],
'DynamicRegistrationBean':[
    {'register(String description, ServletContext servletContext)':[
        'D registration = addRegistration(description, servletContext)模版方法',
        'configure(registration);'
    ]}
],
'ServletRegistrationBean':[
    {'ServletRegistration.Dynamic addRegistration(String description,ServletContext servletContext)':[
        '将Dispatcher加入Servlet',
        'String name = getServletName()',
		'servletContext.addServlet(name, this.servlet)'
    ]}
]
'DispatcherServletRegistrationBean':[
    {'register(String description, ServletContext servletContext)':[
        'D registration = addRegistration(description, servletContext)模版方法',
        'configure(registration);'
    ]}
]

}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 