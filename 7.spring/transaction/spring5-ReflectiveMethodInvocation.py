import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0,parentdir) 


import xmind
from xmind.core.markerref import MarkerId
xmind_name="Transaction"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("ReflectiveMethodInvocation")
r2=s2.getRootTopic()
r2.setTitle("ReflectiveMethodInvocation")


content={
'Joinpoint':[
    '连接点接口',
    {'Object proceed() throws Throwable;':[
        '定义了执行接口'
    ]},
    '执行当前连接点，并跳到拦截器链上的下一个拦截器'
],
'Invocation':[
    '调用接口，继承自Joinpoint',
    {'Object[] getArguments()':[
        '定义了获取参数接口'
    ]},
    '是一个带参数的、可被拦截器拦截的连接点'
],
'MethodInvocation':[
    '方法调用接口，继承自Invocation',
    {'Method getMethod()':[
        '定义了获取方法接口'
    ]},
    '是一个带参数的可被拦截的连接点方法'
],
'ProxyMethodInvocation':[
    '代理方法调用接口，继承自MethodInvocation',
    {'Object getProxy()':[
        '定义了获取代理对象接口'
    ]},
    '一个由代理类执行的方法调用连接点方法'
],
'ReflectiveMethodInvocation':[
    '实现了ProxyMethodInvocation接口，自然就实现了父类接口的的所有接口',
    '获取代理类，获取方法，获取参数，用代理类执行这个方法并且自动跳到下一个连接点',
    {'重写proceed()方法':[
        '((MethodInterceptor) interceptorOrInterceptionAdvice).invoke(this):',
        '回调目标业务方法'
    ]}

]

}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 