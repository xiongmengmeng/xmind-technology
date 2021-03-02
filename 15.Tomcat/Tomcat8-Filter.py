import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="tomcat"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("Filter")
r2=s2.getRootTopic()
r2.setTitle("Filter")


content={
'Servlet 3.0+ 规范':[
    {'ServletContext接囗':[
        'FilterRegistration.Dynamic addFilter(String filterName, String className)',
        'FilterRegistration.Dynamic addFilter(String filterName, Filter filter)',
        'FilterRegistration.Dynamic addFilter(String filterName,Class <? extends Filter> filterClass)'
    ]},
    'servlet3.0后：支持无web.xml配置,Filter、Servlet和Listener支持注解配置',
],
'Filter注册--springboot实现':[
    {'自定义Filter类':[
        '实现Filter接口',
        '重写doFilter方法',
        'public void doFilter(ServletRequest request, ServletResponse response, FilterChain chain)  {',
        '   System.out.println("过滤处理");',
        '   chain.doFilter(request, response);',
        '}'
    ]},
    {'FilterRegistrationBean':[
        '一个用于向Servlet 3.0+容器注册Filter的ServletContextInitializer',
        '本质还是ServletContext.addFilter()',
        '将我们自定义的Filter注册到容器，作用与在web.xml中配置Filter类似',
        '@Bean',
        'public FilterRegistrationBean myFilter() {',
        '   FilterRegistrationBean filterRegistrationBean = new FilterRegistrationBean(new MyFilter());',
        '   filterRegistrationBean.setUrlPatterns(Arrays.asList("/hello","/myServlet"));',
        '   return filterRegistrationBean;',
        '}',
    ]},
    {'ServletContextInitializer接囗':[
        '方法onStartup(ServletContext servletContext)：',
        '最终调用ServletContext的addFilter方法将Filter注册到Servlet容器'
    ]}
],
'springboot启动过程中':[
    '1.spring将@Bean修饰的RegistrationBean注册到beanFactory',
    {'2.然后从beanFactory中获取全部的ServletContextInitializer':[
        {'ServletWebServerApplicationContext#createWebServer':[
            '1.先去spring的beanFactory中获取ServletContextInitializer的全部实例',
            '2.并将其放入到ServletContextInitializerBeans的initializers中',
            '3.遍历initializers，调用每个ServletContextInitializer的onStartup方法'
        ]}
    ]},
    '3.遍历它们并调用他们的onStartup方法将RegistrationBean中的bean注册到servlet容器'
],
'学习':[
    'https://www.cnblogs.com/youzhibing/p/9866690.html'
]

}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 