import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
xmind_name="kafka"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("消费者(上)")
r2=s2.getRootTopic()
r2.setTitle("消费者(上)")


content={
'消费者':[
    '订阅Kafka中的主题（Topic），并且从订阅的主题上拉取消息'
],
'消费组':[
    '一个逻辑上的概念，将旗下的消费者归为一类，每一个消费者只隶属于一个消费组',
    '消费者与消费组这种模型可以让整体的消费能力具备横向伸缩性，通过增加消费者的个数来提高整体的消费能力'
],
'1.配置消费者客户端参数,创建消费者实例':[
    'bootstrap.servers：指定连接Kafka集群所需的broker地址清单',
    'group.id：消费者隶属的消费组名称',
    'key.deserializer 和 value.deserializer:消息中key和value所需反序列化操作的反序列化器',
    {'代码':[
        'Properties props = new Properties();',
        'props.put("group.id", "test-group");',
        'KafkaConsumer<String, String> consumer = new KafkaConsumer<String, String>(props);'
    ]}
],
'2.订阅主题':[
    '消费者自动再均衡的功能，在多个消费者的情况下可以根据分区分配策略来自动分配各个消费者与分区的关系',
    '当消费组内的消费者增加或减少时，分区分配关系会自动调整，以实现消费负载均衡及故障自动转移',
    {'代码':[
        'subscribe()'
    ]}
],
'3.拉取并消费消息':[
    '消费者消费的每条消息类型为ConsumerRecord，与生产者发送消息类型ProducerRecord相对应',
    {'ConsumerRecord':[
        'topic:消息所属主题的名称',
        'partition:所在分区的编号',
        'offset:消息在所属分区的偏移量',
        'timestamp:时间戳,两种类型：CreateTime 和LogAppendTime，分别代表消息创建时间戳和消息追加到日志时间戳',
        'key和value :消息的键和值',
        'count():消息集中的消息个数，返回类型是int',
        'isEmpty():判断消息集是否为空，返回类型是boolean'
    ]},
    '注：ConsumerRecords类中并没提供与partitions()类似的topics()方法来查看消息集中所包含的主题列表',
    {'代码':[
        'poll()'
    ]}
],
'4.提交消费位移offset':[
    '旧消费者客户端中:offset存储在ZooKeeper',
    {'新消费者客户端中':[
        'offset存储在Kafka内部的topic：consumer_offsets',
        'key:group.id+topic+分区号',
        'value:存offset',
        '定期compact：group.id+topic+分区号保留最新的那条数据'
    ]},
    '保证Kakfa集群中同分区的数据偏移量都提交到consumer_offset的同一个分区下',
    '消费者在消费完消息之后需要执行消费位移的提交',
    {'自动提交':[
        'enable.auto.commit=true,auto.commit.interval.ms=5000,5秒提交一次',
        '动作在poll()里，每次向服务端发起拉取请求前检查是否可以进行位移提交，如可以，提交上一次轮询的位移'
    ]},
    '手动提交:enable.auto.commit=false,分为同步提交和异步提交，对应于KafkaConsumer中的commitSync()和commitAsync()',
    {'指定位移消费':[
        '每当消费者查找不到所记录的消费位移时，会根据消费者客户端参数auto.offset.reset配置来决定从何处开始进行消费',
        {'参数':[
            'latest：从分区末尾开始消费消息',
            'earliest：从起始处，也就是0开始消费'
        ]}
    ]}
],
'5.控制或关闭消费':[
    'close()'
]

  
}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 