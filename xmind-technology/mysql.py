import xmind
from xmind.core.markerref import MarkerId
w = xmind.load("c:\\Users\\btr\\Desktop\\mysql.xmind") 
s2=w.createSheet()
s2.setTitle("mysql")
r2=s2.getRootTopic()
r2.setTitle("mysql")


content={
'1.基础架构':[
    {'Server 层':[
        '连接器:管理连接，权限验证',
        '查询缓存：命中即返回',
        '分析器：词法，语法分析',
        '优化器：执行计划生成，索引选择',
        '执行器：操作引擎，返回结果'
    ]},
    '存储引擎层：存储数据，提供读写接囗，常用的存储引擎是 InnoDB'
],
'2.日志系统':[
    {'redo log':[
        'InnoDB引擎特有日志',
        'write pos:当前记录的位置，一边写一边后移',
        'checkpoint:当前要擦除的位置，边写边后移，后移前把记录更新到文件',
        'write pos和checkpoint间空着部分：记录新操作',
        '如write pos追上checkpoint，此时不再执行新更新，需把checkpoint推进',
        '物理日志：记录“在某个数据页上做了什么修改',
        'innodb_flush_log_at_trx_commit=1，每次事务的 redo log 都直接持久化到磁盘，保证异常重启后数据不丢失'
    ]},
    {'binlog':[
        'Server 层的日志',
        '逻辑日志：记录语句的原始逻辑',
        'sync_binlog=1,每次事务的 binlog 都持久化到磁盘,保证异常重启之后 binlog 不丢失'
    ]},
    {'两阶段提交':[
        'edo log 的写入：prepare 和 commit',
        {'update 语句':[
            '1.执行器:找引擎取 ID=2 这一行（ID 是主键），用树搜索这一行，数据页在内存中，返回；否则，先从磁盘读入内存，再返回',
            '2.执行器:拿到引擎给的行数据，把值加上 1，写入新行',
            '3.引擎：将新行更新到内存，写入redo log （prepare 状态），告知执行器可提交事务',
            '4.执行器：写入 binlog，并把 binlog 写入磁盘',
            '5.执行器：调用引擎提交事务接口，redo log 改成commit状态'
        ]}
    ]},
    'WAL（Write-Ahead Logging）：先写日志，再写磁盘',
    'crash-safe:有了 redo log，InnoDB 可以保证即使数据库发生异常重启，之前提交的记录都不会丢失'
    '应用：建备库，恢复某一时间点的数据 ：全量备份+binlog，'
],
'3.事务隔离':[
    '事务支持：引擎层实现',
    'ACID（Atomicity、Consistency、Isolation、Durability，即原子性、一致性、隔离性、持久性）',
    {'隔离性':[
        '读未提交:事务还没提交时，它做的变更就能被别的事务看到',
        {'读提交':[
            '事务提交后，它做的变更才会被其他事务看到',
            '每个SQL语句开始执行的时候创建的'
        ]},
        {'可重复读':[
            '事务执行过程中看到的数据，跟这个事务在启动时看到的数据一致',
            '事务启动时创建的视图，整个事务存在期间都用这个视图'
        ]},
        '串行化:对于同一行记录，“写”会加“写锁”，“读”会加“读锁”。读写锁冲突时，后访问的事务必须等前一个事务执行完成，才能继续执行'
    ]},
    {'事务隔离的实现':[
        '多版本并发控制（MVCC）：一条记录在系统中可存在多个版本',
        {'回滚日志':[
            '回滚段+当前值',
            '删除条件:当没有事务需要用到这些回滚日志时',
            '长事务：系统里面会存在很老的事务视图,要避免'
        ]}
    ]},
],
'4.索引':[
    {'索引模型':[
        {'哈希表':[
            '区间查询慢',
            '适用于等值查询'
        ]},
        {'有序数组':[
            '等值查询和范围查询较优',
            '查询用二分法，时间复杂度是 O(log(N))',
            '插入成本高',
            '适用于静态存储引'
        ]},
        {'搜索树':[
            '以二叉举例',
            '父节点左子树所有结点的值小于父节点的值，右子树所有结点的值大于父节点的值',
            '树高，访问磁盘频繁,因索引不止存在内存中，还要写到磁盘上'
        ]}
    ]},
    {'InnoDB 的索引模型':[
        {'B+ 树':[
            'N=1200,树高4,存1200的3次方,17 亿',
            '树根放内存，查值最多访问3次磁盘',
            '配合磁盘的读写特性，减少单次查询的磁盘访问次数'
        ]},
        '表:根据主键顺序以索引的形式存放的',
        '每一个索引在 InnoDB 里面对应一棵 B+ 树',
        {'类型':[
            {'主键索引':[
                '叶子节点存的是整行数据'
            ]},
            {'非主键索引':[
                '叶子节点内容是主键的值',
                '回表：回到主键索引树搜索'
            ]}
        ]},
        {'索引维护':[
            '页分裂:数据页满了，申请一个新的数据页，挪动部分数据过去',
            '合并：相邻两个页由于删除了数据，利用率很低后'
        ]},
        {'重建索引':[
            '创建一个新索引，数据按顺序插入，页面的利用率变高',
            '解决：因页分裂导致的数据页有空洞',
            '重建主键索引：alter table T engine=InnoDB'
        ]}
    ]},
    {'数据库设计的原则':[
        '尽量少地访问资源',
        '覆盖索引',
        '最左前缀原则',
        '索引下推'
    ]}
],
'5.全局锁和表锁':[
    {'全局锁':[
        '对整个数据库实例加锁,整个库处于只读状态',
        '语法:Flush tables with read lock (FTWRL)',
        {'阻塞':[
            '数据更新语句（数据的增删改）',
            '数据定义语句（包括建表、修改表结构等）',
            '更新类事务的提交语句'
        ]},
        '使用场景:全库逻辑备份',
        {'mysqldump':[
            '官方逻辑备份工具',
            '使用参数–single-transaction',
            '利用MVCC,导数据前启动一个事务，确保拿到一致性视图,过程中数据可正常更新'
        ]}
    ]},
    {'表级锁':[
        {'表锁':[
            '语法：lock tables … read/write',
            '限制别的线程的读写外，也限定了本线程的操作对象'
        ]},
        {'元数据锁（meta data lock，MDL)':[
            '不需显式使用，访问一个表的时会自动加上',
            '当对一个表做【增删改查】操作的时->加 MDL 读锁',
            '当要对表做【结构】变更操作的时->加 MDL 写锁',
            '读锁间不互斥,读写锁间、写锁间互斥',
            '注意：事务中的MDL锁，在语句执行时申请，事务提交后再释放',
            {'给小表加字段':[
                '查当前执行中的事务:information_schema 库的 innodb_trx 表',
                '如要要做DDL变更的表有长事务在执行，考虑暂停DDL，或者kill长事务',
                '热点表:alter table语句中设定等待时间，等待时间内拿不到写锁，不阻塞后面的业务语句'
            ]}
        ]}
    ]},
    {'行锁':[
        '引擎层由各个引擎自己实的',
        '两阶段锁协议:行锁在需要的时候加上，事务结束时释放',
        '事务如要锁多个行，把最可能造成锁冲突的锁后放',
        {'死锁':[
            '并发系统，线程间循环依赖,等待别的线程释放资源，进入无限等待状态',
            {'解决':[
                '1.进入等待，直到超时,超时时间设置：innodb_lock_wait_timeout',
                '2.死锁检测：发现死锁，主动回滚死锁链条中的某一事务，让其他事务可继续执行',
                '语法：innodb_deadlock_detect=on'
                '耗费CPU资源:每个新的被堵线程，判断是否自己加入导致死锁，时间复杂度O(n)',
                '3.控制并发度',
            ]}
        ]}
    ]}],
'6.事务,隔离':[
    {'begin/start transaction':[
        '第一个操作InnoDB表的语句，事务才真正启动',
        '一致性视图是在执行第一个快照读语句时创建的'
    ]},
    'start transaction with consistent snapshot:一致性视图在执行此语句时创建',
    {'transaction id':[
        '每个事务有一个唯一的事务 ID',
        '事务开始时向InnoDB的事务系统申请，顺序严格递增'
    ]},
    {'row trx_id':[
        '每行数据有多个版本',
        '事务更新数据时，生成一个新的数据版本,并把transaction id赋值给据版本的事务ID'
    ]},
    '低水位:数组里面事务ID的最小值',
    '高水位:系统里已经创建事务ID的最大值+ 1'
    '视图数组和高水位，就组成了当前事务的一致性视图（read-view）',
    {'一个数据版本，对于一个事务视图来说，除了自己的更新总是可见以外，有三种情况':[
        '版本未提交，不可见',
        '版本已提交，但是是在视图创建后提交的，不可见',
        '版本已提交，而且是在视图创建前提交的，可见'
    ]},
    '当前读:更新数据都是先读后写的，而这个读，只能读当前的值'
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

xmind.save(w,"c:\\Users\\btr\\Desktop\\mysql.xmind") 