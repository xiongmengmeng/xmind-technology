import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="mysql"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("索引对比和问题")
r2=s2.getRootTopic()
r2.setTitle("索引对比和问题")


content={

'普通索引vs唯一索引':[
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
'索引问题1-选错索引':[
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
'索引问题2-函数':[
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

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 