import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="mysql"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("join")
r2=s2.getRootTopic()
r2.setTitle("join")


content={
'join基础':[
    'inner交集，left左边表的全集，right右边表的全集，outer并集',
    {'驱动表':[
        '主动发起查询的表',
    ]},
    {'被驱动表':[
        '根据on条件被动被查询的表',
    ]},
    '驱动表的行数 N,被驱动表的行数 M',
    '两个表按照各自的条件过滤后，计算参与join的字段总数据量，数据量小的表，应作驱动表'
],
'被驱动表有索引且被使用了':[
    'NLJ 算法',
    '驱动表走全表扫描，被驱动表走树搜索',
    '扫描行业：N+M',
    '近似复杂度: N + N*2*log2M',
    'N小时，复杂度少，驱动表选择小表'
],
'被驱动表无索引或无法使用索引':[
    {'BNL 算法':[
        '1.可能多次扫描被驱动表，占用磁盘 IO 资源',
        '2.判断 join 条件需要执行 M*N 次对比,大表会占用非常多CPU资源',
        '3.可能导致 Buffer Pool 的热数据被淘汰，影响内存命中率'
    ]},
    '借助join_buffer，驱动表全部读入',
    '扫描行数: N+λ*N*M (λ*N分段数)',
    '内存判断:N*M 次',
    'N小时，扫描行数少，驱动表选择小表',
    'λ小时，分段数小，则join_buffer_size 大（一次放入的行多，用join_buffer_size控制）'
],
'优化':[
    {'MRR算法':[
        '顺序读盘，查询语句在索引a上做一个范围查询',
        '得到足够多主键id,排序以后，再去主键索引查数据'
    ]},
    {'BKA算法':[
        '对NLJ算法的优化,暂存驱动表的数据到join_buffer，依赖于 MRR'
    ]}
]
}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 