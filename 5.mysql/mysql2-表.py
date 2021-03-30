import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="mysql"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("表")
r2=s2.getRootTopic()
r2.setTitle("表")


content={
'表复制':[
    'mysqldump 命令将数据导出成一组 INSERT 语句',
    '导出 CSV 文件+load data 命令将数据导入到目标表',
    '物理拷贝方法'
],
'表空间回收':[
    '现象：表数据删掉一半，表文件大小不变',
    '一个InnoDB表包含两部分:表结构定义+数据',
    {'innodb_file_per_table':[
        'On:表数据存储在以.ibd为后缀的文件中,drop table,直接删除文件',
        'OFF:表的数据放在系统共享表空间，跟数据字典一起,表删掉，空间不会回收'
    ]},
    {'数据删除流程':[
        '数据页的复用跟记录的复用',
        'delete命令:把记录的位置，或数据页标记为了“可复用”，磁盘文件大小不会变',
        'insert命令：随机插入，可能造成索引的数据页分裂',
        'update命令：删除一个旧的值，再插入一个新值,会造成空洞'
        '经过大量增删改的表->存在空洞的->把空洞去掉->收缩表空间(重建表)'
    ]},
    {'重建表':[
        {'alter table A engine=InnoDB':[
            '转存数据、交换表名、删除旧表',
            '语句在启动时获取MDL写锁，真正拷贝数据前退化成读锁'
        ]},
        {'退化成读锁原因':[
            '实现Online DDL',
            '不直接解锁,禁止其他线程对这个表同时做DDL'
        ]},
        {'Online DDL':[
            '最耗时是拷贝数据到临时表',
            '如个步骤的执行期间可接受增删改操作',
            '对整个过程来说，锁的时间很短，认为是Online的'
        ]}

    ]}
],
'数据误删后恢复':[
    {'1.误删行':[
        'Flashback 工具，修改binlog（格式为row）内容，拿回原库执行',
        'delete 全表很慢，会生成回滚日志、写 redo、写 binlog',
        '从性能考虑，优先使用truncate table或drop table',
        {'drop、delete、truncate的区别':[
            'drop:删表',
            'delete:只删数据，删除操作作为事务记录在日志中，可进行回滚',
            'truncate:一次性删除表中所有的数据,无操作记录日志，不能恢复'
        ]},
    ]},
    {'2.误删库/表':[
        '全量备份+增量日志',
        '加速方法：在用备份恢复出临时实例之后，将临时实例设置成线上备库的从库'
    ]},
    {'3.rm 删除数据':[
        '备份跨机房，或者最好是跨城市保存'
    ]},
    {'预防误删库/表':[
        '1.账号分离:开发DML权限，运维平时只读，必要时才更新',
        '2.制定操作规范：删表先改名，再在平台操作'
    ]}
],
}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 