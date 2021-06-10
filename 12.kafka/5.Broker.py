import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
xmind_name="kafka"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("Broker")
r2=s2.getRootTopic()
r2.setTitle("Broker")


content={
'核心总控制器Controller':[
    '在Kafka集群中会有一个或者多个broker，其中有一个broker会被选举为控制器Controller',
    {'作用':[
        '负责管理整个集群中所有分区和副本的状态'
    ]},
    {'详细':[
        '1.当某个分区的leader副本出现故障时，由控制器负责为该分区选举新的leader副本',
        '2.当检测到某个分区的ISR集合发生变化时，由控制器负责通知所有broker更新其元数据信息',
        '3.当使用kafka-topics.sh脚本为某个topic增加分区数量时，同样还是由控制器负责让新分区被其他节点感知到'
    ]}
],
'Controller选举机制':[
    '1.集群中每个broker都会尝试在zookeeper上创建一个/controller临时节点',
    '2.zookeeper保证有且仅有一个broker能创建成功',
    '3.这个broker就会成为集群的总控器controller,其余broker监听此/controller临时节点',
    '4.当controller角色的broker宕机，zookeeper临时节点会消失',
    '5.集群里其他broker发现临时节点消失，再次尝试创建临时节点，循环上述过程到有broker创建/controller临时节点',
    {'具备控制器身份的broker':[
        {'1.监听broker相关的变化':[
            '为Zookeeper中的/brokers/ids/节点添加BrokerChangeListener，用来处理broker增减的变化'
        ]},
        {'2.监听topic相关的变化':[
            '为Zookeeper中的/brokers/topics节点添加TopicChangeListener，用来处理topic增减的变化',
            '为Zookeeper中的/admin/delete_topics节点添加TopicDeletionListener，用来处理删除topic的动作'
        ]},
        {'3.监听所有与topic、partition以及broker的信息':[
            '对于所有topic所对应的Zookeeper中的/brokers/topics/[topic]节点添加PartitionModificationsListener',
            '用来监听topic中的分区分配变化'
        ]},
        {'4.更新集群的元数据信息，同步到其他普通的broker节点中':[
            ''
        ]}
    ]}
],
'Partition副本选举Leader机制':[
    '1.controller感知到分区leader所在的broker挂了',
    {'2.unclean.leader.election.enable=false':[
        'controller会从ISR列表里挑第一个broker作为leader',
        '第一个broker最先放进ISR列表，可能是同步数据最多的副本',
        'ISR列表的副本都挂了时，阻塞到ISR列表中的节点重新启动'
    ]},
    {'2.unclean.leader.election.enable=true':[
        '在ISR列表里所有副本都挂了的时候可以在ISR列表以外的副本中选leader',
        '提高可用性，但是选出的新leader有可能数据少很多'
    ]},
    {'副本进入ISR列表有两个条件':[
        '1. 副本节点要能与zookeeper保持会话以及跟leader副本网络连通',
        '2. 副本能复制leader上的所有写操作，并不能落后太多',
        'replica.lag.time.max.ms:超过这个时间没有跟leader同步过的一次的副本会被移出ISR列表'
    ]}
],



}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 