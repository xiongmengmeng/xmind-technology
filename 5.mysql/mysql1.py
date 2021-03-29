import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="mysql"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("other")
r2=s2.getRootTopic()
r2.setTitle("other")


content={
'数据库的三范式':[
    '1NF:字段是原子性的',
    '2NF:必须有主键，非主键必须依赖主键，不能冗余无关联的字段',
    '3NF:非主键不能通过依赖传递关联到主键来依赖'
],
'反模式设计':[
    {'1NF':[
        '字段是原子性的,有些字段是需要合并的，比如数组，这也是mysql设计json字段的原因，当然json字段并不好用，可以用1:N扩展表',
        '但是如果这个字段不需要精准查询，是可以存在一起的',
    ]},
    '2NF:冗余热点查询字段，可以避免连表，提高特定查询的销量',
    '3NF:冗余热点结果字段，可以少查一次表',
    '反模式设计一定是为了某种特殊情况存在的，可以为了解决一些问题而跳出框架，牺牲既定规则得到另一方面的提升'
],
'分库与分表设计':[
    '分库分表，即mysql单机性能不足，需要分开多个库，库中的每张表多分成多张表来存储数据',
    '业务分库其实可以按业务分，只要是不需要join的表按业务分开',
    {'数据分库分表不同，要把一张表切开多张':[
        '按主键分:使用hash方法'
        '按某个字段分：如时间，这样会一定时间增长一个分表'
    ]}
],
'分库与分表带来的分布式困境与应对之策':[
    {' 跨库事务问题':[
        'mysql本身的分布式事务管理，会牺牲很大的性能，分库本身就是为了提升性能',
        '如果代码来实现这个事务，那么每条sql都要写对应的回滚sql，也很麻烦'
    ]},
    {'跨库join问题':[
        '跨库无法join表，需要到每个库去执行结果自己在代码里比对和join'
    ]},
    {'跨库order by问题':[
        '每个库都需要执行这条sql，最后查询到的总量是order by*N，然后再归并排序或者堆排序解决'
    ]},
    {'跨库distinct问题':[
        '框架或者代码自己解决，数据库只支持单实例的distinct'
    ]}
],
'SQL 优化之道':[
    'sql打印出来之后explain看看',
    '查询条件尽量在索引上',
    '避免回表，避免多次回表',
    '排序条件在查询索引上',
    '参与排序的列越少越好，多了就要fileSort',
    'count(*)比其他的快',
    '一张表的索引不能太多',
    '联合索引要考虑最左匹配',
],
'MySQL 遇到的死锁问题':[
    {'事务先更新/删除，然后插入数据，并发会引起间隙锁死锁':[
        '事务A一条删除或更新语句没有执行到数据，加间隙锁',
        '事务B一条删除或更新语句没有执行到数据，加间隙锁，范围相同',
        '事务A的插入语句等待B释放锁',
        '事务B的插入语句等待A释放锁',
        'mysql察觉到死锁，让其中一个回滚，另一个继续执行',
    ]},
    {'RPC中的死锁':[
        '服务1和服务2都需要操作同一个表',
        '服务1开启事务，更新一条数据，RPC调用服务2，等待服务2返回结果',
        '服务2开启事务，更新同一条数据，等待服务1释放锁',
        '服务1等待超时，事务回滚',
        '服务2执行完毕，返回结果，但是RPC已经超时了',
    ]}
],
'存储引擎的 InnoDB 与 MyISAM':[
    '通常我们都是使用InnoDB，mysql默认使用的数据引擎也是innoDB',
    'innoDB和MyISAM都是使用B+树来实现索引，区别是innoDB的叶子节点保存的是主键，MyISAM保存了整行，这样索引占空间更大，但是查询更快，因为索引覆盖',
    'MyISAM维护了每张表的总行数，select count(*) 如果没有where会非常快',
    'innoDB支持行锁，线程安全有保证(重要)
    'innoDB支持数据库事务，在复杂业务中更好用(重要)',
],
'数据库索引的原理':[
    '用一些算法和数据结构达到搜索更快的目的',
    '散列表实现索引，直接使用hash搜索',
    '有序线性表实现索引，使用二分法查找',
    'B+树实现索引，按大小遍历到叶子节点',
],
'为什么要用 B-tree':[
    '散列表无法范围查找，也无法排序',
    '有序线性表更适合在内存，因为在磁盘插入不方便，也没有这么大的连续空间',
    'B+树可以范围查找，查询又快，而且叶子节点在磁盘中可以分开储存',
],
'聚集索引与非聚集索引的区别':[
    '聚集索引的排序方式与数据库中保持一致，非聚集索引则不一致',
    '聚集索引适合范围查询和返回，但是更新的效率慢',
    '非聚集索引适合范围查询，但是不适合范围返回，更新效率更高',
    'innoDB的主键索引是聚集索引，次级索引是非聚集索引，因为叶子节点存储了主键的值，所以要回表查询',
],
'limit 20000 加载很慢怎么解决':[
    '假如你真的需要20000数据，那么只能通过在排序列建立索引，或者把数据导入es，用es搜索引擎查询',
    '假如只是limit 20000,10,那么把20000的值先查出来，作为条件加入到where'
],
'选择合适的分布式主键方案':[
    '通过同一个redis获取自增主键',
    {'按雪花算法':[
        '定义每个分布式服务的每秒钟数据域',
        '比如用10位时间戳，6位的数据域，有10个分布式应用，每个10W个id可以用',
        '可以按业务再分数据域，让每个应用用不同的数据域即可',
        '并且在应用重启时，数据域id同步到zookeeper，避免重启后重复'
    ]}
],
'选择合适的数据存储方案':[
    'mysql，用mysql存储结构化、关联性强，持久化的数据',
    'mongoDB，用MongoDB存储非结构化的，持久化的数据',
    'redis，用redis存储热点、缓存、非持久化得数据',
    'elasticSearch，用es建立海量数据的索引，进行复杂和数据量很大的搜索服务',
],
'mongoDB的ObjectId 规则':[
    'mongo的_id是一个24位16进制字符串，其中包括时间戳，机器hash码，自增id'
],
'聊聊 MongoDB 使用场景':[
    '非结构化数据，如果一个业务每次产生的数据有多种字段，多种结构，那么需要mongo',
    '数组，如果一个数据的结构类型时数组，而且要查a[i]=?的数据，那么需要mongo',
],
'倒排索引':[
    '正排索引指我们为找到关键字在文档、数据表中的位置建立索引，索引的目的是快速在一个确定的文档中找到关键字的位置，在一张确定的表里找到某行数据',
    '倒排索引相反，是为了找到某个文档，由关键字找文档，由某个记录找到所在表',
    '关键字搜索就需要倒排索引，ES就需要倒排索引',
],
'ElasticSearch 使用场景':[
    '数据库有一张几亿数据的表，查询效率极低，但是插入数据不多，导入es中建立索引，每天同步数据建立索引用于查询',
    '数据库中有很多张表需要连表，但是不需要一张大表，连表效率极低，建立包含的数据导入es',
],
'一张自增表里面总共有7条数据，删除了最后2条数据，重启数据库，在插入一条，此时id是几':[
    'innoDB使用的AUTO_INCREMENT其实是select  max(id) +1 和内存中放好的AUTO_INCREMENT比较',
    '每次得到的id会放置在内存中，不会持久化',
    '所以重启数据库之后，内存中的AUTO_INCREMENT消失，得到的最大id是6'
],
'如何获取当前数据库版本':[
    'mysqladmin --version获取当前安装的数据库版本',
    'rpm -qa | grep mysql查询服务器中mysql安装版本'
],
'ACID是什么':[
    '原子性，一致性，隔离性，持久性',
    '原子性，指操作是不可分割的',
    '一致性，指一起成功，一起失败',
    '隔离性，指不会被其他影响',
    '持久性，指每次操作都是已经执行了，已经持久化到磁盘的',
],
'char和 varchar 的区别':[
    'char数组已经确定了大小',
    'varchar 并未确定大小，但是指定了最大值，在插入的时候确定，插入需要判断，时间换空间',
],
'float和 double 的区别':[
    '精度不同和数据范围不同',
    'double是64位，float是32位',
    'double在小数点后到15位',
    'float小数点后7位',
],
'mysql的内连接，左连接右连接有什区别':[
    'inner交集，left左边表的全集，right右边表的全集，outer并集'
],
'mysql索引是怎么实现的':[
    'B+树实现',
    'innoDB叶子节点主键id，聚集索引存行地址，MyISAM都是存整列数据',
    '非叶子节点存储索引值',
],
'怎么验证 mysql 的索引是否满足需求':[
    'explain查询结果',
    '看rows扫描行数是否太多',
    '看是否使用索引，是否使用了想要的索引',
    '索引长度确定使用了索引中的几个字段',
    {'看extra排序方式':[
        'extra是不是using index，using index condition，索引排序或者索引下推',
        '如果是Using where则表示没有使用索引排序，而是全表扫描',
        'Using temporary排序数量过大使用了临时表',
        'Using filesort无法使用索引，用文件排序'
    ]}
],
'MySQL 索引使用的注意事项':[
    '最左匹配规则',
    '索引是正序还是逆序，查询顺序是否符合',
    '索引长度是否过大，如果某些字段过大，就要截取',
    '索引是否太多，比如超过了一张表所有字段的1/3',
],
'说一下数据库的事务隔离':[
    'mysql四种隔离级别，rnw，rw，rr，Serializable',
    '读未提交，基本等于不隔离，在未提交时可以被其他事务读到更新结果，可能产生脏读问题，就是事务回滚了，读到错误数据',
    '读提交，提交后其他事务可读，避免了脏读',
    '可重复度，事务开启时保存快照，每行数据的更新都会保存事务tax_id，读取数据时回滚到比自己tax_id小的',
    '串行化，除了慢没有任何问题，没有脏读，没有幻读'
],
'mysql有那些琐':[
    {'库锁':[
        '锁住整个库不可更新，在迁库之类的特殊情况使用，一般是读锁',
    ]},
    {'表锁':[
        '可以用语句lock table  ··· read/write实现读锁或者写锁',
        '元数据锁，在curd操作是都会加全表读锁，在ddl操作时会自动添加全表的写锁，这样ddl就会与其他任何操作互斥'
    ]},
    {'行锁':[
        '行锁没有读锁，只有写锁',
        'select的时候不加行锁，所以与任意锁都不互斥',
        'update/delete都是加写锁，在执行前添加，在事务提交时释放'
    ]},
    {'间隙锁':[
        '作用是一定程度避免幻读',
        '对任意有唯一索引的字段加锁(包括主键)',
        '间隙锁之间不互斥，间隙锁与写锁互斥',
        '也就是说，加了间隙锁，这一段间隙不可以写和更新数据',
        '在每个涉及唯一索引的更新和删除加间隙锁'
    ]}
],
'mysql中有哪些乐观锁和悲观锁':[
    'mysql本身实现的锁全都是悲观锁'
],
'如何做 mysq| 的性能优化?':[
    'explain sql',
    '看情况加索引',
    '排序列在where条件内',
    '扫描行数越少越好',
    '按业务分库，不同的数据库实例执行',
    '太大的表要分库分表'
]
}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 