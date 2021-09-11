import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="rabbitmq"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("使用")
r2=s2.getRootTopic()
r2.setTitle("使用")


content={
'代码实现':[
    'ConnectionFactory',
    'Connection',
    {'Channel':[
        {'Channel.queueDeclare("queue1",true,false,false,null)':[
            '参数1: 通道对应的队列',
            '参数2：是否持久化队列',
            '参数3：指定是否独占队列',
            '参数4：指定是否自动删除队列',
            '参数2：对队列的额外配置',
        ]},
        {'exchangeDeclare("log_direct","direct")':[
            '声明交换机',
            '参数1：交换机名称',
            '参数2：交换机类型'
        ]},
        {'basicPublish("log_direct",key,null,"routeKey".getBytes())':[
            '发布消息'
        ]},
        {'queueBind(queue,"log_direct","error")':[
            '绑定队列和交换机'
        ]},
        {'queueDeclare().getQueue()':[
            '创建临时队列'
        ]},
        {'basicQos(1)':[
            '一次只接受一条未确认的消息'
        ]},
        {'basicConsume("queue1",true,new DefalutConsumer(channel){})':[
            'handleDelivery(String consumerTag,...)',
            {'basicAck(envelope.getDeliveryTag(),false)':[
                '手动确认消息'
            ]}
        ]}
    ]}
],
'与springboot结合':[
    {'引入依赖':[
        'spring-boot-starter-amqp',
    ]},
    {'生产者':[
        'RabbitTemplate.convertAndSend()',
    ]},
    {'消费者':[
        '@RabbitListener(queuesToDeclare=@Queue("hello"))',
        '@RabbitHandler'
    ]},
]

}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 