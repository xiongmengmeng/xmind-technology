import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
xmind_name="kafka"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("Spring Boot整合Kafka")
r2=s2.getRootTopic()
r2.setTitle("Spring Boot整合Kafka")


content={
'引入spring boot kafka依赖':[
    '<dependency>',
    '   <groupId>org.springframework.kafka</groupId>',
    '   <artifactId>spring‐kafka</artifactId>',
    '</dependency>'
],
'application.yml配置':[
    '...',
    {'listener':[
        {'RECORD':[
            '每一条记录被消费者监听器（ListenerConsumer）处理之后提交'
        ]},
        {'BATCH':[
            '每一批poll()的数据被消费者监听器（ListenerConsumer）处理之后提交'
        ]},
        {'TIME':[
            '当每一批poll()的数据被消费者监听器（ListenerConsumer）处理之后，距离上次提交时间大于TIME时提交'
        ]},
        {'COUNT':[
            '当每一批poll()的数据被消费者监听器（ListenerConsumer）处理之后，被处理record数量大于等于COUNT时提交'
        ]},
        {'COUNT_TIME':[
            'TIME | COUNT有一个条件满足时提交'
        ]},
        {'MANUAL':[
            '当每一批poll()的数据被消费者监听器（ListenerConsumer）处理之后, 手动调用Acknowledgment.acknowledge()后提交'
        ]},
        {'MANUAL_IMMEDIATE':[
            '手动调用Acknowledgment.acknowledge()后立即提交，一般使用这种'
        ]},
    ]}
],
'发送者代码':[
    '通过KafkaTemplate<String, String> kafkaTemplate'
],
'消费者代码':[
    '@KafkaListener(topics = "topicName",groupId = "一般项目名称")',
    'public void listenGroup(ConsumerRecord<String, String> record, Acknowledgment ack){',
    '   //处理消息',
    '}'
]



}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 