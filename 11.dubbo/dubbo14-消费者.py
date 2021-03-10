import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
xmind_name="dubbo"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("服务消费者")
r2=s2.getRootTopic()
r2.setTitle("服务消费者")


content={


'服务消费者首先持有远程服务实例生成的 Invoker，然后把 Invoker 转换成用户接口的动态代理引用':[],
'消费者服务调用服务提供者':[
    '1.检查是否是同一个 JVM 内部引用',
    '2.如果是同一个 JVM 的引用，直接使用 injvm 协议从内存中获取实例',
    '3.注册中心地址后，添加 refer 存储服务消费元数据信息',
    '4.单注册中心消费',
    '5.依次获取注册中心的服务，并且添加到 Invokers 列表中',
    '6.通过 Cluster 将多个 Invoker 转换成一个 Invoker',
    '7.把 Invoker 转换成接口代理',
    '框架进行服务引用的入口,ReferenceBean 中的 getObject 方法',
]

}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 