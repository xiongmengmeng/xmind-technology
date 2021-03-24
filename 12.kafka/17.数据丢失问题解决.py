import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
xmind_name="kafka"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("数据丢失问题解决")
r2=s2.getRootTopic()
r2.setTitle("数据丢失问题解决")


content={
'原因':[
    {'Producer问题':[
        '异步发送，将多个请求进行合并,缓存在本地buffer中,一起发送，如消息产生过快，线程过多，内存打满，程序崩溃，消息丢失',
        '网络问题导致消息丢失，acks:0,网络问题会丢失，acks:1,分区leader挂掉会丢失部分数据'
    ]},
    'Broker问题：消费存储在页缓存，还未刷盘，断电后丢失',
    'Consumer问题：自动提交，且提交时间间隔短(auto.commit.interval.ms=100)，导致offset先提交，消息还未消费完，应用宕机'
],
'解决':[
    {'Producer':[
        {'优化':[
            '扩大Buffer的容量配置,service产生消息时，使用阻塞的线程池，并且线程数有一定上限',
            '消息先写盘，再由另一个线程发送'
        ]},
        {'彻底解决':[
            '异步发送改为同步发送,不使用缓冲，一条条发',
            'acks=-1&min.insync.replicas=2,确保ISR中一定要有两个副本写入成功才能算消息重发成功',
            'retriex = Integer.MAX_VALUE ： 开启无限重试'
        ]}
    ]},
    {'Broker':[
        {'刷盘条件':[
            '主动调用sync或fsync函数',
            '可用内存低于阀值',
            'dirty data时间达到阀值'
        ]},
        {'优化':[
            '调整刷盘机制的参数，如，减少刷盘间隔，减少刷盘数据量大小'
        ]},
        {'彻底解决':[
            'acks=-1',
            '数据从pageCache被刷盘到disk，因为只有disk中的数据才能被同步到replica',
            '数据同步到replica，并且replica成功将数据写入PageCache',
            '在producer得到ack后，哪怕是所有机器都停电，数据也至少会存在于leader的磁盘内',
            'replication.factor = 3:设置每个partition有3个备份以上'
        ]}
    ]},
    {'Consumer':[
        '设置手动提交，enable.auto.commit:false'
    ]}
],
'Kafka总的措施':[
    '1.每个Partition至少得有1个Follower在ISR列表里，保证跟上了Leader的数据同步',
    '2.写入数据时，要求写入Partition Leader成功+ISR里至少一个Follower写入成功，才算消息发送成功',
    '3.如不满足上述两条件，让生产系统不停的尝试重试，直到满足上述两条件，才认为写入成功，或者回调时告警，自主解决',
    '4.设置手动提交消息，消费完数据后再提交'
]
}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 