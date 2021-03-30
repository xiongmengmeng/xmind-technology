import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="mysql"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("索引简介")
r2=s2.getRootTopic()
r2.setTitle("索引简介")


content={
'数据库设计的原则':[
    '尽量少地访问资源',
    '覆盖索引',
    '最左前缀原则',
    '索引下推'
],
'索引模型':[
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
],
'InnoDB 的索引模型':[
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
        '页分裂：数据页满了，申请一个新的数据页，挪部分数据过去',
        '页合并：相邻两个页由于删除了数据，利用率很低后'
    ]},
    {'重建索引':[
        '建一个新索引，数据按顺序插入，页面利用率变高',
        '解决：因页分裂导致的数据页有空洞',
        '重建主键索引：alter table T engine=InnoDB'
    ]}
],
'字符串字段加索引':[
    '完整索引:比较占用空间',
    {'前缀索引':[
        '定义好长度，可节省空间，又不增加太多查询成本',
        '区分度:select count(distinct left(email,4)）as L4 from SUser',
        '用不上覆盖索引对查询性能的优化'
    ]},
    '倒序存储:不支持范围查询',
    '使用 hash 字段:crc32(),不支持范围查询'
]
}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 