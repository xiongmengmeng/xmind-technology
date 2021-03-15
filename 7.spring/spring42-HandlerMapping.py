import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="spring"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("HandlerMapping")
r2=s2.getRootTopic()
r2.setTitle("HandlerMapping")


content={
'概念解析':[
    {'RequestMappingInfo类':[
        '@RequestMapping的一个对应类'
    ]},
    {'HandlerMethod类':[
        '封装了处理器实例（Controller Bean）和 处理方法实例（Method）以及方法参数数组（MethodParameter[]）',
    ]},
    {'MethodParameter':[
        '封装了方法某个参数的相关信息及行为，如参数索引，参数所属方法实例或构造器实例，该参数的类型等'
    ]},
    {'HandlerMapping接囗':[
        '定义请求和处理器之前的映射关系',
        {'方法 getHandler()':[
            '传参：HttpServletRequest request',
            '返回值：HandlerExecutionChain'
        ]},
    ]},
    {'AbstractHandlerMethodMapping':[
        'HandlerMapping的一个基本实现类',
        '定义了请求与HandlerMethod实例的映射关系',
        '实现接囗InitializingBean,重写afterPropertySet()方法'
    ]},
    {'RequestMappingInfoHandlerMapping':[
        'AbstractHandlerMethodMapping的实现类',
        '维护了一个RequestMappingInfo和HandlerMethod的Map属性',
    ]},
    {'RequestMappingHandlerMapping':[
        'RequestMappingInfoHandlerMapping的子类',
        '将@RequestMapping注解转化为RequestMappingInfo实例，并为父类使用',
    ]},
],
'DispatcherServlet.getHandler(processedRequest)':[
    'for循环this.handlerMappings->HandlerMapping hm',
    'HandlerExecutionChain handler = hm.getHandler(request)',
    '注：HandlerMapping这个接口由AbstractHandlerMapping来实现'
],
'AbstractHandlerMapping':[
    {'getHandler(HttpServletRequest request)':[
        '1. 根据request获取handler',
        'Object handler = getHandlerInternal(request);--AbstractHandlerMethodMapping来实现',
        '2.如果handler是字符串类型,handler是bean名称,根据名称获取handler bean对象',
        'handler = getApplicationContext().getBean(handlerName)',
        '3.封装handler执行链:HandlerExecutionChain',
        {'getHandlerExecutionChain()':[
            {'HandlerExecutionChain':[
                'List<HandlerInterceptor> interceptorList：拦截器',
                'Object handler:controller的方法',
            ]},
            '3.1.获取request中的url',
            'String lookupPath = this.urlPathHelper.getLookupPathForRequest(request, LOOKUP_PATH)',
            '3.2.遍历this.adaptedInterceptors，获得HandlerInterceptor interceptor',
            '如interceptor是MappedInterceptor类型，先用lookupPath匹配，再添加到HandlerExecutionChain chain的interceptors中',
            '否则直接添加到HandlerExecutionChain chain的interceptors中'
        ]}
    ]}
]
}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 