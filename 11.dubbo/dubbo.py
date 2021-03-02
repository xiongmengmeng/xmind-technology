import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
xmind_name="dubbo"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("dubbo")
r2=s2.getRootTopic()
r2.setTitle("dubbo")


content={
'概述':[
    '单体应用：JEE时期->MVC框架时期',
    '分布式应用：SOA(Web Service和ESB)->微服务化->云原生',
    {'Dubbo':[
        '核心设计原则： 微内核+插件体系， 平等对待第三方'
    ]},
    '总体架构图',
    {'总体分层：':[
        {'业务层(Biz)':[
            'Service'
        ]},
        {'RPC层':[
            'Config',
            'Proxy',
            'Registry',
            'Cluster',
            'Monitor',
            'Protocol'
        ]},
        {'Remoting':[
            'Exchange',
            'Transport',
            'Serialize'
        ]}
    ]},
    'Dubbo的一次总体调用的过程'
],
'注册中心':[
    '实现了分布式环境中各服务之间的注册与发现， 是各个分布式节点之间的纽带',
    {'主要作用':[
        '动态加入',
        '动态发现',
        '动态调整',
        '统一配置'
    ]},
    'Dubbo有多种注册中心的实现， 分别是ZooKeeper（官方推荐的注册中心）,Redis等',
    {'源码模块dubbo-registry,主要内容':[
        'dubbo-registry-api:注册中心的所有API和抽象实现类',
        'dubbo-registry-zookeeper:使用ZooKeeper作为注册中心的实现'
    ]},
    {'总体流程':[
        '1.服务提供者启动，向注册中心写入自己的元数据信息， 同时订阅配置元数据信息',
        '2.消费者启动，向注册中心写入自己的元数据信息，并订阅服务提供者、路由和配置元数据信息',
        '3.服务治理中心(dubbo-admin)启动，订阅所有消费者、服务提供者、路由和配置元数据信息',
        '4.当服务提供者离开或新服务提供者加入，注册中心服务提供者目录会变化，变化信息会动态通知给消费者、服务治理中心',
        '5.消费方发起服务调用时,异步将调用、统计信息等上报给监控中心（dubbo-monitor・simpl）'
    ]},
    {'ZooKeepr':[
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
    ]},
    {'发布的实现':[
        'zkClient.create(toUrlPath(url)):调用了ZooKeeper的客户端库在注册中心上创建一个目录',
        'zkClient.delete(toUrlPath(url))',
        'org.apache.dubbo.registry.zookeeper.ZookeeperRegistry#doRegister',
        'org.apache.dubbo.registry.zookeeper.ZookeeperRegistry#destroy'
    ]},
    {'订阅的实现':[
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
    ]},
    {'缓存机制':[
        '抽象类AbstractRegistry中实现',
        '使用主体：消费者或服务治理中心',
        {'本地缓存':[
            '内存:private final ConcurrentMap<URL> Map<Stringj List<URL>>> notified =new ConcurrentHashMap<URLMap<String> List<URL>>>()',
            '外层Mkey:消费者的URL,内层key:分类(providers> consumers> routes> configurators四种),value:对应的服务列表',
            '磁盘:private File file'
        ]},
        '缓存的加载:org.apache.dubbo.registry.support.AbstractRegistry#loadProperties',
        '缓存的保存与更新:org.apache.dubbo.registry.support.AbstractRegistry#notify(java.util.List<org.apache.dubbo.common.URL>)'
    ]},
    {'重试机制':[
    ]},
    {'设计模式':[
        '模板模式:如何订阅， 交给继承的子类实现',
        '工厂模式:所有的注册中心实现， 都是通过对应的工厂创建的'
    ]}
],
'扩展点加载机制':[
    '作用：让整个框架的接口和具体实现解耦，增强扩展性',
    {'Java SPI':[
        'Service Provider Interface',
        '使用策略模式， 一个接口多种实现',
        '只声明接口，具体的实现不在程序中直接确定，由程序外的配置掌控',
        {'具体步骤':[
            '定义一个接口及对应的方法',
            '编写该接口的一个实现类',
            '在META-INF/services/目录下，创建一个以接口全路径命名的文件，如com.test.spi.PrintService',
            '文件内容为具体实现类的全路径名，如果有多个，则用分行符分隔',
            '在代码中通过java.util.ServiceLoader来加载具体的实现类'
        ]}
    ]},
    {'Dubbo SPI':[
        '只加载配置文件中的类，分成不同的种类缓存在内存，不会立即初始化，在性能上有更好',
        '增加对IoC和AOP的支持， 一个扩展可以直接setter注入其他扩展',
        '支持包装扩展类，推荐把通用的抽象逻辑放到包装类中， 实现扩展点的AOP特性'
    ]},
    {'分类':[
        'Class缓存:Dubbo SPI获取扩展类时，先从缓存读取，如缓存中不存在，则加载配置文件，根据配置把Class缓存到内存中，不会直接全部初始化',
        '实例缓存:先从缓存中读取，如缓存中读不到，重新加载并缓存起来'
    ]},
    {'扩展类的种类':[
        '普通扩展类:配置在SPI配置文件中',
        '包装扩展类（Wrapper类）:这种Wrapper类无具体的实现，只做了通用逻辑的抽象，需要在构造方法中传入一个具体的扩展接口的实现',
        '自适应扩展类（Adaptive类）:运行时， 通过传入URL中的某些参数动态确定'
    ]}
    {'扩展点的特性':[
        '自动包装:Wrapper--类继承Protocol接口，构造函数中注入了一个Protocol类型的参数(装饰器模式)',
        '自动加载：setter方法----某个扩展类是另外一个扩展点类的成员属性，拥有setter方法， 那么框架也会自动注入对应的扩展点实例',
        '自适应：@Adaptive注解，可动态通过URL中的参数来确定要使用哪个具体的实现类,从而解决自动加载中的实例注入问题',
        '自动激活：@Activate注解，可标记对应的扩展点默认被激活启用'
    ]},
    {'扩展点注解':[
        {'@SPI':[
            '用在类、 接口和枚举类上， Dubbo框架中使用在接口上',
            '作用：标记接口是一个Dubbo SPI接口(一个扩展点)，运行时需要通过配置找到具体实现类',
            'Dubbo中很多地方通过get Extension (Class<T> type. String name)来获取扩展点接口的具体实现'
        ]},
        {'©Adaptive':[
            '标记在类、 接口、 枚举类和方法上',
            '方法级别注解在第一次getExtension时，自动生成和编译一个动态的Adaptive类，达到动态实现类的效果'
        ]},
        {'©Activate':[
            '扩展点自动激活注解',
            '标记在类、 接口、 枚举类和方法上',
            '使用在有多个扩展点实现、需根据不同条件被激活的场景中，如Filter需要多个同时激活， 因为每个Filter实现的是不同的功能'
        ]}
    ]},
    {'ExtensionLoader':[
        '扩展机制的主要逻辑类，卖现了配置的加载、 扩展类缓存、 自适应对象生成等工作',
        '入口getExtension、 getAdaptiveExtension、getActivateExtension三个，分别是获取普通扩展类、 获取自适应扩展类、 获取自动激活的扩展类',
        {'get Extension (String name)':[
            '1.框架读取SPI对应路径下的配置文件，根据配置加载所有扩展类并缓存(不初始化)',
            '2.根据传入的名称初始化对应的扩展类',
            '3.尝试查找符合条件的包装类：包含扩展点的setter方法，包含与扩展点类型相同的构造函数',
            '4.返回对应的扩展类实例'
        ]},
        {'getAdaptiveExtension':[
            '1.和getExtension一样先加载配置文件',
            '2.生成自适应类的代码字符串',
            '3.获取类加载器和编译器， 并用编译器编译刚才生成的代码字符串',
            '4.返回对应的自适应类实例'
        ]}
    ]},
    {'ExtensionFactory':[
        '创建ExtensionLoader类',
        {'三个实现':[
            'AdaptiveExtensionFactory:持有所有的具体工厂，getExtension方法遍历它持有的所有工厂，最终还是调用SPI或Spring工厂实现的getExtension方法',
            'SpiExtensionFactory:获取扩展点接口对应的Adaptive实现类',
            'SpringExtensionFactory:把Spring上下文保存到Set集合,遍历S集合,根据名字从Spring容器中匹配，如没匹配到，根据类型匹配，如还没匹配到返回null'
        ]}
    ]},
    {'扩展点动态编译的实现':[
        'Dubbo SPI的自适应特性让整个框架非常灵活，动态编译是自适应特性的基础，因动态生成的自适应类只是字符串，需通过编译才能得到真正的Class',
        '使用反射来动态代理一个类， 但是在性能上和直接编译好的Class有一定的差距',
        'Dubbo SPI通过代码的动态生成， 并配合动态编译器，灵活地在原始类基础上创建新的自适应类',
        {'三种代码编译器':[
            'JDK编译器',
            'Javassist编译器:默认,不断通过正则表达式匹配不同部位的代码， 然后调用Javassist库中的API生成不同部位的代码， 最后得到一个完整的Class对象',
            'AdaptiveCompiler编译器:管理其他Compile,抽象类， 无法实例化， 但在里面封装了通用的模板逻辑'
        ]}
    ]},
    'Dubbo中很多地方通过get Extension (Class<T> type. String name)来获取扩展点接口的具体实现，此时会对传入的Class做校验，判断是否是接口，以及是否有@SPI注解， 两者缺一不可'
],
'启停原理解析':[
    '3种配置方式:XML配置、 注解、 属性文件(properties和ymal)配置',
    {'基于XML配置原理解析':[
        'DubboNamespaceHandler主要把不同的标签关联至U解析实现类中',
        '',
        'DubboBeanDefinitionParser实现:把标签解析成对应的Bean定义并注册到Spring ±下文中， 同时保证了 Spring容器中相同id的Bean不会被覆盖',
        'Dubbo只做了属性提取的事情， 运行时属性注入和转换都是Spring处理的',
        ''
    ]},
    {'基于注解配置原理解析':[
        '如果用户使用了配置文件， 则框架按需生成对应Bean',
        '将所有使用Dubbo的注解^Service的class提升为Bean',
        '为使用^Reference注解的字段或方法注入代理对象'
    ]},
    {'服务暴露的实现原理':[
        '',
        '',
        ''
    ]}
    'Dubbo配置解析',
    'Dubbo服务暴露原理',
    'Dubbo服务消费原理',
    'Dubbo优雅停机解析'
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