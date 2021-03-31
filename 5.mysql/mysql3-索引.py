import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="mysql"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("分布式ID的生成方案")
r2=s2.getRootTopic()
r2.setTitle("分布式ID的生成方案")


content={

'UUID':[
    '结合机器的网卡、当地时间、一个随记数来生成',
    '优点：本地生成，生成简单，性能好，没有高可用风险',
    '缺点：长度过长，存储冗余，且无序不可读，查询效率低'
],
'数据库自增ID':[
    '使用数据库的id自增策略，如 MySQL 的 auto_increment',
    {'自增值':[
        '用自增列作为主键,可防止页断裂造成的空洞',
        {'自增值':[
            '无符号整型是4个字节，上限是2的32次-1',
            '表定义的自增值达到上限后：再申请下一个id时，得到的值保持不变',
            'InnoDB系统自增row_id,范围从0到2的48次-1'
        ]},
        {'自增值的保存策略-InnoDB':[
            'AUTO_INCREMENT=n:存在表结构定义中，放在后缀名为.frm 的文件（不会保存自增值）',
            {'自增值保存在内存':[
                'MySQL5.7前:没有持久化,每次重启，第一次打开表，找自增值的最大值 max(id)，将其作为这个表当前的自增值',
                'MySQL8.0后:有“自增值持久化”的能力,自增值变更记录在redo log中，重启时候依靠redo log 恢复重启之前的值'
            ]}
        ]},
        {'自增值的行为':[
            'id字段指定为 0、null 或未指定:把当前AUTO_INCREMENT值填到自增字段',
            'id字段指定了具体值:使用指定值'
        ]},
        {'自增值不连续原因':[
            {'双M结构':[
                'auto_increment_increment=2',
                '一个库的自增id是奇数，另一个库的自增id是偶数，避免两库生成的主键发生冲突'
            ]},
            {'唯一键冲突':[
                '先拿到自增值，然后新增数据，报错回滚，但自增值不会回滚'
            ]},
            {'事务回滚':[
                '同上'
            ]}
        ]},
        {'自增锁':[
            'innodb_autoinc_lock_mode:自增锁策略，默1'
            '0：语句执行结束后才释放锁',
            {'1':[
                '普通insert语句，自增锁在申请后马上释放',
                '普通insert语句，含多个value值，一次性申请锁，申请完成后锁释放',
                'insert … select批量插入语句，自增锁要等语句结束后才被释放'
            ]},
            '2：所有申请自增主键的动作都是申请后就释放锁'
        ]},
    ]}
],
'Redis生成ID':[
    'Redis命令操作都是单线程的，本身提供incr和increby这样的自增原子命令，能保证生成的ID肯定是唯一有序的',
    {'优点':[
        '不依赖于数据库，灵活方便，且性能优于数据库',
        '数字ID天然排序，对分页或者需要排序的结果很有帮助',
    ]},
    '缺点：如果系统中没有Redis，还需要引入新的组件，增加系统复杂度'
],
'Twitter的snowflake算法':[
    '利用 zookeeper 实现了一个全局ID生成的服务'
]

}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 