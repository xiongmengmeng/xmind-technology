import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="spring"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("aopConcept")
r2=s2.getRootTopic()
r2.setTitle("aop概念")


content={
'核心概念':[
   'AOP:对方法进行拦截来增强',
   'Spring AOP：基于代理实现，容器启动时生成代理实例，方法调用上会增加栈的深度，性能不如AspectJ好',
   {'AspectJ':[
       '静态织入，织入时机：编绎前，编绎后，类加载时，是AOP编程的完全解决方案',
       'compile-time：编译期织入，在编译的时候一步到位，直接编译出包含织入代码的 .class 文件',
       'post-compile：编译后织入，增强已经编译出来的类，如我们要增强依赖的 jar 包中的某个类的某个方法',
       'load-time：在 JVM 进行类加载的时候进行织入'
   ]}
],
'应用':[
    '日志',
    '监控',
    '数据库连接，切换数据源',
    '自定义权限拦截器',
    '事务'
],
'AOP概念':[
    '连接点（join point）',
    '切点（point cut）:@Pointcut来定义切点',
    {'通知（advice）':[
        '前置通知（before advice）:@Before',
        '后置通知（after advice）:@After',
        '环绕通知（around advice）:@Around',
        '事后返回通知（afterReturning advice）:@AfterReturning',
        '异常通知（afterThrowing advice）:@AfterThrowing'
    ]},
    '目标对象（target）',
    '引入（introduction）:引入新的类和其方法，增强现有Bean的功能',
    {'织入（weaving）':[
        '通过动态代理技术，为原有服务对象生成代理对象',
        '拦截与切点匹配的连接点',
        '按约定将各类通知织入约定流程'
    ]},
    {'切面（aspect）':[
        '一个可以定义切点、各类通知和引入的内容',
        '@Aspect 声明切面',
        '多切面，用@Order定义优先级'
    ]}
],
'学习链接':[
    'https://javadoop.com/post/spring-aop-source',
    'https://blog.csdn.net/linuu/category_9265738.html'
]
}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 