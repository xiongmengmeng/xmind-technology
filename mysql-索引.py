import xmind
from xmind.core.markerref import MarkerId
w = xmind.load("c:\\Users\\btr\\Desktop\\mysql.xmind") 
s2=w.createSheet()
s2.setTitle("mysql-索引")
r2=s2.getRootTopic()
r2.setTitle("mysql-索引")


content={
'1.索引':[
    {'索引模型':[
        {'哈希表':[
            '区间查询慢',
            '适用等值查询'
        ]},
        {'有序数组':[
            '等值查询和范围查询较优',
            '查询用二分法，时间复杂度是 O(log(N))',
            '插入成本高',
            '适用静态存储引擎'
        ]},
        {'搜索树':[
            '以二叉举例',
            '父左子树结点值小于父节点值，右子树结点值大于父节点值',
            '树太高，访问磁盘频繁（索引不止在内存，还在磁盘）'
        ]}
    ]},
    {'InnoDB 的索引模型':[
        {'B+ 树':[
            'N=1200,树高4,存1200的3次方,17 亿',
            '树根放内存，查值最多访问3次磁盘',
            '配合磁盘特性，减少单次查询的磁盘访问数'
        ]},
        '表:根据主键顺序以索引的形式存放',
        '每一个索引在 InnoDB 里对应一棵 B+ 树',
        {'类型':[
            {'主键索引':[
                '叶子节点存整行数据'
            ]},
            {'非主键索引':[
                '叶子节点存主键的值',
                '回表：回到主键索引树搜索'
            ]}
        ]},
        {'索引维护':[
            '页分裂：数据页满了，申请一个新的数据页，挪动部分数据过去',
            '页合并：相邻两个页由于删除了数据，利用率很低后'
        ]},
        {'重建索引':[
            '建一个新索引，数据按顺序插入，页面利用率变高',
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
'2.字符串字段加索引':[
    '完整索引:比较占用空间',
    {'前缀索引':[
        '定义好长度，可节省空间，又不增加太多查询成本',
        '区分度:select count(distinct left(email,4)）as L4 from SUser',
        '用不上覆盖索引对查询性能的优化'
    ]},
    '倒序存储:不支持范围查询',
    '使用 hash 字段:crc32(),不支持范围查询'
],
'3.普通索引vs唯一索引':[
    {'查询过程':[
        '性能差距微乎其微',
        'InnoDB按数据页（默认16KB）为单位来读写数据',
    ]},
    {'更新过程':[
        {'change buffer':[
            '数据页在内存中没有，InnoDB将这些更新操作缓存在change buffer中（减少磁盘读）',
            {'merge':[
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
        '从磁盘读入内存涉及随机IO访问，是数据库里面成本最高的操作之一',
        '唯一索引：先读再写，数据读入内存，不使用change buffer',
        '数据页在内存：性能差距微乎其微',
        '数据页在磁盘：唯一索引要从磁盘读入数据，而普通索引不用（更优）'
    ]},
    {'change buffer 和 redo log':[
        'redo log:节省的是随机写磁盘的 IO 消耗（转成顺序写）',
        'change buffer：节省的则是随机读磁盘的 IO 消耗'
    ]}
],
'4.索引问题1-选错索引':[
    {'优化器选择索引':[
        '扫描行数:扫描行数少，访问磁盘数据次数少，消耗CPU 资源少',
        '使用临时表',
        '是否排序'
    ]},
    '基数：一个索引上不同的值的个数，采样统计取得',
    'explain 命令查看预计扫描行数rows,与基数有关',
    {'处理':[
        '索引统计信息不准：analyze table t',
        '采用 force index 强行选择一个索引',
        '修改语句，引导 MySQL 使用我们期望索引',
        '新建一个更合适的索引，来提供给优化器做选择，或删掉误用的索引'
    ]}],
'5.索引问题2-函数':[
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
        '自动类型转换时，按数据长度增加的方向进行转换,utf8 字符串->utf8mb4字符集',
        'CONVERT() 函数:字符串->utf8mb4 字符集。触发原则：对索引字段做函数操作，优化器会放弃走树搜索功能',
        '连接过程中:尽量在驱动表的索引字段上加函数操作'
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

xmind.save(w,"c:\\Users\\btr\\Desktop\\mysql.xmind") 