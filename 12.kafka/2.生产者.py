import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
xmind_name="kafka"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("生产者")
r2=s2.getRootTopic()
r2.setTitle("生产者")


content={

'1.配置生产者客户端参数，创建相应的生产者实例 KafkaProducer':[
    'bootstrap.servers:指定生产者客户端连接Kafka集群所需的broker地址清单',
    'key.serializer 和 value.serializer:序列化方式',
    'client.id：KafkaProducer对应的客户端id',
    '注：为防止写错，可直接使用客户端中的 org.apache.kafka.clients.producer.ProducerConfig类'
],
'2.构建待发送消息 ProducerRecord':[
    'topic:消息要发往的主题',
    'artition:分区号',
    'headers:消息头部,用来设定一些与应用相关的信息',
    'key:消息的键，可用来计算分区号进而让消息发往特定分区,同一个key的消息会划分到同一个分区',
    'value:消息体，一般不为空，如果为空则表示特定的消息—墓碑消息',
    'timestamp:时间戳，有CreateTime（消息创建时间）和LogAppendTime（消息追加到日志文件时间）两种类型'
],
'3.发送消息：KafkaProducer.send(),返回一个Future类型对象':[
    '发后即忘（fire-and-forget）',
    '同步（sync）',
    '异步（async）'
],
'4.关闭生产者实例':[],
'5.生产者拦截器':[
    {'ProducerInterceptor接口':[
        'onSend（）:在将消息序列化和计算分区之前会调用',
        'onAcknowledgement（）:消息被应答之前或发送失败时调用',
        'close（）:在关闭拦截器时执行一些资源的清理工'
    ]},
    '自定义的拦截器,需在 KafkaProducer 的配置参数interceptor.classes中指定拦截器',
],
'6.序列化':[
    {'Serializer接口':[
        'configure（）:配置当前类',
        'serialize（）:执行序列化操作:将String类型转为byte[]类型',
        'close（）:关闭当前的序列化器'
    ]}
],
'7.分区器':[
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
],
'8.RecordAccumulator ':[
    '缓存消息以便 Sender 线程可以批量发送，减少网络传输的资源消耗',
    '缓存的大小:通过buffer.memory 配置，默认值32MB',
    '生产者发送消息的速度>发送到服务器的速度:生产者空间不足，此时send（）方法调用要么被阻塞，要么抛出异常',
    '内部为每个分区都维护了一个双端队列，队列中的内容就是ProducerBatch，即 Deque＜ProducerBatch＞'
],
'9.Sender 线程':[
    'Sender 从 RecordAccumulator 中获取＜分区，Deque＜ProducerBatch＞＞的缓存消息'
    '转变为：＜Node，List＜ ProducerBatch＞的形式，其中Node表示Kafka集群的broker节点',
    '封装成＜Node，Request＞的形式',
    'Map＜NodeId，Deque＜Request＞＞:缓存了已经发出去但还没有收到响应的请求'
],
'整体架构':[
    '生产者客户端由两个线程协调运行：主线程和Sender线程（发送线程）',
    '主线程中由KafkaProducer创建消息，然后通过可能的拦截器、序列化器和分区器的作用之后缓存到消息累加器',
    'Sender 线程:从RecordAccumulator中获取消息并将其发送到Kafka中',
],
'重要的生产者参数':[
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
]

  
}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 