import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
xmind_name="dubbo"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("Handler")
r2=s2.getRootTopic()
r2.setTitle("Handler")


content={
'NettyHandler':[
    {'messageReceived(ChannelHandlerContext ctx, MessageEvent e)':[
    ]}
],
'DecodeHandler':[
    {'received(Channel channel, Object message)':[
        '核心this.handler.received(channel, message);',
        'this.handler是HeaderExchangeHandler'
    ]}
],
'HeaderExchangeHandler':[
    {'received(Channel channel, Object message)':[
        {'1.Request请求,更新时间戳':[
            'channel.setAttribute(KEY_READ_TIMESTAMP, System.currentTimeMillis())'
        ]},
        {'2.Request请求,处理readonly事件，在channel中打标':[
            'this.handlerEvent(channel, request)'
        ]},
        {'3.Request请求,处理方法调用并返回给客户端':[
            'Response response = this.handleRequest(exchangeChannel, request)',
            'channel.send(response)'
        ]},
        {'4.Request请求,其它':[
            'this.handler.received(exchangeChannel, request.getData())'
        ]},
        {'5.Response请求,接收响应':[
            'handleResponse(channel, (Response)message);'
        ]}
    ]},
    {'handleRequest(ExchangeChannel channel, Request req)':[
        {'调用DubboProtocol#repiy()方法':[
            'Object result = this.handler.reply(channel, data)',
            'res.setStatus((byte)20)',
            'res.setResult(result)'
        ]}
    ]}
]

}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 