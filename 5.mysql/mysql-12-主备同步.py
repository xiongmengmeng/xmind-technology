import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="mysql"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("主备同步")
r2=s2.getRootTopic()
r2.setTitle("主备同步")


content={
'基础知识':[
    {'备库设置成只读（readonly）模式':[
        '1.有时运营类的查询语句会被放到备库上去查，防止误操作',
        '2.防止切换逻辑有bug，如切换过程出现双写，造成主备不一致',
        '3.可用readonly状态，判断节点角色',
        '注：readonly对超级权限用户是无效的，同步更新的线程拥有超级权限'
    ]},
    {'binlog三种格式binlog_format':[
        'statement : 记录SQL语句的原文',
        'row : 占空间，记录真实删除行的主键 id，恢复数据方便',
        'mixed :两种格式都有，确定行数的用statement格式，其余用row'
    ]},
    {'循环复制问题':[
        '备库接到 binlog 并在重放的过程中，生成与原binlog的server id相同的新的binlog',
        '每个库在收到日志后，先判断server id，跟自己的相同，直接丢弃这个日志'
    ]}
],
'事务日志同步过程':[
    '备库B：io_thread--->relay log--->sql_thread',
    '备库B 跟主库A 之间维持了一个长连接。主库A 内部有一个线程，专门用于服务备库B 的这个长连接',
    '1.备库B通过change master命令，设置主库A的 IP、端口、用户名、密码，以及要从哪个位置(包含文件名和日志偏移量)开始请求 binlog',
    '2.备库B执行start slave命令，会启动两个线程:io_thread(负责与主库建立连接)和sql_thread ',
    '3.主库A校验完用户名、密码后，开始按照备库 B 传过来的位置，从本地读取 binlog，发给 B',
    '4.备库B拿到 binlog 后，写到中转日志（relay log）,sql_thread 读取中转日志，解析出日志里的命令，并执行'
],
'读写分离的坑':[
    '一主多从的结构，其实就是读写分离的基本结构',
    {'客户端直连':[
        '整体架构简单，排查问题方便',
        '要了解后端部署细节，在出现主备切换、库迁移等操作时，客户端会感知到，并需调整数据库连接信息',
        '一般伴随一个负责管理后端的组件（如Zookeeper），尽量让业务端只专注业务逻辑开发'
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
'数据库出问题判断':[
    '1.select 1:有返回:进程还在',
    'InnoDB中，innodb_thread_concurrency通常取值64~128，机器CPU 核有限，减少上下文切换',
    {'并发连接和并发查询':[
        '并发连接：show processlist结果里的几千个连接，会占用一些内存',
        '并发查询：当前正在执行的语句，CPU 杀手',
        '线程进入锁等待后，并发线程的计数减一',
    ]},
    '2.查表判断:检测 InnoDB 并发线程数过多导致的系统不可用情况',
    '3.更新判断:判断binlog内存是否正常，但基于外部检测，判断慢',
    '4.内部统计:5.6版本后提供performance_schema 库，在file_summary_by_event_name 表里统计每次IO请求的时间'
]

}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 