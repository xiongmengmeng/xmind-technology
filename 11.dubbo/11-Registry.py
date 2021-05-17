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