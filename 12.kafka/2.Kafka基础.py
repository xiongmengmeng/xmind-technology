import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
xmind_name="kafka"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("Kafka基础")
r2=s2.getRootTopic()
r2.setTitle("Kafka基础")


content={
'Kafka基础':[
    {'1.Topic 主题':[
        '类似于关系型数据库的表',
        '逻辑概念'
    ]},
    {'2.Partition 分区':[
        '在不同的主机上建了不同的目录,同数据库分区',
        '提升性能：多个分区多个线程，多个线程并行处理比单线程好',
        {'注意':[
            '1.分区会有单点故障问题，要为每个分区设置副本数',
            '2.分区的编号是从0开始的'
        ]}
    ]},
    {'3.Producer - 生产者':[
        '往消息系统里面发送数据的',
    ]},
    {'4.Consumer - 消费者':[
        '从kafka里读取数据的',
    ]},
    {'5.Message - 消息':[
        'kafka里面的我们处理的数据',
    ]}
],
'kafka的集群架构':[
    {'Replica - 副本':[
        '有角色之分，它们会选取一个副本作为leader，而其余的作为follower',
        '生产者发送数据:直接发送到leader partition里,然后follower partition去leader里同步数据',
        '消费者消费数据:从leader里消费数据'
    ]},
    {'Consumer Group - 消费者组':[
        'group.id:消费者组的名字',
        '不同组可有唯一的一个消费者去消费同一主题的数据',
        '目的：让多个消费者并行消费信息，它们不会消费到同一个消息',
        '如tms消费组下有消费者a,b,c(对映三台服务器)，其会去消费不同分区上的数据',
        '一个消费者可消费多分区上数据，但多个消费者不同消费一个分区上数据',
        '消费者数据>分区数，会有消费者消费不到数据'
    ]},
    {'Controller':[
        'kafka也是主从式的架构，主节点就叫controller，其余的为从节点，controller是需要和zookeeper进行配合管理整个kafka集群'
    ]},
    {'kafka和zookeeper如何配合工作':[
        '所有broker在启动的时往zookeeper进行注册，选举出一个controller',
        'controller监听zookeeper里的多个目录,如目录信息变化',
        '它会生成集群的元数据信息,并把信息都分发给其他服务器，让其他服务器能感知到集群中其它成员的存在'
    ]}
]
}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 