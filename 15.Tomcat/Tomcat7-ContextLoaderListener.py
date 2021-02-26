import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="tomcat"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("ContextLoaderListener")
r2=s2.getRootTopic()
r2.setTitle("ContextLoaderListener")


content={
'ContextLoaderListener':[
    '一个监听器',
    '由Spring编写并提供',
    '搭建SSM框架时，需在web.xml中配置它',
    '继承ContextLoader类',
    '实现ServletContextListener接囗',
    {'contextInitialized()':[
        'initWebApplicationContext():初始化Spring的IOC容器的'
    ]},
    {'使用过程':[
        '1.web.xml中配置监听器，org.springframework.web.context.ContextLoaderListener',
        '2.tomcat启动时，解析web.xml,反射创建ContextLoaderListener,并其加载到servletContext(web.xml代表ServletContext)',
        '3.servletContext调用init()方法，调用ContextLoaderListener的contextInitialized(ServletContextEvent sce)方法',
        '4.contextInitialized()内，调用initWebApplicationContext()初始化Spring的IOC容器的'
    ]}
],
'注意几个类的关系':[
    'ServletContext对象是Tomcat的',
    'ServletContextListener是Tomcat提供的接口',
    'ContextLoaderListener是Spring写的，实现了ServletContextListener',
],
'ContextLoader':[
    {'initWebApplicationContext(ServletContext servletContext)':[
        '返回值WebApplicationContext：',
        '1.this.context = createWebApplicationContext(servletContext)：传入servletContext对象创建空的IOC容器',
        '2.sc.getInitParameter(CONFIG_LOCATION_PARAM):以contextConfigLocation为key从web.xml中取得spring-context.xml文件位置',
        '3.wac.refresh()：根据spring-context.xml初始化容器',
        '4.servletContext.setAttribute(WebApplicationContext.ROOT_WEB_APPLICATION_CONTEXT_ATTRIBUTE, this.context)：将IOC容器存入servletContext'
    ]}
],
'WebApplicationContextUtils':[
    {'getWebApplicationContext(ServletContext sc)':[
        'Spring提供的工具类，从ServletContext中取出IOC容器'
    ]}
],
'学习':[
    'https://zhuanlan.zhihu.com/p/65258266'
]


}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 