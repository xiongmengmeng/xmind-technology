import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="mysql"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("mysql-sql1")
r2=s2.getRootTopic()
r2.setTitle("mysql-sql1")


content={
'explain':[
    {'Extra 字段':[
        'Using filesort:需要排序，MySQL给每个线程分配一块内存(sort_buffer)用于排序',
        'Using temporary:需要使用临时表',
        'Using index:使用了覆盖索引',
        'Using MRR:用上了 MRR 优化'
    ]}
    ],
'1.count(*)':[
    {'查询表的总行数':[
        'MyISAM:count(*):快，但是不支持事务',
        'show table status:快，不准确(估算出来的)',
        'InnoDB:count(*)遍历全表，结果准确但有性能问题',
    ]},
    {'其它方法':[
        '缓存系统保存计数:丢失更新+逻辑上不精确问题',
        '两个系统，不支持分布式事务，无法拿到一致性视图',
        '数据库保存计数：利用事务保证逻辑上的精确'
    ]},
    {'不同的count对比':[
        'count(主键 id):InnoDB引擎遍历整张表,把每一行的id值取出返回,server层拿到id，判空，按行累加',
        'count(1)：InnoDB引擎遍历表，不取值返回，server层对返回的每一行，放一个数字1，判空，按行累加',
        'count(字段):类count(主键 id)',
        'count(*)：不会把全部字段取出，专门做了优化，不取值，count(*) 肯定不是 null，按行累加',
        'count(1)>count(主键 id):引擎返回 id 会涉及到解析数据行，以及拷贝字段值的操作',
        '效率排序：count(字段)<count(主键 id)<count(1)≈count(*)'
    ]}
],
'2.order by':[
    {'排序使用空间(内存or磁盘）':[
        '排序所需内存',
        'sort_buffer_size：MySQL 为排序开辟的内存（sort_buffer）的大小',
        'max_length_for_sort_data:控制排序行数据长度,如单行长度超过此值，只写排序字段和id'
    ]},
    {'外部排序':[
        '使用归并算法',
        '将需排序数据分成n份，每份单独排序后存入临时文件',
        '最后将n份有序文件合并成一个有序的大文件'
    ]},
    {'全字段排序':[
        '流程：xx索引->表T主键索引->sort_buffer->sort_buffer排序->结果集',
        '内存大，优先选择此算法',
        '字段都放到sort_buffer中，排序后直接从内存返回，不再回表'
    ]},
    {'rowid排序':[
        '流程：xx索引->表T主键索引->sort_buffer->sort_buffer排序->表T主键索引->结果集',
        '归并算法和优先队列排序算法',
        '内存小，影响排序效率,使用此算法',
        '一次可以排序更多行，但需要回表(造成磁盘读)',
        '对于内存表，回表只是根据数据行位置得到数据（不访问磁盘）,优化器优选rowid排序'
    ]},
    'order by语句,未必都要排序，如数据是有序的，直接从索引上取数据，回表，组结果集'
],
'3.order by rand()':[
    'MySQL对临时表排序的执行过程',
    '分析sql:select word from words order by rand() limit 3',
    {'order by rand()':[
        '使用Using temporary（内存临时表）:排序时候使用rowid排序方法',
        'tmp_table_size:限制了内存临时表大小，默认值16M',
        '如临时表超过了tmp_table_size,内存临时表就会转成磁盘临时表',
        '使用Using filesort（sort_buffer排序）'
    ]},
    {'rowid':[
        'rowid：每个引擎用来唯一标识数据行的信息',
        '对有主键的 InnoDB 表，rowid 就是主键 ID',
        '对没有主键的 InnoDB 表，rowid 由系统生成的',
        'MEMORY引擎不是索引组织表,可认为它是一个数组,rowid是数组的下标'
    ]}
],
'4.全表扫描,对server层':[
    '边读边发:查询结果分段发给客户端，扫描全表，返回大量数据，并不会把内存打爆',
    {'取发数据流程':[
        '1.获取一行，写到net_buffer(大小由net_buffer_length定义，默认16k)',
        '2.重复获取行，直到net_buffer写满，调用网络接口发出去',
        '3.发送成功，清空net_buffe，继续取下一行，并写入net_buffer',
        '4.如发送函数返回EAGAIN/WSAEWOULDBLOCK:本地网络栈满，等待,重新可写时再发送'
    ]},
    '正常的线上业务,如查询返回结果不多，建议用mysql_store_result接口，把查询结果保存到本地内存',
    'Sending to client:一个线程处于“等待客户端接收结果”的状态',
    'Sending data:正在执行' 
],
'5.全表扫描,对InnoDB':[
    '有淘汰策略，大查询也不会导致内存暴涨',
    '内存的数据页在Buffer Pool中管理,Buffer Pool有加速查询的作用',
    '加速效果，依赖存命中率（show engine innodb status可查）',
    'Buffer Pool大小由参数innodb_buffer_pool_size确定，建议设置成可用物理内存的60%~80%',
    '淘汰一个旧数据页:用优化后的LRU算法,链表实现,young区域:old区域=5:3',
    {'改进的LRU算法执行流程':[
        '1.访问数据页 P3(在 young 区)，将其移到链表头部',
        '2.访问新的不在当前链表的数据页，淘汰掉数据页Pm，插入新数据页Px放在LRU_old处',
        '3.处于old区域的数据页，每次被访问都要做下判断',
        'a.数据页在LRU链表中存在时间超过1秒，把它移动到链表头部',
        'b.短于1秒(参数 innodb_old_blocks_time 控制,默认1000毫秒)，位置保持不变'
    ]}
]
}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 