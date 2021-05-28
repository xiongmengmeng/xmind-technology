import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
xmind_name="dubbo"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("ServiceConfig")
r2=s2.getRootTopic()
r2.setTitle("ServiceConfig")


content={


'属性':[
    {'ProxyFactory proxyFactory = (ProxyFactory)ExtensionLoader.getExtensionLoader(ProxyFactory.class).getAdaptiveExtension();':[
       
    ]},
    {'Protocol protocol = (Protocol)ExtensionLoader.getExtensionLoader(Protocol.class).getAdaptiveExtension();':[
        
    ]},
    {'List<URL> urls':[
        
    ]},
    {'List<Exporter<?>> exporters':[
       
    ]}
],
'export()':[
    '暴露及注册服务',
    '核心方法this.doExport()'
],
'doExport()':[
    {'this.checkXX()':[
        '配置参数检查与加入'
    ]},
    {'appendProperties(this)':[
        '读出配置文件中配置来覆盖默认配置'
    ]},
    {'this.doExportUrls()':[
        {'List<URL> registryURLs =this.loadRegistries(true)':[
            '获取当前服务配置的注册中心实例',
            {'详细':[
                '1.创建一个map，将各配置信息存入',
                {'2.将address与map信息转成URL':[
                    'UrlUtils.parseURLs(address, map)'
                ]},
                {'3.遍历url,添加参数registry':[
                    'url.addParameter("registry", url.getProtocol())',
                    'url.setProtocol("registry")'
                ]}
            ]}
        ]},
        '遍历协议,依次暴露服务',
        {'this.doExportUrlsFor1Protocol(protocolConfig, registryURLs)':[
            '1.读取其他配置信息到map,用于后续构造URL',
            {'2.封装URL':[
                'URL url=new URL(name, host, port, contextPath, map)'
            ]},
            {'3.本地服务暴露(injvm协议)':[
                'this.exportLocal(url)'
            ]},
            {'4.通过动态代理转换成Invoker':[
                'Invoker<?> invoker=proxyFactory.getInvoker(this.ref, this.interfaceClass,',
                'registryURL.addParameterAndEncoded("export", url.toFullString()))',
                {'registryURL':[
                    '存储的是注册中心地址'
                ]},
                '在服务端生成的是AbstractProxylnvoker实例，所有方法调用都委托给代理，代理转发给服务ref调用'
            ]},
            {'5.服务暴露后向注册中心注册服务信息':[
                'Exporter<?> exporter = protocol.export(wrapperInvoker)'
            ]}
        ]}
    ]}
],
'exportLocal(URL url)':[
    {'1.显式指ze injvm协议进行暴露':[
        'URL local=URL.valueOf(url.toFullString()).setProtocol("injvm").setHost("127.0.0.1").setPort(0)',
        'injvm协议暴露服务:不会做端口打开操作，仅仅把服务保存在内存'
    ]},
    {'2.调用 InjvmProtocol#export':[
        'Exporter<?> exporter = protocol.export(proxyFactory.getInvoker(this.ref, this.interfaceClass, local))',
        '直接返回InjvmExporter实例对象，并将其加入exporterMap中'
    ]}
]


}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 