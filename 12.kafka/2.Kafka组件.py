import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
xmind_name="kafka"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("Kafka组件")
r2=s2.getRootTopic()
r2.setTitle("Kafka组件")


content={
'生产者(Producer)':[
    '向Broker发送消息的客户端'
],
'消费者(Consumer)':[
    '从Broker读取消息的客户端'
],
'Broker':[
    '消息中间件处理节点',
    '一个Kafka节点就是一个broker，一个或者多个Broker可以组成一个Kafka集群',
    {'Controller':[
        'kafka也是主从式的架构，主节点就叫controller，其余的为从节点',
        {'kafka和zookeeper如何配合工作':[
            '所有broker在启动的时往zookeeper进行注册，选举出一个controller',
            'controller监听zookeeper里的多个目录,如目录信息变化',
            '它会生成集群的元数据信息,并把信息分发给其他服务器，让其他服务器能感知到集群中其它成员的存在'
        ]}
    ]},
],
'主题(Topic)':[
    '逻辑概念',
    '类似于关系型数据库的表',
],
'消费者组(ConsumerGroup)':[
    'group.id:消费者组的名字',
    '每个Consumer属于一个特定的Consumer Group，一条消息可以被多个不同的Consumer Group消费',
    '但是一个Consumer Group中只能有一个Consumer能够消费该消息',
    {'例':[
        '如tms消费组下有消费者a,b,c(对映三台服务器)，其会去消费不同分区上的数据',
        '一个消费者可消费多分区上数据，但多个消费者不同消费一个分区上数据',
        '消费者数据>分区数，会有消费者消费不到数据'
    ]}
],
'分区（Partition）':[
    '物理上的概念',
    '在不同的主机上建了不同的目录,同数据库分区',
    '提升性能：多个分区多个线程，多个线程并行处理比单线程好',
    {'注意':[
        '1.分区会有单点故障问题，要为每个分区设置副本数',
        '2.分区的编号是从0开始的'
    ]},
    {'副本(Replica)':[
        '有角色之分，它们会选取一个副本作为leader，其余的作为follower',
        '生产者发送数据:直接发送到leader partition里,然后follower partition去leader里同步数据',
        '消费者消费数据:从leader里消费数据'
    ]},
],
'消息':[
    {'单播消费':[
        '一条消息只能被某一个消费者消费的模式，类似queue模式',
        '只需让所有消费者在同一个消费组里即可'
    ]},
    {'多播消费':[
        '一条消息能被多个消费者消费的模式，类似publish-subscribe模式费',
        '实现多播只要保证这些消费者属于不同的消费组即可'
    ]}
],
'组件关系':[
    'producer通过网络发送消息到Kafka集群，然后consumer来进行消费',
    '服务端(brokers)和客户端(producer、consumer)之间通信通过TCP协议来完成'
],
# '源码学习':[
#     'https://juejin.cn/post/6844904036190142471#heading-48',
#     'https://juejin.cn/post/6844904039499448328'
# ]
}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 