import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="spring"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("JdkDynamicAopProxy")
r2=s2.getRootTopic()
r2.setTitle("JdkDynamicAopProxy")


content={
'实现AopProxy接囗':[
    '重写getProxy(ClassLoader classLoader)方法:创建代理',
    {'getProxy(ClassLoader classLoader)':[
        'Proxy.newProxyInstance(classLoader, proxiedInterfaces, this)',
        {'三个参数 ':[
            'ClassLoader',
            '实现哪些接口',
            'InvocationHandler实例，这里传了this，因JdkDynamicAopProxy实现了InvocationHandler接口'
        ]}
    ]}, 
],
'实现InvocationHandler接囗':[
    '重写invoke(Object proxy, Method method, Object[] args)方法',
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

]
}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 