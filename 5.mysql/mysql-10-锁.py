import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="mysql"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("锁")
r2=s2.getRootTopic()
r2.setTitle("锁")


content={
'都是悲观锁':[],
'全局锁':[
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
'表级锁':[
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
'行锁':[
    '引擎层由各个引擎自己实现,没有读锁，只有写锁',
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
'间隙锁Gap Lock':[
    {'幻读':[
        '一个事务，前后两次查询同一个范围，后一次看到了前一次查询没有看到的行',
        '可重复读隔离级别下,普通查询是快照读,不会看到别的事务插入的数据',
        '幻读在“当前读”下才会出现',
        '幻读仅指新插入的',
    ]},
    {'间隙锁Gap Lock':[
        '锁的是两个值之间的空隙，InnoDB为了解决幻读问题引入的新锁',
        '间隙锁间不存在冲突关系',
        '跟间隙锁存在冲突关系的，是“往这个间隙中插入一个记录”的操作',
        '间隙锁和行锁合称next-key lock（前开后闭区间）',
        '间隙锁的引入，可能会导致同样语句锁住更大范围，是影响并发度的',
        '在可重复读隔离级别下才生效的，读提交隔离条件下是没有间隙锁的'
    ]},
    '读提交隔离条件下,需要把binlog 格式设置为 row'
]
}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 