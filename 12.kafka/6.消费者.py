import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
xmind_name="kafka"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("消费者(下)")
r2=s2.getRootTopic()
r2.setTitle("消费者(下)")


content={
'再均衡':[
    {'coordinator':[
        '每个consumer group都会选择一个broker作为自己的coordinator',
        '负责监控这个消费组里的各个消费者的心跳，以及判断是否宕机，然后开启rebalance'
    ]},
    {'过程':[
        '1.首先有一个消费者组(有group.id)，根据group.id计算出哪一个broker作为它们的coodinator',
        '确定coordinator之后，所有consumer发送一个join group请求注册',
        '2.coordinator默认把第一个注册上来的consumer选择成为leader consumer',
        '3.把整个Topic情况汇报给leader consumer',
        '4.leader consumer会根据负载均衡的思路制定消费方案，返回给coordinator',
        '5.coordinator拿到方案之后再下发给所有的consumer',
        '6.consumer都会向coordinator发送心跳',
        '7.当有consumer长时间不和coordinator保持联系，coordinator会把3-5重新执行一次',
        '如断掉的是leader consumer，会重新选举新的leader，然后coordinator再把3-5重新执行一次'
    ]},
    '作用：为消费组具备高可用性和伸缩性提供保障',
    '再均衡发生期间，消费组内的消费者无法读取消息',
    {'再均衡监听器ConsumerRebalanceListener':[
        'onPartitionsRevoked(Collection＜TopicPartition＞partitions):再均衡开始之前和消费者停止读取消息之后被调用,通过这个回调方法来处理消费位移的提交',
        'onPartitionsAssigned(Collection＜TopicPartition＞partitions):在重新分配分区之后和消费者开始读取消费之前被调用,参数partitions:再均衡后所分配到的分区'
    ]}
],
'消费者拦截器':[
    {'ConsumerInterceptor接口':[
        'ConsumerRecords＜K,V＞onConsume(ConsumerRecords＜K,V＞records):KafkaConsumer会在poll()返回之前调用,对消息进行相应的定制化操作',
        'void onCommit(Map＜TopicPartition,OffsetAndMetadata＞offsets):KafkaConsumer会在提交完消费位移之后调用,如记录跟踪所提交的位移信息',
        'void close()'
    ]}
],
'多线程实现':[
    'KafkaConsumer是非线程安全的',
    {'实现方式':[
        '第一种：线程封闭，即为每个线程实例化一个KafkaConsumer对象',
        '第二种：多个消费线程同时消费同一个分区，通过 assign（）、seek（）等方法实现,不推荐。一般而言，分区是消费线程的最小划分单位',
        '第三种：将处理消息模块改成多线程的实现方式,对于消息的顺序处理就比较困难'
    ]}
],
'重要的消费者参数':[
    {'heartbeat.interval.ms':[
        'consumer心跳时间，必得保持心跳才能知道consumer是否故障',
        '如故障，会通过心跳下发rebalance的指令给其他的consumer通知他们进行rebalance的操作'
    ]},
    {'session.timeout.ms':[
        'kafka多长时间感知不到一个consumer就认为他故障了，默认是10秒'
    ]},
    {'max.poll.interval.ms':[
        '如在两次poll操作间，超过此时间，认为这个consume处理能力太弱，踢出消费组，分区分配给别人去消费'
    ]},
    {'fetch.max.bytes':[
        '获取一条消息最大的字节数，一般建议设置大一些'
    ]},
    {'max.poll.records':[
        '一次poll返回消息的最大条数，默认是500条'
    ]},
    {'auto.offset.reset':[
        'earliest:当各分区下有已提交的offset时，从提交的offset开始消费；无提交的offset时，从头开始消费',
        'latest:(一般设置)当各分区下有已提交的offset时，从提交的offset开始消费；无提交的offset时，从当前位置开始消费',
        'none:topic各分区都存在已提交的offset时，从offset后开始消费；只要有一个分区不存在已提交的offset，则抛出异常'
    ]},
    {'enable.auto.commit':[
        '开启自动提交唯一'
    ]},
    {'auto.commit.ineterval.ms':[
        '多久条件一次偏移量'
    ]},
    {'fetch.min.bytes':[
        'Consumer在一次拉取请求（调用poll（）方法）中能从Kafka中拉取的最小数据量'
    ]},
    {'fetch.max.wait.ms':[
        'Kafka的等待时间，默认值为500（ms）。如果Kafka中没有足够多的消息而满足不了fetch.min.bytes参数的要求，那么最终会等待500ms'
    ]} 
],
'实现代码':[
    'https://www.cnblogs.com/liuming1992/p/6432626.html'
]
}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 