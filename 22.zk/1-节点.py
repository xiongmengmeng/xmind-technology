import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="zk"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("节点")
r2=s2.getRootTopic()
r2.setTitle("节点")


content={
'Zookeeper':[
    '分布式应用协调框架',
    '一个用于存储少量数据的基于内存的数据库',
    {'应用场景':[
        '1. 分布式配置中心',
        '2. 分布式注册中心',
        '3. 分布式锁',
        '4. 分布式队列',
        '5. 集群选举',
        '6. 分布式屏障',
        '7. 发布/订阅',
    ]},
    {'两个核心概念':[
        '文件系统数据结构',
        '监听通知机制'
    ]},
],
'文件系统数据结构':[
    '维护一个类似文件系统的数据结构',
    '每个子目录项都被称作为znode(目录节点)',
    {'六种znode':[
        {'PERSISTENT­':[
            '持久化目录节点'
        ]},
        {'PERSISTENT_SEQUENTIAL­':[
            '持久化顺序编号目录节点'
        ]},
        {'EPHEMERAL­':[
            '临时目录节点',
            '临时节点不能创建子节点',
        ]},
        {'EPHEMERAL_SEQUENTIAL­':[
            '临时顺序编号目录节点'
        ]},
        {'Container':[
            '如没有给其创建子节点，容器节点表现同持久化节点',
            '如给容器节点创建了子节点，后续又把子节点清空，容器节点也会被删除(定时任务默认60s检查一次)'
        ]},
        {'TTL节点':[
            '默认禁用，只能通过系统配置zookeeper.extendedTypesEnabled=true开启，不稳定'
        ]}
    ]}
],
'监听通知机制':[
    {'三种':[
        {'对节点进行监听':[
            'get ‐w /path',
            '当节点被删除或被修改，对应的客户端将被通知'
        ]},
        {'对目录进行监听':[
            'ls ‐w /path',
            '当目录有子节点被创建或删除，对应的客户端将被通知',
            '注意节点内容更新不在监听范围'
        ]},
        {'对目录的递归子节点进行监听':[
            'ls ‐R ‐w /path:‐R 区分大小写，一定用大写',
            '当目录有子节点被创建或删除,或者根节点有数据变化，对应的客户端将被通知'
        ]},
    ]},
    {'Zookeeper事件类型':[
        {'None':[
            '连接建立事件'
        ]},
        {'NodeCreated':[
            '节点创建'
        ]},
        {'NodeDeleted':[
            '节点删除'
        ]},
        {'NodeDataChanged':[
            '节点数据变化'
        ]},
        {'NodeChildrenChanged':[
            '子节点列表变化'
        ]},
        {'DataWatchRemoved':[
            '节点监听被移除'
        ]},
        {'ChildWatchRemoved':[
            '子节点监听被移除'
        ]}
    ]},
    {'注意':[
        '所有通知都是一次性的，一旦触发，对应的监听即被移除',
        '递归子节点，监听是对所有子节点的，所以，每个子节点下面的事件同样只会被触发一次'
    ]}
],

}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 