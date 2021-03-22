import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
xmind_name="kafka"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("kafka中的zk")
r2=s2.getRootTopic()
r2.setTitle("kafka中的zk")


content={
'Broker注册':[
    '在zookeeper中保存为一个临时节点',
    '节点的路径:/brokers/ids/[brokerid]',
    '每个节点会保存对应broker的IP以及端口等信息'
],
'Topic注册':[
    '节点的路径:/brokers/topics',
    '每个topic都会在topics下建立独立的子节点',
    '每个topic节点下都会包含分区以及broker的对应信息'
],
'partition状态信息':[
    '节点的路径:/brokers/topics/[topic]/partitions/[0…N]',
    '其中[0…N]表示partition索引号',
],
'Controller注册信息':[
    '存储center controller中央控制器所在kafka broker的信息'
],
'生产者负载均衡':[
    '当Broker启动时，会注册该Broker的信息，以及可订阅的topic信息',
    '生产者通过注册在Broker以及Topic上的watcher动态感知Broker以及Topic的分区情况，从而将Topic的分区动态的分配到broker上'
],
'消费者':[
    '节点的路径:/consumers/[groupId]/ids/[consumerIdString]',
    'consumerIdString:表示此consumer目前所消费的topic + partitions列表'
],
'消费者与分区的对应关系':[
    '节点的路径:/consumers/[group_id]/owners/[topic]/[broker_id-partition_id]',
    '节点的内容是消费者的Consumer ID',
    '消费者与分区的关系是一对多的关系'
],
'消费者负载均衡':[
    '消费者服务启动时，会创建一个属于消费者节点的临时节点，节点路径:/consumers/[group_id]/ids/[consumer_id],节点内容是消费者订阅的Topic信息',
    '每个消费者会对/consumers/[group_id]/ids节点注册Watcher监听器，一旦消费者的数量增加或减少就会触发消费者的负载均衡',
    '消费者还会对/brokers/ids/[brokerid]节点进行监听，如发现服务器的Broker服务器列表发生变化，也会进行消费者的负载均衡'
]
}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 