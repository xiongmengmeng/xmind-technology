import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
xmind_name="kafka"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("KafkaAdminClient")
r2=s2.getRootTopic()
r2.setTitle("KafkaAdminClient")


content={
'分区（Partition）':[
    '可引入了多副本（Replica）机制，提升容灾能力',
    '一个有序的message序列，这些message按顺序添加到一个叫做commit log的文件中',
    '每个partition中的消息都有一个唯一的编号，称之为offset，用来唯一标示某个分区中的message',

    'kafka一般不会删除消息，只会根据配置的日志保留时间(log.retention.hours)确认消息多久被删除',
    {'consumer':[
        '基于自己在commit log中的消费进度(offset)来进行工作的',
        '在kafka中，消费offset由consumer自己来维护'
    ]}

],
'分区概念':[
    {'leader节点':[
        '负责给定partition的所有读写请求'
    ]},
    {'AR（Assigned Replicas）':[
        '分区中的所有副本',
        'AR=ISR+OSR'
    ]},
    {'ISR（In-Sync Replicas）':[
        '所有与leader副本保持一定程度同步的副本'
    ]},
    {'OSR（Out-of-Sync Replicas）':[
        '与leader副本同步滞后过多的副本'
    ]},
    {'HW(High Watermark)':[
        '高水位',
        'ISR集合中最小的LEO即为分区的HW',
        '消费者只能拉取到这个offset之前的消息',
        '每个replica都有HW,leader和follower各自负责更新自己的HW的状态',
        {'作用':[
            '保证消费者消费数据的一致性'
        ]}
    ]},
    {'LEO(log-end-offset)':[
        '一个partition的最大的offset'
    ]}
],
'理解Topic，Partition和Broker':[
    'topic：代表逻辑上的一个业务数据集，对比数据库里的表',
    'Partition：数据库中的表做了分表，Partition代表其中的一张表',
    'Broker:对比一个数据库'
]
'可以用来管理主题、broker、配置和ACL（Access Control List）':[],
'继承了org.apache.kafka.clients.admin.AdminClient抽象类，并提供了多种方法':[
    '创建主题：CreateTopicsResult createTopics（Collection＜NewTopic＞newTopics）',
    '删除主题：DeleteTopicsResult deleteTopics（Collection＜String＞topics）',
    '列出所有可用的主题：ListTopicsResult listTopics（）',
    '查看主题的信息：DescribeTopicsResult describeTopics（Collection＜String＞topicNames）',
    '查询配置信息：DescribeConfigsResult describeConfigs（Collection＜ConfigResource＞resources）',
    '修改配置信息：AlterConfigsResult alterConfigs（Map＜ConfigResource，Config＞configs）',
    '增加分区：CreatePartitionsResult createPartitions（Map＜String，NewPartitions＞newPartitions）'
],
'主题合法性验证':[
    '自定义实现org.apache.kafka.server.policy.CreateTopicPolicy 接口',
    '实现接口中的configure（）、close（）及validate（）方法'
],
'分区的管理':[
    {'优先副本的选举':[
        'leader副本对外提供读写服务，follower副本只在内部进行消息的同步',
        '优先副本是指在AR集合列表中的第一个副本',
        '所有主题的优先副本在Kafka集群中均匀分布，保证所有分区的leader均衡分布',
        '优先副本的选举:通过一定的方式促使优先副本选举为leader副本，以此促进集群负载均衡',
        'broker 端参数是auto.leader.rebalance.enable，默认值为true:分区自动平衡',
        '不建议设置为true,因为分区及副本的均衡也不能完全确保集群整体的均衡'
    ]},
    {'分区重分配':[
        {'问题':[
            '当集群中新增broker节点时，只有新创建的主题分区才有可能被分配到这个节点上',
            '而之前的主题分区并不会自动分配到新加入的节点中，因在它们被创建时还没有这个新节点',
            '现象：新节点的负载和原先节点的负载之间严重不均衡',
        ]},
        {'操作':[
            '数据复制，先增加新的副本，然后进行数据同步，最后删除旧的副本',
        ]},
        '如某个broker下线，执行分区重分配动作前最好先关闭或重启broker',
        '这样这个broker就不再是任何分区的leader节点了，它的分区就可以被分配给集群中的其他broker',
        '这样可减少broker间的流量复制，以此提升重分配的性能，以及减少对集群的影响'
    ]},
    {'复制限流':[
        '重分配期间，对副本间的复制流量加以限制来保证重分配期间整体服务不会受太大的影响',
        '两种实现方式：kafka-config.sh脚本和kafka-reassign-partitions.sh脚本',
    ]},
    {'修改副本因子':[
        '通过重分配所使用的 kafka-reassign-partition.sh 脚本实现的'
    ]}
],
'何选择合适的分区数':[
]

  
}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 