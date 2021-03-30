import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="mysql"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("Memory引擎")
r2=s2.getRootTopic()
r2.setTitle("Memory引擎")


content={
'Memory引擎':[
    'Memory 引擎的数据和索引是分开的',
    '内存表的数据部分以数组的方式单独存放，而主键 id 索引里，存的是每个数据的位置。主键 id 是 hash 索引，可以看到索引上的 key 并不是有序的',
    {'InnoDB 和 Memory 引擎的数据组织方式是不同的':[
        'InnoDB 引擎把数据放在主键索引上，其他索引上保存的是主键 id',
        'Memory 引擎把数据单独存放，索引上保存数据位置的数据组织形式'
    ]},
    {'不建议在生产环境上使用内存表':[
        '锁粒度问题:不支持行锁，只支持表锁',
        '数据持久化问题:数据库重启的时候，所有的内存表都会被清空'
    ]},
    '但可考虑使用内部临时表'
],
'innodb和myisam的区别':[
    'InnoDB支持行级锁，事务，MVCC,MyISAM不支持',
    'count(*),InnoDB要扫描全表,MyISAM用一个变量保存了整个表的行数'
],
'存储引擎的 InnoDB 与 MyISAM':[
    '通常我们都是使用InnoDB，mysql默认使用的数据引擎也是innoDB',
    'innoDB和MyISAM都是使用B+树来实现索引，区别是innoDB的叶子节点保存的是主键，MyISAM保存了整行，这样索引占空间更大，但是查询更快，因为索引覆盖',
    'MyISAM维护了每张表的总行数，select count(*) 如果没有where会非常快',
    'innoDB支持行锁，线程安全有保证(重要)
    'innoDB支持数据库事务，在复杂业务中更好用(重要)',
],
'MVCC最大的好处':[
    '读不加锁，读写不冲突'
],




    
}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 