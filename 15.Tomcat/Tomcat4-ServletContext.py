import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="tomcat"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("ServletContext")
r2=s2.getRootTopic()
r2.setTitle("ServletContext")


content={
'ServletContext':[
    'Servlet上下文,代表当前应用，本质是个容器,一个map',
    {'创建与销毁时机':[
        '服务器启动与关闭'
    ]},
    {'作用':[
        '在整个Web应用的动态资源（Servlet/JSP）间共享数据'
    ]},
    {'装载共享数据的对象(域对象),JavaWeb中有4个':[
        'ServletContext域（Servlet间共享数据）',
        'Session域（一次会话间共享数据，也可以理解为多次请求间共享数据）',
        'Request域（同一次请求共享数据）',
        'Page域（JSP页面内共享数据）'
    ]},
    {'与web.xml关系':[
        'Tomcat根据web.xml创建ServletContext对象',
        '1.整个web.xml代表ServletContext',
        '2.<servlet>代表servlet',
        '3.init-param中的数据封装为servletConfig'
    ]},
    {'获取ServletContext的5种方式':[
        {'1.ServletConfig#getServletContext()':[
            'ServletConfig对象包含着ServletContext对象',
            'ServletConfig维系着ServletContext的引用'
        ]},
        {'2.GenericServlet#getServletContext()':[
            {'GenericServlet:':[
                '1.init方法：将Tomcat传入的ServletConfig对象作用域由局部变量提升到成员变量',
                '2.getServletContext(),通过ServletConfig得到ServletContext',
            ]}
        ]},
        {'3.HttpSession#getServletContext()':[
            'session.getServletContext()'
        ]},
        {'4.HttpServletRequest#getServletContext();':[
            'request.getServletContext()'
        ]},
        {'5.ServletContextEvent#getServletContext()':[
            'ServletContextEvent包装了ServletContext'
        ]}
    ]}
],
'Filter的4种拦截方式':[
    'REQUEST:浏览器发起，请求到服务器（默认）',
    'FORWARD/INCLUDE:服务器内部的流程，不涉及浏览器',
    'ERROR:发生页面错误时发生'
],
'Servlet映射器':[
    'Tomcat中一个叫Mapper的类',
    {'大概作用':[
        '对于静态资源，Tomcat最后交由DefaultServlet类来处理',
        '对于Servlet ，Tomcat最后交由自定义的Servlet类来处理',
        '对于JSP，Tomcat最后交由JspServlet类来处理'
    ]}
],
'自定义DispatcherServlet':[
    '一个Servlet',
    {'类的doGet方法':[
        '1.通过servletConfig获取springMVC配置文件位置',
        '2.解析文件，反射创建bean,存入springMvc的IOC容器',
        '3.解析url,到IOC容器中找到匹配Bean处理请求'
    ]},
    '需在web.xml中配置类，和类的拦截方式',
    {'拦截方式':[
        '*.do：拦截.do结尾,各Servlet和谐相处',
        '/*：拦截所有,DefaultServlet、JspServlet及我们自己写的其他Servlet都失效',
        '/：拦截所有，但不包括JSP,DefaultServlet失效',
    ]}
],
'conf/web.xml与应用的web.xml':[
    {'conf/web.xml':[
        'Tomcat全局配置web.xml',
        '配置DefaultServlet及其映射路径',
        '配置JspServlet及其映射路径'
    ]},
    'conf/web.xml中的配置相当于写在了每一个应用的web.xml中',
    '每个应用默认都配置了JSPServlet和DefaultServlet处理JSP和静态资源'
]

}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 