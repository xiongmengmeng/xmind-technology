import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="zk"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("选举leader")
r2=s2.getRootTopic()
r2.setTitle("选举leader")


content={
'时机':[
    '启动或leader宕机'
],
'流程':[
    '集群选举主线程QuorumPeer',
    {'run()':[
        'while列循环，根据【当前节点状态】做对应业务处理',
        {'LOOKING选举状态':[
            '1.选举同期+1',
            '2.初始化自己选票并发送',
            {'3.接收选票到选票箱':[
                '选举逻辑pk，决定下次要投的选票',
                '投票机器过半数为leader节点',
                '更新自己的节点状态'
            ]}
        ]},
        {'FOLLOWING':[
            '1.与leader节点建立连接进行数据同步',
            '2.如lean挂了，将自己状态改为LOOKING,进入下一轮选举'
        ]},
        {'LEADING':[
            '1.构建leader请求处理链进行客户端请求的处理',
            '2.接受follower连接进行数据同步LearnerHanler.run()',
            '3.与follower定时发送ping请求保持长连接'
        ]}
    ]}
],
'多层队列架构':[
    {'选举应用层':[
        {'发送选票':[
            '队列：sendqueue',
            '线程：WorkerSender',
            {'过程':[
                '如选票接收机器是自己，把选票放入recvQueue',
                '如选票接收机器是别人，把选票放入queueSendMap',
            ]}
        ]},
        {'接收选票':[
            '队列：recvqueue',
            '线程：WorkerReceiver',
        ]}
    ]},
    {'消息传输层':[
        '按发送的机器分了队列，避免给每台机器发送消息时相互影响',
        {'发送选票':[
            '队列：queueSendMap',
            '线程：SenderWorker'
        ]},
        {'接收选票':[
            '队列：recvQueue',
            '线程：RecvWorker'
        ]}
    ]}
],
'三个端囗':[
    {'1.与客户端建立连接':[
        'NIO通信',
        '负责数据的读写'
    ]},
    {'2.服务器内部数据的通信':[
        'BIO通信',
        '数据的同步及心跳监控(ping)'
    ]},
    {'3.服务器内部leader的选举':[
        'NIO通信',
        '主要负责leader节点的选举'
    ]}
]


}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 