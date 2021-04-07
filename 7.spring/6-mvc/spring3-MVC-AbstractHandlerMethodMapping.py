import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="springMVC"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("AbstractHandlerMethodMapping")
r2=s2.getRootTopic()
r2.setTitle("AbstractHandlerMethodMapping")


content={

'MappingRegistry':[
    {'MultiValueMap<String, T> urlLookup':[
        '例"/register" -> "{GET /register}"'
    ]},
    {'private final Map<T, HandlerMethod> mappingLookup':[
        '例"{GET /register}" -> "com.springboot.chapter2.security10.HelloController#register(String, String, String)"'
    ]}
],
'Match':[
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
],
'afterPropertySet()':[
    '1.通过容器获得所有的Bean',
    '2.遍历Bean,如Bean上有Controller或RequestMapping注解，执行detectHandlerMethods()方法',
    '3.遍历handler(Bean)中的所有方法，找出其中被@RequestMapping注解标记的方法',
    '4.然后遍历这些方法，生成RequestMappingInfo实例',
    '5.将RequestMappingInfo实例以及处理器方法注册到缓存中',
    '6.再遍历这些方法，生成HandlerMethod实例',
    '7.将HandlerMethod实例以及处理器方法注册到缓存中Map<T, HandlerMethod> mappingLookup',
],
'Object handler = getHandlerInternal(request)':[
    '1.获取request中的url,用来匹配handler',
    'String lookupPath = getUrlPathHelper().getLookupPathForRequest(request)',
    '2.根据路径寻找handler(类型是HandlerMethod)',
    {'lookupHandlerMethod()':[
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
]


}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 