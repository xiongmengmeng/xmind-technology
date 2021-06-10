import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="zk"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("持久化")
r2=s2.getRootTopic()
r2.setTitle("持久化")


content={
'集群模式':[
    {'Leader':[
        '处理所有的事务请求（写请求）,也可处理读请求,集群中只能有一个Leader'
    ]},
    {'Follower':[
        '只能处理读请求，同时作为Leader的候选节点',
        '如Leader宕机，Follower节点要参与到新的Leader选举中，有可能成为新的Leader节点'
    ]},
    {'Observer':[
        '只能处理读请求,不能参与选举'
    ]},
    {'3.5.0新特性：集群动态配置':[
        '客户端可以通过监听/zookeeper/confg节点,感知集群的变化,实现集群的动态变更'
    ]}
],
'内存数据':[
    {'DataTree':[
        'ConcurrentHashMap<String, DataNode> nodes =new ConcurrentHashMap<String, DataNode>()',
        'WatchManager dataWatches = new WatchManager()',
        'WatchManager childWatches = new WatchManager()'
    ]},
    {'DataNode':[
        'Zookeeper存储节点数据的最小单位',
        '实现Record接囗',
        'byte data[]',
        'Long acl',
        'StatPersisted stat',
        'Set<String> children = null'
    ]}
],
'持久化':[
    {'事务日志':[
        {'存储路径':[
            'dataLogDir，如果没有配置, 将存储到dataDir （必填项）目录'
        ]},
        {'事务日志文件名':[
            'log.<当时最大事务ID>',
            '最大事务ID：整个事务日志文件中，最小的事务ID，日志满了即进行下一次事务日志文件的创建'
        ]},
        {'提供了格式化工具可以进行数据查看事务日志数据':[
            'org.apache.zookeeper.server.LogFormatter'
        ]}
    ]},
    {'数据快照':[
        '记录Zookeeper服务器上某一时刻的全量数据，并将其写入到指定的磁盘文件',
        '通过配置snapCount配置每间隔多少事务请求个数，生成快照，数据存储在dataDir指定的目录',
        {'快照事务日志文件名':[
            'snapshot.<当时最大事务ID>',
            '日志满了即进行下一次事务日志文件的创建',
        ]}
    ]}
]
}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 