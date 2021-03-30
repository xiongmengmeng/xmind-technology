import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="mysql"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("加锁规则和问题")
r2=s2.getRootTopic()
r2.setTitle("加锁规则和问题")


content={
'加锁规则':[
    {'规则':[
        '两个“原则”、两个“优化”和一个“bug”',
        '原则 1：加锁的基本单位是 next-key lock(前开后闭区间)',
        '原则 2：查找过程中访问到的对象才会加锁,锁加在列上，即索引树上',
        '优化 1：索引上的等值查询，给唯一索引加锁的时候，next-key lock 退化为行锁',
        '优化 2：索引上的等值查询，向右遍历时且最后一个值不满足等值条件的时候，next-key lock 退化为间隙锁',
        '一个 bug：唯一索引上的范围查询会访问到不满足条件的第一个值为止',
        'lock in share mode只锁覆盖索引,for update会顺便给主键索引上满足条件的行加行锁'
    ]},
    '可重复读隔离级别遵守两阶段锁协议，所有加锁的资源，都是在事务提交或者回滚的时候才释放的'
],
'问题':[
    {'1.查询长时间不返回':[
        '大概率是表被锁住,show processlist命令，查看语句处于什么状态',
        {'Waiting for table metadata lock':[
            '等MDL锁,有一个线程正在表t上请求或者持有MDL写锁',
            '查询sys.schema_table_lock_waits表',
            '找出造成阻塞的process id，kill 命令断开连接'
        ]},
        {'Waiting for table flush':[
            '等flush,有一个线程正要对表t做flush,但被阻塞了',
            '即flush tables t with read lock;被阻塞了'
        ]},
        {'statistics':[
            '等行锁,有一个事务在这行记录上持有一个写锁',
            '通过 sys.innodb_lock_waits 表查到占用写锁的线程，kill掉'
        ]}
    ]},
    {'2.查询慢':[
        '直接读慢，lock in share mode快',
        '一致性读，从当前数据开始，依次执行undo log',
        '当前读，直接显示当前数据'
    ]}
],
}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 