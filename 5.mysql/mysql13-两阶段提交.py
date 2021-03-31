import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="mysql"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("两阶段提交")
r2=s2.getRootTopic()
r2.setTitle("两阶段提交")


content={
'一条查询语句的执行流程':[
    {'1.连接':[
        '通过【连接器】跟客户端建立连接、获取权限、维持和管理连接'
    ]},
    {'2.查询':[
        '查询缓存(8.0已经没有了)',
        '分析器：词法分析，语法分析',
        '优化器：原则尽可能扫描少的数据库行纪录',
        '执行器：鉴权，调用引擎APIF进行数据操作，组装结果集返回给客户端'
    ]}
],
'一条更新语句的执行流程':[
    '1.执行器:调用引擎接囗取ID=2这一行',
    {'2.引擎':[
        'ID 是主键，直接用树搜索找到这一行',
        '数据页在内存中，返回',
        '否则，先从磁盘读入内存，再返回'
    ]},
    '3.执行器:拿到引擎给的行数据，把值加上1，得到新的一行数据，调用引擎接口写入这行新数据',
    '4.引擎:将新行更新到内存，写入redo log(prepare 状态),告知执行器可提交事务',
    {'5.执行器':[
        '写入 binlog，并把 binlog 写入磁盘',
        '调用引擎的提交事务接口'
    ]},
    '6:引擎:把刚刚写入的redo log改成提交（commit）状态，更新完成',
    {'总结':[
        '两阶段提交',
        'redo log 的写入：prepare 和 commit'
    ]}
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
    {'binlog':[
        '不能支持崩溃恢复(没有能力恢复“数据页”)'
    ]},
    {'redo log':[
        '系统是 crash-safe,但无法归档（mysql高可用依赖binlogo）',
        '数据落盘与redo log无关：它没有记录数据页的完整数据，没有能力更新磁盘数据页',
        'redo log buffe：一块内存，用来存redo logo日志的,执行commit 语句，把它写入redo log文件'
    ]}
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