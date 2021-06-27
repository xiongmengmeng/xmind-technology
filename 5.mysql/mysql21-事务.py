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
'概述':[
    '事务支持：引擎层实现',
    {'ACID':[
        'Atomicity:原子性，指操作是不可分割的',
        'Consistency:一致性，指一起成功，一起失败',
        'Isolation:隔离性，指不会被其他影响',
        'Durability:持久性，指每次操作都是已经执行了，已经持久化到磁盘的',
    ]}
],
'隔离性':[
    {'读未提交':[
        '事务还没提交时，它做的变更就能被别的事务看到'
    ]},
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
'事务隔离实现':[
    '多版本并发控制（MVCC）：一条记录在系统中可存在多个版本',
],
'基础概念':[
    {'begin/start transaction':[
        '第一个操作InnoDB表的语句，事务才真正启动',
        '一致性视图是在执行第一个快照读语句时创建的'
    ]},
    {'start transaction with consistent snapshot':[
        '一致性视图在执行此语句时创建'
    ]},
    {'transaction id':[
        '每个事务有一个唯一的事务ID',
        '事务开始时向InnoDB的事务系统申请，顺序严格递增'
    ]},
    {'row trx_id':[
        '每行数据有多个版本',
        '事务更新数据时，把transaction id赋值给一个新的数据版本'
    ]},
    {'当前读':[
        'select * table for update/insert/delete',
        '读取的是记录的最新版本，同时保证其他并发事务不能修改当前记录'
    ]},
    {'快照读':[
        '不加锁的select'
    ]}
]


    
}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 