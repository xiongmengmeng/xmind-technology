import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="mysql"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("union,group by")
r2=s2.getRootTopic()
r2.setTitle("union,group by")


content={
'union':[
    'union 要去重，需用到内部临时表',
    'union all 不用去重,依次执行子查询，结果依次发给客户端,不需要临时表',
    {'临时表':[
        '建表语法 create temporary table …',
        '只能被创建它的session访问，对其他线程不可见,session结束，自动删除临时表',
        '可与普通表同名(内存中每个表都有一个table_def_key：库名+表名+server_id+thread_id)',
        'session 内有同名的临时表和普通表，增删改查语句访问的是临时表',
        'binlog_format=row时，临时表的操作不记录到 binlog 中'
    ]},
    {'内部临时表':[
        '存放语句执行过程中的中间数据',
        '比union用到唯一索引约束，group by用到另外一个字段存累积计数'
    ]}
],
'group by':[
    '统计不同的值出现的个数,需要内部临时表来排序',
    '执行流程:内存临时表->sort buffer(排序)-内存临时表',
    {'优化':[
        '1：没有排序要求，语句后加 order by null',
        '2：索引:确保输入数据是有序的',
        '3：直接排序,语句中加入SQL_BIG_RESULT提示,告诉优化器：语句涉及的数据量大，请直接用磁盘临时表',
        'MySQL优化器觉得磁盘临时表是B+树存储，效率不如数组，直接使用数组'
    ]}
],
'limit 20000加载慢怎么解决':[
    '如真需要20000条数据，只能通过在排序列建立索引，或者把数据导入es，用es搜索引擎查询',
    '如只是limit 20000,10,可把20000的值先查出来，作为条件加入到where'
],
'总结':[
    {'内存空间':[
        'join_buffer 是无序数组',
        'sort_buffer 是有序数组',
        '临时表是二维表结构'
    ]},
    {'语句执行过程':[
        '一边读，一边得到结果，不需额外内存，否则需要额外内存来保存中间结果',
    ]}
]
}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 