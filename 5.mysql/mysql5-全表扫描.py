import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="mysql"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("全表扫描")
r2=s2.getRootTopic()
r2.setTitle("全表扫描")


content={
'对server层':[
    {'边读边发':[
        '查询结果分段发给客户端',
        '扫描全表，返回大量数据，并不会把内存打爆'
    ]},
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
'对InnoDB':[
    {'有淘汰策略':[
        '大查询也不会导致内存暴涨',
        '内存的数据页在Buffer Pool中管理,Buffer Pool有加速查询的作用',
        '加速效果，依赖存命中率（show engine innodb status可查）',
        'Buffer Pool大小由参数innodb_buffer_pool_size确定，建议设置成可用物理内存的60%~80%',
    ]},
    {'淘汰一个旧数据页':[
        '用优化后的LRU算法,链表实现,young区域:old区域=5:3'
    ]},
    {'改进的LRU算法执行流程':[
        '1.访问数据页 P3(在 young 区)，将其移到链表头部',
        '2.访问新的不在当前链表的数据页，淘汰掉数据页Pm，插入新数据页Px放在LRU_old处',
        {'3.处于old区域的数据页，每次被访问都要做下判断':[
            'a.数据页在LRU链表中存在时间超过1秒，把它移动到链表头部',
            'b.短于1秒(参数 innodb_old_blocks_time 控制,默认1000毫秒)，位置保持不变'
        ]}
    ]}
]
}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 