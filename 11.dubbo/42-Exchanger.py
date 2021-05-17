import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
xmind_name="dubbo"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("Exchanger")
r2=s2.getRootTopic()
r2.setTitle("Exchanger")


content={
'Exchangers':[
    '工具类，Protocol与Exchanger的工具类',
    {'bind(URL url, ExchangeHandler handler)':[
        'getExchanger(url).bind(url, handler)'
    ]},
    {'connect(URL url, ExchangeHandler handler)':[
        'getExchanger(url).connect(url, handler)'
    ]},
    {'getExchanger(URL url)':[
        'String type = url.getParameter("exchanger", "header")',
        'getExchanger(type)'
    ]},
    {'getExchanger(String type)':[
        'ExtensionLoader.getExtensionLoader(Exchanger.class).getExtension(type)'
    ]},
],
'Exchanger':[
    '类注解：@SPI("header")',
    {'ExchangeServer bind(URL var1, ExchangeHandler var2)':[
        '@Adaptive({"exchanger"})',
    ]},
    {'ExchangeClient connect(URL var1, ExchangeHandler var2)':[
        '@Adaptive({"exchanger"})'
    ]}
],
'HeaderExchanger':[
    {'connect(URL url, ExchangeHandler handler)':[
        'new HeaderExchangeClient(Transporters.connect(url, new ChannelHandler[]{new DecodeHandler(new HeaderExchangeHandler(handler))}), true)'
    ]},
    {'bind(URL url, ExchangeHandler handler)':[
        'new HeaderExchangeServer(Transporters.bind(url, new ChannelHandler[]{new DecodeHandler(new HeaderExchangeHandler(handler))}))',
        '将传入的handler放入HeaderExchangeHandler',
        '再将HeaderExchangeHandler放入DecodeHandler'
    ]},
],
'HeaderExchangeClient':[
    {'属性':[
        {'Client client':[
            '客户端'
        ]},
        {'ExchangeChannel channel':[
            '通道'
        ]}
    ]},
    {'HeaderExchangeClient(Client client, boolean needHeartbeat)':[
        'this.client = client',
        'this.channel = new HeaderExchangeChannel(client)'
    ]},
    {'void send(Object message, boolean sent)':[
        '消费者发送数据给提供者',
        'this.channel.send(message, sent)'
    ]},
    {'ResponseFuture request(Object request, int timeout)':[
        '消费者发送数据给提供者',
        'this.channel.request(request, timeout)'
    ]}
],
'HeaderExchangeServer':[
    {'属性':[
        {'Server server':[
            '服务端'
        ]}
    ]},
    {'HeaderExchangeServer(Server server)':[
        'this.server = server'
    ]},
    {'send(Object message, boolean sent)':[
        'this.server.send(message, sent)'
    ]}
]

}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 