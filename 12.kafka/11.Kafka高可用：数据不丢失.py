import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
xmind_name="kafka"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("Kafka高可用：数据不丢失")
r2=s2.getRootTopic()
r2.setTitle("Kafka高可用：数据不丢失")


content={
'Kafka分布式存储架构':[
    {'分区':[
        '一个topic数据集合拆分为多个数据分区',
        '每个Partition可以在不同机器上，储存部分数据'
    ]},
    {'副本冗余':[
        '每个Partition都可以放一个副本放在别的机器上',
        '某台机器宕机，只不过是Partition其中一个副本丢失',
        {'Partition有多副本':[
            '选举其中一个Parititon副本作为Leader，然后其他的Partition副本是Follower',
            '只Leader Partition对外提供读写操作，Follower Partition从Leader Partition同步数据',
            'Leader Partition宕机，选举其他的Follower Partition作为新的Leader Partition对外提供读写服务'
        ]}
    ]},
    {'ISR机制':[
        '每个Partition维护一个ISR列表，列表里有Leader，还有跟Leader保持同步的Follower',
        '如Follower因自身发生一些问题，不能及时从Leader同步数据，Follower被认为“out-of-sync”，会从ISR列表里踢出'
    ]}
],
'Kafka写入数据如何保证不丢失':[
    '1.每个Partition至少得有1个Follower在ISR列表里，保证跟上了Leader的数据同步',
    '2.写入数据时，要求写入Partition Leader成功+至少一个ISR里的Follower写入成功，才算写入成功',
    '3.如不满足上述两条件，认为写入失败，让生产系统不停的尝试重试，直到满足上述两条件，才能认为写入成功',
    '4.按上述思路配置相应参数，才能保证写入Kafka的数据不会丢失'
],
'kafka数据丢失问题':[
    '生产端的缓存问题',
    '消费端的问题',
    'kafka自己内部的底层算法和机制',
    'leader切换问题:上述只解决这个问题'
]
}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 