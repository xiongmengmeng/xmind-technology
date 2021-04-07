import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0,parentdir) 


import xmind
from xmind.core.markerref import MarkerId
xmind_name="springboot"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("DispatcherServletRegistrationBean")
r2=s2.getRootTopic()
r2.setTitle("DispatcherServletRegistrationBean")


content={
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
        '将Dispatcher加入Servlet容器',
        'String name = getServletName()',
		'servletContext.addServlet(name, this.servlet)'
    ]},
    {'getServlet()':[
        '返回this.servlet'
    ]}
],
'DispatcherServletRegistrationBean':[
    {'register(String description, ServletContext servletContext)':[
        'D registration = addRegistration(description, servletContext)模版方法',
        'configure(registration);'
    ]}
],
'加载DispatcherServletRegistrationBean':[
    'spring-boot-autoconfigure/META-INF/spring.factories:',
    'org.springframework.boot.autoconfigure.EnableAutoConfiguration=',
    'org.springframework.boot.autoconfigure.web.servlet.DispatcherServletAutoConfiguration,',
    {'DispatcherServletAutoConfiguration ':[
        '将DispatcherServletRegistrationBean 当作一个Bean注册到容器',
    ]}
],
'FilterRegistrationBean':[
    {'getFilter()':[
        '返回this.filter'
    ]}
],
'ServletListenerRegistrationBean':[
    {'getListener()':[
        '返回this.listener'
    ]}
],
'TomcatStarter':[
    '成员变量：ServletContextInitializer[] initializers'
    '实现ServletContainerInitializer接囗，重写onStartup()方法：',
    '调用所有注入的initializers的onStartup方法',
]

}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 