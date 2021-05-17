import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
xmind_name="dubbo"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("Invoker")
r2=s2.getRootTopic()
r2.setTitle("Invoker")


content={
'Invoker<T>':[
    'Class<T> getInterface()',
    'Result invoke(Invocation var1)',
    '注：下面有AbstractClusterlnvoker> MockClusterlnvoker和 MergeableClusterlnvoker 3个类'
],
'AbstractClusterInvoker':[
    '抽象类，封装了通用的模板逻辑，如获取服务列表、负载均衡、调用服务提供者等',
    '下面有7个子类，分别实现了不同的集群容错机制',
    {'属性':[
        {'Directory<T> directory':[
            '目录'
        ]},
        {'Invoker<T> stickyInvoker':[
            '粘滞连接的Invoker'
        ]}
    ]},
    {'AbstractClusterInvoker(Directory<T> directory)':[
        'this(directory, directory.getUrl())'
    ]},
    {'Result invoke(Invocation invocation)':[
        {'1.查询invocation关联的invokers':[
            'List<Invoker<T>> invokers = this.list(invocation)',
        ]},
        {'2.获得负载均衡器':[
            'loadbalance = (LoadBalance)ExtensionLoader.getExtensionLoader(LoadBalance.class).getExtension(((Invoker)invokers.get(0)).getUrl().getMethodParameter(RpcUtils.getMethodName(invocation), "loadbalance", "random"));'
        ]},
        {'3.调用doInvoke模版方法':[
            'this.doInvoke(invocation, invokers, loadbalance)'
        ]}
    ]},
    {'doInvoke(T var1, String var2, Class<?>[] var3, Object[] var4)':[
        '模版方法，留给子类实现'
    ]},
    {'List<Invoker<T>> list(Invocation invocation)':[
        'List<Invoker<T>> invokers = this.directory.list(invocation)'
    ]},
    {'select(LoadBalance loadbalance, Invocation invocation, List<Invoker<T>> invokers, List<Invoker<T>> selected)':[
        {'1.检查URL中是否有配置粘滞连接':[
            'boolean sticky = ((Invoker)invokers.get(0)).getUrl().getMethodParameter(methodName, "sticky", false);'
        ]},
        {'2.有,如果有则使用粘滞连接的Invoker':[
            '返回this.stickyInvoker'
        ]},
        {'3.通过负责均衡选择一个invoker':[
            'Invoker<T> invoker = this.doSelect(loadbalance, invocation, invokers, selected)'
        ]}
    ]},
    {'doSelect(LoadBalance loadbalance, Invocation invocation, List<Invoker<T>> invokers, List<Invoker<T>> selected)':[
        {'1.':[
            'loadbalance = (LoadBalance)ExtensionLoader.getExtensionLoader(LoadBalance.class).getExtension("random");'
        ]},
        {'':[
            'Invoker<T> invoker = loadbalance.select(invokers, this.getUrl(), invocation)'
        ]},
        {'':[
            'Invoker<T> rinvoker = this.reselect(loadbalance, invocation, invokers, selected, this.availablecheck);'
        ]}
    ]}
],
'FailoverClusterInvoker<T>':[
    {'doInvoke(Invocation invocation, List<Invoker<T>> invokers, LoadBalance loadbalance)':[
        '拿到directory返回的invoker列表后,通过loadbalance从invoker列表中选择一个invoker,将参数传给invoker，进行远程调用',
        {'1.根据重试次数进行快速失败处理':[
            'int len=this.getUrl().getMethodParameter(invocation.getMethodName(), "retries", 2) + 1'
        ]},
        {'2.每次都从字典获得最新invoker':[
            'copyinvokers = this.list(invocation)'
        ]},
        {'3.通过负载均衡选择一个Invoker':[
            'Invoker<T> invoker=this.select(loadbalance, invocation, copyinvokers, invoked);'
        ]},
        {'4.调用用invoker方法':[
            'Result result=invoker.invoke(invocation)'
        ]}
    ]}
],
'DubboInvoker<T>':[
    {'参数':[
        {'ExchangeClient[] clients':[
            '内部封装了客户端'
        ]}
    ]},
    {'doInvoke(Invocation invocation)':[
        {'选择使用了通信客户端':[
            'currentClient = this.clients[this.index.getAndIncrement() % this.clients.length];'
        ]},
        {'isOneway(没有返回值的方法)':[
            'currentClient.send(inv, isSent)'
        ]},
        {'异步执行的方法':[
            'ResponseFuture future = currentClient.request(inv, timeout)'
        ]},
        {'同步执行有返回值的方法':[
            '(Result)currentClient.request(inv, timeout).get()'
        ]}
    ]}
]

}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 