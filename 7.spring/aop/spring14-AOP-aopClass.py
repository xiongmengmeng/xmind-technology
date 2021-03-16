import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="spring"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("aopClass")
r2=s2.getRootTopic()
r2.setTitle("aop基础类")


content={
'AdvisedSupport':[
    'List<Class<?>> interfaces = new ArrayList<Class<?>>()',
    'List<Advisor> advisors = new LinkedList<Advisor>()',
    {'addAdvice(interceptor)方法':[
        '添加advice'
    ]},
    {'setTargetSource(targetSource)方法':[
        '设置目标对象'
    ]},
    {'setInterfaces(ClassUtils.getAllInterfaces(target))方法':[
        '设置目标对象实现的接囗'
    ]}
],
'ProxyCreatorSupport':[
    '变量AopProxyFactory',
    {'getProxy(ClassLoader classLoader)方法':[
        'getAopProxyFactory()->返回AopProxyFactory对象',
        'createAopProxy(this)'
    ]}
],
'ProxyFactory':[
    'addAdvice(interceptor)',
    'setTargetSource(targetSource)',
    'setInterfaces(ClassUtils.getAllInterfaces(target))',
    'getProxy(ClassLoader classLoader)方法',
    '直接编程，很清晰，在IoC部分去实例化的目标对象且返回代理对象时使用'
],
'ProxyFactoryBean':[
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
],
'AopProxyFactory接囗':[
    {'createAopProxy()方法':[
        '传参：AdvisedSupport config',
        '返回值：AopProxy '
    ]},
],
'DefaultAopProxyFactory':[
    '重写createAopProxy()方法',
    {'JDK动态代理':[
        '被代理目标类实现一个或多个接口',
        '基于接口，所以只有接口中的方法会被增强'
    ]},
    {'CGLIB':[
        '没有实现任何接口||设置proxy-target-class="true"',
        '基于类继承，注意如方法使用final修饰，或private方法，不能被增强'
    ]},
    '方法返回JdkDynamicAopProxy实例或ObjenesisCglibAopProxy实例'
]

}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 