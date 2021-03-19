import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
xmind_name="kafka"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("引入消息中间件")
r2=s2.getRootTopic()
r2.setTitle("引入消息中间件")


content={
'系统解耦':[
    '1.物流的包裹流转数据，各平台都需要，但不可能包裹流转时对每个平台都做一次RPC调用,成本高',
    '只需发下消息，各方订阅即可',
    '2.提升系统稳定性，如果调用服务报错，会影响平台功能'
],
'异步调用':[
    '客户下单时，生成订单信息即可，对于订单的后续拆分，传递都可以通过消息来操作',

],
'流量削峰':[
    '用有限的机器资源承载高并发请求，',
    '如业务场景允许异步削峰，高峰期积压一些请求在MQ里，高峰期过了，系统在一定时间内消费完毕'
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
]
}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 