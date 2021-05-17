import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
xmind_name="dubbo"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("Registry")
r2=s2.getRootTopic()
r2.setTitle("Registry")


content={
'Node接囗':[
    'URL getUrl()',
    'boolean isAvailable()',
    'void destroy()',
],
'RegistryService接囗':[
    {'void register(URL var1)':[
        '注册服务,注册需要处理契约:',
        '1.check=false:注册挫败后不报错，在后台定时重试,否则抛出异常',
        '2.dynamic=false:需持久存储，否则当注册者出现断电等情况异常退出时，自动删除',
        '3.category=overrides:分类存储',
        '4.当注册中心重启，网络抖动，不能丢失数据，包括断线自动删除数据',
        '5.允许URI相同但参数不同的URL并存，不能覆盖',
    ]},
    {'void unregister(URL var1)':[
        '取消注册服务,取消注册需要处理契约',
        '1.dynamic=false:持久存储数据,找不到注册数据,抛异常',
        '2.按全URL匹配取消注册'
    ]},
    {'void subscribe(URL var1, NotifyListener var2)':[
        '订阅服务，订阅需要处理契约',
        ''
    ]},
    {'void unsubscribe(URL var1, NotifyListener var2)':[
        '取消订阅服务，取消订阅需要处理契约',
        '1.如没订阅，忽略',
        '2.按全URL匹配取消订阅'
    ]},
    {'List<URL> lookup(URL var1)':[
        '查询注册列表',
        '与订阅的推模式相对应，这里为拉模式，只返回一次结果'
    ]}
],
'Registry接囗':[
    ''
],
'AbstractRegistry抽象类':[
    '实现注册、订阅、查询、通知,磁盘文件持久化注册信息等方法',
    '但注册、订阅、查询、通知等方法只是简单地把URL加入对应的集合，没有具体的注册或订阅逻辑',
    {'属性':[
        {'Properties properties':[
            '本地缓存',
            '如应用在启动过程中,注册中心无法连接或宕机，则Dubbo框架会自动通过本地缓存加载Invokers'
        ]},
        {'File file':[
            '磁盘文件服务缓存对象'
        ]},
        {'Set<URL> registered':[
            '已经在注册中心注册的url'
        ]},
        {'ConcurrentMap<URL, Set<NotifyListener>> subscribed':[
            'url与url对映的监听器'
        ]},
        {'ConcurrentMap<URL, Map<String, List<URL>>> notified':[
            '内存中的服务缓存对象',
            '外层Map的key:消费者的 URL',
            '内层Map的key:分类，包含 providers> consumers> routes> configurators四种',
            'value:对应的服务列表'
        ]}
    ]},
    {'AbstractRegistry(URL url)':[
        {'this.loadProperties()':[
            '会从本地磁盘文件中把持久化的注册数据读到Properties对象里，并加载到内存缓存中'
        ]}
    ]},
    {'notify(URL url, NotifyListener listener, List<URL> urls)':[
        '封装了更新内存缓存和更新文件缓存的逻辑',
        {'调用时机':[
            '当客户端第一次订阅获取全量数据',
            '订阅得到新数据时'
        ]},
        {'listener.notify(categoryList)':[
            '更新本地Directory管理的Invoker服务列表'
        ]}
       
    ]},
    {'register(URL url)':[
        'this.registered.add(url)'
    ]},
    {'unregister(URL url)':[
        'this.registered.remove(url)'
    ]},
    {'subscribe(URL url, NotifyListener listener)':[
        '向this.subscribed上的url添加listener'
    ]},
    {'unsubscribe(URL url, NotifyListener listener)':[
        '向this.subscribed上的url删除listener'
    ]},
],
'FailbackRegistry抽象类':[
    '重写了父类的注册、订阅、查询和通知等方法，并且添加了重试机制',
    '还添加了四个未实现的抽象模板方法',
    {'属性':[
        {'Set<URL> failedRegistered':[
            '失败的注册'
        ]},
        {'Set<URL> failedUnregistered':[
            '失败的取消注册'
        ]},
        {'ConcurrentMap<URL, Set<NotifyListener>> failedSubscribed':[
            '失败的订阅'
        ]},
        {'ConcurrentMap<URL, Set<NotifyListener>> failedUnsubscribed':[
            '失败的取消订阅'
        ]},
        {'ConcurrentMap<URL, Map<NotifyListener, List<URL>>> failedNotified':[
            '失败的通知'
        ]},
        {'ScheduledExecutorService retryExecutor':[
            '定时器，每经过固定间隔(默认为5秒)调用this.retry()'
        ]},
    ]},
    {'方法':[
        {'register(URL url)':[
            'super.register(url)',
            'this.doRegister(url)',
            '失败时执行:this.failedRegistered.add(url)'
        ]},
        {'subscribe(URL url, NotifyListener listener)':[
            'super.subscribe(url, listener)',
            'this.doSubscribe(url, listener)'
        ]}
    ]}

],
'ZookeeperRegistry':[
    {'':[
        {'ConcurrentMap<URL, ConcurrentMap<NotifyListener, ChildListener>> zkListeners':[
            ''
        ]},
        {'ZookeeperClient zkClient':[
            'dubbo封装的zk客户端'
        ]}
    ]},
    {'ZookeeperRegistry(URL url, ZookeeperTransporter zookeeperTransporter)':[
        {'创建zk客户端':[
            'this.zkClient = zookeeperTransporter.connect(url)'
        ]}
    ]},
    {'doRegister(URL url)':[
        '创建zk节点到zk:',
        'this.zkClient.create(this.toUrlPath(url), url.getParameter("dynamic", true));'
    ]},
    {'doUnregister(URL url)':[
        '删除zk上的节点:',
        'this.zkClient.delete(this.toUrlPath(url))'
    ]},
    {'doSubscribe(final URL url, final NotifyListener listener)':[
        '最终调用this.notify(url, listener, urls)',
    ]}
],
'DubboRegistry':[
    {'属性':[
        '',
        'Invoker<RegistryService> registryInvoker',
        'RegistryService registryService'
    ]},
],
}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 