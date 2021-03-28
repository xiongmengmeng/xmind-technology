import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="redis"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("集群选举--哨兵模式")
r2=s2.getRootTopic()
r2.setTitle("集群选举--哨兵模式")


content={
'Sentinel集群将从剩余的从节点中选举一个新的主节点':[
    '1.故障节点主观下线',
    '2.故障节点客观下线',
    '3.Sentinel集群选举Leader',
    '4.Sentinel Leader决定新主节点'
],
'主观下线':[
    'Sentinel集群的每一个Sentinel节点会定时对redis集群的所有节点发心跳包检测节点是否正常',
    '如一个节点在down-after-milliseconds时间内没有回复Sentinel节点的心跳包,该redis节点被该Sentinel节点主观下线'
],
'客观下线':[
    '当节点被一个Sentinel节点记为主观下线时，节点未必一定故障（可能有网络问题）',
    '还需要Sentinel集群的其他Sentinel节点共同判断为主观下线才行',
    '该Sentinel节点会询问其他Sentinel节点，如过半数节点认为该redis节点主观下线，则该redis客观下线',
    '开始故障转移，从从节点中选举一个节点升级为主节点'
],
'Sentinel集群选举Leader':[
    '当一个Sentinel节点确认redis集群的主节点主观下线后，会请求其他Sentinel节点要求将自己选举为Leader',
    '被请求的Sentinel节点如没同意过其他Sentinel节点的选举请求，则同意该请求(选举票数+1)，否则不同意',
    '如一个Sentinel节点获得的过半数的选票，则该Sentinel节点选举为Leader，否则重新进行选举'
],
'Sentinel Leader决定新主节点':[
    '1.过滤故障的节点',
    '2.选择优先级slave-priority最大的从节点作为主节点，如不存在则继续',
    '3.选择复制偏移量（主服务器会把偏移量同步给从服务器）最大的从节点作为主节点，如不存在则继续',
    '4.选择runid（redis每次启动的时候生成随机的runid作为redis的标识）最小的从节点作为主节点'
],
'Sentinel集群至少3节点':[
    '2个节点，一个节点故障，仅剩的一个Sentinel节点无法成为Leader(最低票数：Sentinel节点数/2+1=2)'
]
}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 