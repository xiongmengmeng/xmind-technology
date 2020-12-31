import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="mysql"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("summary")
r2=s2.getRootTopic()
r2.setTitle("summary")


content={
'drop、delete、truncate的区别':[
    'drop删表,truncate和delete只删除数据',
    'delete删数据，删除操作作为事务记录在日志中，可进行回滚',
    'truncate一次性删除表中所有的数据,无操作记录日志，不能恢复'
],
'innodb和myisam的区别':[
    'InnoDB支持行级锁，事务，MVCC,MyISAM不支持',
    'count(*),InnoDB要扫描全表,MyISAM用一个变量保存了整个表的行数'
],
'用自增列作为主键':[
    '防止页断裂造成的空洞'
],
'使用索引能提高效率':[
    '索引是B+树结构，数据是有序的'
],
'B+树':[
    'https://www.jianshu.com/p/71700a464e97',
    '包含根节点、内部节点和叶子节点',
    '常用于数据库和操作系统的文件系统中',
    '数据稳定有序，插入与修改拥有较稳定的对数时间复杂度',
    '插入：当前结点key<=m-1，插入结束',
    '否则叶子结点分裂，左叶子结点含前m/2个记录，右结点含剩下的，第m/2+1个记录的key进位到父结点中',
    '删除: 结点的key>=Math.ceil(m/2)–1，删除结束',
    '否则若兄弟结点有富余，父结点key下移，兄弟结点key上移',
    '或当前结点和兄弟结点及父结点下移key合并成一个新的结点'
],
'B+树索引和hash索引的区别':[
    'hash索引底层 hash表,进行查找时,把键值换算成哈希值',
    'B+树底层 多路平衡查找树,查询从根节点出发,查找到叶子节点,同层级的节点间有指针相互链接，是有序的',
    'hash索引:等值查询更快,无法进行范围查询,不支持模糊查询'
],
'B树和B+树的区别':[
    'B树，每个节点都存储key和data，所有节点组成这棵树，并且叶子节点指针为null，叶子结点不包含任何关键字信息',
    'B+树，所有的叶子结点中包含了全部关键字的信息，及指向含有这些关键字记录的指针',
    '且叶子结点本身依关键字的大小自小而大的顺序链接',
    '所有的非终端结点可以看成是索引部分，结点中仅含有其子树根结点中最大（或最小）关键字'
],
'表分区与分表的区别':[
    '分表：指的是通过一定规则，将一张表分解成多张不同的表。比如将用户订单记录根据时间成多个表',
    '分表与分区的区别在于：分区从逻辑上来讲只有一张表，而分表则是将一张表分解成多张表'
],
'MVCC最大的好处':[
    '读不加锁，读写不冲突'
],
'explain命令来查看语句的执行计划':[
    ''
],
'varchar和char有什么区别':[
    'char:定长字段,char(10)的空间,无论实际存储多少内容.该字段都占用10个字符',
    'varchar:变长,申请的只是最大长度,占用的空间为实际字符长度+1,最后一个字符存储使用的空间长度',
    '检索效率上来讲,char > varchar'
],
'varchar(10)和int(10)':[
    'varchar的10代表了申请的空间长度,也是可以存储的数据的最大长度',
    'int的10只是代表了展示的长度,不足10位以0填充',
    'int(1)和int(10)所能存储的数字大小以及占用的空间都是相同的,只是在展示时按照长度展示'
],
'MySQL的binlog有有几种录入格式':[
    'statement:记录单元为语句',
    'row:记录单元为每一行的改动',
    'mix:普通操作使用statement记录,当无法使用statement的时候使用row'
]

    
}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 