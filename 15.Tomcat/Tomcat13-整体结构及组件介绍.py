import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="tomcat"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("整体结构及组件介绍")
r2=s2.getRootTopic()
r2.setTitle("整体结构及组件介绍")


content={

'将Tomcat内核高度抽象，则它可以看成由连接器（Connector）组件和容器（Container）组件组成':[],
'其中Connector组件负责在服务器端处理客户端连接，包括接收客户端连接、接收客户端的消息报文以及消息报文的解析等工作':[],
'而Container组件则负责对客户端的请求进行逻辑处理，并把结果返回给客户端':[],
'Server组件':[
    '最顶级的组件，它代表Tomcat的运行实例',
    '一个JVM中只会包含一个Server'
],
'Service组件':[
    '服务的抽象，它代表请求从接收到处理的所有组件的集合',
    'Server组件可以包含多个Service组件',
    '每个Service组件都包含了若干用于接收客户端消息的Connector组件和处理请求的Engine组件',
    '包含了若干Executor组件，每个Executor都是一个线程池，它可以为Service内所有组件提供线程池执行任务'
],
'Connector组件':[
    '主要的职责就是接收客户端连接并接收消息报文，消息报文经由它解析后送往容器中处理',
    'HTTP、AJP等协议每种对应一个Connector组件，目前Tomcat包含HTTP和AJP两种协议的Connector',
    {'3部分':[
        {'Http11Protocol组件':[
            '包含接收客户端连接、接收客户端消息报文、报文解析处理、对客户端响应整个过程',
            '主要包含JIoEndpoint组件和Http11Processor组件',
            '启动时，JIoEndpoint组件内部的Acceptor组件将启动某个端口的监听',
            '请求到来后将被放入线程池Executor，线程池进行任务处理',
            '过程中将通过Http11Processor组件对HTTP协议解析并传递到Engine容器继续处理'
        ]},
        'Mapper组件：客户端请求的路由导航组件，它能通过请求地址找到对应的Servlet',
        'CoyoteAdaptor组件：将Connector和Container适配起来的适配器'
    ]}
],
'Engine组件':[
    'Tomcat内部有4个级别的容器，分别是Engine、Host、Context和Wrapper',
    'Engine代表全局Servlet引擎，每个Service组件只能包含一个Engine容器组件',
    'Engine组件可以包含若干Host容器组件'
],
'Host组件':[
    'Tomcat中Host组件代表虚拟主机，这些虚拟主机可以存放若干Web应用的抽象（Context容器）'
],
'Context组件':[
    '是Web应用的抽象，Web应用部署到Tomcat后运行时就会转化成Context对象',
    '包含了各种静态资源、若干Servlet（Wrapper容器）以及各种其他动态资源'
],
'Wrapper组件':[
    'Wrapper容器是Tomcat中4个级别的容器中最小的，与之相对应的是Servlet，一个Wrapper对应一个Servlet'
]


}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 