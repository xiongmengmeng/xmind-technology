import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="shiro"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("ShiroFilter")
r2=s2.getRootTopic()
r2.setTitle("ShiroFilter")


content={
'ShiroFilter':[
    '一个入口来拦截需要安全控制的URL,里面封装了各过滤器',
    {'自定义认证过滤器':[
        '继承AuthenticatingFilter',
        '重写isAccessAllowed()方法,返回false，执行下述方法',
        {'重写onAccessDenied()方法':[
            '1.判断请求是否有token，没有返回401',
            '2.否则调用认证方法executeLogin(request, response)：subject.login(token)'
        ]},
        '方法调用中用到了大量的模版方法',
        '需要从顶级父类org.apache.shiro.web.servlet.OncePerRequestFilter#doFilter',
        '或org.apache.shiro.web.servlet.AdviceFilter#doFilterInternal跟踪下来才能找出上述重写方法的调用处'
    ]},
    {'DelegatingFilterProxy类':[
        '自动到spring容器查找名字为shiroFilter（filter-name）的bean并把filter请求交给它处理',
    ]}
],
'各Filter':[
    '1.NameableFilter：给Filter起个名字，如果没有设置默认是FilterName',
    '2.ShiroFilter:提供AOP风格的支持，类似于SpringMVC中的Interceptor',
    {'3.AdviceFilter':[
        'preHandler()：类似于AOP中的前置增强；在拦截器链执行之前执行；如返回true继续拦截器链',
        'postHandle()：类似于AOP中的后置返回增强；在拦截器链执行完后执行；进行后处理',
        'afterCompletion()：类似于AOP中的后置最终增强；即不管有没有异常都会执行；可以进行清理资源'
    ]},
    {'4.AccessControlFilter':[
        '提供了访问控制的基础功能；比如是否允许访问/当访问拒绝时如何处理等',
        'isAccessAllowed()：是否允许访问；mappedValue就是[urls]配置中拦截器参数部分，如允许访问返回true',
        'onAccessDenied()：访问拒绝时是否已经处理了,如返回true表示需要继续处理；返回false表示该拦截器实例已经处理了，将直接返回'
    ]}
],
'拦截器链FilterChain':[
    {'DelegatingFilterProxy#doFilter()':[
        '1.得到其配置的过滤器，shiroFilter',
        {'2.调用AbstractShiroFilter的doFilterInternal()方法':[
            '2.1.创建Subject对象：createSubject(request, response)',
            {'2.2.调用组装过滤器链':[
                '找到FilterChainResolver的实现类',
                '组装过滤器链ProxiedFilterChain(对Servlet容器的FilterChain进行了代理)',
                {'递归调用执行过滤器链的方法':[
                    '先执行Shiro自己的Filter 链',
                    '再执行Servlet容器的Filter链'
                ]}
            ]},
            '2.3.执行过滤器相映的方法'
        ]}
    ]},
    {'AbstractShiroFilter':[
        '属性FilterChainResolver，其实现为PathMatchingFilterChainResolver',
        {'FilterChain getExecutionChain(..FilterChain origChain)':[
            '1.如果请求经PathMatchingFilterChainResolver匹配',
            '2.成功请求会先经过shiro Filter链（ProxiedFilterChain），之后再走剩下的servlet Filter链',
            '3.不成功，则直接走剩下的servlet Filter链',
            {'细节':[
                '通过FilterChainResolver根据配置文件中[urls]部分与请求URL是否匹配解析得到',
                'PathMatchingFilterChainResolver内部通过FilterChainManager维护着拦截器链',
                '如DefaultFilterChainManager实现维护着url模式与拦截器链的关系',
                'Shiro对Servlet容器的FilterChain进行了代理，生成代理FilterChain：ProxiedFilterChain'
            ]}
        ]}
    ]},
]
}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 