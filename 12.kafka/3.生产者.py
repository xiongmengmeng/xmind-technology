import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
xmind_name="kafka"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("生产者(上)")
r2=s2.getRootTopic()
r2.setTitle("生产者(上)")


content={
'1.配置生产者客户端参数，创建生产者实例KafkaProducer':[
    'bootstrap.servers:Kafka集群的broker地址清单',
    'key.serializer和value.serializer:序列化方式',
    'client.id：KafkaProducer对应的客户端id',
    '注：为防写错，可使用客户端中的org.apache.kafka.clients.producer.ProducerConfig类',
    {'代码':[
        'Properties props = new Properties();',
        'props.put("bootstrap.servers", "hadoop1:9092,hadoop2:9092,hadoop3:9092")',
        'KafkaProducer<String, String> producer = new KafkaProducer<String, String>(props)'
    ]}
],
'2.构建消息ProducerRecord':[
    'topic:消息要发往的主题',
    'artition:分区号',
    'headers:消息头部,用来设定一些与应用相关的信息',
    'key:消息的键，可用来计算分区号进而让消息发往特定分区,同一个key的消息会划分到同一个分区',
    'value:消息体，一般不为空，如果为空则表示特定的消息—墓碑消息',
    'timestamp:时间戳，有CreateTime（消息创建时间）和LogAppendTime（消息追加到日志文件时间）两种类型',
    {'代码':[
        'ProducerRecord<String, String> record = new ProducerRecord<>("test-topic", "test-value");'
    ]}
],
'3.发送消息':[
    '发后即忘（fire-and-forget）',
    '同步（sync）',
    '异步（async）',
    {'代码':[
        '异步发送的模式',
        'Future future=producer.send(record, new Callback() {...})'
    ]}
],
'4.关闭生产者实例':[
    'producer.close();'
],
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

  
}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 