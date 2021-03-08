import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
xmind_name="dubbo"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("注册中心3")
r2=s2.getRootTopic()
r2.setTitle("注册中心3")


content={
'设计模式':[
    {'模板模式':[
        '如何订阅， 交给继承的子类实现',
        {'com.alibaba.dubbo.registry.RegistryService':[
            {'void register(URL url)':[
                '注册数据',
                '比如：提供者地址，消费者地址，路由规则，覆盖规则，等数据'
            ]},
            {'unregister(URL url)':[
                '取消注册'
            ]},
            {'void subscribe(URL url, NotifyListener listener)':[
                '订阅符合条件的已注册数据，当有注册数据变更时自动推送'
            ]},
            {'unsubscribe(URL url, NotifyListener listener)':[
                '取消订阅'
            ]},
            {'List<URL> lookup(URL url)':[
                '查询符合条件的已注册数据，与订阅的推模式相对应，这里为拉模式，只返回一次结果'
            ]}
        ]},
        {'AbstractRegistry':[
            '实现注册、 订阅、 查询、 通知、磁盘文件持久化注册信息等方法',
            '但注册、 订阅、 查询、 通知等方法只是简单地把URL加入对应的集合， 没有具体的注册或订阅逻辑'
        ]},
        {'FailbackRegistry':[
            '重写了父类的注册、 订阅、 查询和通知等方法， 并且添加了重试机制',
            '如重写了subscribe方法， 但只实现了订阅的大体逻辑及异常处理等通用性的东西。 具体如何订阅， 交给继承的子类实现',
            {'添加了四个未实现的抽象模板方法':[
                'protected abstract void doRegister(URL url);',
                'protected abstract void dollnregister(URL url);',
                'protected abstract void doSubscribe(URL url. NotifyListener listener);',
                'protected abstract void doUnsubscribe(URL url. NotifyListener listener);'
            ]}
        ]}
    ]},
    {'工厂模式':[
        '所有的注册中心实现， 都是通过对应的工厂创建的',
        {'RegistryFactory':[
            '连接注册中心',
            'Registry getRegistry(URL url)'
        ]},
        {'AbstractRegistryFactory':[
            {'实现方法getRegistry(URL url)':[
                '一个通用实现',
                '完成加锁和调用抽象模板方法createRegistry(URL url)创建具体实现， 并缓存在内存中'
            ]}
        ]}
    ]}
]
}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 