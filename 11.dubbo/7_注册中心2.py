import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
xmind_name="dubbo"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("注册中心2")
r2=s2.getRootTopic()
r2.setTitle("注册中心2")


content={
'发布的实现':[
    'zkClient.create(toUrlPath(url)):调用了ZooKeeper的客户端库在注册中心上创建一个目录',
    'zkClient.delete(toUrlPath(url)):zkClient删除路径源码',
    'org.apache.dubbo.registry.zookeeper.ZookeeperRegistry#doRegister',
    'org.apache.dubbo.registry.zookeeper.ZookeeperRegistry#destroy'
],
'订阅的实现':[
    {'订阅的两种方式':[
        'pull:客户端定时轮询注册中心拉取配置',
        'push:注册中心主动推送数据给客户端'
    ]},
    'Dubbo:第一次启动拉取方式， 后续接收事件重新拉取数据',
    {'Dubbo中的ZooKeeper客户端实现':[
        '无论服务提供者还是消费者， 或者是服务治理中心，连接到ZooKeeper注册中心都需要使用一个客户端',
        'Apache Curator:默认',
        'zkClient'
    ]},
    {'事件通知+客户端拉取':[
        '客户端第一次连接注册中心，获取对应目录下全量数据,并在订阅节点上注册一个watcher,客户端与注册中心之间保持TCP长连接',
        '节点有任何数据变化，注册中心会回调主动通知客户端（事件通知）',
        '客户端接到通知，把对应节点下的全量数据都拉取过来（客户端拉取）',
        'ZooKeeper的节点有一个版本号， 当节点数据发生变化，节点对应的版本号也会变化，触发watcher事件， 推送数据给订阅方'
    ]},
    '服务端启动时，服务端订阅configurators用于监听动态配置',
    '消费端启动时，消费端订阅providers、 routers和configuratops，对应服务提供者、 路由和动态配置变更通知',
    'org.apache.dubbo.registry.zookeeper.ZookeeperRegistry#doSubscribe'
],
'缓存机制':[
    '缓存的存在:用空间换取时间',
    '抽象类AbstractRegistry中实现',
    '使用主体：消费者或服务治理中心',
    {'本地缓存':[
        '内存:private final ConcurrentMap<URL> Map<Stringj List<URL>>> notified =new ConcurrentHashMap<URLMap<String> List<URL>>>()',
        '外层Mkey:消费者的URL,内层key:分类(providers> consumers> routes> configurators四种),value:对应的服务列表',
        '磁盘:private File file'
    ]},
    {'缓存的加载':[
        'AbstractRegistry#loadProperties'
    ]},
    {'缓存的保存与更新':[
        '客户端第一次订阅获取全量数据，或后续由于订阅得到新数据时调用',
        'AbstractRegistry#notify(java.util.List<org.apache.dubbo.common.URL>)'
    ]}
],
'重试机制':[
    'FailbackRegistry实现',
    '引入ScheduledExecutorService,每经过固定间隔(默认为5秒)调用FailbackRegistry#retry()方法'
],
'支持多注册中心':[
    '同一服务向多注册中心同时注册',
    '不同服务分别注册到不同注册中心',
    '同时引用注册在不同注册中心上的同名服务'
],
}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 