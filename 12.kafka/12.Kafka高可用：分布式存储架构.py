import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
xmind_name="kafka"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("Kafka高可用：分布式存储架构")
r2=s2.getRootTopic()
r2.setTitle("Kafka高可用：分布式存储架构")


content={
'分区':[
    '一个topic数据集合拆分为多个数据分区',
    '每个Partition可以在不同机器上，储存部分数据'
],
'副本冗余':[
    '每个Partition都可以放一个副本放在别的机器上',
    '某台机器宕机，只不过是Partition其中一个副本丢失',
    {'Partition有多副本':[
        '选举其中一个Parititon副本作为Leader，然后其他的Partition副本是Follower',
        '只Leader Partition对外提供读写操作，Follower Partition从Leader Partition同步数据',
        'Leader Partition宕机，选举其他的Follower Partition作为新的Leader Partition对外提供读写服务'
    ]}
],
'ISR机制':[
    'In-Sync Replicas:保持同步的副本',
    '每个Partition维护一个ISR列表，列表里有Leader，还有跟Leader保持同步的Follower',
    '如Follower因自身发生一些问题，不能及时从Leader同步数据，Follower被认为“out-of-sync”，会从ISR列表里踢出',
    {'多副本间数据如何同步':[
        'Leader副本接收到数据后',
        'Follower副本会不停的给他发送请求尝试去拉取最新的数据，拉取到自己本地后，写入磁盘',
    ]}
],
'ack参数':[
    '在KafkaProducer，即生产者客户端里设置',
    '0:KafkaProducer在客户端，只要把消息发送出去，不管数据是否落盘，直接认为消息发送成功',
    '1:(默认)Partition Leader收到消息且写入磁盘，不管其他Follower有无同步消息，认为消息发送成功',
    {'all(-1)':[
        'Partition Leader收到消息后，还要求ISR列表里跟Leader保持同步的Follower要把消息同步过去，才认为消息发送成功',
        {'配合min.insync.replicas=2使用':[
            '确保ISR中一定要有两个副本写入成功才能算消息重发成功',
            '不然ISR只有leader一个副本，acks就退化回1'
        ]}
    ]}
]

}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 