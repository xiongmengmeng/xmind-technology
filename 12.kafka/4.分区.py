import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
xmind_name="kafka"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("主题与分区")
r2=s2.getRootTopic()
r2.setTitle("主题与分区")


content={
'主题':[
    {'创建主题':[
        'kafka-topics.sh脚本的create指令，实际通过kafka.admin.TopicCommand类管理主题',
        'kafka-topics.sh脚本中的 zookeeper、partitions、replication-factor和topic这4个参数分别代表ZooKeeper连接地址、分区数、副本因子和主题名称',
        {'实质':[
            '在ZooKeeper中的/brokers/topics节点下创建与该主题对应的子节点并写入分区副本分配方案',
            '在/config/topics/节点下创建与该主题对应的子节点并写入主题相关的配置信息'
        ]},
        '主题名称:由大小写字母、数字、点号“.”、连接线“-”、下画线“_”组成，不能只有点号“.”或双点号“..”',
        {'主题、分区、副本和Log之间的关系':[
            '主题和分区都是提供给上层用户的抽象，而在副本层面或更加确切地说是Log层面才有实际物理上的存在',
            '同一个分区中的多个副本必须分布在不同的broker中，这样才能提供有效的数据冗余'
        ]},

    ]},
    {'查看主题':[
        'kafka-topics.sh脚本中的list、describe指令',
    ]},
    {'修改主题':[
        '由kafka-topics.sh脚本中的alter指令',
        '不支持减少分区'
    ]},
    {'配置管理':[
        'kafka-configs.sh脚本:在运行状态下修改原有的配置，达到动态变更的目的'
    ]},
    {'删除主题':[
        'kafka-topics.sh脚本中的delete指令,broker端配置参数delete.topic.enable需为true才能够删除主题',
        '实质：在ZooKeeper中的/admin/delete_topics 路径下创建一个与待删除主题同名的节点，以此标记该主题为待删除的状态'
    ]}
],
'KafkaAdminClient':[
    '可以用来管理主题、broker、配置和ACL（Access Control List）',
    {'继承了org.apache.kafka.clients.admin.AdminClient抽象类，并提供了多种方法':[
        '创建主题：CreateTopicsResult createTopics（Collection＜NewTopic＞newTopics）',
        '删除主题：DeleteTopicsResult deleteTopics（Collection＜String＞topics）',
        '列出所有可用的主题：ListTopicsResult listTopics（）',
        '查看主题的信息：DescribeTopicsResult describeTopics（Collection＜String＞topicNames）',
        '查询配置信息：DescribeConfigsResult describeConfigs（Collection＜ConfigResource＞resources）',
        '修改配置信息：AlterConfigsResult alterConfigs（Map＜ConfigResource，Config＞configs）',
        '增加分区：CreatePartitionsResult createPartitions（Map＜String，NewPartitions＞newPartitions）'
    ]},
    {'主题合法性验证':[
        '自定义实现org.apache.kafka.server.policy.CreateTopicPolicy 接口',
        '实现接口中的configure（）、close（）及validate（）方法'
    ]},
    {'分区的管理':[
        '优先副本的选举、分区重分配、复制限流、修改副本因子等内容',
        {'优先副本的选举':[
            '分区使用多副本机制来提升可靠性，但只有leader副本对外提供读写服务，而follower副本只负责在内部进行消息的同步',
            '优先副本是指在 AR 集合列表中的第一个副本',
            '所有主题的优先副本在Kafka集群中均匀分布，这样就保证了所有分区的leader均衡分布',
            '优先副本的选举:通过一定的方式促使优先副本选举为leader副本，以此来促进集群的负载均衡，这一行为也可以称为“分区平衡',
            'broker 端参数是auto.leader.rebalance.enable，此参数的默认值为true:分区自动平衡',
            '不建议设置为true,因为分区及副本的均衡也不能完全确保集群整体的均衡'
        ]},
        {'分区重分配':[
            '当集群中新增broker节点时，只有新创建的主题分区才有可能被分配到这个节点上，而之前的主题分区并不会自动分配到新加入的节点中，因为在它们被创建时还没有这个新节点，这样新节点的负载和原先节点的负载之间严重不均衡',
            '让分区副本再次进行合理的分配，也就是所谓的分区重分配',
            '数据复制，先增加新的副本，然后进行数据同步，最后删除旧的副本来达到最终的目的',
            '如果要将某个broker下线，那么在执行分区重分配动作之前最好先关闭或重启broker。这样这个broker就不再是任何分区的leader节点了，它的分区就可以被分配给集群中的其他broker。这样可以减少broker间的流量复制，以此提升重分配的性能，以及减少对集群的影响'
        ]},
        {'复制限流':[
            '重分配期间，对副本间的复制流量加以限制来保证重分配期间整体服务不会受太大的影响',
            '两种实现方式：kafka-config.sh脚本和kafka-reassign-partitions.sh脚本',
            ''
        ]},
        {'修改副本因子':[
            '通过重分配所使用的 kafka-reassign-partition.sh 脚本实现的'
        ]}
    ]},
    {'何选择合适的分区数':[
        ''
    ]}

]
  
}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 