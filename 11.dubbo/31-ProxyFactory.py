import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
xmind_name="dubbo"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("ProxyFactory")
r2=s2.getRootTopic()
r2.setTitle("ProxyFactory")


content={
'ProxyFactory':[
    {'类注解':[
        '@SPI("javassist")'
    ]},
    {'<T> Invoker<T> getInvoker(T var1, Class<T> var2, URL var3)':[
        '方法注解@Adaptive({"proxy"})'
    ]},
    {'spi对映文件内容':[
        'stub=com.alibaba.dubbo.rpc.proxy.wrapper.StubProxyFactoryWrapper',
        'jdk=com.alibaba.dubbo.rpc.proxy.jdk.JdkProxyFactory',
        'javassist=com.alibaba.dubbo.rpc.proxy.javassist.JavassistProxyFactory'
    ]}
],
'JavassistProxyFactory':[
    {'getInvoker(T proxy, Class<T> type, URL url)':[
        {'1.封装Invoke代码，最后通过编译器获得Invoke包装类':[
            'Wrapper wrapper=Wrapper.getWrapper(proxy.getClass().getName().indexOf(36)<0?proxy.getClass():type)'
        ]},
        {'2.创建一个继承自AbstractProxyInvoker的对象':[
            'new AbstractProxyInvoker<T>(proxy, type, url)'
        ]},
        {'3.重写其doInvoke()方法':[
            '核心wrapper.invokeMethod(proxy, methodName, parameterTypes, arguments)'
        ]}
    ]},
    {'getProxy(Invoker<T> invoker, Class<?>[] interfaces)':[
        'Proxy.getProxy(interfaces).newInstance(new InvokerInvocationHandler(invoker))'
    ]},
],
'InvokerInvocationHandler':[
    '实现InvocationHandler接囗，重写其invoke(Object proxy, Method method, Object[] args)方法',
    {'invoke(Object proxy, Method method, Object[] args)':[
        '核心this.invoker.invoke(new RpcInvocation(method, args)).recreate()'
    ]}
]


}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 