import xmind
from xmind.core.markerref import MarkerId
w = xmind.load("c:\\Users\\btr\\Desktop\\redis.xmind") 
s2=w.createSheet()
s2.setTitle("redis_summary")
r2=s2.getRootTopic()
r2.setTitle("redis_summary")


content={
'1.Redis':[
    '单线程 : 避免了不必要的上下文切换和竞争条件,队列技术将并发访问变为串行访问',
    '数据类型丰富：键的类型只能为字符串，值支持5种数据类型：字符串、列表、集合、散列表、有序集合',
    '基于内存:CPU不是Redis的瓶颈，瓶颈可能是内存大小或网络带宽，类似于HashMap，查找和操作的时间复杂度都是O(1)',
    {'应用场景':[
        '计数器',
        '会话缓存',
        '分布式锁:Redis 自带的 SETNX 命令'
    ]}
],
'2.持久化':[
    {'RDB':[
        '默认持久化方式',
        '按照一定的时间将内存的数据以快照的形式保存到硬盘中',
        '对应数据文件dump.rdb',
        '核心函数rdbSave(生成RDB文件)和rdbLoad（从文件加载内存）'
    ]},
    {'AOF':[
        'Append Only File持久化',
        '将Redis执行的每次写命令记录到单独的日志文件',
        '重启Redis会从持久化的日志中文件恢复数据'
    ]},
    {'持久化策略选择':[
        'Redis中的数据完全丢弃也没有关系，可以不进行任何持久化',
        '单机环境，如可接受十几分钟或更多数据丢失，选择RDB；如只能接受秒级数据丢失，选择AOF',
        '多数情况，会配置主从环境，slave既可实现数据的热备，也可分担Redis读请求，以及在master宕掉后继续提供服务'
    ]},
    {'常见性能问题':[
        'Master最好不做任何持久化工作，如RDB内存快照和AOF日志文件',
        '如数据重要，某个Slave开启AOF备份数据，策略设置为每秒同步一次',
        '为了主从复制的速度和连接的稳定性，Master和Slave最好在同一个局域网'
    ]}
],
'3.过期':[
    {'过期策略':[
        '定时过期：每个设置过期时间的key需创建一个定时器，过期立即清除，占用cpu',
        '惰性过期：当访问一个key时，才判断key是否过期，过期则清除,占用内存',
        '定期过期：隔段时间，扫描一定数量的expires字典中一定数量的key，清除其中已过期key'
    ]},
    'Redis中同时使用了惰性过期和定期过期两种过期策略',
    {'Redis内存淘汰策略':[
        '内存不足时，怎么处理需要新写入且需要申请额外空间的数据',
        {'全局的键空间选择性移除':[
            'noeviction：内存不足时，新写入操作会报错',
            'allkeys-lru：内存不足时，在键空间中，移除最近最少使用的key(最常用)',
            'allkeys-random：内存不足时，在键空间中，随机移除某个key'
        ]},
        {'设置过期时间的键空间选择性移除':[
            'volatile-lru：内存不足时，在设置了过期时间的键空间中，移除最近最少使用的key',
            'volatile-random：内存不足时，在设置了过期时间的键空间中，随机移除某个key',
            'volatile-ttl：内存不足时，在设置了过期时间的键空间中，有更早过期时间的key优先移除'
        ]}
    ]}
],
'4.集群——哨兵模式':[
    '主要功能：自动化的故障恢复。缺陷：写操作无法负载均衡；存储能力受到单机的限制。',
    {'功能':[
        '集群监控：监控 redis master 和 slave 进程是否正常工作',
        '消息通知：如某redis实例故障，发送消息作为报警通知给管理员',
        '故障转移：如master node 挂掉，自动转移到slave node',
        '配置中心：如故障转移发生了，通知client客户端新的master地址'
    ]},
    '哨兵用于实现redis集群高可用，本身也是分布式的（至少需3个实例，保证自己的健壮性）',
    '哨兵 + redis 主从的部署架构，不保证数据零丢失，只保证 redis 集群的高可用性'  
],
'5.主从架构':[
    'redis replication->主从架构->读写分离->,数据的多机备份,水平扩容支撑读高并发',
    '缺陷：故障恢复无法自动化；写操作无法负载均衡；存储能力受到单机的限制',
    'slave node做复制时，不block master的正常工作和自己的查询操作（用旧数据集提供服务）',
    '复制完成时，需删除旧数据集，加载新数据集，此时会暂停对外服务',
    'slave node用来进行横向扩容，做读写分离，扩容的slave node可提高读的吞吐量',
    '建议开启master node的持久化,应对异常情况：主库重启，从库数据被清空',
    {'主从复制原理':[
        '当启动一个slave node时，它会发送一个PSYNC命令给master node',
        'master node收到命令，在后台保存快照和缓存快照期间的命令,发送给slave node',
        '中断后重新连接，master node仅会复制给slave缺少的数据'
    ]}
],
'6.分区':[
    '管理更大内存，使用所有机器的内存',
    {'实现方案':[
        '客户端分区',
        '代理分区',
        'Redis Cluster,查询路由'
    ]}
],
'7.分布式问题':[
    {'SETNX分布式锁':[
        '使用SETNX(SET if Not eXists)命令获取锁，若返回0（key已存在，锁已存在）则获取失败，反之获取成功',
        '为key设置“合理”的过期时间，防止获取锁后程序出现异常，导致其他线程调用SETNX命令总是返回0而进入死锁状态',
        '释放锁：使用DEL命令将锁数据删除'
    ]},
    {'zookeeper锁':[
        '基于zookeeper临时有序节点实现',
        '客户端对某方法加锁，在zookeeper上的与该方法对应的指定节点目录下，生成一个唯一的瞬时有序节点',
        '判断是否获取锁:判断有序节点中序号最小的一个',
        '释放锁：将瞬时节点删除'
    ]}
],
'8.缓存异常':[
    {'缓存雪崩':[
        '缓存同一时间大面积失效，请求都落到数据库上',
        '解决：缓存数据的过期时间设置随机'
    ]},
    {'缓存穿透':[
        '指缓存和数据库中都没有的数据，请求落到数据库上',
        '一些恶意的请求会故意查询不存在的key,请求量很大，就会对后端系统造成很大的压力',
        '解决：对key加锁并排队，用户鉴权，限流',
        '对查询结果为空的情况也进行缓存，缓存时间设置短一点'
    ]},
    {'缓存击穿':[
        '前提：缓存中没有但数据库中有数据（缓存到期）',
        '并发用户多，同时读缓存没读到数据，同时去数据库查',
        '设置热点数据永远不过期'
    ]},
    {'缓存预热':[
        '系统上线后，将相关的缓存数据直接加载到缓存系统',
        '写个脚本，上线后执行下'
    ]},
    {'缓存降级':[
        '当访问量剧增等问题影响到核心流程的性能时，系统根据一些数据进行自动降级',
        '目的：防止Redis服务故障，导致数据库雪崩,保证核心服务可用'
    ]}
],
'9.Jedis与Redisson对比':[
    'Jedis是Redis的Java实现的客户端，其API提供了较全面的Redis命令支持',
    'Redisson实现了分布式和可扩展的Java数据结构，功能较简单，不支持字符串操作,排序、事务、管道、分区等'
],
'其它':[
    '一致性哈希算法，哈希槽',
    'https://www.cnblogs.com/lpfuture/p/5796398.html',
    'http://www.jasontec.cn/articles/2020/04/11/1586586130767.html'
]
  
}

for key in content:
    t1 = r2.addSubTopic()
    t1.setTopicHyperlink(s2.getID()) 
    list=key.split(":")
    t1.setTitle(list[0])
    if len(list)>1:
        t1.setPlainNotes(list[1]) 
    # print(content[key])
    for i in content[key]:
        # print(type(i))
        if(type(i).__name__=='dict'):
            for t in i:
                t2 = t1.addSubTopic()
                t2.setTopicHyperlink(t1.getID()) 
                t2.setTitle(t)
                for j in i[t]:
                    #print(j)
                    if(type(j).__name__=='dict'):
                        for h in j:
                            t3 = t2.addSubTopic()
                            t3.setTopicHyperlink(t2.getID()) 
                            t3.setTitle(h) 
                            for m in j[h]:
                                if(type(m).__name__=='dict'):
                                    for n in m:
                                        t4 = t3.addSubTopic()
                                        t4.setTitle(n) 
                                        for l in m[n]:
                                            if(type(l).__name__=='dict'):
                                                for k in l:
                                                    t5 = t4.addSubTopic()       
                                                    t5.setTitle(k)
                                                    for p in l[k]:
                                                        if(type(p).__name__=='dict'):
                                                            for u in p:
                                                                t6 = t5.addSubTopic()
                                                                t6.setTitle(u)
                                                                for y in p[u]:
                                                                    if(type(y).__name__=='dict'):
                                                                        for a in y:
                                                                            t7 = t6.addSubTopic()
                                                                            t7.setTitle(a)
                                                                            for b in y[a]:
                                                                                t8 = t7.addSubTopic()
                                                                                t8.setTitle(b)
                                                                    else:
                                                                        t7 = t6.addSubTopic()
                                                                        t7.setTopicHyperlink(t2.getID()) 
                                                                        t7.setTitle(y)              
                                                        else:
                                                            t6 = t5.addSubTopic()
                                                            t6.setTopicHyperlink(t2.getID()) 
                                                            t6.setTitle(p)                                                        
                                            else:
                                                t5 = t4.addSubTopic()
                                                t5.setTopicHyperlink(t3.getID()) 
                                                t5.setTitle(l) 
                                else:
                                    t4 = t3.addSubTopic()
                                    t4.setTopicHyperlink(t3.getID()) 
                                    t4.setTitle(m) 
                    else:
                        t3 = t2.addSubTopic()
                        t3.setTopicHyperlink(t2.getID()) 
                        t3.setTitle(j) 
        else:
            t2 = t1.addSubTopic()
            t2.setTopicHyperlink(t1.getID()) 
            t2.setTitle(i) 



topics=r2.getSubTopics()
for topic in topics:
    topic.addMarker(MarkerId.starBlue)

xmind.save(w,"c:\\Users\\btr\\Desktop\\redis.xmind") 