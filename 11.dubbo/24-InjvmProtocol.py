import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
xmind_name="dubbo"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("InjvmProtocol")
r2=s2.getRootTopic()
r2.setTitle("InjvmProtocol")


content={
'InjvmProtocol':[
    {'export(Invoker<T> invoker)':[
        'new InjvmExporter(invoker, invoker.getUrl().getServiceKey(), this.exporterMap)',
        '直接返回InjvmExporter实例对象，并将其加入exporterMap中'
    ]},
    {'refer(Class<T> serviceType, URL url)':[
        'new InjvmInvoker(serviceType, url, url.getServiceKey(), this.exporterMap)'
    ]}
],
'ProtocolFilterWrapper':[
    {'buildInvokerChain(final Invoker<T> invoker, String key, String group)':[
        {'1.获得过滤器':[
            'List<Filter> filters=ExtensionLoader.getExtensionLoader(Filter.class).getActivateExtension(invoker.getUrl(), key, group)'
        ]},
        {'2.封装基于Invoker的Filter链':[
            'filter.invoke(last, invocation)'
        ]}
    ]},
    {'export(Invoker<T> invoker)':[
        {'"registry".equals(invoker.getUrl().getProtocol())':[
            {'是':[
                'this.protocol.export(invoker)'
            ]},
            {'否':[
                'this.protocol.export(buildInvokerChain(invoker, "service.filter", "provider"))'
            ]}
        ]}
    ]},
    {'refer(Class<T> type, URL url)':[
        {'"registry".equals(url.getProtocol())':[
            {'是':[
                'this.protocol.refer(type, url)'
            ]},
            {'否':[
                'buildInvokerChain(this.protocol.refer(type, url), "reference.filter", "consumer")'
            ]}
        ]}
    ]}
],
'ProtocolListenerWrapper':[
    {'export(Invoker<T> invoker)':[
        '(Exporter)("registry".equals(invoker.getUrl().getProtocol()) ? ',
        'this.protocol.export(invoker) :',
        'new ListenerExporterWrapper(this.protocol.export(invoker), Collections.unmodifiableList(ExtensionLoader.getExtensionLoader(ExporterListener.class).getActivateExtension(invoker.getUrl(), "exporter.listener"))))'
    ]},
    {'refer(Class<T> type, URL url)':[
        '(Invoker)("registry".equals(url.getProtocol()) ?',
        'this.protocol.refer(type, url) :',
        'new ListenerInvokerWrapper(this.protocol.refer(type, url), Collections.unmodifiableList(ExtensionLoader.getExtensionLoader(InvokerListener.class).getActivateExtension(url, "invoker.listener"))))'
    ]}
],
'类似':[
    'QosProtocolWrapper'
],




}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 