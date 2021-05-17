import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
xmind_name="dubbo"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("DubboProtocol")
r2=s2.getRootTopic()
r2.setTitle("DubboProtocol")


content={


'属性':[
    {'Map<String, ExchangeServer> serverMap = new ConcurrentHashMap()':[
        '存入暴露的服务'
    ]},
    {'Map<String, ExchangeServer> serverMap':[
        '存入'
    ]}
],
'export(Invoker<T> invoker)':[
    {'1.根据服务分组、版本、接口和端口构造key':[
        'String key = serviceKey(url)',
    ]},
    {'2.封装Exporter':[
        'DubboExporter<T> exporter=new DubboExporter(invoker, key, this.exporterMap)'
    ]},
    {'3.把exporter存储到单例DubboProtocol中':[
        'this.exporterMap.put(key, exporter)'
    ]},
    {'4.服务初次暴露会创建监听服务器':[
        'this.openServer(url)',
        '注：同一个协议暴露有很多接口，只有初次暴露的接口才需要打开端口监听'
    ]},
],
'openServer(URL url)':[
    '将Exporter存入map中',
    '调用this.serverMap.put(key, this.createServer(url));'
],
'createServer(URL url)':[
    {'创建NettyServer并且初始化Handler':[
        'ExchangeServer server=Exchangers.bind(url, this.requestHandler)->',
        'getExchanger(url).bind(url, handler)',
        '注：this.requestHandler:是ExchangeHandlerAdapter'
    ]}
],
'refer(Class<T> serviceType, URL url)':[
    '服务引用',
    'DubboInvoker<T> invoker = new DubboInvoker(serviceType, url, this.getClients(url), this.invokers)',
    {'注参数 ':[
        'this.getClients(url)'
    ]}
],
'getClients(URL url)':[
    '启动客户端',
    'service_share_connect: 是否共享共一个连接',
    {'service_share_connect为true':[
        'this.getSharedClient(url)'
    ]}
],
'getSharedClient(URL url)':[
    'ExchangeClient exchangeClient = this.initClient(url);'
],
'initClient(URL url)':[
    'client = Exchangers.connect(url, this.requestHandler)'
],
'ExchangeHandlerAdapter内部类':[
    {'reply(Exchangechannel channel. Object message) ':[
        {'1.找invocation关联的Invoker':[
            'Invoker<?> invoker = DubboProtocol.this.getInvoker(channel, inv)'
        ]},
        {'2.调用业务方具体方法':[
            'invoker.invoke(inv);'
        ]}
    ]}
],
'getInvoker(Channel channel, Invocation inv)':[
    {'1.组装key':[
        'key由四部分组成：端囗，接囗名，接囗版本，接囗分组',
        'String serviceKey = serviceKey(port, path, (String)inv.getAttachments().get("version"), (String)inv.getAttachments().get("group"));'
    ]},
    {'2.根据key拿到exporter':[
        'DubboExporter<?> exporter = (DubboExporter)this.exporterMap.get(serviceKey)'
    ]},
    {'3.从exporter中取出invoker':[
        'exporter.getInvoker()'
    ]}
]





}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 