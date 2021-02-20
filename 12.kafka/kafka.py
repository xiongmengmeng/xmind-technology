import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
xmind_name="kafka"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("kafka")
r2=s2.getRootTopic()
r2.setTitle("kafka")


content={
'1.概述':[
    '一个多分区、多副本且基于ZooKeeper协调的分布式消息系统',
    {'三大角色':[
        '消息系统',
        '存储系统',
        '流式处理平台'
    ]},
    {'体系结构':[
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
    ]},
    {'安装与配置':[
        'JDK',
        'ZooKeeper:实施对元数据信息的管理，包括集群、broker、主题、分区等内容',
        'Kafka'
    ]},
    {'服务端参数配置':[
        'zookeeper.connect:broker要连接的ZooKeeper集群的服务地址（含端口号）',
        'listeners:客户端要连接broker的入口地址列表',
        'broker.id:指定Kafka集群中broker的唯一标识，默认值为-1',
        'log.dir和log.dirs:配置 Kafka 日志文件存放的根目录',
        'message.max.bytes:指定broker所能接收消息的最大值'
    ]}],
'2.生产者':[
    {'1.配置生产者客户端参数，创建相应的生产者实例 KafkaProducer':[
        'bootstrap.servers:指定生产者客户端连接Kafka集群所需的broker地址清单',
        'key.serializer 和 value.serializer:序列化方式',
        'client.id：KafkaProducer对应的客户端id',
        '注：为防止写错，可直接使用客户端中的 org.apache.kafka.clients.producer.ProducerConfig类'
    ]},
    {'2.构建待发送消息 ProducerRecord':[
        'topic:消息要发往的主题',
        'artition:分区号',
        'headers:消息头部,用来设定一些与应用相关的信息',
        'key:消息的键，可用来计算分区号进而让消息发往特定分区,同一个key的消息会划分到同一个分区',
        'value:消息体，一般不为空，如果为空则表示特定的消息—墓碑消息',
        'timestamp:时间戳，有CreateTime（消息创建时间）和LogAppendTime（消息追加到日志文件时间）两种类型'
    ]},
    {'3.发送消息：KafkaProducer.send(),返回一个Future类型对象':[
        '发后即忘（fire-and-forget）',
        '同步（sync）',
        '异步（async）'
    ]},
    '4.关闭生产者实例',
    {'5.生产者拦截器':[
        {'ProducerInterceptor接口':[
            'onSend（）:在将消息序列化和计算分区之前会调用',
            'onAcknowledgement（）:消息被应答之前或发送失败时调用',
            'close（）:在关闭拦截器时执行一些资源的清理工'
        ]},
        '自定义的拦截器,需在 KafkaProducer 的配置参数interceptor.classes中指定拦截器',
    ]},
    {'6.序列化':[
        {'Serializer接口':[
            'configure（）:配置当前类',
            'serialize（）:执行序列化操作:将String类型转为byte[]类型',
            'close（）:关闭当前的序列化器'
        ]}
    ]},
    {'7.分区器':[
        {'消息在通过send（）方法发往broker':[
            '拦截器（Interceptor）',
            '序列化器（Serializer）',
            '分区器（Partitioner）'
        ]},
        'ProducerRecord中指定了partition字段，不需要分区器',
        'ProducerRecord中未指定partition字段，依赖分区器根据key计算partition',
        {'Partitioner接口':[
            'partition（）:计算分区号，返回值为int类型',
            'close（）:关闭分区器的时候用来回收一些资源',
            'configure（）:获取配置信息及初始化数据(继承自父类)'
        ]}
    ]},
    {'8.RecordAccumulator ':[
        '缓存消息以便 Sender 线程可以批量发送，减少网络传输的资源消耗',
        '缓存的大小:通过buffer.memory 配置，默认值32MB',
        '生产者发送消息的速度>发送到服务器的速度:生产者空间不足，此时send（）方法调用要么被阻塞，要么抛出异常',
        '内部为每个分区都维护了一个双端队列，队列中的内容就是ProducerBatch，即 Deque＜ProducerBatch＞'
    ]},
    {'9.Sender 线程':[
        'Sender 从 RecordAccumulator 中获取＜分区，Deque＜ProducerBatch＞＞的缓存消息'
        '转变为：＜Node，List＜ ProducerBatch＞的形式，其中Node表示Kafka集群的broker节点',
        '封装成＜Node，Request＞的形式',
        'Map＜NodeId，Deque＜Request＞＞:缓存了已经发出去但还没有收到响应的请求'
    ]},
    {'整体架构':[
        '生产者客户端由两个线程协调运行：主线程和Sender线程（发送线程）',
        '主线程中由KafkaProducer创建消息，然后通过可能的拦截器、序列化器和分区器的作用之后缓存到消息累加器',
        'Sender 线程:从RecordAccumulator中获取消息并将其发送到Kafka中',
    ]},
    {'重要的生产者参数':[
        'acks:',
        {'acks':[
            '指定分区中必须要有多少个副本收到这条消息，之后生产者才会认为这条消息是成功写入的',
            '配置的值是一个字符串类型'
            'acks=1:只要分区的leader副本成功写入消息，那么它就会收到来自服务端的成功响应',
            'acks=0:生产者发送消息之后不需要等待任何服务端的响应',
            'acks=-1:生产者在消息发送之后，需要等待ISR中的所有副本都成功写入消息之后才能够收到来自服务端的成功响应'
        ]},
        'max.request.size:限制生产者客户端能发送的消息的最大值，默认值为 1048576B，即 1MB',
        'retries和retry.backoff.ms:生产者重试的次数，默认值为0，两次重试之间的时间间隔,默认值为100',
        'request.timeout.ms:Producer等待请求响应的最长时间，默认值为30000（ms）。请求超时之后可以选择进行重试'
    ]}
],
'消费者':[
    '消费者:订阅Kafka中的主题（Topic），并且从订阅的主题上拉取消息',
    '消费组：一个逻辑上的概念，将旗下的消费者归为一类，每一个消费者只隶属于一个消费组',
    '消费者与消费组这种模型可以让整体的消费能力具备横向伸缩性，通过增加消费者的个数来提高整体的消费能力',
    {'消息消费逻辑':[
        '1.配置消费者客户端参数及创建相应的消费者实例',
        '2.订阅主题',
        '3.拉取消息并消费',
        '4.提交消费位移',
        '5.关闭消费者实例'
    ]},
    {'1.配置消费者客户端参数及创建相应的消费者实例':[
        'bootstrap.servers：指定连接Kafka集群所需的broker地址清单',
        'group.id：消费者隶属的消费组名称',
        'key.deserializer 和 value.deserializer:消息中key和value所需反序列化操作的反序列化器',
        'client.id：设定KafkaConsumer对应的客户端id'
    ]},
    {'2.订阅主题:subscribe（）方法':[
        '消费者自动再均衡的功能，在多个消费者的情况下可以根据分区分配策略来自动分配各个消费者与分区的关系',
        '当消费组内的消费者增加或减少时，分区分配关系会自动调整，以实现消费负载均衡及故障自动转移'
    ]},
    {'3.拉取消息并消费poll（）方法':[
        '消费者消费到的每条消息的类型为ConsumerRecord，与生产者发送的消息类型ProducerRecord相对应',
        {'ConsumerRecord':[
            'topic:消息所属主题的名称',
            'partition:所在分区的编号',
            'offset:消息在所属分区的偏移量',
            'timestamp:时间戳,有两种类型：CreateTime 和LogAppendTime，分别代表消息创建的时间戳和消息追加到日志的时间戳',
            'headers:消息的头部内容',
            'key 和 value :消息的键和消息的值',
            'count（）:计算消息集中的消息个数，返回类型是int',
            'isEmpty（）:判断消息集是否为空，返回类型是boolean',
            'empty（）:获取一个空的消息集，返回类型是ConsumerRecord＜K，V＞。'
        ]},
        '注：ConsumerRecords 类中并没提供与 partitions（）类似的 topics（）方法来查看消息集中所包含的主题列表'
    ]},
    {'4.提交消费位移offset':[
        '旧消费者客户端中，消费位移是存储在ZooKeeper中的',
        '新消费者客户端中，消费位移存储在Kafka内部的主题__consumer_offsets中',
        '消费者在消费完消息之后需要执行消费位移的提交',
        {'自动提交':[
            'enable.auto.commit=true,auto.commit.interval.ms=5000,5秒提交一次',
            '动作是在poll（）方法里，每次向服务端发起拉取请求前检查是否可以进行位移提交，如可以，提交上一次轮询的位移'
        ]},
        '手动提交:enable.auto.commit=false,分为同步提交和异步提交，对应于 KafkaConsumer 中的 commitSync（）和commitAsync（）方法'
    ]},
    '5.控制或关闭消费close（）方法',
    {'指定位移消费':[
        '在 Kafka 中每当消费者查找不到所记录的消费位移时，就会根据消费者客户端参数auto.offset.reset的配置来决定从何处开始进行消费',
        {'':[
            'latest”，表示从分区末尾开始消费消息',
            '“earliest”，那么消费者会从起始处，也就是0开始消费'
        ]}
    ]},
    {'再均衡':[
        '分区的所属权从一个消费者转移到另一消费者的行为，它为消费组具备高可用性和伸缩性提供保障',
        '',
        '再均衡发生期间，消费组内的消费者是无法读取消息的,重发消费消息',
        {'再均衡监听器 ConsumerRebalanceListener':[
            'onPartitionsRevoked(Collection＜TopicPartition＞partitions):再均衡开始之前和消费者停止读取消息之后被调用,通过这个回调方法来处理消费位移的提交',
            '',
            'onPartitionsAssigned(Collection＜TopicPartition＞partitions):在重新分配分区之后和消费者开始读取消费之前被调用。参数partitions表示再均衡后所分配到的分区。'
        ]}
    ]},
    {'消费者拦截器':[
        {'ConsumerInterceptor接口':[
            'public ConsumerRecords＜K,V＞onConsume(ConsumerRecords＜K,V＞records):KafkaConsumer会在poll（）方法返回之前调用,对消息进行相应的定制化操作',
            'public void onCommit(Map＜TopicPartition,OffsetAndMetadata＞offsets):KafkaConsumer会在提交完消费位移之后调用拦截器的onCommit（）方法,如记录跟踪所提交的位移信息',
            'public void close()'
        ]}
    ]},
    {'多线程实现':[
        'KafkaConsumer却是非线程安全的',
        {'实现方式':[
            '第一种：线程封闭，即为每个线程实例化一个KafkaConsumer对象',
            '第二种方式是多个消费线程同时消费同一个分区，这个通过 assign（）、seek（）等方法实现,不推荐。一般而言，分区是消费线程的最小划分单位',
            '第三种实现方式，将处理消息模块改成多线程的实现方式,对于消息的顺序处理就比较困难'
        ]}
    ]},
    {'重要的消费者参数':[
        'fetch.min.bytes：Consumer在一次拉取请求（调用poll（）方法）中能从Kafka中拉取的最小数据量',
        'fetch.max.wait.ms：Kafka的等待时间，默认值为500（ms）。如果Kafka中没有足够多的消息而满足不了fetch.min.bytes参数的要求，那么最终会等待500ms',
        'max.poll.records：配置Consumer在一次拉取请求中拉取的最大消息数，默认值为500（条）',
        
    ]}],
'4.主题与分区':[
    {'主题':[
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
    ]},
    {'KafkaAdminClient':[
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

    ]}

]
}

for key in content:
    t1 = r2.addSubTopic()
    t1.setTopicHyperlink(s2.getID()) 
    list=key.split(":")
    t1.setTitle(list[0])
    if len(list)>1:
        t1.setPlainNotes(list[1]) 
    # print(content[key])
    for i in content[key]:
        # print(type(i))
        if(type(i).__name__=='dict'):
            for t in i:
                t2 = t1.addSubTopic()
                t2.setTopicHyperlink(t1.getID()) 
                t2.setTitle(t)
                for j in i[t]:
                    #print(j)
                    if(type(j).__name__=='dict'):
                        for h in j:
                            t3 = t2.addSubTopic()
                            t3.setTopicHyperlink(t2.getID()) 
                            t3.setTitle(h) 
                            for m in j[h]:
                                if(type(m).__name__=='dict'):
                                    for n in m:
                                        t4 = t3.addSubTopic()
                                        t4.setTitle(n) 
                                        for l in m[n]:
                                            if(type(l).__name__=='dict'):
                                                for k in l:
                                                    t5 = t4.addSubTopic()       
                                                    t5.setTitle(k)
                                                    for p in l[k]:
                                                        if(type(p).__name__=='dict'):
                                                            for u in p:
                                                                t6 = t5.addSubTopic()
                                                                t6.setTitle(u)
                                                                for y in p[u]:
                                                                    if(type(y).__name__=='dict'):
                                                                        for a in y:
                                                                            t7 = t6.addSubTopic()
                                                                            t7.setTitle(a)
                                                                            for b in y[a]:
                                                                                t8 = t7.addSubTopic()
                                                                                t8.setTitle(b)
                                                                    else:
                                                                        t7 = t6.addSubTopic()
                                                                        t7.setTopicHyperlink(t2.getID()) 
                                                                        t7.setTitle(y)              
                                                        else:
                                                            t6 = t5.addSubTopic()
                                                            t6.setTopicHyperlink(t2.getID()) 
                                                            t6.setTitle(p)                                                        
                                            else:
                                                t5 = t4.addSubTopic()
                                                t5.setTopicHyperlink(t3.getID()) 
                                                t5.setTitle(l) 
                                else:
                                    t4 = t3.addSubTopic()
                                    t4.setTopicHyperlink(t3.getID()) 
                                    t4.setTitle(m) 
                    else:
                        t3 = t2.addSubTopic()
                        t3.setTopicHyperlink(t2.getID()) 
                        t3.setTitle(j) 
        else:
            t2 = t1.addSubTopic()
            t2.setTopicHyperlink(t1.getID()) 
            t2.setTitle(i) 



topics=r2.getSubTopics()
for topic in topics:
    topic.addMarker(MarkerId.starBlue)

xmind.save(w,"c:\\Users\\btr\\Desktop\\kafka.xmind") 