import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="zk"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("ZAB协议")
r2=s2.getRootTopic()
r2.setTitle("ZAB协议")


content={
'ZAB协议':[
    'Zookeeper Atomic Broadcast（Zookeeper 原子广播协议）',
    '是为分布式协调服务 Zookeeper 专门设计的一种支持【崩溃恢复】和【原子广播】协议'
],
'主备模式':[
    '来保持集群中各个副本之间数据一致性',
    '所有客户端写入数据都是写入到【主进程leader】中',
    '然后由Leader复制到备份进程Follower中',
    '复制过程类似2PC,ZAB 只需Follower有一半以上返回Ack信息就可执行提交,减小了同步阻塞,也提高了可用性'
],
'消息广播':[
    '使用一个原子广播协议，类似一个二阶段提交过程',
    {'广播流程':[
        '1.leader发送proposal消息(有zxid)给follower',
        '2.leader写本地数据文件',
        '3.leader给自己发ack',
        '4.follower返回ack给leader',
        '4.leader收到半数以上ack发送commit给follower',
        '5.leader发送inform让observer存储消息',
        '6.leader写自己的内存数据',
        '7.follower收到commit后，写自己的内存数据',
        '8.leader回发节点数据变动通知客户端，触发客户端命令操作结果',
        '9.返回客户端命令操作结果'
    ]},
    {'细节':[
        '1.Leader收到客户端请求后，将请求封装成一个事务，并给这个事务分配一个全局递增的ID（ZXID）',
        'ZAB协议需保证事务的顺序，因此必须将每一个事务按照ZXID进行先后排序然后处理，主要通过消息队列实现',
        '2.为保证所有进程能够有序的顺序执行，Leader服务器接受写请求',
        '即使Follower服务器接受到客户端的写请求,也会转发到Leader服务器进行处理，Follower只处理读请求',
        '3.ZAB协议规定了如果一个事务在一台机器上被处理(commit)成功，那么应该在所有的机器上都被处理成功，哪怕机器出现故障崩溃',
    ]}
],
'崩溃恢复':[
    {'ZAB定义了2个原则':[
        '1.ZAB协议确保丢弃那些只在Leader提出/复制，但没有提交的事务',
        '2.ZAB 协议确保那些已经在Leader提交的事务最终会被所有服务器提交'
    ]},
    {'选举算法':[
        '能够确保提交已经被Leader提交的事务，同时丢弃已经被跳过的事务'
    ]},
    {'数据同步':[
        {'事务编号ZXID':[
            '一个64位的数字',
            {'高32位':[
                'epoch值(leader选举周期)，当一轮新的选举结束后，会对这个值加一，并且事务id又从0开始自增',
            ]},
            {'低32位':[
                '事务id',
                '针对客户端的每一个事务请求，Leader都会产生一个新的事务Proposal并对该计数器进行+1操作'
            ]},
            '高32位代表了每代Leader的唯一性，低32代表了每代Leader中事务的唯一性',
        ]},
        {'基于事务编号ZXID':[
            '当Follower连接上Leader后，Leader服务器会根据自己服务器上最后被提交的ZXID和Follower上的ZXID进行比对',
            '比对结果Follower要么回滚，要么和Leader同步'
        ]}
    ]}
]

}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 