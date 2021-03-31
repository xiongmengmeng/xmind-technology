import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="mysql"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("sql分析")
r2=s2.getRootTopic()
r2.setTitle("sql分析")


content={
'explain':[
    {'possible_keys':[
        '可以使用的索引'
    ]},
    {'key':[
        '使用的索引'
    ]},
    {'rows':[
        '查询扫描行数'
    ]},
    {'extra':[
        'Using index:使用了覆盖索引,不用回表',
        'Using Where:全表扫描，或者使用了索引但要回表',
        'Using filesort:需要排序，但无法利用索引完成排序，给线程分配一块内存(sort_buffer)用于排序',
        'Using temporary:使用临时表来保存中间结果，常见于排序OrderBy 和分组查询GroupBy',
        'Using Join Buffer:使用了连接缓存（join太多表，配置文件里面的JoinBuffer值可调大一点',
        'Using MRR:用上了 MRR 优化'
    ]},
    {'分析':[
        '看是否使用索引：是否使用了想要的索引(查询条件尽量在索引上)',
        '索引长度：确定使用了索引中的几个字段',
        '看rows扫描行数是否太多',
        {'看是否使用了临时表，join_buffer，sort_buffer等额外空间':[
            '排序条件尽量在索引上:参与排序的列越少越好，多了要使用fileSort',
            '避免回表，避免多次回表',
        ]},
        '一张表的索引不能太多:影响新增与更新的性能',
    ]}
    ],
'count(*)':[
    {'查询表的总行数':[
        'MyISAM:count(*):快，但不支持事务',
        'show table status:快，不准确(估算出来的)',
        'InnoDB:count(*)遍历全表，结果准确但有性能问题',
    ]},
    {'其它方法':[
        '缓存系统保存计数:丢失更新+逻辑上不精确问题',
        '两个系统，不支持分布式事务，无法拿到一致性视图',
        '数据库保存计数：利用事务保证逻辑上的精确'
    ]},
    {'不同的count对比':[
        {'count(主键 id)':[
            'InnoDB引擎遍历整张表,把每一行的id值取出返回,server层拿到id，判空，按行累加'
        ]},
        {'count(1)':[
            'InnoDB引擎遍历表，不取值返回，server层对返回的每一行，放一个数字1，判空，按行累加'
        ]},
        {'count(字段)':[
            '类count(主键 id)'
        ]},
        {'count(*)':[
            '不会把全部字段取出，专门做了优化，不取值，count(*) 肯定不是 null，按行累加'
        ]},
        {'总结':[
            'count(1)>count(主键 id):引擎返回 id 会涉及到解析数据行，以及拷贝字段值的操作',
            '效率排序：count(字段)<count(主键 id)<count(1)≈count(*)'
        ]}
    ]}
]
}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 