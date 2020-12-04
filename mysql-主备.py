import xmind
from xmind.core.markerref import MarkerId
w = xmind.load("c:\\Users\\btr\\Desktop\\mysql.xmind") 
s2=w.createSheet()
s2.setTitle("mysql-主备")
r2=s2.getRootTopic()
r2.setTitle("mysql-主备")


content={
'1.基础知识':[
    {'备库设置成只读（readonly）模式':[
        '1.有时运营类的查询语句会被放到备库上去查，防止误操作',
        '2.防止切换逻辑有bug，如切换过程出现双写，造成主备不一致',
        '3.可用readonly状态，判断节点角色',
        '注：readonly对超级权限用户是无效的，同步更新的线程拥有超级权限'
    ]},
    {'binlog三种格式binlog_format':[
        'statement : 记录的就是 SQL 语句的原文',
        'row : 占空间，记录了真实删除行的主键 id，恢复数据方便',
        'mixed :两种格式都有，确定行数的用statement格式的，其余用row的'
    ]},
    {'循环复制的问题':[
        '备库接到 binlog 并在重放的过程中，生成与原binlog的server id相同的新的binlog',
        '每个库在收到日志后，先判断server id，跟自己的相同，直接丢弃这个日志'
    ]}
],
'2.事务日志同步过程':[
    '备库B：io_thread--->relay log--->sql_thread',
    '备库B 跟主库A 之间维持了一个长连接。主库A 内部有一个线程，专门用于服务备库B 的这个长连接',
    '1.备库B通过change master命令，设置主库A的 IP、端口、用户名、密码，以及要从哪个位置(包含文件名和日志偏移量)开始请求 binlog',
    '2.备库B执行start slave命令，会启动两个线程:io_thread(负责与主库建立连接)和sql_thread ',
    '3.主库A校验完用户名、密码后，开始按照备库 B 传过来的位置，从本地读取 binlog，发给 B',
    '4.备库B拿到 binlog 后，写到中转日志（relay log）,sql_thread 读取中转日志，解析出日志里的命令，并执行'
],
'3.主备延迟现象':[
    'show slave status 命令,seconds_behind_master显示当前备库延迟秒数',
    '网络正常时，日志从主库传给备库所需时间很短',
    '主备延迟的主要:备库接收完 binlog 和执行完这个事务之间的时间差',
    '表现:备库消费中转日志（relay log）的速度，比主库生产binlog慢'
],
'4.主备延迟原因':[
    '1.备库所在机器性能比主库差:更新请求对IOPS的压力，在主库和备库上是无差别的',
    '2.备库的压力大:备库上的查询耗费了大量CPU资源，影响同步速度',
    '解决：2.1一主多从，分担读的压力',
    '2.2通过 binlog 输出到外部系统(如Hadoop)，让外部系统提供统计类查询',
    '3.大事务:一次性地delete删除太多数据/大表 DDL',
    '4.备库的并行复制能力'
],
'5.主备切换过程':[
    '1.判断备库 B 的 seconds_behind_master，小于5 秒，继续下一步，否则持续重试',
    '2.把主库 A 改成只读状态（readonly 设置为 true）',
    '3.判断备库 B 的 seconds_behind_master，直到变成 0 为止',
    '4.把备库 B 改成可读写状态（readonly 设置为 false）',
    '5.把业务请求切到备库 B'
],
'6.备库延迟解决':[
    'sql_thread 执行中转日志,改为多线程复制策略',
    '1.按库分发策略',
    '2.commit状态，即同一组里提交的事务不会更新同一行（利用redo log组提交优化）',
    '3.rego log于prepare与commit状态的事务，在备库执行时可并行',
    '4.按行分发策略'
],
'7.一主多从的正确切换':[
    '基于位点的主备切换:需主动跳过错误',
    {'GTID':[
        '全局事务ID，一个事务在提交的时候生成，是事务的唯一标识',
        'GTID=server_uuid:gno',
        'server_uuid:一个实例第一次启动时自动生成的，一个全局唯一的值',
        'gno:一个整数，初始值1，每次commit的时候分配给这个事务，并加 1',
        '启动一个MySQL实例时，加上参数gtid_mode=on和enforce_gtid_consistency=on'
    ]},
    {'基于GTID的主备切换':[
        '备库 B 要设置为新主库 A’的从库',
        '1.实例 B 指定主库 A’，基于主备协议建立连接',
        '2.实例 B 把 set_b 发给主库 A’',
        '3.实例 A’算出set_a与set_b差集（存在于set_a，不存在set_b的GTID集合）',
        '判断 A’本地是否包含了差集需要的所有binlog事务',
        'a.不包含：A’已经把实例 B 需要的 binlog 删掉了，直接返回错误',
        'b.全部包含：A’从自己的 binlog 文件里，找出第一个不在set_b的事务，发给B',
        '4.之后从这个事务开始，往后读文件，按顺序取binlog发给B去执行'
    ]}
],
'8.读写分离的坑':[
    '一主多从的结构，其实就是读写分离的基本结构',
    {'客户端直连':[
        '整体架构简单，排查问题方便',
        '要了解后端部署细节，在出现主备切换、库迁移等操作时，客户端会感知到，并需调整数据库连接信息',
        '一般伴随一个负责管理后端的组件（如Zookeeper），尽量让业务端只专注业务逻辑开发'
    ]},
    {'带proxy的读写分离架构':[
        '对客户端友好',
        '后端维护团队的要求高，且proxy也需要有高可用架构'
    ]},
    {'处理过期读的方案':[
        '强制走主库:将查询请求做分类',
        'Sleep ',
        '判断主备无延迟方案:超时放弃,并转到主库查询',
        '等主库位点方案',
        'GTID 方案'
    ]}
],
'9.数据库出问题判断':[
    '1.select 1:有返回:进程还在',
    'InnoDB中，innodb_thread_concurrency通常取值64~128，机器CPU 核有限，减少上下文切换',
    {'并发连接和并发查询':[
        '并发连接：show processlist结果里的几千个连接，会占用一些内存',
        '并发查询：当前正在执行的语句，CPU 杀手',
        '线程进入锁等待后，并发线程的计数减一',
    ]},
    '2.查表判断:检测 InnoDB 并发线程数过多导致的系统不可用情况',
    '3.更新判断:判断binlog内存是否正常，但基于外部检测，判断慢',
    '4.内部统计:5.6版本后提供performance_schema 库，在file_summary_by_event_name 表里统计每次IO请求的时间'
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