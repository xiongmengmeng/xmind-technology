import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="zk"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("Curator")
r2=s2.getRootTopic()
r2.setTitle("Curator")


content={
'Curator':[
    '现在ZooKeeper客户端中使用最多，对ZooKeeper版本支持最好的第三方客户端'
],
'maven依赖':[
    '<dependency>',
    '   <groupId>org.apache.curator</groupId>',
    '   <artifactId>>curator‐recipes</artifactId>',
    '   <version>5.0.0</version>',
    '</dependency>'
],
'会话创建':[
    'RetryPolicy retryPolicy = new ExponentialBackoffRetry(1000, 3)',
    'CuratorFramework client = CuratorFrameworkFactory.builder()',
    '   .connectString("192.168.128.129:2181") //服务器地址列表',
    '   .sessionTimeoutMs(5000) // 会话超时时间',
    '   .connectionTimeoutMs(5000) // 连接超时时间',
    '   .retryPolicy(retryPolicy)   //重试策略',
    '   .namespace("base") //隔离名称',
    '   .build();',
    'client.start();'
],
'创建节点':[
    'String path=curatorFramework.create().withMode(CreateMode.PERSISTENT).forPath("/curator‐node")',
    {'一次性创建带层级结构的节点':[
        'String pathWithParent="/node‐parent/sub‐node‐1";',
        'curatorFramework.create().creatingParentsIfNeeded().forPath(pathWithParent);'
    ]}
],
'获取数据':[
    'byte[] bytes = curatorFramework.getData().forPath("/curator‐node")'
],
'更新节点':[
    'curatorFramework.setData().forPath("/curator‐node","changed!".getBytes())'
],
'删除节点':[
    'String pathWithParent="/node‐parent"',
    'curatorFramework.delete().guaranteed().deletingChildrenIfNeeded().forPath(pathWithParent)',
    {'guaranteed':[
        '只要该客户端的会话有效，就会在后台持续发起删除请求，直到该数据节点在ZooKeeper服务端被删除'
    ]},
    {'deletingChildrenIfNeeded':[
        '系统在删除该数据节点的时候会以递归的方式直接删除其子节点，以及子节点的子节点'
    ]}
],
'监听器----CuratorListener接口':[
    '方法void eventReceived(CuratorFramework client, CuratorEvent event)'
],
'Caches':[
    '引入了Cache来实现对Zookeeper服务端事件监听，Cache事件监听可以理解为一个本地缓存视图与远程Zookeeper视图的对比过程',
    '提供了反复注册的功能',
    {'Cache分两类注册类型':[
        '节点监听',
        '子节点监听'
    ]},
    {'对某一个节点进行监听':[
        'NodeCache(CuratorFramework client,String path)',
        'PathChildrenCache(CuratorFramework client,String path,boolean cacheData)'
    ]},
    {'通过注册监听器实现对当前节点数据变化的处理':[
        'addListener(NodeCacheListener listener)'
    ]}
]



}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 