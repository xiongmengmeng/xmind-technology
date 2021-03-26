import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="redis"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("内存淘汰策略")
r2=s2.getRootTopic()
r2.setTitle("内存淘汰策略")


content={
'内存不足时，怎么处理需要新写入且需要申请额外空间的数据':[],
'allkey类型':[
    'lru：(least recently used)在键空间(server.db\[i\].dict)中，最少使用的key(最常用)',
    'random：随机',
    'lfu:(least recently used)最近访问次数最少'
    'noeviction：内存不足时，新写入操作报错',
],
'volatile类型':[
    'lru：在设置了过期时间的键空间中(server.db\[i\].expires)，移除最近最少使用的key',
    'lfu:最近访问次数最少',
    'ttl：在设置了过期时间的键空间中，快要过期的key优先移除',
    'random：内存不足时，在设置了过期时间的键空间中，随机移除某个key',
],
'使用策略规则':[
    '1.如数据呈现幂律分布，一部分数据访问频率高，一部分访问频率低，使用allkeys-lru2',
    '2.如数据呈现平等分布，所有的数据访问频率都相同，使用allkeys-random'
],
'注':[
    {'LRU实现':[
        '是近似LRU,节约内存与CPU的原则',
        '随机采样N个key并对其排序，选出最久没有使用的一个key进行淘汰'
    ]},
    {'LFU':[
        'Redis4.0后出现，最近最少使用实际上并不精确'
    ]}
],
'常见的性能问题及解决':[
    '超过10W的并发访问量->使用集群',
    '服务器内存不够->考虑过期数据删除机制是否有效，如有都是有效数据，使用集群',
    '偶尔有慢查询->可禁用一些keys，hgetall之类的指令，或把大key分解'
]

}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 