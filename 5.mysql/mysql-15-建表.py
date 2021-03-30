import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="mysql"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("建表")
r2=s2.getRootTopic()
r2.setTitle("建表")


content={
'自增主键':[
    {'自增id':[
        '无符号整型 (unsigned int) 是 4 个字节，上限就是 2的32次-1',
        '表定义的自增值达到上限后的逻辑是：再申请下一个 id 时，得到的值保持不变',
        'InnoDB 系统自增 row_id,范围，是从 0 到 2的48次-1',
        'Xid'
    ]},
    'AUTO_INCREMENT=n，存在表结构定义中，放在后缀名为.frm 的文件（不会保存自增值）',
    {'自增值的保存策略':[
        'MyISA：保存在数据文件中',
        'InnoDB：保存在内存里，MySQL 8.0后有了“自增值持久化”的能力'
    ]},
    {'修改机制及不连续原因':[
        'id 字段指定为 0、null 或未指定，把表当前AUTO_INCREMENT值填到自增字段',
        'id 字段指定了具体值，使用语句里指定的值',
        '双M结构里，auto_increment_increment=2，一个库的自增id是奇数，另一个库的自增id是偶数，避免两库生成的主键发生冲突',
        '唯一键冲突',
        '事务回滚'
    ]},
    {'innodb_autoinc_lock_mode，默1':[
        '0：语句执行结束后才释放锁',
        '1：普通insert 语句，自增锁在申请之后就马上释放；类似insert … select的批量插入语句，自增锁要等语句结束后才被释放',
        '2：所有的申请自增主键的动作都是申请后就释放锁'
    ]},
    '普通insert语句，含多个 value 值，一次性申请锁，申请完成后锁释放'
],
'最快地复制一张表':[
    'mysqldump 命令将数据导出成一组 INSERT 语句',
    '导出 CSV 文件+load data 命令将数据导入到目标表',
    '物理拷贝方法'
],
'分区表':[
    '一个.frm 文件和 4 个.ibd 文件，每个分区对应一个.ibd 文件',
    '对引擎层:4 个表；对Server层：1 个表',
    {'手动分表和分区表区别':[
        '引擎层：无差别',
        'server层:分区表由server层决定使用哪个分区，手动分表由应用层代码来决定使用哪个分表'
    ]},
    {'问题':[
        'MySQL第一次打开分区表的时候，需要访问所有的分区',
        'server层：认为是同一张表，所有分区共用同一个 MDL 锁',
        '引擎层：认为不同表，MDL 锁后的执行过程，会根据分区表规则，只访问必要的分区'
    ]},
    {'应用场景':[
        '对业务透明，相对于用户分表，业务代码更简洁',
        '方便的清理历史数据,alter table t drop partition删除'
    ]}
],
'表分区与分表的区别':[
    '分表：指的是通过一定规则，将一张表分解成多张不同的表。比如将用户订单记录根据时间成多个表',
    '分表与分区的区别在于：分区从逻辑上来讲只有一张表，而分表则是将一张表分解成多张表'
],
}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 