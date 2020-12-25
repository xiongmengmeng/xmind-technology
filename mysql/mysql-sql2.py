import xmind
from xmind.core.markerref import MarkerId
w = xmind.load("c:\\Users\\btr\\Desktop\\mysql.xmind") 
s2=w.createSheet()
s2.setTitle("mysql-sql2")
r2=s2.getRootTopic()
r2.setTitle("mysql-sql2")


content={
'1.join基础':[
    '驱动表:主动发起查询的表 ',
    '被驱动表:根据on条件被动被查询的表',
    '驱动表的行数 N,被驱动表的行数 M',
    '两个表按照各自的条件过滤后，计算参与 join 的字段总数据量，数据量小的表，应作驱动表'
],
'2.使用被驱动表的索引':[
    'NLJ 算法',
    '驱动表是走全表扫描，被驱动表是走树搜索',
    '扫描行业：N+M',
    '近似复杂度: N + N*2*log2M',
    'N小时，复杂度少，驱动表选择小表'
],
'3.被驱动表用不上索引':[
    {'BNL 算法':[
        '1.可能多次扫描被驱动表，占用磁盘 IO 资源',
        '2.判断 join 条件需要执行 M*N 次对比,大表会占用非常多CPU 资源',
        '3.可能导致 Buffer Pool 的热数据被淘汰，影响内存命中率'
    ]},
    '借助join_buffer，驱动表全部读入',
    '扫描行数: N+λ*N*M (λ*N分段数)',
    '内存判断:N*M 次',
    'N小时，扫描行数少，驱动表选择小表',
    'λ小时，分段数小，则join_buffer_size 大（一次放入的行多，用join_buffer_size控制）'
],
'4.优化':[
    {'MRR算法':[
        '顺序读盘，查询语句在索引a上做一个范围查询',
        '得到足够多主键id,排序以后，再去主键索引查数据'
    ]},
    {'BKA算法':[
        '对NLJ算法的优化,暂存驱动表的数据到join_buffer，依赖于 MRR'
    ]}
],
'5.临时表':[
    '建表语法 create temporary table …',
    '只能被创建它的session访问，对其他线程不可见,session结束，自动删除临时表',
    '可与普通表同名(内存中每个表都有一个table_def_key：库名+表名+server_id+thread_id)',
    'session 内有同名的临时表和普通表，增删改查语句访问的是临时表',
    'binlog_format=row时，临时表的操作不记录到 binlog 中'
],
'6.内部临时表-union 执行流程':[
    'union 要去重，需用到内部临时表',
    'union all 不用去重,依次执行子查询，结果依次发给客户端,不需要临时表'
],
'7.内部临时表-group by':[
    '统计不同的值出现的个数,需要临时表来排序',
    '执行流程:内存临时表->sort buffer(排序)-内存临时表',
    '优化1：没有排序要求，语句后加 order by null',
    '优化2：索引:确保输入数据是有序的',
    '优化3：直接排序,语句中加入SQL_BIG_RESULT提示',
    '告诉优化器：语句涉及的数据量大，请直接用磁盘临时表',
    'MySQL优化器觉得磁盘临时表是B+树存储，效率不如数组，直接使用数组'
],
'8.内部临时表-总结':[
    '存放语句执行过程中的中间数据',
    'join_buffer 是无序数组，sort_buffer 是有序数组，临时表是二维表结构',
    '语句执行过程:一边读，一边得到结果，不需额外内存，否则需要额外内存来保存中间结果',
    '执行逻辑用到二维表特性,比union用到唯一索引约束，group by用到另外一个字段存累积计数'
   
]
}

for key in content:
    t1 = r2.addSubTopic()
    t1.setTopicHyperlink(s2.getID()) 
    list=key.split(":")
    t1.setTitle(list[0])
    if len(list)>1:
        t1.setPlainNotes(list[1]) 
    # print(content[key])
    for i in content[key]:
        # print(type(i))
        if(type(i).__name__=='dict'):
            for t in i:
                t2 = t1.addSubTopic()
                t2.setTopicHyperlink(t1.getID()) 
                t2.setTitle(t)
                for j in i[t]:
                    #print(j)
                    if(type(j).__name__=='dict'):
                        for h in j:
                            t3 = t2.addSubTopic()
                            t3.setTopicHyperlink(t2.getID()) 
                            t3.setTitle(h) 
                            for m in j[h]:
                                if(type(m).__name__=='dict'):
                                    for n in m:
                                        t4 = t3.addSubTopic()
                                        t4.setTitle(n) 
                                        for l in m[n]:
                                            if(type(l).__name__=='dict'):
                                                for k in l:
                                                    t5 = t4.addSubTopic()       
                                                    t5.setTitle(k)
                                                    for p in l[k]:
                                                        if(type(p).__name__=='dict'):
                                                            for u in p:
                                                                t6 = t5.addSubTopic()
                                                                t6.setTitle(u)
                                                                for y in p[u]:
                                                                    if(type(y).__name__=='dict'):
                                                                        for a in y:
                                                                            t7 = t6.addSubTopic()
                                                                            t7.setTitle(a)
                                                                            for b in y[a]:
                                                                                t8 = t7.addSubTopic()
                                                                                t8.setTitle(b)
                                                                    else:
                                                                        t7 = t6.addSubTopic()
                                                                        t7.setTopicHyperlink(t2.getID()) 
                                                                        t7.setTitle(y)              
                                                        else:
                                                            t6 = t5.addSubTopic()
                                                            t6.setTopicHyperlink(t2.getID()) 
                                                            t6.setTitle(p)                                                        
                                            else:
                                                t5 = t4.addSubTopic()
                                                t5.setTopicHyperlink(t3.getID()) 
                                                t5.setTitle(l) 
                                else:
                                    t4 = t3.addSubTopic()
                                    t4.setTopicHyperlink(t3.getID()) 
                                    t4.setTitle(m) 
                    else:
                        t3 = t2.addSubTopic()
                        t3.setTopicHyperlink(t2.getID()) 
                        t3.setTitle(j) 
        else:
            t2 = t1.addSubTopic()
            t2.setTopicHyperlink(t1.getID()) 
            t2.setTitle(i) 



topics=r2.getSubTopics()
for topic in topics:
    topic.addMarker(MarkerId.starBlue)

xmind.save(w,"c:\\Users\\btr\\Desktop\mysql.xmind") 