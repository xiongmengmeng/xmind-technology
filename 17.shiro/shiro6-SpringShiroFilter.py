import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="shiro"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("SpringShiroFilter")
r2=s2.getRootTopic()
r2.setTitle("SpringShiroFilter")


content={
'ShiroFilterFactoryBean':[
    '实现了FactoryBean',
    {'getObject方法':[
        '创建了一个实例SpringShiroFilter',
        '并注册到了spring容器'
    ]},
    {'SpringShiroFilter':[
        '作用:生成shiro的代理filter链ProxiedFilterChain，并将请求交给ProxiedFilterChain'
    ]}
],
'ServletContextInitializerBeans':[
    {'addServletContextInitializerBeans(beanFactory)':[
        '会将spring bean工厂中类型是ServletContextInitalizer类型的实例',
        '添加进ServletContextInitializerBeans的initializers属性中',
        {'ServletContextInitalizer类型的实例':[
            'ServletRegistrationBean',
            'FilterRegistrationBean',
            'DelegatingFilterProxyRegistrationBean',
            'ServletListenerRegistrationBean'
        ]}
    ]},
    {'addAdaptableBeans(beanFactory)':[
        '会将beanFactory中的Servlet、Filter、Listener实例封装成对应的RegistrationBean',
        '然后添加到ServletContextInitializerBeans的initializers',
    ]}
],
'shiro中的Filter链':[
    '除SpringShiroFilter外，shiro还有默认的11个Filter',
    '创建DefaultFilterChainManager，会把默认的11个Filter添加到它的filters中',
    {'SpringShiroFilter的doFilter方法':[
        '1.路径匹配：pathMatches(pathPattern, requestURI)，默认的Fliter逐个与请求URI进行匹配',
        '2.代理FilterChain：ProxiedFilterChain',
        '3.如果匹配不上，那么直接走servlet的FilterChain',
        '4.否则先走shiro的代理FilterChain（ProxiedFilterChain），之后再走servlet的FilterChain'
    ]}
],
'springboot注册Filter的3种方式（Servlet、Listener类似）':[
    'FilterRegistrationBean',
    '@WebFilter',
    '@Bean',
    {'总结':[
        '只要受spring容器管理，最终都会添加到ServletContextInitializerBeans的initializers中，都会成功注册到servlet容器',
        '@WebFilter方式和@Bean方式注册的Filter都会被封装成FilterRegistrationBean，然后添加进ServletContextInitializerBeans的initializers',
        'SpringShiroFilter的注册是@Bean方式注册的'
    ]}
]
}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 