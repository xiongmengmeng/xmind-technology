import xmind
from xmind.core.markerref import MarkerId
w = xmind.load("c:\\Users\\btr\\Desktop\\mysql2.xmind") 
s2=w.createSheet()
s2.setTitle("mysql2")
r2=s2.getRootTopic()
r2.setTitle("mysql2")


content={
'7.误删数据后恢复':[
    '1.误删行：Flashback 工具，修改binlog（格式为row）内容，拿回原库执行',
    'delete 全表很慢，会生成回滚日志、写 redo、写 binlog。从性能考虑，优先使用truncate table或drop table',
    '2.误删库/表:全量备份+增量日志',
    '加速的方法：在用备份恢复出临时实例之后，将临时实例设置成线上备库的从库',
    '3.rm 删除数据：备份跨机房，或者最好是跨城市保存',
    {'预防误删库/表':[
        '1.账号分离:开发DML权限，运维平时只读，必要时才更新',
        '2.制定操作规范：删表先改名，再在平台操作'
    ]}
]
'11.数据库表的空间回收':[
    '现象：表数据删掉一半，表文件大小不变',
    '一个InnoDB表包含两部分:表结构定义+数据',
    {'innodb_file_per_table':[
        'On:表数据存储在以.ibd为后缀的文件中,drop table,直接删除文件',
        'OFF:表的数据放在系统共享表空间，跟数据字典一起,表删掉，空间不会回收'
    ]},
    {'数据删除流程':[
        '数据页的复用跟记录的复用',
        'delete命令:把记录的位置，或数据页标记为了“可复用”，磁盘文件大小不会变',
        'insert命令：随机插入，可能造成索引的数据页分裂',
        'update命令：删除一个旧的值，再插入一个新值,会造成空洞'
        '经过大量增删改的表->存在空洞的->把空洞去掉->收缩表空间(重建表)'
    ]},
    {'重建表':[
        {'alter table A engine=InnoDB':[
            '转存数据、交换表名、删除旧表',
            '语句在启动时获取MDL写锁，真正拷贝数据前退化成读锁'
        ]},
        {'退化成读锁原因':[
            '实现Online DDL',
            '不直接解锁,禁止其他线程对这个表同时做 DDL'
        ]},
        {'Online DDL':[
            '最耗时是拷贝数据到临时表',
            '如个步骤的执行期间可接受增删改操作',
            '对整个过程来说，锁的时间很短，认为是Online的'
        ]}

    ]}
],

'20.“饮鸩止渴”提高性能的方法':[
    {'短连接风暴':[
        '先处理掉那些占着连接但是不工作的线程',
        '减少连接过程的消耗:跳过权限验证'
    ]},
    {'慢查询性能问题':[
        '索引没有设计好:直接执行alter table语句(创建索引支持Online DDL)的',
        'SQL 语句没写好：查询重写query_rewrite 功能',
        'MySQL 选错了索引：紧急给这个语句加上 force index'
    ]},
    {'QPS 突增问题':[
        '查询重写功能，把压力最大的 SQL 语句直接重写成"select 1"返回'
    ]}
],

'29.kill不掉的语句':[
    {'MySQL中的kill命令':[
        'kill query + 线程 id：终止线程中正在执行的语句',
        'kill connection + 线程 id：断开线程的连接'
    ]},
    {'执行kill query thread_id_B 时':[
        '1.把session B运行状态改成THD::KILL_QUERY',
        '2.给session B执行线程发一个信号'
    ]},
    {'kill 无效':[
        {'1.线程没有执行到判断线程状态的逻辑':[
            '等锁，未进入InnoDB',
            'IO压力大，读写IO的函数无法返回，导致不能及时判断线程状态'
        ]},
        {'2.终止逻辑耗时较长':[
            '超大事务执行期间被kill',
            '大查询回滚:删除临时文件需要等待 IO 资源',
            'DDL命令执行到最后阶段被kill:删除中间过程的临时文件,需要等待 IO 资源'
        ]}
    ]},
    '发送kill命令的客户端，不会强行停止目标线程的执行，只是设置了状态，并唤醒对应的线程',
    '被kill线程，需执行到判断状态的“埋点”，才会开始进入终止逻辑阶段(需要耗费时间)',
    {'于客户端误解':[
        '1.如果库里面的表多，连接会慢:不是服务端慢，而是客户端慢',
        '客户端在连接成功后，需多做一些操作：构建一个本地的哈希表（表多，耗时）'
        '2.–quick参数：让客户端变得更快,',
        {'MySQL客户端接收服务端返回结果':[
            '本地缓存，在本地开一片内存',
            '不缓存，读一个处理一个'
        ]},
        '加–quick，使用不缓存方式，如本地处理慢，会导致服务端发送结果被阻塞，让服务端变慢'
    ]}
],

'34.Memory引擎':[
    'Memory 引擎的数据和索引是分开的',
    '内存表的数据部分以数组的方式单独存放，而主键 id 索引里，存的是每个数据的位置。主键 id 是 hash 索引，可以看到索引上的 key 并不是有序的',
    {'InnoDB 和 Memory 引擎的数据组织方式是不同的':[
        'InnoDB 引擎把数据放在主键索引上，其他索引上保存的是主键 id',
        'Memory 引擎把数据单独存放，索引上保存数据位置的数据组织形式'
    ]},
    {'不建议在生产环境上使用内存表':[
        '锁粒度问题:不支持行锁，只支持表锁',
        '数据持久化问题:数据库重启的时候，所有的内存表都会被清空'
    ]},
    '但可考虑使用内部临时表'
],
'35.自增主键为什么不是连续的':[
    'AUTO_INCREMENT=n，存在表结构定义中，放在后缀名为.frm 的文件（不会保存自增值）',
    {'自增值的保存策略':[
        'MyISA：保存在数据文件中',
        'InnoDB：保存在内存里，MySQL 8.0后有了“自增值持久化”的能力'
    ]},
    {'修改机制及不连续原因':[
        'id 字段指定为 0、null 或未指定，把表当前AUTO_INCREMENT值填到自增字段',
        'id 字段指定了具体值，使用语句里指定的值',
        '双M结构里，auto_increment_increment=2，一个库的自增 id 是奇数，另一个库的自增 id 是偶数，避免两库生成的主键发生冲突',
        '唯一键冲突',
        '事务回滚'
    ]},
    {'innodb_autoinc_lock_mode，默1':[
        '0：语句执行结束后才释放锁',
        '1：普通 insert 语句，自增锁在申请之后就马上释放；类似 insert … select 这样的批量插入数据的语句，自增锁还是要等语句结束后才被释放',
        '2：所有的申请自增主键的动作都是申请后就释放锁'
    ]},
    '普通insert语句，含多个 value 值，一次性申请锁，申请完成后锁释放'
],
'36. 最快地复制一张表':[
    'mysqldump 命令将数据导出成一组 INSERT 语句',
    '导出 CSV 文件+load data 命令将数据导入到目标表',
    '物理拷贝方法'
],
'37.分区表':[
    '一个.frm 文件和 4 个.ibd 文件，每个分区对应一个.ibd 文件',
    '对引擎层:4 个表；对Server层：1 个表',
    {'手动分表和分区表区别':[
        '引擎层：无差别',
        'server层:分区表由server层决定使用哪个分区，手动分表由应用层代码来决定使用哪个分表'
    ]},
    {'问题':[
        'MySQL第一次打开分区表的时候，需要访问所有的分区',
        'server层：认为是同一张表，所有分区共用同一个 MDL 锁',
        '引擎层：认为不同表，MDL 锁后的执行过程，会根据分区表规则，只访问必要的分区'
    ]},
    {'应用场景':[
        '对业务透明，相对于用户分表，业务代码更简洁',
        '方便的清理历史数据,alter table t drop partition删除'
    ]}
],
{'':[
    '，join 将判断条件是否全部放在 on 部分就没有区别了',
    ''
]}
    
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

xmind.save(w,"c:\\Users\\btr\\Desktop\\mysql2.xmind") 