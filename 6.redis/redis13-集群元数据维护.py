import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="redis"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("集群元数据维护")
r2=s2.getRootTopic()
r2.setTitle("集群元数据维护")


content={
'集中式':[
    '将集群元数据（节点信息、故障等等）存储在某个节点上',
    '代表：zookeeper（分布式协调的中间件）对所有元数据进行存储维护',
    {'好处':[
        '元数据的读取和更新，时效性好',
        '一旦元数据出现变更，立即更新到集中式的存储中，其它节点读取时可感知到',
    ]},
    {'坏处':[
        '所有元数据的更新压力全部集中在一个地方，可能导致元数据的存储有压力',
    ]}
],
'Gossip 协议':[
    '所有节点持有一份元数据，不同的节点如出现元数据的变更，不断将元数据发给其它节点，让其它节点也进行元数据变更',
    '代表：redis cluster节点间采用gossip协议进行通信',
    {'好处':[
        '元数据更新比较分散，不是集中在一个地方，更新请求会陆陆续续打到所有节点上去更新，降低了压力',
    ]},
    {'坏处':[
        '元数据更新有延时，导致集群中的一些操作有滞后',
    ]},
    '交换的信息：故障，节点的增加和删除，hash slot等',
    {'gossip协议命令':[
        'ping：节点频繁给其他节点发送ping，内容：自己的状态还有自己维护的集群元数据，互相通过ping交换元数据',
        'pong: 返回ping和meet，内容：自己的状态和其他信息，也可以用于信息广播和更新',
        'fail: 节点判断另一个节点fail之后，发送fail给其他节点，通知其他节点，指定的节点宕机了',
        'meet：节点发送meet给新加入的节点，让新节点加入集群中，然后新节点就会开始与其它节点进行通信'
    ]},
],
'学习':[
    '元数据维护和寻址：https://blog.csdn.net/gv7lzb0y87u7c/article/details/90816057',
    'redis cluster：https://blog.csdn.net/weixin_39770626/article/details/111173010',
    '一致性hash:https://www.cnblogs.com/lpfuture/p/5796398.html',
    '缓存异常：http://www.360doc.com/content/18/0225/14/16915_732337300.shtml',
    '更新缓存的几种方式：https://studygolang.com/articles/31182'
]
}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 