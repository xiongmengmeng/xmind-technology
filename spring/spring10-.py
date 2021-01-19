import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="spring"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("aop"")
r2=s2.getRootTopic()
r2.setTitle("aop")


content={
'概念':[
   'AOP:对方法进行拦截来增强',
   'Spring AOP：基于代理实现，容器启动时生成代理实例，方法调用上会增加栈的深度，性能不如AspectJ好',
   'AspectJ：静态织入，织入时机：编绎前，编绎后，类加载时，是AOP编程的完全解决方案'
],
'三种配置方式':[
    {'Spring1.2基于接口':[
        '最早的 Spring AOP 是完全基于几个接口的，看源码可从这里开始',
        {'ProxyFactoryBean':[
            'proxyInterfaces',
            'target',
            {'interceptorNames':[
                'Advice',
                'Intercepter',
                'Advisor'
            ]}
        ]},
        'BeanNameAutoProxyCreator',
        'DefaultAdvisorAutoProxyCreator'
    ]},
    'Spring2.0基于schema-based：XML方式配置，使用命名空间 <aop />',
    {'Spring2.0基于@AspectJ':[
        '使用注解的方式来配置',
        '@AspectJ:标记切面,这个和 AspectJ没啥关系',
        '@Pointcut:切点，类似上面的Advisor',
        '@Before:通知，类似上面的Advice,传参使用：JoinPoint',
        '@Around:传参使用ProceedingJoinPoint，它有procceed()方法'
    ]}
],
'原理':[
    '动态代理',
    '接口+真实实现类+代理类',
    '其中【真实实现类】和【代理类】都要实现接口，实例化时要使用代理类',
    {'Spring AOP实现':[
        '生成一个代理类，替换掉真实实现类来对外提供服务',
        '在Spring IOC容器中，getBean(…) 时返回代理类的实例'
    ]}
],
'源码':[
    {'入囗':[
        'doCreateBean()中，回调方法：initializeBean()->',
        'DefaultAdvisorAutoProxyCreator.postProcessAfterInitialization()->',
        'AbstractAutoProxyCreator.postProcessAfterInitialization()[方法是继承父类]'
    ]},
    {'AbstractAutoProxyCreator.postProcessAfterInitialization() ':[
        '1.getAdvicesAndAdvisorsForBean(bean.getClass(), beanName, null)',
        '得到所有的可用于拦截当前 bean 的 advisor、advice、interceptor',
        '2.createProxy(Class<?> beanClass, String beanName, Object[] specificInterceptors, TargetSource targetSource):'
    ]},
    {'createProxy':[
        '1.new ProxyFactory():创建一个ProxyFactory的实例',
        '2.set一堆内容',,
        '3.proxyFactory.getProxy(classLoader):',
        '通过这个实例来创建代理,内部调用',
        'DefaultAopProxyFactory.createAopProxy(AdvisedSupport config)'
    ]},
    {'DefaultAopProxyFactory.createAopProxy()':[
        {'JDK动态代理':[
            '被代理目标类实现一个或多个接口',
            '基于接口，所以只有接口中的方法会被增强'
        ]},
        {'CGLIB':[
            '没有实现任何接口||设置proxy-target-class="true"',
            '基于类继承，注意如方法使用final修饰，或private方法，不能被增强'
        ]},
        '方法返回JdkDynamicAopProxy实例或ObjenesisCglibAopProxy实例'
    ]},
    {'JdkDynamicAopProxy.getProxy(classLoader)':[
        {'Proxy.newProxyInstance(…),三个参数 ':[
            'ClassLoader',
            '实现哪些接口',
            'InvocationHandler实例，这里传了this，因为JdkDynamicAopProxy本身实现了InvocationHandler 接口'
        ]},
        {'JdkDynamicAopProxy.invoke()':[
            '1.创建一个 chain，包含所有要执行的 advice',
            '',
            ''
        ]}
    ]}
],
'基于注解的 Spring AOP 源码分析':[
    {'开启 @AspectJ 的两种方式':[
        '1.<aop:aspectj-autoproxy/>',
        '2.@EnableAspectJAutoProxy',
        '原理一样，都通过注册一个bean来实现'
    ]}
],
'AOP':[
    '连接点（join point）',
    '切点（point cut）:@Pointcut来定义切点',
    {'通知（advice）':[
        '前置通知（before advice）:@Before',
        '后置通知（after advice）:@After',
        '环绕通知（around advice）:@Around',
        '事后返回通知（afterReturning advice）:@AfterReturning',
        '异常通知（afterThrowing advice）:@AfterThrowing'
    ],
    '目标对象（target）',
    '引入（introduction）:引入新的类和其方法，增强现有Bean的功能',
    {'织入（weaving）':[
        '通过动态代理技术，为原有服务对象生成代理对象',
        '拦截与切点匹配的连接点',
        '按约定将各类通知织入约定流程'
    ]},
    {'切面（aspect）':[
        '一个可以定义切点、各类通知和引入的内容',
        '@Aspect 声明切面'
    ]},
    '多切面，用@Order定义优化级',
    '数据库连接',
    {'事务':[
        '@Transactional',
        '事务定义器 TransactionDefinition',
        '事务管理器 PlatormTransactionManager',
        '@Transactional调用失效问题'
        ]
    }
],
'https://javadoop.com/post/spring-aop-source':[]
}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 