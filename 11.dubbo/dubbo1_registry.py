import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
xmind_name="dubbo_registry"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("dubbo_registry")
r2=s2.getRootTopic()
r2.setTitle("dubbo_registry")


content={

'实现了分布式环境中各服务之间的注册与发现， 是各个分布式节点之间的纽带':[],
'主要作用':[
    '动态加入',
    '动态发现',
    '动态调整',
    '统一配置'
],
'Dubbo有多种注册中心的实现， 分别是ZooKeeper（官方推荐的注册中心）,Redis等':[],
'源码模块dubbo-registry,主要内容':[
    'dubbo-registry-api:注册中心的所有API和抽象实现类',
    'dubbo-registry-zookeeper:使用ZooKeeper作为注册中心的实现'
],
'总体流程':[
    '1.服务提供者启动，向注册中心写入自己的元数据信息， 同时订阅配置元数据信息',
    '2.消费者启动，向注册中心写入自己的元数据信息，并订阅服务提供者、路由和配置元数据信息',
    '3.服务治理中心(dubbo-admin)启动，订阅所有消费者、服务提供者、路由和配置元数据信息',
    '4.当服务提供者离开或新服务提供者加入，注册中心服务提供者目录会变化，变化信息会动态通知给消费者、服务治理中心',
    '5.消费方发起服务调用时,异步将调用、统计信息等上报给监控中心（dubbo-monitor・simpl）'
],
'ZooKeepr':[
    '树形结构的注册中心',
    {'四种节点类型':[
        '持久节点：服务注册后保证节点不丢失，注册中心重启也会存在',
        '持久顺序节点：在持久节点特性基础上增加了节点先后顺序的能力',
        '临时节点：服务注册后连接丢失或session超时，注册的节点会自动被移除',
        '临时顺序节点：在临时节点特性的基础上增加了节点先后顺序的能力'
    ]},
    'Dubbo使用ZooKeeper作为注册中心，只创建持久节点和临时节点',
    {'树形结构':[
        'Root--根节点:注册中心分组，值来自配置<dubbo:registry>的grou 属性，默认是/dubbo',
        'Service--接口名称：服务接口',
        'Type--四种服务目：providers,consumers,routers,configurators',
        'URL--具体的Dubbo服务URL：URL元数据信息'
    ]},
],
'发布的实现':[
    'zkClient.create(toUrlPath(url)):调用了ZooKeeper的客户端库在注册中心上创建一个目录',
    'zkClient.delete(toUrlPath(url))',
    'org.apache.dubbo.registry.zookeeper.ZookeeperRegistry#doRegister',
    'org.apache.dubbo.registry.zookeeper.ZookeeperRegistry#destroy'
],
'订阅的实现':[
    {'订阅的两种方式':[
        'pull:客户端定时轮询注册中心拉取配置',
        'push:注册中心主动推送数据给客户端'
    ]},
    'Dubbo:第一次启动拉取方式， 后续接收事件重新拉取数据',
    {'事件通知+客户端拉取':[
        '客户端第一次连接上注册中心时，获取对应目录下全量的数据,并在订阅的节点上注册一个watcher,客户端与注册中心之间保持TCP长连接',
        '节点有任何数据变化，注册中心会回调主动通知客户端（事件通知）',
        '客户端接到通知，把对应节点下的全量数据都拉取过来（客户端拉取）'
    ]},
    '服务暴露时，服务端订阅configurators用于监听动态配置',
    '消费端启动时，消费端订阅providers、 routers和configuratops，对应服务提供者、 路由和动态配置变更通知',
    'org.apache.dubbo.registry.zookeeper.ZookeeperRegistry#doSubscribe'
],
'缓存机制':[
    '抽象类AbstractRegistry中实现',
    '使用主体：消费者或服务治理中心',
    {'本地缓存':[
        '内存:private final ConcurrentMap<URL> Map<Stringj List<URL>>> notified =new ConcurrentHashMap<URLMap<String> List<URL>>>()',
        '外层Mkey:消费者的URL,内层key:分类(providers> consumers> routes> configurators四种),value:对应的服务列表',
        '磁盘:private File file'
    ]},
    '缓存的加载:org.apache.dubbo.registry.support.AbstractRegistry#loadProperties',
    '缓存的保存与更新:org.apache.dubbo.registry.support.AbstractRegistry#notify(java.util.List<org.apache.dubbo.common.URL>)'
],
'重试机制':[
],
'设计模式':[
    '模板模式:如何订阅， 交给继承的子类实现',
    '工厂模式:所有的注册中心实现， 都是通过对应的工厂创建的'
]
}

for key in content:
    t1 = r2.addSubTopic()
    t1.setTopicHyperlink(s2.getID()) 
    list=key.split(":")
    t1.setTitle(list[0])
    if len(list)>1:
        t1.setPlainNotes(list[1]) 
    # print(content[key])
    for i in content[key]:
        # print(type(i))
        if(type(i).__name__=='dict'):
            for t in i:
                t2 = t1.addSubTopic()
                t2.setTopicHyperlink(t1.getID()) 
                t2.setTitle(t)
                for j in i[t]:
                    #print(j)
                    if(type(j).__name__=='dict'):
                        for h in j:
                            t3 = t2.addSubTopic()
                            t3.setTopicHyperlink(t2.getID()) 
                            t3.setTitle(h) 
                            for m in j[h]:
                                if(type(m).__name__=='dict'):
                                    for n in m:
                                        t4 = t3.addSubTopic()
                                        t4.setTitle(n) 
                                        for l in m[n]:
                                            if(type(l).__name__=='dict'):
                                                for k in l:
                                                    t5 = t4.addSubTopic()       
                                                    t5.setTitle(k)
                                                    for p in l[k]:
                                                        if(type(p).__name__=='dict'):
                                                            for u in p:
                                                                t6 = t5.addSubTopic()
                                                                t6.setTitle(u)
                                                                for y in p[u]:
                                                                    if(type(y).__name__=='dict'):
                                                                        for a in y:
                                                                            t7 = t6.addSubTopic()
                                                                            t7.setTitle(a)
                                                                            for b in y[a]:
                                                                                t8 = t7.addSubTopic()
                                                                                t8.setTitle(b)
                                                                    else:
                                                                        t7 = t6.addSubTopic()
                                                                        t7.setTopicHyperlink(t2.getID()) 
                                                                        t7.setTitle(y)              
                                                        else:
                                                            t6 = t5.addSubTopic()
                                                            t6.setTopicHyperlink(t2.getID()) 
                                                            t6.setTitle(p)                                                        
                                            else:
                                                t5 = t4.addSubTopic()
                                                t5.setTopicHyperlink(t3.getID()) 
                                                t5.setTitle(l) 
                                else:
                                    t4 = t3.addSubTopic()
                                    t4.setTopicHyperlink(t3.getID()) 
                                    t4.setTitle(m) 
                    else:
                        t3 = t2.addSubTopic()
                        t3.setTopicHyperlink(t2.getID()) 
                        t3.setTitle(j) 
        else:
            t2 = t1.addSubTopic()
            t2.setTopicHyperlink(t1.getID()) 
            t2.setTitle(i) 



topics=r2.getSubTopics()
for topic in topics:
    topic.addMarker(MarkerId.starBlue)

xmind.save(w,"c:\\Users\\btr\\Desktop\\dubbo.xmind") 