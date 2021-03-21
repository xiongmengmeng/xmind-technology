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
'环境搭建':[
    '1.创建数据目录和日志目录',
    '2.创建myid文件:存放在数据目录下，内容只能是一个数字',
    {'3.创建和修改配置文件“.cfg”':[
        '前面准备的日志目录和数据目录',
        '端口信息clientPort',
        {'节点信息':[
            '配置集群中所有节点的（id）编号、IP地址和端口号',
            'server.id=host:port:port,前一个端口用于节点之间的通信，后一个端口用于选举主节点',
            {'ZooKeeper节点数要求':[
                'ZooKeeper集群节点数必须是奇数',
                'ZooKeeper集群至少是3个'
            ]}
        ]},
        {'时间相关选项':[
            {'tickTime':[
                '配置单元时间,默认值为3000，单位是毫秒（ms）'
            ]},
            {'initLimit':[
                '节点的初始化时间,用于Follower（从节点）的启动，并完成与Leader（主节点）进行数据同步的时间'
            ]},
            {'syncLimit':[
                '心跳最大延迟周期,用于配置Leader节点和Follower节点之间进行心跳检测的最大延时时间'
            ]}
        ]}
    ]},
    {'4.启动':[
        '为每一个节点制作一份启动命令".cmd"文件'
    ]}
],
'存储模型':[
    {'定义':[
        '一棵以 "/" 为根节点的树',
        '每一个节点，叫作ZNode（ZooKeeper Node）节点',
        '每个ZNode节点都用一个以 "/"（斜杠）分隔的完整路径来唯一标识',
        '整个树形的目录结构全部都放在内存中',
        '每个节点存放的有效负载数据（Payload）的上限仅为1MB'
    ]},
    {'zkCli客户端命令清单':[
        'create:创建znode路径节点',
        'ls:查看目录下的节点',
        'get',
        'set',
        'delete'
    ]},
    'ZNode节点信息的主要属性',
    {'ZooKeeper应用开发,通过Java客户端API去连接和操作ZooKeeper集群':[
        'ZooKeeper官方的Java客户端API',
        '第三方的Java客户端API:ZkClient',
        '第三方的Java客户端API:Curator'
    ]}
]
}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 