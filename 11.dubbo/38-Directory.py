import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
xmind_name="dubbo"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("RegistryDirectory<T>")
r2=s2.getRootTopic()
r2.setTitle("RegistryDirectory<T>")


content={
'作为':[
    'Directory的动态列表实现',
    '会自动从注册中心更新Invoker列表、配置信息、路由列表'
],
'两条逻辑线':[
    '框架与注册中心的订阅，并动态更新本地Invoker列表、路由列表、配置信息的逻辑',
    '子类实现父类的doList方法'
],
'属性':[
    {'Map<String, List<Invoker<T>>> methodInvokerMap':[
        'key是对应的方法名称，value是整个Invoker列表',
        '存入invoker，refreshInvoker(invokerUrls)时更新'
    ]}
],
'subscribe(URL url)':[
    '订阅某个URL的更新信息',
    'this.registry.subscribe(url, this)',
    '在引用每个需要RPC调用的Bean的时,调用此方法来订阅这个Bean的各种URL的变化'
],
'notify(List<URL> urls)':[
    '监听到配置中心对应的URL的变化，然后更新本地的配置参数',
    {'监听的URL分为三类':[
        '配置configurators',
        '路由规则router',
        'Invoker列表'
    ]},
    {'工作流程':[
        {'1.建立3个list,分类存放监听返回的url信息':[
            '新建三个List,分别保存更新的Invoker URL、路由配置URL、配置URL',
            '遍历监听返回的所有URL,分类后放入三个List中'
        ]},
        {'2.解析并更新配置参数':[
            {'对router类参数':[
                '遍历所有router类型的URL',
                '通过Router工厂把每个URL包装成路由规则',
                '更新本地的路由信息'
            ]},
            {'对Configurator类的参数':[
                '在dubbo-admin动态配置功能上修改生产者的参数,参数会保存在配置中心的configurators类目下',
                'notify监听到URL配置参数变化，会解析并更新本地的Configurator配置'
            ]},
            {'对providers类的参数':[
                '核心refreshInvoker(invokerUrls)', 
                '对Invoker类型的参数,订阅方会更新本地Directory管理的Invoker服务列表',
                '如empty协议的URL,会禁用该服务，并销毁本地缓存的Invoker',
                '如监听到的Invoker类型URL是空的，说明没有更新，直接使用本地的老缓存',
                '如监听到的Invoker类型URL不为空，把新的URL和本地老的URL合并，创建新的Invoker,找出差异的老Invoker并销毁'
            ]},
            '首先,然后通过Router工厂把每个URL包装成路由规则，最后'
        ]}
    ]}
],
'doList(Invocation invocation)':[
    '在字典里匹配出可以调用的Invoker列表，并返回给上层',
    {'1.根据方法名和首参数匹配Invoke':[
        'invokers = (List)localMethodInvokerMap.get(methodName + "." + args[0])'
    ]},
    {'2.根据方法名匹配Invoker':[
        'invokers = (List)localMethodInvokerMap.get(methodName)'
    ]},
    {'3.根据"*”匹配Invoke':[
        'invokers = (List)localMethodInvokerMap.get("*")'
    ]},
    {'4.遍历methodlnvokerMap,找到第一个Invoker列表返回':[
        'invokers = (List)iterator.next()'
    ]},
    '核心Map<String, List<Invoker<T>>> localMethodInvokerMap=this.methodInvokerMap',
    
],
'toInvokers(List<URL> urls)':[
    {'根据消费方protocol配置过滤不匹配协议':[
        'providerUrl.getProtocol().equals(acceptProtocol)'
    ]},
    {'合并provider端配置数据,I比如服务端IP和port等':[
        'URL url = mergeUrl(providerUrl);'
    ]},
    {'使用具体协议创建远程连接':[
        'invoker=new RegistryDirectory.InvokerDelegate(this.protocol.refer(this.serviceType, url), url, providerUrl)'
    ]}
]


}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 