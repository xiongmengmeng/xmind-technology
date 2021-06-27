import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="mysql"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("ShardingSphere")
r2=s2.getRootTopic()
r2.setTitle("ShardingSphere")


content={
'ShardingJDBC':[
    '做客户端分库分表',
    '在Java的JDBC层提供的额外服务',
    '增强版的JDBC驱动，完全兼容JDBC和各种ORM框架',
    {'核心功能':[
        {'表':[
            {'逻辑表':[
                '水平拆分的数据库的相同逻辑和数据结构表的总称'
            ]},
            {'真实表':[
                '在分片的数据库中真实存在的物理表'
            ]},
            {'数据节点':[
                '数据分片的最小单元',
                '由数据源名称和数据表组成'
            ]},
            {'绑定表':[
                '分片规则一致的主表和子表'
            ]},
            {'广播表':[
                '公共表，在所有数据源中都存在的表',
                '表结构和表中的数据在每个数据库中都完全一致'
            ]},
        ]},
        {'分片':[
            {'分片键':[
                '将数据库(表)进行水平拆分的关键字段'
            ]},
            {'分片算法':[
                '通过分片算法将数据进行分片，支持通过=、BETWEEN和IN分片',
                '分片算法由应用开发者自行实现，可实现的灵活度非常'
            ]},
            {'分片策略':[
                '分片键+分片算法',
                '在ShardingJDBC中一般采用基于Groovy表达式的inline分片策略',
                '分片键的算法表达式来制定分片策略',
                '如t_user_$->{u_id%8}标识根据u_id模分成8张表，表名称为t_user_0到t_user_7'
            ]},
        ]}
    ]},
    {'配置(4.1.1版本)':[
        '1.数据源',
        {'2.表的分布情况':[
            '表在哪个数据库',
            '表名是什么',
            '水平分表，分两个表:m1.course_1,m1.course_2',
            'spring.shardingsphere.sharding.tables.course.actual-data-nodes=m1.course_$->{1..2}

        ]},
        {'2.表的主键,及其生成策略':[
            '....course.key-generator.column=cid',
            '....course.key-generator.type=SNOWFLAKE'
        ]},
        {'4.分片策略':[
            {'选定计算的字段':[
                '....course.table-strategy.inline.sharding-column=cid'
            ]},
            {'根据计算的字段算出对应的表名':[
                '....course.table-strategy.inline.algorithm-expression=course_$->{cid%2+1}'
            ]}
        ]}
    ]},
    {'分片算法(五种)':[
        {'NoneShardingStrategy':[
            '不分片'
        ]},
        {'InlineShardingStrategy':[
            '提供一个分片键和一个分片表达式来制定分片算法',
            {'配置参数':[
                'inline.shardingColumn 分片键',
                'inline.algorithmExpression 分片表达式'
            ]},
            {'实现方式':[
                '按照分片表达式来进行分片'
            ]}
        ]},
        {'StandardShardingStrategy':[
            '支持单分片键的标准分片策略',
            {'配置参数':[
                'standard.sharding-column 分片键',
                'standard.precisealgorithm-class-name 精确分片算法类名',
                'standard.range-algorithmclass-name 范围分片算法类名'
            ]},
            ]},
            {'实现方式':[
                {'preciseAlgorithmClassName':[
                    '指向一个实现PreciseShardingAlgorithm接口的java类名',
                    '提供按照 = 或者 IN 逻辑的精确分片'
                ]},
                {'rangeAlgorithmClassName':[
                    '指向一个实现RangeShardingAlgorithm接口的java类名',
                    '提供按照Between 条件进行的范围分片'
                ]},
            ]}
        ]},
        {'ComplexShardingStrategy':[
            '支持多分片键的复杂分片策略',
            {'配置参数':[
                'complex.sharding-columns 分片键(多个)',
                'complex.algorithm-class-name 分片算法实现类'
            ]},
            {'实现方式':[
                {'algorithmClassName':[
                    '指向一个实现ComplexKeysShardingAlgorithm接口的java类名',
                    '提供按照多个分片列进行综合分片的算法'
                ]},
            ]}
        ]},
        {'HintShardingStrategy':[
            '不需要分片键的强制分片策略',
            '分片键不再跟SQL语句相关联，而是用程序另行指定',
            {'配置参数':[
                'hint.algorithm-class-name 分片算法实现类'
            ]},
            {'实现方式':[
                {'algorithmClassName':[
                    '指向一个实现HintShardingAlgorithm接口的java类名',
                ]},
            ]}
        ]},
    ]},
    {'SQL使用限制':[
        ''
    ]}
],
'分库分表带来的问题':[
    {'分库分表的原因':[
        '单机数据库容量的问题'
    ]},
    {'解决方案':[
        '缓存技术着手降低对数据库的访问压力',
        '数据库读写分离策略',
        '分库分表',
        {'分布式存储产品':[
            '如PostGreSQL',
            'VoltDB甚至HBase',
            'Hive、ES等这些大数据组件来存储'
        ]}
    ]}

],
'ShardingProxy':[
    '做服务端分库分表的产品',
    '透明化的数据库代理端，提供封装了数据库⼆进制协议的服务端版本，⽤于完成对异构语⾔的⽀持'
],

}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 