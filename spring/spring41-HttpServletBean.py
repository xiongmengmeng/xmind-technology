import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="spring"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("HttpServletBean")
r2=s2.getRootTopic()
r2.setTitle("HttpServletBean")


content={
'HttpServletBean':[
    'SpringMVC基于Servlet来运行',
    'HttpServletBean继承HttpServlet,所以这个HttpServletBean为一个Servlet',
    {'Servlet的生命周期':[
        '1.tomcat启动时会去查询web.xml中的配置文件找到servlet配置，通过new关键字创建这个servlet的实例',
        '2.然后调用servlet的init方法去初始化，接着把这个servlet放入容器中管理，等待使用',
        '3.容器关闭时，tomcat会调用这个servlet的destroy方法来做一些善后工作'
    ]},
    {'init()':[
        '1.在Web.xml中读取配置文件',
        'new ServletConfigPropertyValues(getServletConfig(), this.requiredProperties)',
        '2.通过BeanWrapper代理器创建DispatcherServlet',
        'BeanWrapper bw = PropertyAccessorFactory.forBeanPropertyAccess(this);',
        '3.该类为空实现，由他的子类实现也就是FrameworkServlet',
        'initServletBean()'
    ]},
    {'doGet(HttpServletRequest req, HttpServletResponse resp)':[
        'doGet()--子类FrameworkServlet实现'
    ]}
],
'FrameworkServlet':[
    {'initServletBean()':[
        '1.webApplicationContext的初始化',
        {'initWebApplicationContext()':[
            {'1.1.createWebApplicationContext()':[
                '1.1.1.通过反射实例化Web上下文',
                'ConfigurableWebApplicationContext wac=BeanUtils.instantiateClass(contextClass);',
                '1.1.2.IOC的初始化流程',
                'configureAndRefreshWebApplicationContext(wac)->wac.refresh()'
            ]},
            '1.2.onRefresh()--子类DispatchServlet实现',
        ]},
        '2.空方法，在设置任何bean属性之后调用,子类可以覆盖此方法来执行它们需要的初始化',
        'initFrameworkServlet()',
    ]},
    {'doGet()':[
        'doService(request, response)--子类DispatchServlet实现'
    ]}

],
'DispatchServlet':[
    {'onRefresh(ApplicationContext context)':[
        '1.初始化文件上传处理',
        'initMultipartResolver(context);',
        '2.初始化处理器映射器(用来保存controller中配置的RequestMapping与Method对应关系)',
        'initHandlerMappings(context);',
        '3.初始化处理器适配器(用来动态匹配Method参数 包括类转换 动态赋值)',
        'initHandlerAdapters(context);',
        '4.初始化处理器异常处理',
        'initHandlerExceptionResolvers(context);'
    ]},
    {'doService(request, response)':[
        '->doDispatch(HttpServletRequest request, HttpServletResponse response)',
    ]},
    {'doDispatch(request, response)':[
        '',
        'checkMultipart(request)',
        '',
        'mappedHandler = getHandler(processedRequest);',
        '',
        'HandlerAdapter ha = getHandlerAdapter(mappedHandler.getHandler());',
        '',
        'mappedHandler.applyPreHandle(processedRequest, response)',
        ''
        'mv = ha.handle(processedRequest, response, mappedHandler.getHandler())',
        '',
        'mappedHandler.applyPostHandle(processedRequest, response, mv);',
        '',
        'processDispatchResult(processedRequest, response, mappedHandler, mv, dispatchException)'
    ]}
]
}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 