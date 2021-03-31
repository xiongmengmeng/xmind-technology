import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="mysql"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("引擎")
r2=s2.getRootTopic()
r2.setTitle("引擎")


content={
'MyISAM':[
    {'每个MyISAM在磁盘上存储成三个文件':[
        '1.frm文件：存储表的定义数据',
        '2.MYD文件：存放表具体记录的数据',
        '3.MYI文件：存储索引,仅保存记录所在页的指针，索引的结构是B+树结构'
    ]},
    '存储引擎通过MYI的B+树结构来查找记录页，再根据记录页查找记录',
    '不支持事务'
],
'InnoDB':[
    '1.通过自动增长auto_increment,生成id',
    '2.支持事务:默认隔离级别为可重复度，通过MVCC（并发版本控制）来实现',
    '3.使用的锁粒度为行级锁，可支持更高的并发',
    '4.存在着缓冲管理:通过缓冲池，将索引和数据全部缓存起来，加快查询的速度',
    '5.InnoDB类型的表，其数据的物理组织形式是聚簇表,所有数据按照主键来组织,数据和索引放在一块，位于B+数的叶子节点上'
    '6.支持事务'
],
'Memory':[
    '1.支持数据类型有限:如不支持TEXT和BLOB类型，对字符串类型，只支持固定长度的，VARCHAR会被自动存储为CHAR类型',
    '2.支持的锁粒度为表级锁:访问量大时，表级锁会成为MEMORY存储引擎的瓶颈',
    '3.数据存放在内存中:一旦服务器出现故障，数据会丢失',
    '4.默认使用hash索引'
],
'InnoDB和Memory的区别':[
    'InnoDB引擎：把数据放在主键索引上，其他索引上保存的是主键id',
    'Memory引擎：把数据单独存放，索引上保存数据位置'
],
'InnoDB和MyISAM的区别':[
    '都是使用B+树来实现索引，但innoDB的叶子节点保存的是主键和数据(占空间更大,但查询更快)，MyISAM保存了数据指针',
    '锁：InnoDB支持行级锁，事务，MVCC,MyISAM不支持',
    'count(*)：InnoDB要扫描全表,MyISAM用一个变量保存了整个表的行数'
]
}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 