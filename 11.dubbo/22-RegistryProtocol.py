import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
xmind_name="dubbo"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("RegistryProtocol")
r2=s2.getRootTopic()
r2.setTitle("RegistryProtocol")


content={


'属性':[
    {'Protocol protocol':[
        '协议，一般是DubboProtocol'
    ]},
],
'export(Invoker<T> originInvoker)':[
    '服务暴露与注册',
    {'1.启动netty服务器，绑定端囗':[
        'this.doLocalExport(originInvoker)',
        '核心exporter=new RegistryProtocol.ExporterChangeableWrapper(this.protocol.export(invokerDelegete), originInvoker);',
        '参数this.protocol.export(invokerDelegete)=>DubboProtocol.export(Invoker<T> invoker)'
    ]},
    {'2.创建注册中心实例':[
        'Registry registry = getRegistry(origininvoker);'
    ]},
    {'3.服务暴露之后，注册服务元数据':[
        'this.register(registryUrl, registeredProviderUrl)'
    ]},
    {'4.获取订阅URL':[
        'URL overrideSubscribeUrl=this.getSubscribedOverrideUrl(registeredProviderUrl)',
        '第一次发起订阅时会进行一次数据拉取操作，同时触发RegistryDirectory#notify方法'
    ]},
    {'5.向注册中心订阅configurators节点':[
        'registry.subscribe(overrideSubscribeUrl, overrideSubscribeListener);'
    ]}
],
'unexport()':[
    '取消服务暴露与注册',
    {'1.移除已注册的元数据':[
        'registry.unregister(this.registerUrl)'
    ]},
    {'2.去掉订阅配置监听器':[
        'registry.unsubscribe(this.subscribeUrl, listener)'
    ]},
    {'3.Invoker销毁时注销端口和map中服务实例等资源':[
        'exporter.unexport();'
    ]},
],
'register(URL registryUrl, URL registedProviderUrl)':[
    '服务注册',
    {'1.通过registryUrl获得对映的注册中心':[
        'Registry registry = this.registryFactory.getRegistry(registryUrl);'
    ]},
    {'2.向注册中心上添加节点':[
        'registry.register(registedProviderUrl)'
    ]}
],
'refer(Class<T> type, URL url)':[
    '完成了注册中心实例的创建，元数据注册到注册中心及订阅的功能',
    {'1.设置具体注册中心协议,如ZooKeeper':[
        'url=url.setProtocol(url.getParameter("registry", "dubbo")).removeParameter("registry")'
    ]},
    {'2.创建具体注册中心实例':[
        'Registry registry=this.registryFactory.getRegistry(url)'
    ]},
    {'3.根据配置处理多分组结果聚合':[
        'String group = (String)qs.get("group")'
    ]},
    {'4.处理订阅数据并通过cluster合并多个Invoker,返回一个伪装的invoker':[
        'this.doRefer(this.cluster, registry, type, url)'
    ]}
],
'doRefer(Cluster cluster, Registry registry, Class<T> type, URL url)':[
    {'1.构建动态字典对象':[
        'RegistryDirectory<T> directory = new RegistryDirectory(type, url)',
        '消费核心关键，持有实际Invoker和接收订阅通知'
    ]},
    {'2.将消费信息到注册中心 ':[
        'registry.register(registeredConsumerUrl)'
    ]},
    {'3.订阅配置,路由,提供者,可缓存更新服务提供者信息':[
        'directory.subscribe(subscribeUrl.addParameter("category", "providers,configurators,routers"));'
    ]},
    {'4.通过Cluster合并invokers':[
        '通过集群将多个服务提供者伪装成一个invoker(里面还是多个),默认failover',
        'Invoker invoker = cluster.join(directory)'
    ]}
]
  



}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 