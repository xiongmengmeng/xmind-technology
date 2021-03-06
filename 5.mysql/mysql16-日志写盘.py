import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="mysql"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("日志写盘")
r2=s2.getRootTopic()
r2.setTitle("日志写盘")


content={
'binlog写盘':[
    'binlog cache:系统分配内存，每个线程一个（binlog_cache_size控制单线程内binlog cache大小），如超过，存到磁盘',
    {'binlog 的写入机制':[
        '事务执行过程，先把日志写到 binlog cache',
        '事务提交时，把 binlog cache 写到 binlog 中'
        '注意：一个事务的 binlog 不能被拆开'
    ]},
    'binlog 写盘状态:binlog cache-----write---->binlogo files----fsync---->disk',
    'write:把日志写入到文件系统的 page cache(没有把数据持久化到磁盘),速度快',
    'fsync:数据持久化到磁盘(占磁盘的 IOPS)',
    {'write和fsync的时机':[
        'sync_binlog=0 : 每次提交事务都只 write，不 fsync',
        'sync_binlog=1 : 每次提交事务都会执行 fsync',
        'sync_binlog=N(N>1) : 每次提交事务都 write，累积 N 个事务后才 fsync',
        'sync_binlog=N的风险：如果主机发生异常重启，会丢失最近 N 个事务的 binlog 日志'
    ]}
],
'redo log写盘':[
    {'存储状态':[
        '1.存在 redo log buffer 中，物理上是在 MySQL 进程内存中',
        '2.写到磁盘 (write)，但是没有持久化（fsync)，物理上是在文件系统的page cache里',
        '3.持久化到磁盘，对应的是hard disk'
    ]},
    {'写入策略':[
        'innodb_flush_log_at_trx_commit 参数',
        '0 : 每次事务提交时都只是把 redo log 留在 redo log buffer 中',
        '1 : 每次事务提交时都将 redo log 直接持久化到磁盘',
        '2 : 每次事务提交时都只是把 redo log 写到 page cache'
    ]},
    {'数据落盘':[
        'InnoDB有一后台线程，每隔1秒',
        '把redo log buffer中的日志，调用write写到文件系统的page cache',
        '最后调用 fsync 持久化到磁盘'
    ]},
    {'双 1”配置':[
        'sync_binlog 和 innodb_flush_log_at_trx_commit都为1',
        '一个事务完整提交前，需要等待两次刷盘，一次是 redo log（prepare 阶段），一次是 binlog'
    ]}
],
'细节':[
    '日志逻辑序列号LSN:单调递增，用来对应redo log的一个个写入点',
    '每次写入长度为length的redo log，LSN值就会加上 length',
    {'两阶段提交细化':[
        '1.redo log prepare:write',
        '2.binlog:write',
        '3.redo log prepare:fsync',
        '4.binlog:fsync',
        '5.redo log commit:write'
    ]},
    '并发更新场景下，第一个事务写完 redo log buffer 以后，fsync 越晚调用，组员可能越多，节约 IOPS 的效果就越好',
    {'MySQL出现IO性能瓶颈':[
        '1.设置binlog_group_commit_sync_delay和binlog_group_commit_sync_no_delay_count参数',
        '减少binlog的写盘次数',
        '基于“额外的故意等待”来实现，可能会增加语句响应时间，但没有丢失数据的风险',
        '2.sync_binlog设置为大于 1 的值（常见100~1000),风险是主机掉电时会丢 binlog 日志',
        '3.innodb_flush_log_at_trx_commit设置为2,风险是主机掉电的时候会丢数据'
    ]}
]
    
}
#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 