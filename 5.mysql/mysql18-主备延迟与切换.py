import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="mysql"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("主备延迟与切换")
r2=s2.getRootTopic()
r2.setTitle("主备延迟与切换")


content={
'主备延迟现象':[
    'show slave status 命令,seconds_behind_master显示当前备库延迟秒数',
    '网络正常时，日志从主库传给备库所需时间很短',
    '主备延迟的主要:备库接收完 binlog 和执行完这个事务之间的时间差',
    '表现:备库消费中转日志（relay log）的速度，比主库生产binlog慢'
],
'主备延迟原因':[
    '1.备库所在机器性能比主库差:更新请求对IOPS的压力，在主库和备库上是无差别的',
    {'2.备库的压力大:备库上的查询耗费了大量CPU资源，影响同步速度':[
        '一主多从，分担读的压力',
        '通过 binlog 输出到外部系统(如Hadoop)，让外部系统提供统计类查询'
    ]},
    '3.大事务:一次性地delete删除太多数据/大表 DDL',
    '4.备库的并行复制能力'
],
'主备切换过程':[
    '1.判断备库 B 的 seconds_behind_master，小于5 秒，继续下一步，否则持续重试',
    '2.把主库 A 改成只读状态（readonly 设置为 true）',
    '3.判断备库 B 的 seconds_behind_master，直到变成 0 为止',
    '4.把备库 B 改成可读写状态（readonly 设置为 false）',
    '5.把业务请求切到备库 B'
],
'备库延迟解决':[
    'sql_thread 执行中转日志,改为多线程复制策略',
    '1.按库分发策略',
    '2.commit状态，即同一组里提交的事务不会更新同一行（利用redo log组提交优化）',
    '3.rego log于prepare与commit状态的事务，在备库执行时可并行',
    '4.按行分发策略'
],
'一主多从的正确切换':[
    '基于位点的主备切换:需主动跳过错误',
    {'GTID':[
        '全局事务ID，一个事务在提交的时候生成，是事务的唯一标识',
        'GTID=server_uuid:gno',
        'server_uuid:一个实例第一次启动时自动生成的，一个全局唯一的值',
        'gno:一个整数，初始值1，每次commit的时候分配给这个事务，并加 1',
        '启动一个MySQL实例时，加上参数gtid_mode=on和enforce_gtid_consistency=on'
    ]},
    {'基于GTID的主备切换':[
        '备库 B 要设置为新主库 A’的从库',
        '1.实例 B 指定主库 A’，基于主备协议建立连接',
        '2.实例 B 把 set_b 发给主库 A’',
        '3.实例 A’算出set_a与set_b差集（存在于set_a，不存在set_b的GTID集合）',
        '判断 A’本地是否包含了差集需要的所有binlog事务',
        'a.不包含：A’已经把实例 B 需要的 binlog 删掉了，直接返回错误',
        'b.全部包含：A’从自己的 binlog 文件里，找出第一个不在set_b的事务，发给B',
        '4.之后从这个事务开始，往后读文件，按顺序取binlog发给B去执行'
    ]}
],
}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 