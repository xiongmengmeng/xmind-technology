import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="spring"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("aopBaseClass")
r2=s2.getRootTopic()
r2.setTitle("aop基础")


content={
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
        'DefaultAdvisorAutoProxyCreator，实现了BeanPostProcessor接囗'
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
    '动态代理:接口+真实实现类+代理类',
    '其中【真实实现类】和【代理类】都要实现接口，实例化时要使用代理类',
    {'Spring AOP实现':[
        '生成一个代理类，替换掉真实实现类来对外提供服务',
        '在Spring IOC容器中，getBean(…) 时返回代理类的实例->FactoryBean.getObject()'
    ]}
],
'基础架构':[
    {'AdvisedSupport':[
        'List<Class<?>> interfaces = new ArrayList<Class<?>>()',
        'List<Advisor> advisors = new LinkedList<Advisor>()'
    ]},
    {'ProxyCreatorSupport':[
        '方法：createAopProxy()'
    ]},
    {'ProxyFactoryBean':[
        '实现BeanClassLoaderAware接口:创建proxy第一个参数是classLoader',
        '实现BeanFactoryAware接口:把被代理的对象实例化好',
        '实现FactoryBean<Object>接囗：初始化和返回的代理对象',
        {'getObject()':[
            {'initializeAdvisorChain()':[
                '初始化advisor',
                '1.advice = this.beanFactory.getBean(name),用beanFactory实例化并获得advice类型的bean',
                '2.addAdvisorOnChainCreation(advice, name)：将advice封装成advisor，放入advisor链List<Advisor> advisors',
            ]},
            {'getSingletonInstance()':[
                '返回单例代理对象',
                '1.createAopProxy():根据代理的目标对象是否实现接口，来返回JdkDynamicAopProxy的动态代理或者cglib的代理',
                '2.getProxy(AopProxy aopProxy)->Proxy.newProxyInstance(classLoader, proxiedInterfaces, this)',
            ]}
        ]}
    ]},
    {'ProxyFactory':[
        '添加advice:addAdvice(interceptor)',
        '设置目标对象：setTargetSource(targetSource)',
        '设置目标对象实现的接囗：setInterfaces(ClassUtils.getAllInterfaces(target))',
        '直接编程，很清晰，在IoC部分去实例化的目标对象且返回代理对象时使用'
    ]}
]
}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 