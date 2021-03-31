import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="mysql"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("索引模型")
r2=s2.getRootTopic()
r2.setTitle("索引模型")


content={

'索引模型':[
    '用一些算法和数据结构达到搜索更快的目的',
    {'哈希表':[
        '使用hash搜索，适用等值查询',
        '范围查询慢,不支持模糊查询'
    ]},
    {'有序数组':[
        '使用二分法查找，时间复杂度是 O(log(N))',
        '等值查询和范围查询较优',
        '插入成本高',
        '更适合在内存，因为在磁盘插入不方便，也没有这么大的连续空间'
    ]},
    {'搜索树':[
        '以二叉举例',
        '父左子树结点值小于父节点值，右子树结点值大于父节点值',
        '树太高，访问磁盘频繁（索引不止在内存，还在磁盘）',
        {'B+树':[
            '多路平衡查找树,查询从根节点出发,查找到叶子节点,同层级的节点间有指针相互链接，是有序的'
        ]}
    ]}
],
'InnoDB 的索引模型':[
    '表:根据主键顺序以索引的形式存放',
    '每一个索引在 InnoDB 里对应一棵 B+ 树',
    {'类型':[
        {'主键索引(聚簇索引)':[
            '叶子节点存整行数据'
        ]},
        {'非主键索引(非聚簇索引)':[
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
],  
}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 