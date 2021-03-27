import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="redis"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("持久化")
r2=s2.getRootTopic()
r2.setTitle("持久化")


content={
'目的':[
    '解决宕机数据丢失问题'
],
'RDB':[
    '默认持久化方式',
    '定时将内存的数据以快照形式保存到硬盘',
    'dump.rdb',
    {'写磁盘方式':[
        '二进制 + 数据压缩的方式写磁盘，文件体积小，数据恢复速度快'
    ]},
    {'快照条件':[
        'save 900 1 (900秒内至少有一个键被更改)'
    ]},
    {'快照过程':[
        {'rdbSave(生成RDB文件)':[
            'fork函数（创建子进程）+cow函数（使用写时复制copy-on-write策略）:',
            '父子进程共享数据段，父进程继续提供读写服务，写脏的页面数据会逐渐和子进程分离开来'
        ]},
        'rdbLoad（从文件加载内存）'
    ]},
    {'加载':[
        'redis启动后会读取RDB快照文件，将数据从磁盘载入内存'
    ]},
    {'风险':[
        'redis异常退出，会丢失最后一次快照后的更改数据'
    ]}
],
'AOF':[
    'Append Only File----每次写操作都持久到磁盘',
    '通过参数appendonly yes开启，默认文件appendonly.aof',
    {'写磁盘方式':[
        '纯文本文件，内容为redis客户端向redis发送的原始通信协议内容',
        '记录的是每一次写命令，数据最全，但文件体积大，数据恢复速度慢'
    ]},
    {'加载':[
        '从持久化的日志中文件恢复数据'
    ]},
    {'风险':[
        '操作系统的缓存机制，数据并没有真正写入磁盘，只是进入系统的磁盘缓存，默认30s同步一次',
        '通过参数优化此行为:appendfsync everysec(默认)，每秒执行一次同步操作'
    ]},
    '对AOF文件定时rewrite，避免文件体积持续膨胀'

],
'混合持久化':[
    'AOF rewrite时，以RDB格式在AOF文件中写入一个数据快照，再把在这期间产生的每一个写命令，追加到AOF文件中',
    'RDB是二进制压缩写入，AOF文件体积变小',
    'Redis 4.0 以上版本支持'
],
'持久化策略选择':[
    'Redis中的数据完全丢弃也没有关系，可以不进行任何持久化',
    '单机环境，如可接受十几分钟或更多数据丢失，选择RDB；如只能接受秒级数据丢失，选择AOF',
    '多数情况，会配置主从环境，slave既可实现数据的热备，也可分担Redis读请求，以及在master宕掉后继续提供服务'
],
{'常见性能问题':[
    {'master写内存快照':[
        'save命令调度rdbSave函数',
        '会阻塞主线程工作',
        '当快照比较大时对性能影响非常大，会间断性暂停服务'
    ]},
    {'master AOF持久化':[
        '如不重写AOF文件，对性能的影响较小',
        '但AOF文件会不断增大，AOF文件过大会影响Master重启的恢复速度',
        'Master调用BGREWRITEAOF重写AOF文件，会占大量的CPU和内存资源，导致服务load过高，出现短暂服务暂停现象'
    ]},
    '总结:Master最好不做任何持久化工作，如RDB内存快照和AOF日志文件',
    {'建议':[
        '如数据重要，某个slave开启AOF备份数据，策略设置为每秒同步一次',
        '为了主从复制的速度和连接的稳定性，master和slave最好在同一个局域网'
    ]}  
]

  
}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 