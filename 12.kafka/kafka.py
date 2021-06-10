import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
xmind_name="kafka"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("kafka")
r2=s2.getRootTopic()
r2.setTitle("kafka")


content={
'消息中间件意义':[
    '系统解耦',
    '异步调用',
    '流量削峰'
],
'ZooKeeper':[
    {'broker':[
        '监测broker状态',
        '选举controller',
        '记录ISR',
        'topic注册和记录配置' 
    ]},
    {'consumer':[
        'consumer注册',
        '分区注册'
    ]}
],
'Producer':[
    'KafkaProducer',
    'ProducerRecord',
    # 'ProducerInterceptor',
    # '序列化',
    # '分区器',
    # 'RecordAccumulator',
    # 'Sender',
    # '参数'
],
'Broker':[
    '主从架构',
    'controller',
    {'Reactor模式':[
        'Acceptor(mainReactor)',
        'Processor',
        'KafkaRequestHandlerPool'
    ]},
    {'高并发':[
        '页缓存技术 + 磁盘顺序写',
        '零拷贝技术'
    ]},
],
'Consumer':[
    'Consumer Group',
    'KafkaConsumer',
    'ConsumerRecord',
    'offset',
    '选择一个Broker做为coordinator'
],
'Topic':[
    'Message',
    {'Partition':[
        '多副本，leader--follower',
        'LEO',
        'ISR',
        'HW'
    ]}
],
'监控':[
    'Monitor',
    'Manager',
    'Eagle'
],
'遇到问题':[
    '消息丢失',
    '消息重复消费',
],
# '源码':[]
}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 