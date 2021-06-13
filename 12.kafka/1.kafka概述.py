import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
xmind_name="kafka"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("kafka概述")
r2=s2.getRootTopic()
r2.setTitle("kafka概述")


content={
'介绍':[
    '一个多分区、多副本且基于ZooKeeper协调的分布式消息系统',
],
'三大作用':[
    {'消息系统':[
        {'系统解耦':[
            '1.物流的包裹流转数据，各平台都需要，如使用RPC调用成本高,只需发下消息，各方订阅即可',
            '2.提升系统稳定性，如果调用服务报错，会影响平台功能'
        ]},
        {'异步调用':[
            '客户下单时，生成订单信息即可，对于订单的后续拆分，传递都可以通过消息来操作',
        ]},
        {'流量削峰':[
            '用有限的机器资源承载高并发请求',
            '如业务场景允许异步削峰，高峰期积压一些请求在MQ里，高峰期过了，系统在一定时间内消费完毕'
        ]},
    ]},
    {'存储系统':[
        '日志收集',
        '用户活动跟踪',
        '运营指标'
    ]},
    '流式处理平台'
],
'缺点':[
    {'系统可用性降低':[
        '多一台应用，有挂掉风险'
    ]},
    {'系统稳定性降低':[
        '网络故障等问题导致消息丢失',
        '重复发送消息，导致脏数据',
        '宕机了几个小时，导致无法消费消息'
    ]},
    {'分布式一致性':[
        '系统消费消息失败，导致系统整体数据不一致'
    ]},
],
'安装与配置':[
    {'JDK':[
        'kafka由Scala语言开发的，但也运行在JVM上'
    ]},
    {'ZooKeeper':[
        '实施对元数据信息的管理，包括集群、broker、主题、分区等内容'
    ]},
    {'Kafka':[
        {'服务端参数配置':[
            {'broker.id':[
                'Kafka集群中broker的唯一标识，默认值为-1'
            ]},
            {'listeners':[
                'kafka部署的机器ip和提供服务的端口号'
            ]},
            {'log.dir和log.dirs':[
                'kafka的消息存储文件'
            ]},
            {'zookeeper.connect':[
                'broker要连接的ZooKeeper集群的服务地址（含端口号）'
            ]},
            {'message.max.bytes':[
                'broker所能接收消息的最大值'
            ]},
            {'log.retention.hours':[
                '每个日志文件删除之前保存的时间,默168'
            ]},
            {'num.partitions':[
                '创建topic的默认分区数,默1'
            ]},
            {'default.replication.factor':[
                'default.replication.factor,默1'
            ]},
            {'min.insync.replicas':[
                '当producer设置acks为-1时，min.insync.replicas指定replicas的最小数目'
            ]}
        ]}
    ]}
],


  
}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 