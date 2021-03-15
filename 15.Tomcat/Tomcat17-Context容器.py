import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="tomcat"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("Context容器")
r2=s2.getRootTopic()
r2.setTitle("Context容器")


content={
'Context容器':[
    '一个Context对应一个Web应用程序',
    {'Context容器组件':[
        {'Context容器的配置文件':[
            'Tomcat的server.xml配置文件中的<Context>节点',
            'Tomcat的web.xml',
            '项目的web.xml',
        ]},
        '包装器——Wrapper',
        'Context域——Realm',
        '访问日志——AccessLog',
        '错误页面——ErrorPage：对应web.xml中的error-page元素',
        '会话管理器——Manager',
        '目录上下文——DirContext：通过某些字符串便捷地获取对应的内容',
        '安全认证：web.xml中<security-constraint>和<login-config>元素的映射',
        'Jar扫描器——JarScanner：对Web应用的WEB-INF/lib目录的Jar包进行扫描',
        {'过滤器':[
            '对应web.xml中的filter元素',
            {'过滤器模块的主要对象':[
                'FilterDef',
                'ContextFilterMaps',
                'ApplicationFilterConfig'
            ]}
        ]},
        '命名资源——NamingResource:将配置文件中声明的不同的资源及其属性映射到内存中',
        'Servlet映射器——Mapper',
        '管道——Pipeline',
        'Web应用载入器——WebappLoader:真正完成类加载工作的加载器WebappClassLoader',
        'ServletContext的实现——ApplicationContext:实现了ServletContext接口',
        '实例管理器——InstanceManager:实现对Context容器中监听器、过滤器以及Servlet等实例的管理',
        'ServletContainerInitializer初始化器：在Web容器启动时为让第三方组件机做一些初始化工作，例如注册Servlet或者Filters等',
        'Context容器的监听器'
    ]}
]
}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 