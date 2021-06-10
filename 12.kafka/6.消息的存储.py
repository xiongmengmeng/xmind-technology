import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
xmind_name="kafka"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("消息的存储")
r2=s2.getRootTopic()
r2.setTitle("消息的存储")


content={
'producer发布消息机制':[
    {'1.写入方式':[
        'push模式将消息发布到broker,每条消息都被append到patition中，属于顺序写磁盘'
    ]},
    {'2.消息路由':[
        '1.指定patition，则直接使用',
        '2.未指定patition但指定key，通过对key的value进行hash选出一个patition',
        '3.patition和key都未指定，使用轮询选出一个patition'
    ]},
    {'3.写入流程':[
        '1.producer先从zookeeper的"/brokers/.../state"节点找到该partition的leader',
        '2.producer将消息发送给该leader',
        '3.leader将消息写入本地log',
        '4.followers从leader pull消息，写入本地log后向leader发送ACK',
        '5.leader收到所有ISR中replica的ACK后，增加HW并向producer发送ACK'
    ]}
],
'日志分段存储':[
    'Kafka一个分区的消息数据对应存储在一个文件夹下，以topic名称+分区号命名',
    '消息在分区内是分段(segment)存储，每个段的消息都存储在不一样的log文件里,方便old segment file快速被删除',
    'kafka规定了一个段位的log文件最大为1G(log.segment.bytes设置)，方便把log文件加载到内存去操作',
    '一个日志段文件满了，会自动开一个新的日志段文件来写入，避免单个文件过大，影响文件的读写性能',
    {'三种日志文件':[
        {'00000000000005367851.index':[
            'offset索引文件，存储offset和指针(指向log文件中offset数据的位置)',
            'kafka每次往分区发4K(可配置)消息就会记录一条当前消息的offset到index文件',
            '定位消息的offset会先在这个文件里快速定位，再去log文件里找具体消息'
        ]},
        {'00000000000005367851.log':[
            '消息存储文件，主要存offset和消息体'
        ]},
        {'00000000000005367851.timeindex':[
            '消息的发送时间索引文件,存储时间戳和指针(指向log文件中offset数据的位置)',
            'kafka每次往分区发4K(可配置)消息就会记录一条当前消息的发送时间戳与对应的offset到timeindex文件',
            '如果按照时间来定位消息的offset，会先在这个文件里查找'
        ]},
        '数字:代表了这个日志段文件里包含的起始Offset'
    ]}
]

}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 