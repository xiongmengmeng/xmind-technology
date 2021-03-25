import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="redis"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("redis集群选举")
r2=s2.getRootTopic()
r2.setTitle("redis集群选举")


content={
'集群模式下':[
    {'gossip协议':[
        '各节点之间都会保持通讯，当某一个节点挂掉或者新增的时候，与它相邻的节点就会感知到，这时候此节点就是失去链接或者创建链接',
        {'命令':[
            'ping：每个节点都会频繁给其他节点发送ping，其中包含自己的状态还有自己维护的集群元数据，互相通过ping交换元数据',
            'pong: 返回ping和meet，包含自己的状态和其他信息，也可以用于信息广播和更新',
            'fail: 某个节点判断另一个节点fail之后，就发送fail给其他节点，通知其他节点，指定的节点宕机了',
            'meet：某个节点发送meet给新加入的节点，让新节点加入集群中，然后新节点就会开始与其他节点进行通信，不需要发送形成网络的所需的所有CLUSTER MEET命令 '
        ]}
    ]},
    {'选择过程':[
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
    ]}
],
'哨兵模式下':[
    {'Sentinel集群将从剩余的从节点中选举一个新的主节点':[
        '1.故障节点主观下线',
        '2.故障节点客观下线',
        '3.Sentinel集群选举Leader',
        '4.Sentinel Leader决定新主节点'
    ]},
    {'主观下线':[
        'Sentinel集群的每一个Sentinel节点会定时对redis集群的所有节点发心跳包检测节点是否正常',
        '如一个节点在down-after-milliseconds时间内没有回复Sentinel节点的心跳包,该redis节点被该Sentinel节点主观下线'
    ]},
    {'客观下线':[
        '当节点被一个Sentinel节点记为主观下线时，节点未必一定故障（可能有网络问题）',
        '还需要Sentinel集群的其他Sentinel节点共同判断为主观下线才行',
        '该Sentinel节点会询问其他Sentinel节点，如过半数节点认为该redis节点主观下线，则该redis客观下线',
        '始故障转移，从从节点中选举一个节点升级为主节点'
    ]},
    {'Sentinel集群选举Leader':[
        '当一个Sentinel节点确认redis集群的主节点主观下线后，会请求其他Sentinel节点要求将自己选举为Leader',
        '被请求的Sentinel节点如没同意过其他Sentinel节点的选举请求，则同意该请求(选举票数+1)，否则不同意',
        '如一个Sentinel节点获得的过半数的选票，则该Sentinel节点选举为Leader，否则重新进行选举'
    ]},
    {'Sentinel Leader决定新主节点':[
        '1.过滤故障的节点',
        '2.选择优先级slave-priority最大的从节点作为主节点，如不存在则继续',
        '3.选择复制偏移量（主服务器会把偏移量同步给从服务器）最大的从节点作为主节点，如不存在则继续',
        '4.选择runid（redis每次启动的时候生成随机的runid作为redis的标识）最小的从节点作为主节点'
    ]},
    {'Sentinel集群至少3节点':[
        '2个节点，一个节点故障，仅剩的一个Sentinel节点无法成为Leader(最低票数：Sentinel节点数/2+1=2)'
    ]}
]

}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 