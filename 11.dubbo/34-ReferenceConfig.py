import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
xmind_name="dubbo"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("ReferenceConfig")
r2=s2.getRootTopic()
r2.setTitle("ReferenceConfig")


content={


'属性':[
    {'Protocol refprotocol = (Protocol)ExtensionLoader.getExtensionLoader(Protocol.class).getAdaptiveExtension()':[
        '协议'
    ]},
    {'Cluster cluster = (Cluster)ExtensionLoader.getExtensionLoader(Cluster.class).getAdaptiveExtension()':[
        '集群'
    ]},
    {'ProxyFactory proxyFactory = (ProxyFactory)ExtensionLoader.getExtensionLoader(ProxyFactory.class).getAdaptiveExtension()':[
        '代理工厂'
    ]},
    {'List<Exporter<?>> exporters':[
        '暴露的服务'
    ]},
    {'List<URL> urls':[
        '存储服务消费元数据信息'
    ]}
],
'get()':[
    '引用服务',
    '核心方法this.init()'
],
'init()':[
    {'this.checkXX()':[
        '配置参数检查与加入'
    ]},
    {'appendProperties(this)':[
        '读出配置文件中配置来覆盖默认配置'
    ]},
    {'this.createProxy(map)':[
        {'1.默认检查是否是同一个JVM内部引用':[
            'isDvmRefer = InjvmProtocol.getlnjvmProtocol().islnjvmRefer(tmpUrl)'
        ]},
        {'2.直接使用比jvm 协议从内存中获取实例':[
            'this.invoker = refprotocol.refer(this.interfaceClass, url)'
        ]},
        {'3.注册中心地址后添加refer,存储':[
            'this.urls.add(url.addParameterAndEncoded("refer", StringUtils.toQueryString(map)));'
        ]},
        {'4.单注册中心消费，获得invoker':[
            'invoker=refprotocol.refer(this.interfaceClass, (URL)this.urls.get(0))',
            '方法返回invoker'
        ]},
        {'5.通过Cluster将多个Invoker转换成一个 Invoker':[
            'this.invoker = cluster.join(new StaticDirectory(u, invokers))'
        ]},
        {'6.把Invoker转换成接口代理':[
            'proxyFactory.getProxy(this.invoker)'
        ]}
    ]}
]



}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 