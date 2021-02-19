import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="spring"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("getHandler()")
r2=s2.getRootTopic()
r2.setTitle("getHandler()")


content={
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
        '3.封装handler执行链',
        {'HandlerExecutionChain executionChain = getHandlerExecutionChain()':[
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
],
'AbstractHandlerMethodMapping':[
    {'MappingRegistry':[
        {'MultiValueMap<String, T> urlLookup':[
            '例"/register" -> "{GET /register}"'
        ]},
        {'private final Map<T, HandlerMethod> mappingLookup':[
            '例"{GET /register}" -> "com.springboot.chapter2.security10.HelloController#register(String, String, String)"'
        ]}
    ]},
    {'Match':[
        {'T mapping':[
            '例{GET /register}'
        ]},
        {'HandlerMethod handlerMethod':[
            {'Object bean':[
                 '例helloController'
            ]},
            {'Class<?> beanType':[
                '例class com.springboot.chapter2.security10.HelloController'
            ]},
            {'Method method':[
                '例public java.lang.Object com.springboot.chapter2.security10.HelloController.register(java.lang.String,java.lang.String,java.lang.String)'
            ]}
        ]}
    ]},
    {'Object handler = getHandlerInternal(request)':[
        '1.获取request中的url,用来匹配handler',
        'String lookupPath = getUrlPathHelper().getLookupPathForRequest(request)',
        '2.根据路径寻找handler',
        {'HandlerMethod handlerMethod = lookupHandlerMethod()':[
            '2.1.直接匹配',
            'List<T> directPathMatches = this.mappingRegistry.getMappingsByUrl(lookupPath)-->this.urlLookup.get(urlPath)',
            '2.2.存在匹配 则添加到匹配列表中',
            'addMatchingMappings(directPathMatches, matches, request)',
            '2.3.存在匹配,排序之后获取第一个',
            'Match bestMatch = matches.get(0)',
            '2.4.设置request参数',
            'handleMatch(bestMatch.mapping, lookupPath, request)',
            '2.5.返回匹配的url处理方法',
            'bestMatch.handlerMethod'           
        ]}
    ]}
]
}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 