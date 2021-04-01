import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="mysql"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("基础架构与日志设计")
r2=s2.getRootTopic()
r2.setTitle("基础架构与日志设计")


content={
'基础架构':[
    {'Server 层':[
        '连接器:管理连接，权限验证',
        '查询缓存：命中即返回',
        '分析器：词法，语法分析',
        '优化器：执行计划生成，索引选择',
        '执行器：操作引擎，返回结果'
    ]},
    '存储引擎层：存储数据，提供读写接囗，常用的存储引擎是 InnoDB'
],
'redo log':[
    'InnoDB引擎特有',
    'write pos:当前记录的位置，一边写一边后移',
    'checkpoint:当前要擦除的位置，边写边后移，后移前把记录更新到文件',
    'write pos和checkpoint间空着部分：记录新操作',
    '如write pos追上checkpoint，此时不再执行新更新，需把checkpoint推进',
    '物理日志：记录“在某个数据页"上做了什么修改',
    'innodb_flush_log_at_trx_commit=1，每次事务的redo log都直接持久化到磁盘，保证异常重启后数据不丢失',
],
'binlog':[
    'Server 层的日志',
    '逻辑日志：记录语句的原始逻辑',
    'sync_binlog=1,每次事务的 binlog 都持久化到磁盘,保证异常重启之后 binlog 不丢失',
    {'binlog的几种录入格式':[
        'statement:记录单元为语句',
        'row:记录单元为每一行的改动',
        'mix:普通操作使用statement记录,当无法使用statement的时候使用row'
    ]},
    {'一个事务的binlog格式':[
        'statement格式 : 最后有COMMIT',
        'row格式 : 最后有一个XID event'
    ]},
],
'刷脏页':[
    {'脏页':[
        '内存跟磁盘数据页内容不一致的时候，内存页为脏页'
    ]},
    {'干净页':[
        '内存数据写入到磁盘，内存和磁盘数据页内容一致'
    ]},
    '更新操作:平时执行很快，主要是写内存和日志',
    'MySQL偶尔抖动瞬间->可能在刷脏页（flush）',
    {'flush触发条件':[
        '1.redo log写满了,停止所有更新操作，将checkpoint往前推进',
        '2.系统内存不足：需新的内存页，要淘汰些数据页，如淘汰的是脏页，要先将脏页写到磁盘',
        '3.MySQL 认为系统“空闲”的时候',
        '4.MySQL 正常关闭时'
    ]},
    {'内存页三种状态':[
        'InnoDB 用缓冲池（buffer pool）管理内存',
        '1.还没有使用的',
        '2.使用了并且是干净页',
        '3.使用了并且是脏页'
    ]},
    {'刷脏页的控制策略':[
        {'刷盘速度':[
            'innodb_io_capacity:告诉InnoDB主机的IO能力',
            '建议设置成磁盘的IOPS'
        ]},
        {'刷盘条件':[
            '脏页比例(不要让它经常接近 75%)',
            'redo log 写盘速度'
        ]},
        {'刷盘方式':[
            'innodb_flush_neighbors=0：只刷自己，不带邻居'
        ]}
    ]}
],

}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 