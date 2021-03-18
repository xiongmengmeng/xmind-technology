import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
xmind_name="kafka"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("kafka概述")
r2=s2.getRootTopic()
r2.setTitle("kafka概述")


content={
'一个多分区、多副本且基于ZooKeeper协调的分布式消息系统':[],
'三大角色':[
    '消息系统',
    '存储系统',
    '流式处理平台'
],
'体系结构':[
    'Producer：生产者',
    'Consumer：消费者',
    'Broker：服务代理节点',
    '主题（Topic）',
    {'分区（Partition）':[
        '一个分区只属于单个主题',
        '分区有序而不是主题有序',
        '引入了多副本（Replica）机制，提升容灾能力',
        'AR（Assigned Replicas）:分区中的所有副本',
        'ISR（In-Sync Replicas）:所有与leader副本保持一定程度同步的副本',
        'OSR（Out-of-Sync Replicas）:与leader副本同步滞后过多的副本',
        'AR=ISR+OSR',
        {'HW(High Watermark)':[
            '高水位',
            '标识一个特定的消息偏移量（offset）',
            '消费者只能拉取到这个offset之前的消息',
            'ISR集合中最小的LEO即为分区的HW'
        ]}
    ]}
],
'安装与配置':[
    'JDK',
    'ZooKeeper:实施对元数据信息的管理，包括集群、broker、主题、分区等内容',
    'Kafka'
],
'服务端参数配置':[
    'zookeeper.connect:broker要连接的ZooKeeper集群的服务地址（含端口号）',
    'listeners:客户端要连接broker的入口地址列表',
    'broker.id:指定Kafka集群中broker的唯一标识，默认值为-1',
    'log.dir和log.dirs:配置 Kafka 日志文件存放的根目录',
    'message.max.bytes:指定broker所能接收消息的最大值'
]
  
}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 