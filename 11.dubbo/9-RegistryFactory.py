import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
xmind_name="dubbo"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("RegistryFactory")
r2=s2.getRootTopic()
r2.setTitle("RegistryFactory")


content={
'RegistryFactory接囗':[
    {'类注解':[
        '@SPI("dubbo")'
    ]},
    {'方法':[
        '@Adaptive({"protocol"})',
        'Registry getRegistry(URL var1)',
        {'详细':[
            '连接注册中心,连接注册中心需要处理契约:',
            'check=false:不检查连接,否则连接不上时抛出异常',
            'username:password权限认证',
            'backup=10.20.153.10备选注册中心集群地址',
            'file=registry.cache:本地磁盘文件缓存',
            'timeout=1000:请求超时设置',
            'session=60000:会话超时或过期设置',
        ]}
    ]}
],
'AbstractRegistryFactory抽象类':[
    {'属性':[
        'ReentrantLock LOCK = new ReentrantLock()',
        {'Map<String, Registry> REGISTRIES':[
            '缓存注册中心'
        ]}
    ]},
    {'方法':[
        {'getRegistry(URL url)':[
            'LOCK.lock()',
            {'Registry registry = (Registry)REGISTRIES.get(key)':[
                '模版方法',
                '根据url来创建具体的注册中心'
            ]},
            {'REGISTRIES.put(key, registry)':[
                '将其放入缓存'
            ]},
            'LOCK.unlock()'
        ]}
    ]}
],
'ZookeeperRegistryFactory':[
    {'createRegistry(URL url)':[
        'new ZookeeperRegistry(url, this.zookeeperTransporter)'
    ]}
],
'DubboRegistryFactory':[
    {'属性':[
        'Protocol protocol',
        'ProxyFactory proxyFactory',
        'Cluster cluster',
        'Map<String, Registry> REGISTRIES'
    ]},
    {'方法':[
        {'getRegistryURL(URL url)':[
            '去Map<String, Registry> REGISTRIES中取',
            '取不到调用createRegistry(URL url)'
        ]},
        {'createRegistry(URL url)':[
            '模版方法'
        ]}
    ]}
],

}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 