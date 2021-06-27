import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="mysql"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("mysql-MVCC")
r2=s2.getRootTopic()
r2.setTitle("mysql-MVCC")


content={
'MVCC':[
    'Multi-Version Concurrency Control',
    '一种并发控制的方法',
    '维持一个数据的多个版本，使得读写操作没有冲突',
    {'目的':[
        '提高数据库并发性能，用更好的方式处理读写冲突',
        '做到即使有读写冲突，也能不加锁，非阻塞并发读'
    ]},
    {'原理':[
        '执行任何查询sql时会生成当前事务的一致性视图read-view',
        '该视图在事务结束之前都不会变化(如是读已提交隔离级别每次执行查询sql时会重新生成)',
        '视图由执行查询时所有未提交事务id数组和已创建的最大事务id组成',
        {'事务里的sql查询结果':[
            '从对应版本链里的最新数据开始逐条跟read-view做比',
            '从而得到最终的快照结果'
        ]}
    ]},
    {'实现':[
        {'表的两个隐藏字段':[
            {'trx_id':[
                '最近修改(插入)事务id',
            ]},
            {'roll_ptr':[
                '回滚指针',
                '指向这条记录的上一个版本(配合undo log)'
            ]},
        ]},
        {'undo log 回滚段':[
        ]}
    ]},
],
'回滚日志的问题':[
    {'删除条件':[
        '当没有事务需要用到这些回滚日志时'
    ]},
    {'问题':[
        '长事务会导致系统里存在很老的事务视图,要避免'
    ]}
],
'数据版本':[
    {'低水位':[
        '数组里面事务ID的最小值'
    ]},
    {'高水位':[
        '系统里已经创建事务ID的最大值+1'
    ]},
    {'当前事务的一致性视图（read-view）':[
        '视图数组',
        '高水位'
    ]},
    '一个数据版本，对于一个事务视图来说，自己的更新总是可见',
    {'可见性有三种情况':[
        '版本未提交，不可见',
        '版本已提交，但是是在视图创建后提交的，不可见',
        '版本已提交，而且是在视图创建前提交的，可见'
    ]},
]


    
}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 