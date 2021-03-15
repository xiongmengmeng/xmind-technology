import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="Tomcat"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("Tomcat")
r2=s2.getRootTopic()
r2.setTitle("Tomcat")


content={
'基础':[
    'HTTP协议',
    {'服务器作用':[
        '将资源对外暴露',
        '配合各种传输协议进行响应输出'
    ]},
    'Tomcat服务器 = Web服务器 + Servlet/JSP容器（Web容器）',
    'Cookie与Session'
],
'Tomcat架构':[
    {'Server':[
        {'Service':[
            'Connector',
            {'Engine':[
                'Context'
            ]}
        ]}
    ]}
],
'ServletContext':[
    '代表当前应用',
    '根据web.xml创建',
    {'核心内容':[
        'Filter',
        'Listener'
        'Servlet映射器',
    ]}


],
'Filter':[
    {'核心方法：doFilter':[
        '拦截逻辑',
        'chain.doFilter(request, response)',
    ]},
    '责任链模式'
],
'Listener':[
    '监听器6+2',
    {'核心':[
        'ServletContextListener',
        'ServletRequestListener',
        'HttpSessionListener'
    ]},
    '核心方法：contextInitialized()',
    {'ContextLoaderListener':[
        '实现ServletContextListener接囗',
        'contextInitialized()->初始化Spring的IOC容器'
    ]}
],
'servlet':[
    {'5个方法':[
        '1.void init(ServletConfig config)',
        '2.ServletConfig getServletConfig()',
        '3.service(ServletRequest req, ServletResponse res):处理请求',
        '4.String getServletInfo()',
        '5.void destroy()'
    ]},
    'GenericServlet',
    'HttpServlet'
],
}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 