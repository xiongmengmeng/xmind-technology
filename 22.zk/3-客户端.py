import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="zk"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("客户端")
r2=s2.getRootTopic()
r2.setTitle("客户端")


content={
'Zookeeper Java客户端':[
    {'maven依赖':[
        '<dependency>',
        '   <groupId>org.apache.zookeeper</groupId>',
        '   <artifactId>zookeeper</artifactId>',
        '   <version>3.5.8</version>',
        '</dependency>'
    ]},
    {'创建Zookeeper实例':[
        'ZooKeeper(String connectString, int sessionTimeout, Watcher watcher)',
        {'connectString':[
            'ZooKeeper服务器列表，由英文逗号分开的host:port字符串组成，每一个都代表一台ZooKeeper机器'
        ]},
        {'sessionTimeout':[
            '会话的超时时间，一个以“毫秒”为单位的整型值',
            '一个会话周期内，ZooKeeper客户端和服务器间通过心跳检测机制来维持会话的有效性',
            '一旦在sessionTimeout时间内没有进行有效的心跳检测，会话就会失效'
        ]},
        {'watcher':[
            '默认的Watcher事件通知处理器',
            '该参数可以设置为null,表明不需要设置默认的Watcher处理器'
        ]}
    ]}
],
'命令':[
    {'创建zookeeper节点':[
        'create [‐s] [‐e] [‐c] [‐t ttl] path [data] [acl]',
        '默认创建持久化节点',
        '-s: 顺序节点',
        '-e: 临时节点',
        '-c: 容器节点',
        '-t: 给节点添加过期时间，默认禁用，需通过系统参数启用',
        'path:所有的节点一定是以/开头,是绝对地址'
    ]},
    {'查看节点':[
        'get [‐s] [‐w] path',
        '-s:查看节点状态信息同时查看数据',
        '-w:对节点添加监听'
    ]},
    {'修改节点数据':[
        'set [‐s] [‐v] path data',
        '-v:版本号version'
    ]},
    {'查看节点状态信息':[
        {'cZxid':[
            '创建znode的事务ID（Zxid的值）'
        ]},
        {'mZxid':[
            '最后修改znode的事务ID'
        ]},
        {'pZxid':[
            '最后添加或删除子节点的事务ID（子节点列表发生变化才会发生改变）'
        ]},
        {'ctime':[
            'znode创建时间'
        ]},
        {'mtime':[
            'znode最近修改时间'
        ]},
        {'dataVersion':[
            'znode的当前数据版本(有并发修改数据实现乐观锁的功能)'
        ]},
        {'cversion':[
            'znode的子节点结果集版本（一个节点的子节点增加、删除都会影响这个版本）'
        ]},
        {'aclVersion':[
            '对此znode的acl版本'
        ]},
        {'ephemeralOwner':[
            'znode是临时znode，表示znode所有者的session ID',
            '如znode不是临时znode，该字段设置为零'
        ]},
        {'dataLength':[
            'znode数据字段的长度'
        ]},
        {'numChildren':[
            'znode的子znode的数量'
        ]}
    ]}
],


}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 