import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="mysql"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("order by")
r2=s2.getRootTopic()
r2.setTitle("order by")


'order by':[
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
'order by rand()':[
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
]
}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 