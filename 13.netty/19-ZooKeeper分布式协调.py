import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="netty"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("ZooKeeper分布式协调")
r2=s2.getRootTopic()
r2.setTitle("ZooKeeper分布式协调")


content={
'分布式命名服务':[
    {'场景':[
        '分布式API目录',
        '分布式的ID生成器',
        '分布式节点的命名'
    ]},
    {'ID生成器方案':[
        {'Java的UUID':[
            '经由一定的算法机器生成的,是本地生成的ID，不需要进行远程调用，时延低，性能高',
            '缺点是过长，16字节共128位，通常以36字节长的字符串来表示，同时没有排序，无法保证趋势递增，因此用于数据库索引字段的效率就很低，添加记录存储入库时性能差'
        ]},
        {'分布式缓存Redis生成ID':[
            '利用Redis的原子操作INCR和INCRBY，生成全局唯一的ID'
        ]},
        {'Twitter的SnowFlake算法':[
            '生成的ID是一个64bit的长整型数字,可以使用ZK实现SnowFlakeID算法',
            '优点:在内存生成，高性能和高可用性,容量大,ID呈趋势递增，后续插入数据库的索引树时，性能较高',
            '缺点：依赖于系统时钟的一致性，如果某台机器的系统时钟回拨了，有可能造成ID冲突，或者ID乱序'
        ]},
        {'ZooKeeper生成ID':[
            '利用ZooKeeper的顺序节点，生成全局唯一的ID'
        ]},
        {'MongoDb的ObjectId':[
            'MongoDB是一个分布式的非结构化NoSQL数据库，每插入一条记录会自动生成全局唯一的一个“_id”字段值，它是一个12字节的字符串，可以作为分布式系统中全局唯一的ID'
        ]}
    ]}
],
'分布式锁':[
    '可重入的公平锁',
    {'ZooKeeper分布式锁':[
        {'原理':[
            '一个ZooKeeper分布式锁，首先需要创建一个父节点，尽量是持久节点（PERSISTENT类型）',
            '然后每个要获得锁的线程都在这个节点下创建个临时顺序节点',
            '由于Zk节点是按照创建的顺序依次递增的，为了确保公平，可以简单地规定，编号最小的那个节点表示获得了锁',
            '因此，每个线程在尝试占用锁之前，首先判断自己的排号是不是当前最小的，如果是，则获取锁'
        ]},
        {'优点':[
            'ZooKeeper的每一个节点都是一个天然的顺序发号器',
            'ZooKeeper节点的递增有序性可以确保锁的公平',
            'ZooKeeper的节点监听机制可以保障占有锁的传递有序而且高效',
            'ZooKeeper的临时顺序节点,能保证由于网络异常或者其他原因造成集群中占用锁的客户端失联时，锁能够被有效释放。',
            'ZooKeeper的节点监听机制能避免羊群效应:当一个节点挂掉，只有它后面的那一个节点才作出反应'
        ]},
        {'缺点':[
            '性能不太高:每次在创建锁和释放锁的过程中，都要动态创建、销毁暂时节点来实现锁功能',
            'Zk中创建和删除节点只能通过Leader（主）服务器来执行，然后Leader服务器还需要将数据同步到所有的Follower（从）服务器上，频繁的网络通信'
        ]},
        {'基于ZooKeeper实现一下分布式锁':[
            '1.一把锁，使用一个ZNode节点表示，如果锁对应的ZNode节点不存在，那么先创建ZNode节点',
            '2.抢占锁的所有客户端，使用锁的ZNode节点的子节点列表来表示；如果某个客户端需要占用锁，则在“/test/lock”下创建一个临时有序的子节点',
            '3.客户端创建子节点后,判断自己创建的子节点是否为当前子节点列表中序号最小的子节点。如果是，则认为加锁成功；如果不是，则监听前一个ZNode子节点的变更消息，等待前一个节点释放锁',
            '4.一旦队列中后面的节点获得前一个子节点的变更通知，进行判断自己是否为当前子节点列表中序号最小的子节点，如果是，则认为加锁成功；如果不是，则持续监听，一直到获得锁',
            '5.获取锁后，开始处理业务流程。在完成业务流程后，删除自己对应的子节点，完成释放锁的工作，以便后面的节点能捕获到节点的变更通知，获得分布式锁'
        ]},
        'Curator的InterProcessMutex可重入锁'
    ]} 
]
}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 