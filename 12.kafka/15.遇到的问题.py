import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
xmind_name="kafka"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("遇到问题")
r2=s2.getRootTopic()
r2.setTitle("遇到问题")


content={
'kafka新topic第一次消息无法消费':[
    '版本0.8，offSet存在zk上',
    {'原因':[
        '只有topic生成后，consumer才会去zookeeper进行注册，并且offset直接取的当前最大的logsize',
        'consumer就从当前broker队列的最大offset+1（logsize）开始消费，即之前发的消息不会被消费'
    ]},
    {'解决':[
        '上线前去http://kafka-manager.qipeipu.net/，创建topic'
    ]}
],
'消息丢失':[
    '略'
],
'消息重复消费':[
    {'原因':[
        '消费方先消费消息再提交offset，结果挂机导致offset没提交，重启后重新拉取同匹数据消费'
    ]},
    {'解决':[
        '消费消费时，业务逻辑实现幂等（redis,数据库唯一键等）'
    ]}
],
'消息顺序消费':[
    '具体情况具体分析',
    '分区内都是顺序的',
    {'生产者':[
        '引入第三方的序号id'
    ]},
    {'消费者':[
        '如是多线程，只能用队列+锁来控制'
    ]}
],
'无限循环消费同一批数据':[
    {'原因':[
        'consumer在session.timeout.ms时间内没有消费完消息,consumer coordinator会由于没有接受到心跳而挂掉',
        '自动提交offset失败，然后重新分配partition给客户端,重新分配了partition的客户端又重新消费之前的一批数据',
        '接着consumer重新消费，又出现了消费超时，无限循环下去',
    ]},
    {'解决':[
        '修改max.poll.records，调小单次拉取数量',
        '改为多线程消费',
        '修改业务代码，使执行时间变短'
    ]}
],
'学习':[
    'https://mp.weixin.qq.com/s?__biz=MzUxODkzNTQ3Nw==&mid=2247486202&idx=1&sn=23f249d3796eb53aff9cf41de6a41761',
    'https://blog.csdn.net/wl044090432/article/details/51124779'
]
}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 