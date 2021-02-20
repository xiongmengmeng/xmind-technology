import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="spring"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("aopSourceCode")
r2=s2.getRootTopic()
r2.setTitle("aop源码")


content={
'JdkDynamicAopProxy':[
    '实现AopProxy接囗：核心方法getProxy(ClassLoader classLoader)，由子类实现',
    '实现InvocationHandler接囗：核心方法invoke(Object proxy, Method method, Object[] args)，由子类实现',
    {'getProxy(ClassLoader classLoader)':[
        'Proxy.newProxyInstance(classLoader, proxiedInterfaces, this)',
         {'三个参数 ':[
            'ClassLoader',
            '实现哪些接口',
            'InvocationHandler实例，这里传了this，因JdkDynamicAopProxy实现了InvocationHandler接口'
        ]}
    ]},
    {'invoke(Object proxy, Method method, Object[] args)':[
        '1.如被代理的目标对象要执行equal方法，则执行JdkDynamicAopProxy的equal方法',
        '2.如被代理的目标对象要执行hashcode方法，则执行JdkDynamicAopProxy的hashcode方法',
        '3.如被代理的对象本身实现了Advised接口，不做处理，直接执行',
        '4.List<Object> chain = this.advised.getInterceptorsAndDynamicInterceptionAdvice(method, targetClass)',
        '获取一下这个方法所有的拦截器，形成拦截链返回，',
        '5.拦截器链不空：new ReflectiveMethodInvocation(proxy, target, method, args, targetClass, chain)',
        '封装一个ReflectiveMethodInvocation对象，它持有着重要的参数',
        '6.ReflectiveMethodInvocation对象，执行proceed(),递归调用执行拦截器方法：',
        '((MethodInterceptor) interceptorOrInterceptionAdvice).invoke(this)，里面还会执行proceed(),递归调用',
        '7.最后invokeJoinpoint():执行目标对象的方法'
    ]}
],
'aop源码':[
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
    {'createProxy()':[
        '1.new ProxyFactory():创建一个ProxyFactory的实例',
        '2.set一堆内容',
        '3.proxyFactory.getProxy(classLoader):',
        '通过这个实例来创建代理,内部调用createAopProxy().getProxy(classLoader)',
        'createAopProxy()->DefaultAopProxyFactory.createAopProxy(AdvisedSupport config)',
        'getProxy(classLoader)->JdkDynamicAopProxy.getProxy(classLoader)'
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
    ]}
],
'基于注解的 Spring AOP 源码分析':[
    {'开启 @AspectJ 的两种方式':[
        '1.<aop:aspectj-autoproxy/>:AopNamespaceHandler->AnnotationAwareAspectJAutoProxyCreator',
        '2.@EnableAspectJAutoProxy',
        '原理一样，都通过注册一个bean来实现'
    ]}
]

}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 