import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
xmind_name="dubbo"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("Transporter")
r2=s2.getRootTopic()
r2.setTitle("Transporter")


content={
'Transporters':[
    '工具类，Exchangerl与Transporter的工具类',
    {'bind(URL url, ChannelHandler... handlers)':[
        '核心方法:getTransporter().bind(url, (ChannelHandler)handler)',
    ]},
    {'connect(URL url, ChannelHandler... handlers)':[
        '核心方法:getTransporter().connect(url, (ChannelHandler)handler)'
    ]}
],
'Transporter':[
    '类注解：@SPI("netty")',
    {'Server bind(URL var1, ChannelHandler var2)':[
        '@Adaptive({"server", "transporter"})',
    ]},
    {'Client connect(URL var1, ChannelHandler var2)':[
        '@Adaptive({"server", "transporter"})'
    ]}
],
'NettyTransporter':[
    {'Server bind(URL url, ChannelHandler listener)':[
        'return new NettyServer(url, listener)'
    ]},
    {'Client connect(URL url, ChannelHandler listener)':[
        'return new NettyClient(url, listener)'
    ]}
]





}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 