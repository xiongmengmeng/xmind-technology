import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="mysql"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("数据库")
r2=s2.getRootTopic()
r2.setTitle("数据库")


content={
'数据库三范式':[
    '1NF:字段是原子性的',
    '2NF:必须有主键，非主键必须依赖主键，不能冗余无关联字段',
    '3NF:非主键不能通过依赖传递关联到主键来依赖'
],
'反模式设计':[
    {'1NF':[
        '字段是原子性的,有些字段是需要合并的',
        '如这个字段不需要精准查询，是可以存在一起的',
    ]},
    '2NF:冗余热点查询字段，可以避免连表，提高特定查询的效率',
    '3NF:冗余热点结果字段，可以少查一次表',
    '为了解决实际问题可以跳出框架，牺牲既定规则得到另一方面的提升'
],
'分库':[
    'mysql单机性能不足，需分开多个库，库中的每张表多分成多张表来存储数据',
    '如不需join，可按业务分库'
],
'分表':[
    '通过一定规则，将一张表分解成多张不同的表',
    '比如将用户订单记录根据时间成多个表'
],
'分区':[
    '一个.frm 文件和 4 个.ibd 文件，每个分区对应一个.ibd 文件',
    '对引擎层:4 个表；对Server层：1 个表',
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
'分库、分表带来的分布式困境与应对之策':[
    {'跨库事务问题':[
        'mysql本身的分布式事务管理，会牺牲很大的性能，分库本身就是为了提升性能',
        '如果代码来实现这个事务，那么每条sql都要写对应的回滚sql，也很麻烦'
    ]},
    {'跨库join问题':[
        '跨库无法join表，需要到每个库去执行结果自己在代码里比对和join'
    ]},
    {'跨库order by问题':[
        '每个库都需要执行这条sql，最后查询到的总量是order by*N，然后再归并排序或者堆排序解决'
    ]},
    {'跨库distinct问题':[
        '框架或者代码自己解决，数据库只支持单实例的distinct'
    ]}
],
'分区与分表(手动)的对比':[
    '引擎层：无差别',
    'server层:分区表由server层决定使用哪个分区，手动分表由应用层代码来决定使用哪个分表'
    '区别：分区从逻辑上来讲只有一张表，而分表则是将一张表分解成多张表'
],
}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 