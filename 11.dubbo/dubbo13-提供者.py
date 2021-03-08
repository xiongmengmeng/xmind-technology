import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
xmind_name="dubbo"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("服务提供者")
r2=s2.getRootTopic()
r2.setTitle("服务提供者")


content={
'服务提供者':[
    {'暴露服务流程':[
        '1.会通过Config组件中的ServiceConfig读取服务的配置信息(有三种形式，XML文件，注解和属性文件)',
        '2.读取配置文件生成服务实体后，通过ProxyFactory将Proxy转换成Invoker',
        '3.Invoker被定义Protocol，之后会被包装成Exporter',
        '4.Exporter发送到注册中心，作为服务的注册信息',
        '实现：ServiceConfig中的doExport方法'
    ]},
    {'服务提供者暴露服务的七个步骤':[
        '1.读取其他配置信息到map中，用来后面构造URL',
        '2.读取全局配置信息',
        '3.配置不是remote，也就是暴露本地服务',
        '4.如果配置了监控地址，则服务调用信息会上报',
        '5.通过Proxy转化成Invoker，RegistryURL存放的是注册中心的地址',
        '6.暴露服务以后，向注册中心注册服务信息',
        '7.没有注册中心直接暴露服务'
    ]},
    {'注册中心暴露服务的五个步骤':[
        '1.委托具体协议进行服务暴露，创建NettyServer监听端口，并保持服务实例',
        '2.创建注册中心对象，创建对应的TCP连接',
        '3.注册元数据到注册中心',
        '4.订阅Configurators节点',
        '5.如果需要销毁服务，需要关闭端口，注销服务信息',
        '实现：RegistryProtocol中的Export方法'
    ]}
]
}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 