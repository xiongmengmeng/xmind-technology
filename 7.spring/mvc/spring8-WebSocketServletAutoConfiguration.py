import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0,parentdir) 


import xmind
from xmind.core.markerref import MarkerId
xmind_name="springMVC"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("WebSocketServletAutoConfiguration")
r2=s2.getRootTopic()
r2.setTitle("WebSocketServletAutoConfiguration")


content={
'DispatcherServlet':[
    '主控制器'
],
'HttpServletBean':[
    '覆写init()方法:将web.xml中配置的参数设置到Servlet中'
],
'FrameworkServlet':[
    '将Servlet上下文与Spring容器上下文关联',
    '初始化FrameworkServlet属性webApplicationContext(代表SpringMVC上下文对象),类型ConfigurableWebApplicationContext',
    '如项目中用到spring,它有父容器，既web.xml 中配置的ContextLoaderListener 监听器初始化的容器上下文'
],
'HandlerMapping接口':[
    '根据当前请求找到对应的Handler（HandlerMethod(Controller中的方法)、 Controller对象）',
    '将Handler与一堆HandlerInterceptor（拦截器）封装到HandlerExecutionChain对象中',
    {'方法':[
        'HandlerExecutionChaingetHandler(HttpServletRequestrequest)'
    ]},
    {'实现类':[
        'AbstractHandlerMapping',
        'AbstractHandlerMethodMapping（得到HandlerMethod）',
        'AbstractUrlHandlerMapping（得到Controllert）'
    ]}
],
'HandlerAdapter接口':[
    '使用适配器模式来解决不同Handler 的执行',
    '根据Handler找到支持它的HandlerAdapter，通过HandlerAdapter执行Handler得到ModelAndView 对象',
    {'方法':[
        'booleansupports(Objecthandler)：判断是否支持传入的Handler ModelAndView',
        'handle(HttpServletRequest request, HttpServletResponse response, Object handler)：使用Handler处理请求',
        'long getLastModified(HttpServletRequest request, Object handler)：获取资料的Last-Modified值'
    ]},
    {'实现类':[
        {'AbstractHandlerMethodAdapter抽象类':[
            '利用RequestMappingHandlerMapping获取的Handler是HadnlerMethod类型',
            '代表Controller里要执行的方法',
            'handlerInternal 是子类 RequestMappingHandlerAdapter 中的方法'
        ]},
        {'RequestMappingHandlerAdapter类':[
            '执行@RequestMapping注解的方法'
        ]},
        {'HttpRequestHandlerAdapter类':[
            '执行HttpRequestHandler类型的Handler',
            '其实就是Controller中的handleRequest方法'
        ]},
        {'SimpleControllerHandlerAdapter类':[
            'Controller实现类的适配器',
            '其本质也是执行 Controller 中的 handleRequest 方法',
        ]},
        {'SimpleServletHandlerAdapter类':[
            'Servlet的适配器，其最终执行的方法是Servle的service方法',
        ]}
    ]}
],
'注意':[
    'HandlerMapping跟HandlerAdapter都在spring-webmvcjar中，servlet架包下的DispatcherServlet.properties配置文件',
    {'HandlerMapping':[
        'BeanNameUrlHandlerMapping：XML配置方式的控制器',
        'RequestMappingHandlerMapping：注解方式的控制器',
        'RouterFunctionMapping'
    ]},
    {'HandlerAdapter':[
        'HttpRequestHandlerAdapter',
        'SimpleControllerHandlerAdapter：XML的配置方式',
        'RequestMappingHandlerAdapter：注解的配置方式',
        'HandlerFunctionAdapter'
    ]}
]
}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 