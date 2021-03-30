import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="mysql"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("日志简介")
r2=s2.getRootTopic()
r2.setTitle("日志简介")


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
    '物理日志：记录“在某个数据页上做了什么修改',
    'innodb_flush_log_at_trx_commit=1，每次事务的 redo log 都直接持久化到磁盘，保证异常重启后数据不丢失' 
],
'binlog':[
    'Server 层的日志',
    '逻辑日志：记录语句的原始逻辑',
    'sync_binlog=1,每次事务的 binlog 都持久化到磁盘,保证异常重启之后 binlog 不丢失',
    {'binlog的几种录入格式':[
        'statement:记录单元为语句',
        'row:记录单元为每一行的改动',
        'mix:普通操作使用statement记录,当无法使用statement的时候使用row'
    ]}
],
'两阶段提交':[
    'redo log 的写入：prepare 和 commit',
    '以update 语句为例：',
    '1.执行器:找引擎用树搜索ID=2这一行（ID主键），数据页在内存中，返回；否则，先从磁盘读入内存，再返回',
    '2.执行器:拿到引擎给的行数据，把值加上 1，写入新行',
    '3.引擎：将新行更新到内存，写入redo log （prepare 状态），告知执行器可提交事务',
    '4.执行器：写入 binlog，并把 binlog 写入磁盘',
    '5.执行器：调用引擎提交事务接口，redo log 改成commit状态'
],
'数据恢复':[
    '两阶段提交简图：写redo log(prepare)--A--->bingo--B--->redo log(commit)',
    'A状态：发生crash，此时 binlog 还没写，redo log 也没提交，崩溃恢复时，事务会回滚',
    {'B状态':[
        '如redo log里事务是完整的(有commit标识）,直接提交',
        {'如redo log里事务有完整prepare，判断事务binlog是否完整':[
            '是，提交事务（保证主备一致）',
            '否则，回滚事务'
        ]}
    ]},
    'redo log 和 binlog通过XID关联',
    {'一个事务的binlog格式':[
        'statement格式 : 最后有COMMIT',
        'row格式 : 最后有一个XID event'
    ]},
    'binlog:不能支持崩溃恢复(没有能力恢复“数据页”)',
    'redo log:系统是 crash-safe,但无法归档（mysql高可用依赖binlogo）',
    '数据落盘与redo log无关：它没有记录数据页的完整数据，没有能力更新磁盘数据页',
    'redo log buffe：一块内存，用来存redo logo日志的,执行commit 语句，把它写入redo log文件'
],
'日志系统总结':[
    'WAL（Write-Ahead Logging）：先写日志，再写磁盘',
    'crash-safe:通过redo log，InnoDB可保证数据库发生异常重启，之前提交的记录不丢失',
    '应用：建备库，恢复某一时间点的数据（全量备份+binlog）'
],

}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 