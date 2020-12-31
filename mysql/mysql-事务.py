import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="mysql"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("mysql-事务")
r2=s2.getRootTopic()
r2.setTitle("mysql-事务")


content={
'1.概述':[
    '事务支持：引擎层实现',
    'ACID（Atomicity、Consistency、Isolation、Durability)',
    '原子性、一致性、隔离性、持久性',
],
'2.隔离性':[
    '读未提交:事务还没提交时，它做的变更就能被别的事务看到',
    {'读提交':[
        '事务提交后，它做的变更才会被其他事务看到',
        '每个SQL语句开始执行的时候创建的'
    ]},
    {'可重复读':[
        '事务执行过程中看到的数据，跟这个事务在启动时看到的数据一致',
        '事务启动时创建的视图，整个事务存在期间都用这个视图'
    ]},
    {'串行化':[
        '对于同一行记录，写会加写锁，读会加读锁',
        '读写锁冲突时，后访问的事务必须等前一个事务执行完成，才能继续执行'
    ]}
],
'3.事务隔离实现':[
    '多版本并发控制（MVCC）：一条记录在系统中可存在多个版本',
    {'回滚日志':[
        '回滚段+当前值',
        '删除条件:当没有事务需要用到这些回滚日志时',
        '长事务：系统里面会存在很老的事务视图,要避免'
    ]}
],
'4.事务隔离细节':[
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
        '事务更新数据时，把transaction id赋值给一个新的数据版本'
    ]},
    '低水位:数组里面事务ID的最小值',
    '高水位:系统里已经创建事务ID的最大值+ 1',
    '视图数组和高水位，组成当前事务的一致性视图（read-view）',
    '一个数据版本，对于一个事务视图来说，自己的更新总是可见',
    {'其余三种情况':[
        '版本未提交，不可见',
        '版本已提交，但是是在视图创建后提交的，不可见',
        '版本已提交，而且是在视图创建前提交的，可见'
    ]},
    '当前读:更新数据都是先读后写的，而这个读，只能读当前的值'
],
'5.幻读':[
    {'幻读':[
        '一个事务，前后两次查询同一个范围，后一次看到了前一次查询没有看到的行',
        '可重复读隔离级别下,普通查询是快照读,不会看到别的事务插入的数据',
        '幻读在“当前读”下才会出现',
        '幻读仅指新插入的'
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