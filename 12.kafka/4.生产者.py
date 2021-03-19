import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
xmind_name="kafka"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("生产者(下)")
r2=s2.getRootTopic()
r2.setTitle("生产者(下)")


content={

'7.分区器':[
    {'消息在通过send()方法发往broker':[
        '拦截器（Interceptor）',
        '序列化器（Serializer）',
        '分区器（Partitioner）'
    ]},
    'ProducerRecord中指定partition字段，不需要分区器',
    'ProducerRecord中未指定partition字段，无key，轮询，有key,根据key计算partition(先hash，再根据分区数取模)',
    {'Partitioner接口':[
        'partition（）:计算分区号，返回值为int类型',
        'close（）:关闭分区器的时候用来回收一些资源',
        'configure（）:获取配置信息及初始化数据(继承自父类)'
    ]}
],
'8.RecordAccumulator':[
    '缓存消息以便Sender线程可批量发送，减少网络传输的资源消耗',
    '缓存大小:通过buffer.memory 配置，默认值32MB',
    '生产者发送消息的速度>发送到服务器的速度:生产者空间不足，此时send()方法调用要么被阻塞，要么抛出异常',
    '内部为每个分区都维护了一个双端队列，队列中的内容就是ProducerBatch，即 Deque＜ProducerBatch＞'
],
'9.Sender 线程':[
    'Sender从RecordAccumulator中获取＜分区，Deque＜ProducerBatch＞＞的缓存消息',
    '转变为：＜Node，List＜ ProducerBatch＞的形式，其中Node表示Kafka集群的broker节点',
    '封装为：＜Node，Request＞的形式',
    'Map＜NodeId，Deque＜Request＞＞:缓存了已经发出去但还没有收到响应的请求'
],
'整体架构':[
    '生产者客户端由两个线程协调运行：主线程和Sender线程（发送线程）',
    '主线程:由KafkaProducer创建消息，然后通过可能的拦截器、序列化器和分区器的作用之后缓存到消息累加器',
    'Sender线程:从RecordAccumulator中获取消息并将其发送到Kafka中',
],
'重要的生产者参数':[
    {'acks':[
        '指定分区中必须要有多少个副本收到这条消息，之后生产者才会认为这条消息是成功写入的',
        '配置的值是一个字符串类型',
        'acks=0:生产者发送消息后不需等待服务端响应,认为消息发送成功',
        'acks=1:只要分区的leader副本成功写入消息，收到来自服务端的成功响应，认为消息发送成功',
        'acks=-1:等待ISR中的所有副本都成功写入消息后，收到来自服务端的成功响应，认为消息发送成功'
    ]},
    {'retries':[
        '生产者重试的次数，默认0'
    ]},
    {'retry.backoff.ms':[
        '两次重试之间的时间间隔,默认100'
    ]},
    {'batch.size':[
        '批次大小,默认16K,可提高增加系统吞吐量'
    ]},
    {'linger.ms':[
        '发送时间限制,Batch没满也发送'
    ]},
    {'buffer.memory':[
        '缓冲区大小,默认32M',
        'Sender线程处理缓慢，生产数据的速度快时，中间的缓冲区如容量不够，生产者无法再继续生产数据'
    ]},
    {'max.request.size':[
        '限制生产者客户端能发送的消息的最大值，默认1MB,可根据业务调大些',
    ]},
    {'request.timeout.ms':[
        'Producer等待请求响应的最长时间，默认30s',
        '请求超时之后可以选择进行重试,防止因网络抖动导致的数据丢失，限制等待时间'
    ]}
]
}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 