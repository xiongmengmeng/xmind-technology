import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
xmind_name="kafka"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("消费者Rebalance机制")
r2=s2.getRootTopic()
r2.setTitle("消费者Rebalance机制")


content={
'消费者Rebalance机制':[
    '如消费组里的消费者数量有变化或消费的分区数有变化，kafka会重新分配消费者消费分区的关系'
],
'注意':[
    '1.rebalance只针对subscribe这种不指定分区消费的情况',
    '如通过assign这种消费方式指定了分区，kafka不会进行rebanlance',
    '2.rebalance过程中，消费者无法从kafka消费消息，这对kafka的TPS会有影响',
    '如kafka集群内节点较多，比如数百个，那重平衡会耗时极多，所以应尽量避免在系统高峰期进行'
],
'作用':[
    '为消费组具备高可用性和伸缩性提供保障',
],
'触发消费者rebalance的情况':[
    '1. 消费组里的consumer增加或减少',
    '2. 动态给topic增加了分区',
    '3. 消费组订阅了更多的topic'
],
'Rebalance过程':[
    {'1.选择组协调器':[
        {'组协调器GroupCoordinator':[
            '每个consumer group(有group.id)都会选择一个broker作为自己的coordinator',
            '负责监控这个消费组里的各个消费者的心跳，以及判断是否宕机，然后开启消费者rebalance'
        ]},
        {'组协调器选择方式':[
            '1.通过如下公式选出consumer消费的offset要提交到__consumer_offsets的哪个分区',
            '公式：hash(group.id)%__consumer_offsets主题的分区数',
            '2.这个分区leader对应的broker就是这个consumer group的coordinator'
        ]},
        'consumer group根据group.id计算出哪一个broker作为它们的GroupCoordinator，接着与其GroupCoordinator建立网络连接',
    ]},
    {'2.加入消费组JOIN GROUP':[
        '2.1.消费者会向GroupCoordinator发送JoinGroupRequest请求注册，并处理响应',
        '2.2.GroupCoordinator默认把第一个注册上来的consumer作为leader(消费组协调器)',
        '2.3.GroupCoordinator把整个Topic情况汇报给leader consumer',
        '2.4.leader consumer会根据负载均衡的思路制定消费方案'
    ]},
    {'3.SYNC GROUP':[
        'consumer leader通把SyncGroupRequest分区方案发送给GroupCoordinator',
        'GroupCoordinator在consumer上传心跳时,把分区方案下发给各个consumer',
        'consumer会与指定分区的leader broker进行网络连接以及消息消费'
    ]},
    '4.当有consumer长时间不和coordinator保持联系，coordinator会把2.3-3重新执行一次',
    '5.如断掉的是leader consumer，coordinator会把2.2-3重新执行一次'
],
'Rebalance分区分配策略':[
    'partition.assignment.strategy:设置消费者与订阅主题之间的分区分配策略,默认分配策略range',
    {'range':[
        '按照分区序号排序'
    ]},
    {'round-robin':[
        '轮询分配'
    ]},
    {'sticky':[
        '初始时分配策略与round-robin类似，但是在rebalance的时候，需要保证如下两个原则',
        '1.分区的分配要尽可能均匀',
        '2.分区的分配尽可能与上次分配的保持相同'
    ]}
]


}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 