import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="tomcat"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("Connector组件")
r2=s2.getRootTopic()
r2.setTitle("Connector组件")


content={
'端口监听+请求报文解析(生成Request对象)+响应报文组装(Response对象)':[],
'SSL安全通道支持:配置server.xml的<Connector>节点SSLEnabled属性开启':[],
'想像成门':[],
'3部分':[
    {'Protocol组件':[
        '对不同通信协议（HTTP和AJP）处理进行了封装，有：Http11Protocol、Http11NioProtocol',
        {'Endpoint':[
            '不同的I/O模式(server.xml的<Connector>节点配置),不同Endpoint',
            'BIO模式的JIoEndpoint',
            'NIO模式的NioEndpoint和本地库I/O模式的AprEndpoint',
            {'2部分':[
                'Acceptor：接收客户端连接的接收器组件',
                'Executor：处理客户端请求的线程池'
            ]}
        ]},
        {'Processor组件':[
            '处理客户端请求的处理器，不同的协议和I/O模式有不同的Processor'
        ]}
    ]},
    {'Mapper组件':[
        '路由器，对客户端请求URL进行映射',
        '通过它将请求转发到对应的Host组件、Context组件、Wrapper组件以进行处理并响应客户端',
        '将某客户端请求发送到某虚拟主机上的某个Web应用的某个Servlet'
    ]},
    {'CoyoteAdaptor组件':[
        '适配器，将Connector组件和Engine容器适配连接',
        '把请求报文解析生成的请求对象和响应对象Response传递到Engine容器，交由容器处理'
    ]}
]

}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 