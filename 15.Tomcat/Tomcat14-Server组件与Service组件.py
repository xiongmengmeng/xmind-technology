import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="tomcat"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("Server组件与Service组件")
r2=s2.getRootTopic()
r2.setTitle("Server组件与Service组件")


content={
'Server组件':[
    'Server组件是代表整个Tomcat的Servlet容器',
    'Tomcat的运行实例的抽象',
    {'3部分':[
        {'GlobalNamingResources组件':[
            '通过JNDI提供统一的命名对象访问接口，它的使用范围是整个Server'
        ]},
        {'ServerSocket组件':[
            '监听某个端口是否有SHUTDOWN命令，一旦接收到则关闭Server，即关闭Tomcat'
        ]},
        {'6个监听器组件':[
            'AprLifecycleListener监听',
            'JasperListener监听',
            'JreMemoryLeakPreventionListener监听',
            'GlobalResourcesLifecycleListener监听',
            'ThreadLocalLeakPreventionListener监听',
            'NamingContextListener监听'
            
        ]}
    ]},
    {'作用':[
        '提供了监听器机制，用于在Tomcat整个生命周期中对不同事件进行处理',
        '提供了Tomcat容器全局的命名资源实现',
        '监听某个端口以接收SHUTDOWN命令'
    ]},
],
'Service组件':[
    'Tomcat内的不同服务的抽象',
    '若干Connector组件和Executor组件组合而成',
    {'2部分':[
        {'Connector组件':[
            '负责监听某端口的客户端请求，不同的端口对应不同的Connector'
        ]},
        {'Executor组件':[
            '在Service抽象层面提供了线程池，让Service下的组件可以共用线程池',
            'JDK的JUC工具包'
        ]}
    ]}
]
}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 