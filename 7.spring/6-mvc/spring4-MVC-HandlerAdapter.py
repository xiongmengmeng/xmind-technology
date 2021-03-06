import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="springMVC"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("HandlerAdapter")
r2=s2.getRootTopic()
r2.setTitle("HandlerAdapter")


content={
'初始化时':[
    '1.ApplicationContext初始化时建立所有url和controller类的对应关系(用Map保存)',
    '2.根据请求url找到对应的controller，并从controller中找到处理请求的方法',
    '3.request参数绑定到方法的形参，执行方法处理请求,并返回结果视图'
],
'springMVC请求处理流程':[
    '1.DispatcherServlet:SpringMVC中的前端控制器(front controller)，负责接收request',
    '2.HanlerMapping:SpringMVC中完成url到Controller映射的组件,从HandlerMapping查找处理request的controller',
    '3.Cntroller:处理request，并返回ModelAndView对象',
    '4.视图解析器解析ModelAndView对象并返回对应的视图给客户端'
],
'HandlerAdapter':[
    '调用处理器（Handler|Controller）',
    'Spring mvc采用适配器模式来适配调用指定Handler，根据Handler的不同种类采用不同的Adapter',
    {'Handler与 HandlerAdapter':[
        'Handler类别        对应适配器                      描述',
        'Controller         SimpleControllerHandlerAdapter 标准控制器(实现Controller接口)，返回ModelAndView',
        'HttpRequestHandler HttpRequestHandlerAdapter      实现HttpRequestHandler接囗,不需要通过modelAndView转到视图',
        'Servlet            SimpleServletHandlerAdapter    基于标准的servlet处理',
        'HandlerMethod      RequestMappingHandlerAdapter   用注解@Controller配置控制器,用@requestMapping配置方法'

    ]},
    '前后端交互通过json数据，利用@RequestBody和@ResponseBody实现数据到 java对象的绑定',
    {'请求参数封装':[
        '支持基本类型，POJO 类型和集合类型',
        {'RequestParam':[
            '@RequestParam():注解内容作为参数名',
            'request.getParameterValues():根据参数名获取的参数值'
        ]},
        {'RequestBody':[
            '把请求的json数组转为对象'
        ]},
        {'PathVariable':[
            '把请求URL中的参数，给我们控制器方法的形参赋值'
        ]}
    ]}
],
'AbstractHandlerMethodAdapter':[
    {'handle()->':[
        'handleInternal(request, response, (HandlerMethod) handler)'
    ]},
],
'RequestMappingHandlerAdapter':[
    {'handleInternal()':[
        'mav = invokeHandlerMethod(request, response, handlerMethod):',
        {'1.获取方法解析器':[
            'ServletInvocableHandlerMethod invocableMethod = createInvocableHandlerMethod(handlerMethod)'
        ]},
        {'2.执行方法':[
            'invocableMethod.invokeAndHandle(webRequest, mavContainer)'
        ]},
        {'3.封装结果视图':[
            'getModelAndView(mavContainer, modelFactory, webRequest)'
        ]}
    ]}
],
'invokeAndHandle()':[
    {'invokeForRequest()':[
        {'1.处理传参,完成request中的参数和方法参数上数据的绑定':[
            'Object[] args = getMethodArgumentValues(request, mavContainer, providedArgs)',
            {'详细':[
                '1.声明数组,用来存参数的值',
                'Object[] args = new Object[parameters.length]',
                '2.resolvers是否能处理传参',
                'this.resolvers.supportsParameter(parameter)',
                '3.将参数和方法参数上数据的绑定',
                'args[i] = this.resolvers.resolveArgument(parameter, mavContainer, request, this.dataBinderFactory)'
            ]}
        ]},
        {'2.调用方法,反射':[
            'doInvoke(args)'
        ]}
    ]},
    {'3.处理返回值':[
        'this.returnValueHandlers.handleReturnValue(returnValue, getReturnValueType(returnValue), mavContainer, webRequest)'
    ]}
]
}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 