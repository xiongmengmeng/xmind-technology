import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="rabbitmq"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("rabbitmq")
r2=s2.getRootTopic()
r2.setTitle("rabbitmq")


content={
'简介':[
    'erlang语言开发',
    '基于AMQP协议',
],
'mq':[
    {'优点':[
        '应用解耦：提升容错性和可维护性',
        '异步提速',
        '削峰填谷: 提升系统稳定性'
    ]},
    {'缺点':[
        '系统可用性下降：因为要保证mq的高可用',
        '系统复杂性下降'
    ]},
],
'组件':[
    'publisher',
    {'broker':[
        {'exchanges':[
            '交换机，用来实现消息的路由'
        ]},
        {'queue':[
            '消息队列，消息存放在队列中，等待消费，消费后被移除队列'
        ]},
        {'virtual hosts':[
            '虚拟主机,是一个独立的访问路径，不同用户使用不同路径，',
            '各自有自己的队列，交换机，互相不影响'
        ]}
    ]},
    'consumer'
],
'6种工作模式':[
    {'简单(直连)':[
        '无交换机，一个队列，一个消费者',
    ]},
    {'工作队列(work queue)':[
        '无交换机，一个队列，多个消费者',
        '默认情况下，rabbitmq按顺序下发消息给使用者，每个消费者都会收到相同数量的消息'
    ]},
    {'发布订阅(fanout)':[
        '有交换机，多个队列，多个消费者',
        {'消息发送流程':[
            '每个消费者都有自己的queue队列',
            '每个队列都要绑定到Exchange交换机',
            '生产者发送的消息，只能发送到交换机，交换机来决定要发给哪个队列，生产者无法决定',
            '交换机把消息发送给绑定过的所有队列',
            '队列的消费者都能拿到消息，实现一条消息被多个消费者消费'
        ]}
    ]},
    {'路由':[
        '有交换机，多个队列，多个消费者',
        {'与发布订阅的区别':[
            '交换机，type=direct',
            '消息，带有key',
            '消费者，只消费特定key的消息'
        ]},
        {'详细':[
            '队列与交换机绑定，不能是任意绑定，而是要指定一个routingKey(路由key)',
            '消息的发送方在向Exchange发送消息时，也必须指定消息的RoutingKey',
            'Exchange不再把消息交给每一个绑定的队列 ，而是根据消息的Routing key进行判断',
            '只有队列的RoutingKey与消息的Routing key完全一致，才会接收到消息'
        ]}
    ]},
    {'主题':[
        '有交换机，多个队列，多个消费者',
        {'与发布订阅的区别':[
            '交换机，type=topic',
            '消费者，只消费匹配key的消息,匹配是通过通配符'
        ]}
    ]},
]

}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 