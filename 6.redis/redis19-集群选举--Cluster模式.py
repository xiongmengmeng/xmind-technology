import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="redis"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("集群选举--Cluster模式")
r2=s2.getRootTopic()
r2.setTitle("集群选举--Cluster模式")


content={
'故障转移':[
    'Redis Cluster集群自身实现了高可用，通过节点之间的相互监控实现',
    {'故障发现':[
        '通过ping/pong消息实现故障发现，不需要sentinel',
        '故障发现分主观下线和客观下线',
        {'主观下线':[
            '某个节点认为另一个节点不可见，存在一定的偏见'
        ]},
        {'客观下线':[
            '当半数以上持有槽的主节点都标记某节点主观下线',
            '故障列表包含：当前节点收到的每个节点对其他节点的信息',
            '通知集群内所有节点标记故障节点为客观下线',
            '通知故障节点的从节点触发故障转移流程'
        ]}
    ]},
    {'故障恢复':[
        {'资格检查':[
            '每个从节点检查与故障主节点的断线时间(默认150s)',
            '超过cluster-node-timeout * cluster-slave-validity-factor取消资格',
            'cluster-slave-validity-factor默认值是10'
        ]},
        {'准备选举时间':[
            '保证偏移量比较大的节点获得更小的延迟时间，获得更多的票数'
        ]},
        {'选举投票':[
            '从节点达到选举时间后，对主节点发起选举，让主节点给它投票',
            '偏移量更大的获取选举延迟时间更短，获得更多票数机会更大'
        ]},
        {'替换主节点':[
            '当前从节点取消复制变为主节点(slaveof no one)',
            '执行clusterDelSlot撤销故障主节点负责的槽，并执行clusterAddSlot把这些槽分配给自己',
            '向集群广播自己的pong消息，表明已经替换了故障从节点'
        ]}
    ]}
],
'从库':[
    '1.slave发现自己的master变为FAIL',
    '2.slave将记录集群的currentEpoch（选举周期）加1',
    '3.slave广播FAILOVER_AUTH_REQUEST信息给集中的每一个masters,让其进行选举',
    '4.master收到消息后返回FAILOVER_AUTH_ACK信息，对于同一个Epoch，只能响应一次ack',
    '5.slave收集maste返回的ack消息',
    '6.slave判断收到的ack消息个数是否大于半数的master个数，若是，则变成新的master',
    '7.广播Pong消息通知其他集群节点，自己已经成为新的master',
    {'注':[
        '从节点并不是在主节点一进入FAIL状态就马上尝试发起选举，而是有一定延迟',
        '确保FAIL状态已经在集群中传播，防止slave立即尝试选举，其它masters未意识到FAIL状态，拒绝投票',
        '延迟计算公式：DELAY = 500ms + random(0 ~ 500ms) + SLAVE_RANK * 1000ms'
    ]},
    '8.如slave在两倍的DELAY 时间内（至少2秒）未赢得选举，则放弃本次选举，然后在四倍NODE_TIMEOUT时间（至少4秒）后重新发起选举'
],
'redis-cluster不可用情况':[
    '1.集群主库半数宕机（无论是否从库存活）',
    '2.集群某一节点的主从全数宕机'
]


}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 