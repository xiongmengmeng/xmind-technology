import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="tomcat"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("Servlet规范")
r2=s2.getRootTopic()
r2.setTitle("Servlet规范")


content={
'定义':[
    '描述HTTP请求及响应处理过程相关的对象及其作用',
    'Java体系的Web服务器都会遵循Servlet规范',
    'Tomcat是一个Servlet容器，它也需要遵守Servlet规范',
    '在Servlet容器中，每个Servlet类只能对应一个Servlet对象，所有请求都由同一个Servlet对象处理',
    '对于Web容器来说，实现SingleThreadModel接口意味着一个Servlet对象对应着一个线程',
],
'Servlet接口':[
    {'两个Servlet类':[
        'GenericServlet：通用的、协议无关的Servlet',
        {'HttpServlet':[
            'HTTP的Servlet',
            'service方法把HTTP协议的GET请求转发到doGet处理方法',
            'POST、PUT、DELETE、HEAD、OPTIONS、TRACE请求同上'
        ]}
    ]},
    {'核心方法:service方法':[
        '处理客户端请求的方法',
        '客户端发起的请求会被路由到对应的Servlet对象上',
    ]},
    {'Servlet的生命周期':[
        '加载实例化:由Web容器完成',
        {'初始化':[
            '对应Servlet的init方法(参数为ServletConfig)',
            'ServletConfig为web.xml文件中配置的初始化参数',
            '由Web容器完成web.xml配置读取并封装成ServletConfig对象'
        ]},
        {'处理客户端请求':[
            '对应Servlet的service方法',
            '请求被封装成ServletRequest类型的请求对象和ServletResponse类型的响应对象'
        ]},
        {'销毁':[
            '对应Servlet的destroy方法',
            '调用destroy方法前要保证所有正在执行service方法的线程都完成执行',
            '把Servlet从Web容器中移除'
        ]}
    ]},
    {'ServletRequest接口':[
        '实现类封装了客户端请求的所有信息',
        'HTTP对应HttpServletRequest类,包含请求行和请求头部'
    ]},
    {'ServletContext接口':[
        '定义了运行所有Servlet的Web应用的视图',
        '添加Servlet,Filter,Listener到ServletContext里的方法'
    ]},
    {'ServletResponse接口':[
        '封装了服务器要返回客户端的所有信息'
    ]},
    {'Filter接口':[
        '允许Web容器对请求和响应做统一处理'
    ]},
    {'会话':[
        'HTTP对应的会话接口：HttpSession',
        'Cookie：常用的会话跟踪机制，标准名字JSESSIONID，会话ID通过调用HttpSession.getId()获取',
        'HttpSession对象限定在ServletContext级别，会话里面的属性不能在不同ServletContext之间共享',
        '分布式环境中，会话的所有请求在同一时间必须仅被一个JVM处理',
        '分布式容器迁移会话时会通知实现了HttpSessionActivationListener接口的所有会话属性'
    ]},
    {'注解':[
        '@WebServlet,@WebFilter,@WebInitParam,@WebListener'
    ]},
    {'Web应用':[
        '与ServletContext接口对象1：1，ServletContext对象提供了一个Servlet和它的应用程序视图',
        {'Web应用部署到容器':[
            '实例化web.xml中<listener>元素标识的每个事件监听器的一个实例',
            '对于已实例化且实现了ServletContextListener接口的监听器实例，调用contextInitialized()方法',
            '实例化web.xml中<filter>元素标识的每个过滤器的一个实例，并调用每个过滤器实例的init()方法',
            '根据load-on-startup 元素值定义的顺序，包含<load-on-startup>元素的<servlet>元素为每个Servlet实例化一个实例，并调用每个Servlet实例的init()方法'
        ]},
        '对不包含Servlet、Filter或Listener的Web应用，或使用注解声明的Web应用，不需要web.xml部署描述符'
    ]},
    'Servlet映射'
]
}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 