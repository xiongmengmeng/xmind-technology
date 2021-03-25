import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="redis"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("缓存异常")
r2=s2.getRootTopic()
r2.setTitle("缓存异常")


content={
'分布式问题':[
    {'SETNX分布式锁':[
        '使用SETNX(SET if Not eXists)命令获取锁，若返回0（key已存在，锁已存在）则获取失败，反之获取成功',
        '为key设置“合理”的过期时间，防止获取锁后程序出现异常，导致其他线程调用SETNX命令总是返回0而进入死锁状态',
        '先拿setnx来争抢锁，抢到之后，再用expire给锁加一个过期时间防止锁忘记了释放',
        'setnx和expire在一条指令里'
        '释放锁：使用DEL命令将锁数据删除'
    ]},
    {'zookeeper锁':[
        '基于zookeeper临时有序节点实现',
        '客户端对某方法加锁，在zookeeper上的与该方法对应的指定节点目录下，生成一个唯一的瞬时有序节点',
        '判断是否获取锁:判断有序节点中序号最小的一个',
        '释放锁：将瞬时节点删除'
    ]}
],
'缓存异常':[
    {'缓存雪崩':[
        '缓存同一时间大面积失效，请求都落到数据库上',
        '解决：缓存数据的过期时间+随机值'
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
'Jedis与Redisson对比':[
    'Jedis：Redis的Java实现的客户端，其API提供了较全面的Redis命令支持',
    'Redisson：实现了分布式和可扩展的Java数据结构，功能较简单，不支持字符串操作,排序、事务、管道、分区等'
],
'其它':[
    '一致性哈希算法，哈希槽',
    'https://www.cnblogs.com/lpfuture/p/5796398.html'
]
}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 