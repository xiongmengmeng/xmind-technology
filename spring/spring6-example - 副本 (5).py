import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="spring"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("spring")
r2=s2.getRootTopic()
r2.setTitle("spring")


content={
'':[
   'AOP:对方法进行拦截来增强',
   'Spring AOP：基于代理实现的，在容器启动的时候生成代理实例，在方法调用上会增加栈的深度，使得 Spring AOP 的性能不如 AspectJ 那么好',
   'AspectJ：静态织入，织入时机，编绎前，编绎后，类加载时，是 AOP 编程的完全解决方案'
],

'三种配置方式':[
    {'Spring 1.2 基于接口的配置':[
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
    'Spring2.0 schema-based配置：XML方式配置，使用命名空间 <aop />',
    {'Spring 2.0 @AspectJ配置':[
        '使用注解的方式来配置',
        '@AspectJ:标记切面,这个和 AspectJ没啥关系',
        '@Pointcut:切点，类似上面的Advisor',
        '@Before：通知，类似上面的Advice,传参使用：JoinPoint',
        '@Around，传参使用 ProceedingJoinPoint，它有 procceed()/procceed(args[]) 方法。',
        
        ''
    ]}
],
'原理':[
    '动态代理:接口 + 真实实现类 + 代理类,其中 真实实现类 和 代理类 都要实现接口，实例化的时候要使用代理类',
    'Spring AOP 需要做的是生成这么一个代理类，然后替换掉真实实现类来对外提供服务',
    '实现:在Spring IOC容器中，在getBean(…) 时返回代理类的实例',
    ''
],
'源码':[
    {'入囗':[
        'doCreateBean()中，回调方法：initializeBean()',
    ]},
    '',
    '',
    '',
    '',
    ''
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
}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 