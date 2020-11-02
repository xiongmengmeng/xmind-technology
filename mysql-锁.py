import xmind
from xmind.core.markerref import MarkerId
w = xmind.load("c:\\Users\\btr\\Desktop\\mysql-锁.xmind") 
s2=w.createSheet()
s2.setTitle("mysql-锁")
r2=s2.getRootTopic()
r2.setTitle("mysql-锁")


content={
'1.全局锁':[
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
        '利用MVCC,导数据前启动一个事务，拿到一致性视图,过程中数据可正常更新'
    ]}
],
'2.表级锁':[
    '语法：lock tables … read/write',
    '限制别的线程的读写外，也限定了本线程的操作对象',
    {'元数据锁MDL':[
        '不需显式使用，访问一个表的时会自动加上',
        '对一个表做【增删改查】操作的时->加 MDL 读锁',
        '对表做【结构】变更操作的时->加 MDL 写锁',
        '读锁间不互斥,读写锁间、写锁间互斥',
        '注意：事务中的MDL锁，在语句执行时申请，事务提交后再释放',
        {'给小表加字段':[
            '查当前执行中的事务:information_schema 库的 innodb_trx 表',
            '如要要做DDL变更的表有长事务在执行，考虑暂停DDL，或者kill长事务',
            '热点表:alter table语句中设定等待时间，不阻塞后面的业务语句'
        ]}
    ]}
],
'3.行锁':[
    '引擎层由各个引擎自己实现',
    '两阶段锁协议:行锁在需要的时候加上，事务结束时释放',
    '事务如要锁多个行，把最可能造成锁冲突的锁后放',
    {'死锁':[
        '并发系统，线程间循环依赖,等待别的线程释放资源，进入无限等待状态',
        {'解决':[
            '1.进入等待，直到超时,超时时间设置：innodb_lock_wait_timeout',
            '2.死锁检测：发现死锁，主动回滚死锁链条中的某一事务，让其他事务可继续执行',
            '语法：innodb_deadlock_detect=on',
            '耗费CPU资源:每个新的被堵线程，判断是否自己加入导致死锁，时间复杂度O(n)',
            '3.控制并发度',
        ]}
    ]}
],
'4.问题':[
    {'1.查询长时间不返回':[
        '大概率是表被锁住,show processlist命令，查看语句处于什么状态',
        {'Waiting for table metadata lock':[
            '等MDL锁,有一个线程正在表t上请求或者持有MDL写锁',
            '查询sys.schema_table_lock_waits表',
            '找出造成阻塞的process id，kill 命令断开连接'
        ]},
        {'Waiting for table flush':[
            '等flush,有一个线程正要对表t做flush,但被阻塞了',
            '即flush tables t with read lock;被阻塞了'
        ]},
        {'statistics':[
            '等行锁,有一个事务在这行记录上持有一个写锁',
            '通过 sys.innodb_lock_waits 表查到占用写锁的线程，kill掉'
        ]}
    ]},
    {'2.查询慢':[
        '直接读慢，lock in share mode快',
        '一致性读，从当前数据开始，依次执行undo log',
        '当前读，直接显示当前数据'
    ]}
],
'5.加锁规则':[
    {'规则':[
        '两个“原则”、两个“优化”和一个“bug”',
        '原则 1：加锁的基本单位是 next-key lock(前开后闭区间)',
        '原则 2：查找过程中访问到的对象才会加锁,锁加在列上，即索引树上',
        '优化 1：索引上的等值查询，给唯一索引加锁的时候，next-key lock 退化为行锁',
        '优化 2：索引上的等值查询，向右遍历时且最后一个值不满足等值条件的时候，next-key lock 退化为间隙锁',
        '一个 bug：唯一索引上的范围查询会访问到不满足条件的第一个值为止',
        'lock in share mode只锁覆盖索引,for update会顺便给主键索引上满足条件的行加行锁'
    ]},
    '可重复读隔离级别遵守两阶段锁协议，所有加锁的资源，都是在事务提交或者回滚的时候才释放的'
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

xmind.save(w,"c:\\Users\\btr\\Desktop\\mysql-锁.xmind") 