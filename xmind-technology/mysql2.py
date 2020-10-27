import xmind
from xmind.core.markerref import MarkerId
w = xmind.load("c:\\Users\\btr\\Desktop\\mysql2.xmind") 
s2=w.createSheet()
s2.setTitle("mysql2")
r2=s2.getRootTopic()
r2.setTitle("mysql2")


content={
'1.基础架构':[
    {'Server 层':[
        '连接器:管理连接，权限验证',
        '查询缓存：命中即返回',
        '分析器：词法，语法分析',
        '优化器：执行计划生成，索引选择',
        '执行器：操作引擎，返回结果'
    ]},
    '存储引擎层：存储数据，提供读写接囗，常用的存储引擎是 InnoDB'
],
'2.日志系统':[
    {'redo log':[
        'InnoDB引擎特有日志',
        'write pos:当前记录的位置，一边写一边后移',
        'checkpoint:当前要擦除的位置，边写边后移，后移前把记录更新到文件',
        'write pos和checkpoint间空着部分：记录新操作',
        '如write pos追上checkpoint，此时不再执行新更新，需把checkpoint推进',
        '物理日志：记录“在某个数据页上做了什么修改',
        'innodb_flush_log_at_trx_commit=1，每次事务的 redo log 都直接持久化到磁盘，保证异常重启后数据不丢失'
    ]},
    {'binlog':[
        'Server 层的日志',
        '逻辑日志：记录语句的原始逻辑',
        'sync_binlog=1,每次事务的 binlog 都持久化到磁盘,保证异常重启之后 binlog 不丢失'
    ]},
    {'两阶段提交':[
        'edo log 的写入：prepare 和 commit',
        {'update 语句':[
            '1.执行器:找引擎取 ID=2 这一行（ID 是主键），用树搜索这一行，数据页在内存中，返回；否则，先从磁盘读入内存，再返回',
            '2.执行器:拿到引擎给的行数据，把值加上 1，写入新行',
            '3.引擎：将新行更新到内存，写入redo log （prepare 状态），告知执行器可提交事务',
            '4.执行器：写入 binlog，并把 binlog 写入磁盘',
            '5.执行器：调用引擎提交事务接口，redo log 改成commit状态'
        ]}
    ]},
    'WAL（Write-Ahead Logging）：先写日志，再写磁盘',
    'crash-safe:有了 redo log，InnoDB 可以保证即使数据库发生异常重启，之前提交的记录都不会丢失'
    '应用：建备库，恢复某一时间点的数据 ：全量备份+binlog，'
],
'3.事务隔离':[
    '事务支持：引擎层实现',
    'ACID（Atomicity、Consistency、Isolation、Durability，即原子性、一致性、隔离性、持久性）',
    {'隔离性':[
        '读未提交:事务还没提交时，它做的变更就能被别的事务看到',
        {'读提交':[
            '事务提交后，它做的变更才会被其他事务看到',
            '每个SQL语句开始执行的时候创建的'
        ]},
        {'可重复读':[
            '事务执行过程中看到的数据，跟这个事务在启动时看到的数据一致',
            '事务启动时创建的视图，整个事务存在期间都用这个视图'
        ]},
        '串行化:对于同一行记录，“写”会加“写锁”，“读”会加“读锁”。读写锁冲突时，后访问的事务必须等前一个事务执行完成，才能继续执行'
    ]},
    {'事务隔离的实现':[
        '多版本并发控制（MVCC）：一条记录在系统中可存在多个版本',
        {'回滚日志':[
            '回滚段+当前值',
            '删除条件:当没有事务需要用到这些回滚日志时',
            '长事务：系统里面会存在很老的事务视图,要避免'
        ]}
    ]},
],
'4.索引':[
    {'索引模型':[
        {'哈希表':[
            '区间查询慢',
            '适用于等值查询'
        ]},
        {'有序数组':[
            '等值查询和范围查询较优',
            '查询用二分法，时间复杂度是 O(log(N))',
            '插入成本高',
            '适用于静态存储引'
        ]},
        {'搜索树':[
            '以二叉举例',
            '父节点左子树所有结点的值小于父节点的值，右子树所有结点的值大于父节点的值',
            '树高，访问磁盘频繁,因索引不止存在内存中，还要写到磁盘上'
        ]}
    ]},
    {'InnoDB 的索引模型':[
        {'B+ 树':[
            'N=1200,树高4,存1200的3次方,17 亿',
            '树根放内存，查值最多访问3次磁盘',
            '配合磁盘的读写特性，减少单次查询的磁盘访问次数'
        ]},
        '表:根据主键顺序以索引的形式存放的',
        '每一个索引在 InnoDB 里面对应一棵 B+ 树',
        {'类型':[
            {'主键索引':[
                '叶子节点存的是整行数据'
            ]},
            {'非主键索引':[
                '叶子节点内容是主键的值',
                '回表：回到主键索引树搜索'
            ]}
        ]},
        {'索引维护':[
            '页分裂:数据页满了，申请一个新的数据页，挪动部分数据过去',
            '合并：相邻两个页由于删除了数据，利用率很低后'
        ]},
        {'重建索引':[
            '创建一个新索引，数据按顺序插入，页面的利用率变高',
            '解决：因页分裂导致的数据页有空洞',
            '重建主键索引：alter table T engine=InnoDB'
        ]}
    ]},
    {'数据库设计的原则':[
        '尽量少地访问资源',
        '覆盖索引',
        '最左前缀原则',
        '索引下推'
    ]}
],
'5.全局锁和表锁':[
    {'全局锁':[
        '对整个数据库实例加锁,整个库处于只读状态',
        '语法:Flush tables with read lock (FTWRL)',
        {'阻塞':[
            '数据更新语句（数据的增删改）',
            '数据定义语句（包括建表、修改表结构等）',
            '更新类事务的提交语句'
        ]},
        '使用场景:全库逻辑备份',
        {'mysqldump':[
            '官方逻辑备份工具',
            '使用参数–single-transaction',
            '利用MVCC,导数据前启动一个事务，确保拿到一致性视图,过程中数据可正常更新'
        ]}
    ]},
    {'表级锁':[
        {'表锁':[
            '语法：lock tables … read/write',
            '限制别的线程的读写外，也限定了本线程的操作对象'
        ]},
        {'元数据锁（meta data lock，MDL)':[
            '不需显式使用，访问一个表的时会自动加上',
            '当对一个表做【增删改查】操作的时->加 MDL 读锁',
            '当要对表做【结构】变更操作的时->加 MDL 写锁',
            '读锁间不互斥,读写锁间、写锁间互斥',
            '注意：事务中的MDL锁，在语句执行时申请，事务提交后再释放',
            {'给小表加字段':[
                '查当前执行中的事务:information_schema 库的 innodb_trx 表',
                '如要要做DDL变更的表有长事务在执行，考虑暂停DDL，或者kill长事务',
                '热点表:alter table语句中设定等待时间，等待时间内拿不到写锁，不阻塞后面的业务语句'
            ]}
        ]}
    ]},
    {'行锁':[
        '引擎层由各个引擎自己实的',
        '两阶段锁协议:行锁在需要的时候加上，事务结束时释放',
        '事务如要锁多个行，把最可能造成锁冲突的锁后放',
        {'死锁':[
            '并发系统，线程间循环依赖,等待别的线程释放资源，进入无限等待状态',
            {'解决':[
                '1.进入等待，直到超时,超时时间设置：innodb_lock_wait_timeout',
                '2.死锁检测：发现死锁，主动回滚死锁链条中的某一事务，让其他事务可继续执行',
                '语法：innodb_deadlock_detect=on'
                '耗费CPU资源:每个新的被堵线程，判断是否自己加入导致死锁，时间复杂度O(n)',
                '3.控制并发度',
            ]}
        ]}
    ]}],
'6.事务,隔离':[
    {'begin/start transaction':[
        '第一个操作InnoDB表的语句，事务才真正启动',
        '一致性视图是在执行第一个快照读语句时创建的'
    ]},
    'start transaction with consistent snapshot:一致性视图在执行此语句时创建',
    {'transaction id':[
        '每个事务有一个唯一的事务 ID',
        '事务开始时向InnoDB的事务系统申请，顺序严格递增'
    ]},
    {'row trx_id':[
        '每行数据有多个版本',
        '事务更新数据时，生成一个新的数据版本,并把transaction id赋值给据版本的事务ID'
    ]},
    '低水位:数组里面事务ID的最小值',
    '高水位:系统里已经创建事务ID的最大值+ 1'
    '视图数组和高水位，就组成了当前事务的一致性视图（read-view）',
    {'一个数据版本，对于一个事务视图来说，除了自己的更新总是可见以外，有三种情况':[
        '版本未提交，不可见',
        '版本已提交，但是是在视图创建后提交的，不可见',
        '版本已提交，而且是在视图创建前提交的，可见'
    ]},
    '当前读:更新数据都是先读后写的，而这个读，只能读当前的值'
],
'7.普通索引和唯一索引':[
    {'查询过程':[
        '性能差距微乎其微',
        'InnoDB按数据页（默认16KB）为单位来读写数据',
    ]},
    {'更新过程':[
        {'change buffer':[
            '数据页在内存中没有，InnoDB将这些更新操作缓存在change buffer中（减少磁盘读）',
            {'merge 的执行流程':[
                '将change buffer中的操作应用到原数据页，得到最新结果的过程',
                '1.从磁盘读入数据页到内存',
                '2.从change buffer里找出此数据页的change buffer记录(可能多个），依次应用，得到新版数据页',
                '3.写redo log(包含数据变更和change buffer变更)',
                '此时，数据页和内存中change buffer对应的磁盘位置都还没有修改，属于脏页，之后各自刷回自己的物理数据'
            ]},
            {'触发条件':[
                '访问这个数据页',
                '系统的后台线程定期',
                '数据库正常关闭（shutdown）的过程中'
            ]},
            'change buffer用的是buffer pool里的内存，不能无限增大',
            '适用于写多读少的场景',
            '场景：账单类、日志类',
            'innodb_change_buffer_max_size=50:change buffer最多只能占用buffer pool的50%'
        ]},
        '从磁盘读入内存涉及随机IO访问，是数据库里面成本最高的操作之一'
        '唯一索引：先读再写，数据读入内存，不使用change buffer',
        '数据页在内存：性能差距微乎其微'
        '数据页在磁盘：唯一索引要从磁盘读入数据，而普通索引不用（更优）'
    ]},
    {'change buffer 和 redo log':[
        'redo log:节省的是随机写磁盘的 IO 消耗（转成顺序写）',
        'change buffer：节省的则是随机读磁盘的 IO 消耗'
    ]}
],
'8.MySQL选错索引':[
    {'优化器选择索引':[
        '扫描行数:扫描行数少，访问磁盘数据次数少，消耗CPU 资源少',
        '使用临时表',
        '是否排序'
    ]},
    '基数：一个索引上不同的值的个数，采样统计取得',
    'explain 命令查看预计扫描行数rows,与基数有关',
    {'处理':[
        '索引统计信息不准导致的：analyze table t'
        '采用 force index 强行选择一个索引',
        '修改语句，引导 MySQL 使用我们期望的索引',
        '新建一个更合适的索引，来提供给优化器做选择，或删掉误用的索引'
    ]}],
'9.给字符串字段加索引':[
    '完整索引:比较占用空间',
    {'前缀索引':[
        '定义好长度，可节省空间，又不增加太多查询成本',
        '区分度:select count(distinct left(email,4)）as L4 from SUser',
        '用不上覆盖索引对查询性能的优化'
    ]},
    '倒序存储:不支持范围查询',
    '使用 hash 字段:crc32(),不支持范围查询'
],
'10.MySQL抖动':[
    '脏页:内存跟磁盘数据页内容不一致的时候，内存页为脏页',
    '干净页:内存数据写入到磁盘，内存和磁盘数据页内容一致',
    '更新操作:平时执行很快，主要是写内存和日志',
    'MySQL偶尔抖动瞬间->可能在刷脏页（flush）',
    {'flush触发条件':[
        '1.redo log写满了,停止所有更新操作，将checkpoint往前推进',
        '2.系统内存不足：需要新的内存页时，要淘汰一些数据页，如果淘汰的是“脏页”，要先将脏页写到磁盘',
        '3.MySQL 认为系统“空闲”的时候',
        '4.MySQL 正常关闭时'
    ]},
    {'内存页三种状态':[
        'InnoDB 用缓冲池（buffer pool）管理内存'
        '1.还没有使用的',
        '2.使用了并且是干净页',
        '3.使用了并且是脏页'
    ]},
    {'刷脏页的控制策略':[
        {'刷盘速度':[
            'innodb_io_capacity:告诉InnoDB主机的IO能力',
            '建议设置成磁盘的IOPS'
        ]},
        {'刷盘条件':[
            '脏页比例(不要让它经常接近 75%)',
            'redo log 写盘速度'
        ]},
        {'刷盘方式':[
            'innodb_flush_neighbors=0：只刷自己，不带邻居'
        ]}
    ]}
],
'11.数据库表的空间回收':[
    '现象：表数据删掉一半，表文件大小不变',
    '一个InnoDB表包含两部分:表结构定义+数据',
    {'innodb_file_per_table':[
        'On:表数据存储在以.ibd为后缀的文件中,drop table,直接删除文件',
        'OFF:表的数据放在系统共享表空间，跟数据字典一起,表删掉，空间不会回收'
    ]},
    {'数据删除流程':[
        '数据页的复用跟记录的复用',
        'delete命令:把记录的位置，或数据页标记为了“可复用”，磁盘文件大小不会变',
        'insert命令：随机插入，可能造成索引的数据页分裂',
        'update命令：删除一个旧的值，再插入一个新值,会造成空洞'
        '经过大量增删改的表->存在空洞的->把空洞去掉->收缩表空间(重建表)'
    ]},
    {'重建表':[
        {'alter table A engine=InnoDB':[
            '转存数据、交换表名、删除旧表',
            '语句在启动时获取MDL写锁，真正拷贝数据前退化成读锁'
        ]},
        {'退化成读锁原因':[
            '实现Online DDL',
            '不直接解锁,禁止其他线程对这个表同时做 DDL'
        ]},
        {'Online DDL':[
            '最耗时是拷贝数据到临时表',
            '如个步骤的执行期间可接受增删改操作',
            '对整个过程来说，锁的时间很短，认为是Online的'
        ]}

    ]}
],
'12.count(*)':[
    {'查询表的总行数':[
        'MyISAM:count(*):快，但是不支持事务',
        'show table status:快，不准确(估算出来的)',
        'InnoDB:count(*)遍历全表，结果准确但有性能问题',
    ]},
    {'其它方法':[
        '缓存系统保存计数:丢失更新+逻辑上不精确问题（）',
        '两个系统，不支持分布式事务，无法拿到一致性视图',
        '数据库保存计数：利用事务保证逻辑上的精确'
    ]},
    {'不同的count对比':[
        'count(主键 id):InnoDB引擎遍历整张表,把每一行的id值取出返回,server层拿到id，判断非空，按行累加',
        'count(1)：InnoDB 引擎遍历整张表，不取值返回，server层对于返回的每一行，放一个数字“1”，判断非空，按行累加',
        'count(字段):类count(主键 id)',
        'count(*)：不会把全部字段取出，专门做了优化，不取值，count(*) 肯定不是 null，按行累加',
        'count(1)>count(主键 id):引擎返回 id 会涉及到解析数据行，以及拷贝字段值的操作',
        '效率排序：count(字段)<count(主键 id)<count(1)≈count(*)'
    ]}
],
'13.日志和索引相关问题':[
    '两阶段提交简图：写redo log(prepare)--A--->bingo--B--->redo log(commit)',
    'A状态：发生crash，此时 binlog 还没写，redo log 也没提交，崩溃恢复时，事务会回滚',
    {'B状态':[
        '如redo log里事务是完整的(有commit标识）,直接提交',
        {'如redo log里事务有完整prepare，判断事务binlog是否完整':[
            '是，则提交事务（保证主备库一致）',
            '否则，回滚事务'
        ]}
    ]},
    'redo log 和 binlog通过XID关联',
    {'一个事务的binlog 完整格式':[
        'statement格式的，最后有 COMMIT',
        'row格式的，最后有一个 XID event'
    ]},
    'binlog:不能支持崩溃恢复(没有能力恢复“数据页”)',
    'redo log:系统是 crash-safe,但无法归档（mysql高可用依赖binlogo）',
    '数据落盘与redo log无关：它没有记录数据页的完整数据，没有能力更新磁盘数据页',
    'redo log buffe：一块内存，用来存 redo logo日志的,执行commit 语句，把它写入redo log文件'
],
'14.order by':[
    {'排序使用空间(内存or磁盘）':[
        '排序所需内存',
        'sort_buffer_size：MySQL 为排序开辟的内存（sort_buffer）的大小',
        'max_length_for_sort_data:控制排序行数据长度,如单行长度超过此值，只写排序字段和id'
    ]},
    {'外部排序':[
        '使用归并算法',
        '将需排序数据分成n份，每份单独排序后存入临时文件',
        '最后将n份有序文件合并成一个有序的大文件'
    ]},
    {'全字段排序':[
        '流程：xx索引->表T主键索引->sort_buffer->sort_buffer排序->结果集',
        '内存大，优先选择此算法',
        '字段都放到sort_buffer中，排序后直接从内存返回，不再回表'
    ]},
    {'rowid排序':[
        '流程：xx索引->表T主键索引->sort_buffer->sort_buffer排序->表T主键索引->结果集',
        '归并算法和优先队列排序算法',
        '内存小，影响排序效率,使用此算法',
        '一次可以排序更多行，但需要回表(造成磁盘读)',
        '对于内存表，回表只是根据数据行位置得到数据（不访问磁盘）,优化器优选rowid排序'
    ]},
    'order by语句,未必都要排序，如数据是有序的，直接从索引上取数据，回表，组结果集'
],
'15.正确地显示随机消息':[
    'MySQL对临时表排序的执行过程',
    '分析sql:select word from words order by rand() limit 3',
    {'order by rand()':[
        '使用Using temporary（内存临时表）:排序时候使用rowid排序方法',
        'tmp_table_size:限制了内存临时表大小，默认值16M',
        '如临时表超过了tmp_table_size,内存临时表就会转成磁盘临时表',
        '使用Using filesort（sort_buffer排序）'
    ]},
    {'rowid':[
        'rowid：每个引擎用来唯一标识数据行的信息',
        '对有主键的 InnoDB 表，rowid 就是主键 ID',
        '对没有主键的 InnoDB 表，rowid 由系统生成的',
        'MEMORY引擎不是索引组织表,可认为它是一个数组,rowid是数组的下标'
    ]}
],
'explain':[
    {'Extra 字段':[
        'Using filesort:需要排序，MySQL给每个线程分配一块内存(sort_buffer)用于排序',
        'Using index:使用覆盖索引',
        'Using temporary:需要使用临时表',
        'Using index:使用了覆盖索引'
    ]}
    ],
'16.SQL语句逻辑相同，性能却差异巨大':[
    {'1.条件字段函数操作':[
        'B+树提供的快速定位能力，源于同一层兄弟节点的有序性',
        '对索引字段做函数操作，可能破坏索引值的有序性，导致优化器放弃走树搜索功能'
    ]},
    {'2.隐式类型转换':[
        '类型转换：如字段类型是varchar(32)，输入参数是整型',
        '需将字符串->数字，触发原则：对索引字段做函数操作，优化器放弃走树搜索功能'
    ]},
    {'3.隐式字符编码转换':[
        '两表字符集不同，一个utf8，一个utf8mb4，表连接查询时用不上关联字段的索引',
        'utf8mb4是utf8的超集,自动类型转换时，按数据长度增加的方向进行转换,utf8 字符串->utf8mb4字符集',
        'CONVERT() 函数:把输入的字符串转成 utf8mb4 字符集。触发原则：对索引字段做函数操作，优化器会放弃走树搜索功能',
        '连接过程中:尽量在驱动表的索引字段上加函数操作'
    ]}
],
'17.只查一行的语句，也执行这么慢':[
    '表锁、行锁和一致性读',
    {'1.查询长时间不返回':[
        '大概率是表 t 被锁住了,show processlist 命令，看看当前语句处于什么状态',
        {'Waiting for table metadata lock':[
            '等 MDL 锁,有一个线程正在表t上请求或者持有MDL写锁',
            '查询sys.schema_table_lock_waits表，找出造成阻塞的process id，把这个连接用 kill 命令断开',
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
        {'直接读慢，lock in share mode快':[
            '一致性读，从当前数据开始，依次执行undo log',
            '当前读，直接显示当前数据'
        ]}
    ]}
],
'18.幻读':[
    {'幻读':[
        '一个事务在前后两次查询同一个范围的时候，后一次查询看到了前一次查询没有看到的行',
        '可重复读隔离级别下,普通查询是快照读,不会看到别的事务插入的数据, 幻读在“当前读”下才会出现',
        '幻读仅指新插入的'
    ]},
    {'间隙锁 (Gap Lock)':[
        '锁的就是两个值之间的空隙，InnoDB为了解决幻读问题引入的新锁',
        '间隙锁间不存在冲突关系',
        '跟间隙锁存在冲突关系的，是“往这个间隙中插入一个记录”的操作',
        '间隙锁和行锁合称next-key lock（前开后闭区间）',
        '间隙锁的引入，可能会导致同样语句锁住更大范围，是影响并发度的'
        '在可重复读隔离级别下才生效的，读提交隔离条件下是没有间隙锁的'
    ]},
    '读提交隔离条件下,需要把binlog 格式设置为 row'
],
'19.只改一行的语句，锁这么多':[
    {'规则':[
        '两个“原则”、两个“优化”和一个“bug”',
        '原则 1：加锁的基本单位是 next-key lock(前开后闭区间)',
        '原则 2：查找过程中访问到的对象才会加锁,锁加在列上，即索引树上',
        '优化 1：索引上的等值查询，给唯一索引加锁的时候，next-key lock 退化为行锁',
        '优化 2：索引上的等值查询，向右遍历时且最后一个值不满足等值条件的时候，next-key lock 退化为间隙锁',
        '一个 bug：唯一索引上的范围查询会访问到不满足条件的第一个值为止',
        'lock in share mode只锁覆盖索引,for update会顺便给主键索引上满足条件的行加行锁'
    ]},
    '可重复读隔离级别遵守两阶段锁协议，所有加锁的资源，都是在事务提交或者回滚的时候才释放的',
    ''
],
'20.“饮鸩止渴”提高性能的方法':[
    {'短连接风暴':[
        '先处理掉那些占着连接但是不工作的线程',
        '减少连接过程的消耗:跳过权限验证'
    ]},
    {'慢查询性能问题':[
        '索引没有设计好:直接执行alter table语句(创建索引支持Online DDL)的',
        'SQL 语句没写好：查询重写query_rewrite 功能',
        'MySQL 选错了索引：紧急给这个语句加上 force index'
    ]},
    {'QPS 突增问题':[
        '查询重写功能，把压力最大的 SQL 语句直接重写成"select 1"返回'
    ]}
],
'21.保证数据不丢':[
    'binlog cache:系统分配内存，每个线程一个（binlog_cache_size控制单线程内binlog cache大小），如超过，存到磁盘',
    {'binlog 的写入机制':[
        '事务执行过程，先把日志写到 binlog cache',
        '事务提交时，把 binlog cache 写到 binlog 中'
        '注意：一个事务的 binlog 不能被拆开'
    ]},
    'binlog 写盘状态:binlog cache-----write---->binlogo files----fsync---->disk',
    'write:把日志写入到文件系统的 page cache(没有把数据持久化到磁盘),速度快',
    'fsync:数据持久化到磁盘(占磁盘的 IOPS)',
    {'write和fsync的时机，由参数 sync_binlog 控制':[
        'sync_binlog=0 : 每次提交事务都只 write，不 fsync',
        'sync_binlog=1 : 每次提交事务都会执行 fsync',
        'sync_binlog=N(N>1) : 每次提交事务都 write，累积 N 个事务后才 fsync',
        'sync_binlog=N的风险：如果主机发生异常重启，会丢失最近 N 个事务的 binlog 日志'
    ]},
    {'redo log写入机制':[
        {'MySQL redo log 存储状态':[
            '1.存在 redo log buffer 中，物理上是在 MySQL 进程内存中',
            '2.写到磁盘 (write)，但是没有持久化（fsync)，物理上是在文件系统的 page cache 里面',
            '3.持久化到磁盘，对应的是 hard disk'
        ]},
        {'redo log 的写入策略，InnoDB 提供了 innodb_flush_log_at_trx_commit 参数':[
            '0 : 每次事务提交时都只是把 redo log 留在 redo log buffer 中',
            '1 : 每次事务提交时都将 redo log 直接持久化到磁盘',
            '2 : 每次事务提交时都只是把 redo log 写到 page cache'
        ]},
        'InnoDB有一个后台线程，每隔1秒,把redo log buffer中的日志，调用write写到文件系统的page cache，然后调用 fsync 持久化到磁盘',
        'MySQL“双 1”配置:sync_binlog 和 innodb_flush_log_at_trx_commit都为1，即一个事务完整提交前，需要等待两次刷盘，一次是 redo log（prepare 阶段），一次是 binlog'
        ''
    ]},
    '日志逻辑序列号（log sequence number，LSN）:单调递增的，用来对应 redo log 的一个个写入点。每次写入长度为 length 的 redo log， LSN 的值就会加上 length',
    {'两阶段提交细化':[
        '1.redo log prepare:write',
        '2.binlog:write',
        '3.redo log prepare:fsync',
        '4.binlog:fsync',
        '5.redo log commit:write'
    ]},
    '并发更新场景下，第一个事务写完 redo log buffer 以后，fsync 越晚调用，组员可能越多，节约 IOPS 的效果就越好',
    {'MySQL出现IO性能瓶颈':[
        '1.设置binlog_group_commit_sync_delay和binlog_group_commit_sync_no_delay_count参数，减少binlog的写盘次数',
        '基于“额外的故意等待”来实现，可能会增加语句响应时间，但没有丢失数据的风险',
        '2.sync_binlog设置为大于 1 的值（常见100~1000),风险是主机掉电时会丢 binlog 日志',
        '3.innodb_flush_log_at_trx_commit设置为2,风险是主机掉电的时候会丢数据'
    ]}
],
'22.主备一致':[
    {'备库设置成只读（readonly）模式':[
        '1.有时运营类的查询语句会被放到备库上去查，防止误操作',
        '2.防止切换逻辑有bug，如切换过程出现双写，造成主备不一致',
        '3.可用readonly状态，判断节点角色',
        '注：readonly对超级 (super) 权限用户是无效的，同步更新的线程拥有超级权限'
    ]},
    '备库B：io_thread--->relay log--->sql_thread',
    '备库B 跟主库A 之间维持了一个长连接。主库A 内部有一个线程，专门用于服务备库B 的这个长连接',
    {'一个事务日志同步过程':[
        '1.备库 B 通过 change master 命令，设置主库 A 的 IP、端口、用户名、密码，以及要从哪个位置(包含文件名和日志偏移量)开始请求 binlog',
        '2.备库 B 执行 start slave 命令，会启动两个线程:io_thread(负责与主库建立连接)和 sql_thread ',
        '3.主库 A 校验完用户名、密码后，开始按照备库 B 传过来的位置，从本地读取 binlog，发给 B',
        '4.备库 B 拿到 binlog 后，写到中转日志（relay log）,sql_thread 读取中转日志，解析出日志里的命令，并执行'
    ]},
    {'binlog 的三种格式':[
        'binlog_format=statement : binlog 里面记录的就是 SQL 语句的原文',
        'binlog_format=row : 很占空间，记录了真实删除行的主键 id，恢复数据方便',
        'binlog_format=mixed :两种格式都有，确定行数的用statement格式的，其余用row的'
    ]},
    {'循环复制的问题':[
        '备库接到 binlog 并在重放的过程中，生成与原binlog的server id相同的新的binlog',
        '每个库在收到日志后，先判断server id，跟自己的相同，直接丢弃这个日志'
    ]}
],
'23.保证高可用':[
    {'主备延迟':[
        'show slave status 命令,seconds_behind_master显示当前备库延迟秒数',
        '网络正常时，日志从主库传给备库所需时间很短',
        '主备延迟的主要:备库接收完 binlog 和执行完这个事务之间的时间差',
        '表现:备库消费中转日志（relay log）的速度，比主库生产binlog慢'
    ]},
    {'主备延迟的来源':[
        '1.备库所在机器性能比主库差:更新请求对IOPS的压力，在主库和备库上是无差别的',
        '2.备库的压力大:备库上的查询耗费了大量CPU资源，影响同步速度',
        '解决：2.1一主多从，分担读的压力',
        '2.2通过 binlog 输出到外部系统(如Hadoop)，让外部系统提供统计类查询',
        '3.大事务:一次性地delete删除太多数据/大表 DDL',
        '4.备库的并行复制能力'
    ]},
    {'主备切换过程（可靠性优先策略）':[
        '1.判断备库 B 的 seconds_behind_master，如果小于5 秒，继续下一步，否则持续重试',
        '2.把主库 A 改成只读状态（readonly 设置为 true）',
        '3.判断备库 B 的 seconds_behind_master，直到变成 0 为止',
        '4.把备库 B 改成可读写状态（readonly 设置为 false）',
        '5.把业务请求切到备库 B'
    ]}
],
'24.备库延迟好几个小时':[
    'sql_thread 执行中转日志,改为多线程复制策略',
    '1.按库分发策略',
    '2.commit状态，即同一组里提交的事务不会更新同一行（利用redo log组提交优化）',
    '3.rego log于prepare与commit状态的事务，在备库执行时可并行',
    '4.按行分发策略'
],
'25.主库出问题了，从库怎么办':[
    '一主多从的切换正确性',
    '基于位点的主备切换:需主动跳过错误',
    {'GTID':[
        '全局事务ID，一个事务在提交的时候生成，是事务的唯一标识',
        'GTID=server_uuid:gno',
        'server_uuid:一个实例第一次启动时自动生成的，一个全局唯一的值',
        'gno:一个整数，初始值是 1，每次提交事务的时候分配给这个事务，并加 1',
        '启动一个 MySQL 实例的时候，加上参数gtid_mode=on和enforce_gtid_consistency=on'
    ]},
    {'基于 GTID 的主备切换(备库 B 要设置为新主库 A’的从库)':[
        '1.实例 B 指定主库 A’，基于主备协议建立连接',
        '2.实例 B 把 set_b 发给主库 A’',
        '3.实例 A’算出set_a与set_b差集（存在于set_a，不存在set_b的GTID集合）,判断 A’本地是否包含了差集需要的所有binlog事务',
        'a.不包含：A’已经把实例 B 需要的 binlog 删掉了，直接返回错误',
        'b.全部包含：A’从自己的 binlog 文件里，找出第一个不在set_b的事务，发给B',
        '4.之后从这个事务开始，往后读文件，按顺序取binlog发给B去执行'
    ]}
],
'26.读写分离的坑':[
    '一主多从的结构，其实就是读写分离的基本结构',
    {'客户端直连':[
        '整体架构简单，排查问题方便',
        '要了解后端部署细节，在出现主备切换、库迁移等操作时，客户端会感知到，并需调整数据库连接信息',
        '一般伴随一个负责管理后端的组件（如 Zookeeper），尽量让业务端只专注业务逻辑开发'
    ]},
    {'带proxy的读写分离架构':[
        '对客户端友好',
        '后端维护团队的要求高，且proxy也需要有高可用架构'
    ]},
    {'处理过期读的方案':[
        '强制走主库:将查询请求做分类',
        'Sleep ',
        '判断主备无延迟方案:超时放弃,并转到主库查询',
        '等主库位点方案',
        'GTID 方案'
    ]}
],
'27.如何判断一个数据库是不是出问题了':[
    '1.select 1:有返回:进程还在',
    'InnoDB中，innodb_thread_concurrency通常取值64~128，机器CPU 核有限，减少上下文切换',
    {'并发连接和并发查询':[
        '并发连接：show processlist结果里的几千个连接，会占用一些内存',
        '并发查询：当前正在执行的语句，CPU 杀手',
        '线程进入锁等待后，并发线程的计数减一',
    ]},
    '2.查表判断:检测 InnoDB 并发线程数过多导致的系统不可用情况',
    '3.更新判断:判断binlog内存是否正常，但基于外部检测，判断慢',
    '4.内部统计:5.6版本后提供performance_schema 库，在file_summary_by_event_name 表里统计每次IO请求的时间',

],
'28.误删数据后恢复':[
    '1.误删行：Flashback 工具，修改binlog（格式为row）内容，拿回原库执行',
    'delete 全表很慢，会生成回滚日志、写 redo、写 binlog。从性能考虑，优先使用truncate table或drop table',
    '2.误删库/表:全量备份+增量日志',
    '加速的方法：在用备份恢复出临时实例之后，将临时实例设置成线上备库的从库',
    '3.rm 删除数据：备份跨机房，或者最好是跨城市保存',
    {'预防误删库/表':[
        '1.账号分离:开发DML权限，运维平时只读，必要时才更新',
        '2.制定操作规范：删表先改名，再在平台操作'
    ]}
],
'29.kill不掉的语句':[
    {'MySQL中的kill命令':[
        'kill query + 线程 id：终止线程中正在执行的语句',
        'kill connection + 线程 id：断开线程的连接'
    ]},
    {'执行kill query thread_id_B 时':[
        '1.把session B运行状态改成THD::KILL_QUERY',
        '2.给session B执行线程发一个信号'
    ]},
    {'kill 无效':[
        {'1.线程没有执行到判断线程状态的逻辑':[
            '等锁，未进入InnoDB',
            'IO压力大，读写IO的函数无法返回，导致不能及时判断线程状态'
        ]},
        {'2.终止逻辑耗时较长':[
            '超大事务执行期间被kill',
            '大查询回滚:删除临时文件需要等待 IO 资源',
            'DDL命令执行到最后阶段被kill:删除中间过程的临时文件,需要等待 IO 资源'
        ]}
    ]},
    '发送kill命令的客户端，不会强行停止目标线程的执行，只是设置了状态，并唤醒对应的线程',
    '被kill线程，需执行到判断状态的“埋点”，才会开始进入终止逻辑阶段(需要耗费时间)'
    {'于客户端误解':[
        '1.如果库里面的表多，连接会慢:不是服务端慢，而是客户端慢',
        '客户端在连接成功后，需多做一些操作：构建一个本地的哈希表（表多，耗时）'
        '2.–quick参数：让客户端变得更快,',
        {'MySQL客户端接收服务端返回结果':[
            '本地缓存，在本地开一片内存',
            '不缓存，读一个处理一个'
        ]},
        '加–quick，使用不缓存方式，如本地处理慢，会导致服务端发送结果被阻塞，让服务端变慢'
    ]}
]
    
}

for key in content:
    t1 = r2.addSubTopic()
    t1.setTopicHyperlink(s2.getID()) 
    list=key.split(":")
    t1.setTitle(list[0])
    if len(list)>1:
        t1.setPlainNotes(list[1]) 
    # print(content[key])
    for i in content[key]:
        # print(type(i))
        if(type(i).__name__=='dict'):
            for t in i:
                t2 = t1.addSubTopic()
                t2.setTopicHyperlink(t1.getID()) 
                t2.setTitle(t)
                for j in i[t]:
                    #print(j)
                    if(type(j).__name__=='dict'):
                        for h in j:
                            t3 = t2.addSubTopic()
                            t3.setTopicHyperlink(t2.getID()) 
                            t3.setTitle(h) 
                            for m in j[h]:
                                if(type(m).__name__=='dict'):
                                    for n in m:
                                        t4 = t3.addSubTopic()
                                        t4.setTitle(n) 
                                        for l in m[n]:
                                            if(type(l).__name__=='dict'):
                                                for k in l:
                                                    t5 = t4.addSubTopic()       
                                                    t5.setTitle(k)
                                                    for p in l[k]:
                                                        if(type(p).__name__=='dict'):
                                                            for u in p:
                                                                t6 = t5.addSubTopic()
                                                                t6.setTitle(u)
                                                                for y in p[u]:
                                                                    if(type(y).__name__=='dict'):
                                                                        for a in y:
                                                                            t7 = t6.addSubTopic()
                                                                            t7.setTitle(a)
                                                                            for b in y[a]:
                                                                                t8 = t7.addSubTopic()
                                                                                t8.setTitle(b)
                                                                    else:
                                                                        t7 = t6.addSubTopic()
                                                                        t7.setTopicHyperlink(t2.getID()) 
                                                                        t7.setTitle(y)              
                                                        else:
                                                            t6 = t5.addSubTopic()
                                                            t6.setTopicHyperlink(t2.getID()) 
                                                            t6.setTitle(p)                                                        
                                            else:
                                                t5 = t4.addSubTopic()
                                                t5.setTopicHyperlink(t3.getID()) 
                                                t5.setTitle(l) 
                                else:
                                    t4 = t3.addSubTopic()
                                    t4.setTopicHyperlink(t3.getID()) 
                                    t4.setTitle(m) 
                    else:
                        t3 = t2.addSubTopic()
                        t3.setTopicHyperlink(t2.getID()) 
                        t3.setTitle(j) 
        else:
            t2 = t1.addSubTopic()
            t2.setTopicHyperlink(t1.getID()) 
            t2.setTitle(i) 



topics=r2.getSubTopics()
for topic in topics:
    topic.addMarker(MarkerId.starBlue)

xmind.save(w,"c:\\Users\\btr\\Desktop\\mysql2.xmind") 