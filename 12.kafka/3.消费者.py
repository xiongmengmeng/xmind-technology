import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
xmind_name="kafka"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("消费者")
r2=s2.getRootTopic()
r2.setTitle("消费者")


content={
'消费者:订阅Kafka中的主题（Topic），并且从订阅的主题上拉取消息':[],
'消费组：一个逻辑上的概念，将旗下的消费者归为一类，每一个消费者只隶属于一个消费组':[],
'消费者与消费组这种模型可以让整体的消费能力具备横向伸缩性，通过增加消费者的个数来提高整体的消费能力':[],
'消息消费逻辑':[
    '1.配置消费者客户端参数及创建相应的消费者实例',
    '2.订阅主题',
    '3.拉取消息并消费',
    '4.提交消费位移',
    '5.关闭消费者实例'
],
'1.配置消费者客户端参数及创建相应的消费者实例':[
    'bootstrap.servers：指定连接Kafka集群所需的broker地址清单',
    'group.id：消费者隶属的消费组名称',
    'key.deserializer 和 value.deserializer:消息中key和value所需反序列化操作的反序列化器',
    'client.id：设定KafkaConsumer对应的客户端id'
],
'2.订阅主题:subscribe（）方法':[
    '消费者自动再均衡的功能，在多个消费者的情况下可以根据分区分配策略来自动分配各个消费者与分区的关系',
    '当消费组内的消费者增加或减少时，分区分配关系会自动调整，以实现消费负载均衡及故障自动转移'
],
'3.拉取消息并消费poll（）方法':[
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
],
'4.提交消费位移offset':[
    '旧消费者客户端中，消费位移是存储在ZooKeeper中的',
    '新消费者客户端中，消费位移存储在Kafka内部的主题__consumer_offsets中',
    '消费者在消费完消息之后需要执行消费位移的提交',
    {'自动提交':[
        'enable.auto.commit=true,auto.commit.interval.ms=5000,5秒提交一次',
        '动作是在poll（）方法里，每次向服务端发起拉取请求前检查是否可以进行位移提交，如可以，提交上一次轮询的位移'
    ]},
    '手动提交:enable.auto.commit=false,分为同步提交和异步提交，对应于 KafkaConsumer 中的 commitSync（）和commitAsync（）方法'
],
'5.控制或关闭消费close（）方法':[],
'指定位移消费':[
    '在 Kafka 中每当消费者查找不到所记录的消费位移时，就会根据消费者客户端参数auto.offset.reset的配置来决定从何处开始进行消费',
    {'':[
        'latest”，表示从分区末尾开始消费消息',
        '“earliest”，那么消费者会从起始处，也就是0开始消费'
    ]}
],
'再均衡':[
    '分区的所属权从一个消费者转移到另一消费者的行为，它为消费组具备高可用性和伸缩性提供保障',
    '',
    '再均衡发生期间，消费组内的消费者是无法读取消息的,重发消费消息',
    {'再均衡监听器 ConsumerRebalanceListener':[
        'onPartitionsRevoked(Collection＜TopicPartition＞partitions):再均衡开始之前和消费者停止读取消息之后被调用,通过这个回调方法来处理消费位移的提交',
        '',
        'onPartitionsAssigned(Collection＜TopicPartition＞partitions):在重新分配分区之后和消费者开始读取消费之前被调用。参数partitions表示再均衡后所分配到的分区。'
    ]}
],
'消费者拦截器':[
    {'ConsumerInterceptor接口':[
        'public ConsumerRecords＜K,V＞onConsume(ConsumerRecords＜K,V＞records):KafkaConsumer会在poll（）方法返回之前调用,对消息进行相应的定制化操作',
        'public void onCommit(Map＜TopicPartition,OffsetAndMetadata＞offsets):KafkaConsumer会在提交完消费位移之后调用拦截器的onCommit（）方法,如记录跟踪所提交的位移信息',
        'public void close()'
    ]}
],
'多线程实现':[
    'KafkaConsumer却是非线程安全的',
    {'实现方式':[
        '第一种：线程封闭，即为每个线程实例化一个KafkaConsumer对象',
        '第二种方式是多个消费线程同时消费同一个分区，这个通过 assign（）、seek（）等方法实现,不推荐。一般而言，分区是消费线程的最小划分单位',
        '第三种实现方式，将处理消息模块改成多线程的实现方式,对于消息的顺序处理就比较困难'
    ]}
],
'重要的消费者参数':[
    'fetch.min.bytes：Consumer在一次拉取请求（调用poll（）方法）中能从Kafka中拉取的最小数据量',
    'fetch.max.wait.ms：Kafka的等待时间，默认值为500（ms）。如果Kafka中没有足够多的消息而满足不了fetch.min.bytes参数的要求，那么最终会等待500ms',
    'max.poll.records：配置Consumer在一次拉取请求中拉取的最大消息数，默认值为500（条）',
    
],
  
}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 