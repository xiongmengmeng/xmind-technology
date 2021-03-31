import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="mysql"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("mysql")
r2=s2.getRootTopic()
r2.setTitle("mysql")


content={
'数据库':[
    '数据库三范式',
    '分库',
    '分表',
    '分区'
],
'表':[
    '表复制',
    '表空间回收',
    '数据误删后恢复',
    '分布式id的生成方案',
    '字段'
],
'SQL':[
    'explain',
    'count(*)',
    {'全表扫描':[
        '对Server',
        '对InnoDB'
    ]},
    'join--join_buffer--无序数组',
    'order by--sort_buffer--有序数组',
    'union,group by--临时表--二维表结构'
],
'索引':[
    '引擎',
    {'索引模型':[
        '哈希表',
        '有序数组',
        '搜索树'
    ]},
    'InnoDB 的索引模型--B+树',
    '普通索引vs唯一索引',
    {'索引问题':[
        '选错索引',
        '函数'
    ]}
],
'日志':[
    {'基础架构':[
        'Server 层',
        '存储引擎层'
    ]},
    'redo log',
    'binlog',
    '两阶段提交',
    '数据恢复',
    '刷脏页',
    'redo log写盘',
    'binlog写盘',
],
'锁':[
    '全局锁',
    '表级锁',
    '行锁',
    '间隙锁Gap Lock',
    '加锁规则',
    '锁的问题',
],
'事务':[
    {'隔离性':[
        '读未提交',
        '读提交',
        '可重复读',
        '串行化'
    ]},
    '事务隔离实现:mvcc+回滚日志',
    '事务隔离细节',
    '幻读'
],
'主备':[
    {'binlog三种格式':[
        'statement',
        'row',
        'mixed'
    ]},
    '主备同步',
    '主备延迟',
    '主备切换',
]
}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 