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
'数据库的三范式':[
    '1NF:字段是原子性的',
    '2NF:必须有主键，非主键必须依赖主键，不能冗余无关联的字段',
    '3NF:非主键不能通过依赖传递关联到主键来依赖'
],
'反模式设计':[
    {'1NF':[
        '字段是原子性的,有些字段是需要合并的，比如数组，这也是mysql设计json字段的原因，当然json字段并不好用，可以用1:N扩展表',
        '但是如果这个字段不需要精准查询，是可以存在一起的',
    ]},
    '2NF:冗余热点查询字段，可以避免连表，提高特定查询的销量',
    '3NF:冗余热点结果字段，可以少查一次表',
    '反模式设计一定是为了某种特殊情况存在的，可以为了解决一些问题而跳出框架，牺牲既定规则得到另一方面的提升'
],
'分库与分表设计':[
    '分库分表，即mysql单机性能不足，需要分开多个库，库中的每张表多分成多张表来存储数据',
    '业务分库其实可以按业务分，只要是不需要join的表按业务分开',
    {'数据分库分表不同，要把一张表切开多张':[
        '按主键分:使用hash方法'
        '按某个字段分：如时间，这样会一定时间增长一个分表'
    ]}
],
'分库与分表带来的分布式困境与应对之策':[
    {' 跨库事务问题':[
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
}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 