import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="redis"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("主从&哨兵&分片")
r2=s2.getRootTopic()
r2.setTitle("主从&哨兵&分片")


content={
'3.主从复制：多副本':[
    '目的：避免单点故障,读写分离，水平扩容支撑读高并发',
    {'原理':[
        '当启动一个slave node时，它会发送一个PSYNC命令给master node',
        'master node收到命令，在后台保存快照和缓存快照期间的命令,发送给slave node',
        '中断后重新连接，master node仅会复制给slave缺少的数据'
    ]},
    {'优点':[
        '缩短不可用时间：master发生宕机，我们可手动把slave提升为master继续提供服务',
        '提升读性能：让slave分担一部分读请求，提升应用的整体性能'
    ]},
    {'缺陷':[
        '故障恢复无法自动化；写操作无法负载均衡；存储能力受到单机的限制'
    ]},
    'slave node做复制时，不block master的正常工作和自己的查询操作（用旧数据集提供服务）',
    '复制完成时，需删除旧数据集，加载新数据集，此时会暂停对外服务',
    'slave node用来进行横向扩容，做读写分离，扩容的slave node可提高读的吞吐量',
    '建议开启master node的持久化,应对异常情况：主库重启，从库数据被清空',
],
'4.哨兵：故障自动切换':[
    '哨兵:实时监测master健康状态'
    '目的：自动化的故障恢复',
    {'优点':[
        '集群监控：监控 redis master 和 slave 进程是否正常工作',
        '消息通知：如某redis实例故障，发送消息作为报警通知给管理员',
        '故障转移：如master node 挂掉，自动转移到slave node',
        '配置中心：如故障转移发生了，通知client客户端新的master地址'
    ]},
    {'缺陷':[
        '写操作无法负载均衡；存储能力受到单机的限制'
    ]},
    '哨兵用于实现redis集群高可用，本身也是分布式的（至少需3个实例，保证自己的健壮性）',
    '哨兵+redis 主从的部署架构，不保证数据零丢失，只保证redis集群的高可用性'  
],
'5.分片集群：横向扩展':[
    '目的：横向扩展,提升系统性能，支撑更大的写流量',
    '部署多个实例，然后把这些实例按照一定规则组织起来，把它们当成一个整体，对外提供服务',
    {'分片集群根据路由规则所在位置的不同，还可以分为两大类':[
        '客户端分片:客户端分片 Redis Cluster ',
        '服务端分片:代理分片 Twemproxy、Codis'
    ]}
]
  
}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 