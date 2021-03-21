import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="netty"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("ZooKeeper分布式协调")
r2=s2.getRootTopic()
r2.setTitle("ZooKeeper分布式协调")


content={
'Curator':[
    {'三个主要的模块':[
        {'curator-framework':[
            '对ZooKeeper的底层API的一些封装'
        ]},
        {'curator-client':[
            '提供了一些客户端的操作，例如重试策略等'
        ]},
        {'curator-recipes':[
            '封装了一些高级特性，如：Cache事件监听、选举、分布式锁、分布式计数器、分布式Barrier等'
        ]}
    ]},
    {'基本操作':[
        {'Curator客户端实例的创建':[
            '1.使用工厂类CuratorFrameworkFactory的静态newClient()方法',
            '2.使用工厂类CuratorFrameworkFactory的静态builder构造者方法'
        ]},
        {'创建ZNode节点':[
            '一般使用链式调用来完成节点的创建',
            'client.create().creatingParentsIfNeeded().withMode(CreateMode.PERSISTENT).forPath("/test/CRUD/node-1", "hello".getBytes("UTF-8"))'
        ]},
        {'读取节点':[
            '首先是判断节点是否存在，调用checkExists方法',
            '其次是获取节点的数据，调用getData方法',
            '最后是获取子节点列表，调用getChildren方法'
        ]},
        {'更新节点':[
            'setData()方法进行同步更新',
            'inBackground(AsyncCallback callback)方法，设置一个AsyncCallback回调实例,将更新数据的行为从同步执行变成了异步执行'
        ]},
        {'删除节点':[
            'delete()'
        ]}
    ]},
    {'对ZooKeeper服务器端的事件监听':[
        {'事件监听有两种模式':[
            {'标准的观察者模式':[
                '通过Watcher监听器实现',
                '只能监听一次'
            ]},
            {'缓存监听模式':[
                '引入了一种本地缓存视图Cache机制去实现',
                '事件监听的种类有3种：Path Cache,Node Cache和Tree Cache'
            ]}
        ]},
        {'接口类型Watcher':[
            '一个标准的事件处理器，用来定义收到事件通知后相关的回调处理逻辑',
            '事件回调方法：process（WatchedEvent event）',
            {'Watcher监听器实例向服务器端注册':[
                '通过GetDataBuilder、GetChildrenBuilder和ExistsBuilder等这类实现了Watchable<T>接口的构造者',
                '使用构造者的usingWatcher(Watcher w)方法，为构造者设置Watcher监听器实例',
                '例子：client.getData().usingWatcher(w).forPath("/test/CRUD/node-1")'
            ]}, 
            {'WatchedEvent包含了三个基本属性':[
                '通知状态（keeperState）',
                '事件类型（EventType）',
                '节点路径（path）'
            ]}
        ]},
        {'NodeCache节点缓存的监听':[
            {'分类':[
                'Node Cache节点缓存可用于ZNode节点的监听',
                'Path Cache子节点缓存可用于ZNode的子节点的监听',
                'Tree Cache树缓存是Path Cache的增强，不光能监听子节点，还能监听ZNode节点自身'
            ]},
            {'步骤':[
                '1.构造一个NodeCache缓存实例',
                '2.构造一个NodeCacheListener监听器实例,回调方法nodeChanged()',
                '3.将NodeCacheListener的实例注册到NodeCache缓存实例，使用缓存实例的addListener方法',
                '4.使用缓存实例nodeCache的start方法来启动节点的事件监听'
            ]},
            {'原理':[
                'Node Cache用来观察ZNode自身，如果ZNode节点本身被创建，更新或者删除，那么Node Cache会更新缓存，并触发事件给注册的监听器',
                'Node Cache是通过NodeCache类来实现的，监听器对应的接口为NodeCacheListener'
            ]}

        ]}
    ]}
]
}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 