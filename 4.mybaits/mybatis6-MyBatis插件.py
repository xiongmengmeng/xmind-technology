import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="mybatis"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("MyBatis插件(下)")
r2=s2.getRootTopic()
r2.setTitle("MyBatis插件(下)")


content={
'Interceptor接口':[
    '自定义的插件都必须实现Interceptor接口',
    {'注解,例':[
        '@Intercepts({@Signature(type = StatementHandler.class, method = "prepare", args = {Connection.class, Integer.class})})'
    ]},
    {'intercept()':[
        '定义拦截逻辑，方法在目标方法调用时执行,Invocation对象作参数'
    ]},
    {'plugin()':[
        '用于创建Executor、ParameterHandler、ResultSetHandler或StatementHandler的代理对象'
    ]},
    {'setProperties()':[
        '设置插件的属性值'
    ]}
],
'InterceptorChain interceptorChain':[
    'Configuration类中的拦截器链，存放通过<plugins>标签注册的所有拦截器',
    '变量：List<Interceptor> interceptors = new ArrayList<Interceptor>()',
    {'pluginAll(Object target)':[
        '调用所有拦截器实例的plugin()方法，返回一个目标对象的代理对象',
        'for (Interceptor interceptor : interceptors) {',
        '   target = interceptor.plugin(target);',
        'return target;'
    ]}
],
'Invocation类':[
    'Object target:目标对象',
    'Method method:目标方法',
    'Object[] args:参数信息',
    {'proceed()':[
        '执行目标方法的逻辑',
        'method.invoke(target, args);'
    ]}
],
'Plugin工具类':[
    '实现InvocationHandler接口，重写invoke()方法',
    'wrap()：简化动态代理对象的创建',
    {'invoke()':[
        '在调用目标对象的方法时执行',
        '判断方法是否被Intercepts注解指定拦截的方法',
        '是，调用用户自定义拦截器的intercept()方法，将目标方法信息封装成Invocation对象作为传参',
        '否,调用目标方法'
    ]},
    {'wrap()':[
        '动态代理对象的创建',
        '调用Proxy类的静态方法newProxyInstance()创建动态代理对象'
    ]}
],


    
}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 