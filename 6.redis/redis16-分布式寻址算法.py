import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="redis"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("分布式寻址算法")
r2=s2.getRootTopic()
r2.setTitle("分布式寻址算法")


content={
'简介':[
    {'目的':[
        '使得集群能够水平扩展'
    ]},
    {'首要问题':[
        '如何将整个数据集按照一定的规则分配到多个节点上'
    ]},
    {'常用数据分片方法':[
        '范围分片',
        '哈希分片',
        '一致性哈希算法',
        '虚拟哈希槽'
    ]}
],
'hash算法（大量缓存重建）':[
    '一个 key，计算 hash 值，然后对节点数取模，确定master节点',
    '某一个master节点宕机，所有请求过来，都会基于最新的剩余master节点数取模，尝试去取数据',
    '导致大部分的请求过来，全部无法拿到有效的缓存，导致大量的流量涌入数据库。'
],
'一致性hash算法+虚拟节点':[
    '自动缓存迁移+自动负载均衡',
    {'算法内容':[
        '构造一个0到2^32的整数环(hash环，java中可用SortedMap实现)',
        '根据服务器名称(也可以是ip:port)计算出hash值，根据其hash值将服务器放置在hash环上',
        '根据数据的Key值计算得到其Hash值，在hash环上顺时针查找距离最近的服务器节点(SortedMap.tailMap(key)实现)，进行set/set操作'
    ]},
    {'实现':[
        'java实现(TreeMap)：https://zhuanlan.zhihu.com/p/34969287'
    ]},
    {'优点':[
        '减少了服务器数量变化导致的缓存迁移',
        '一定程度上改善缓存雪崩问题,在移除/添加一台服务器时，尽可能小的改变已存在的key映射关系，避免大量key的重新映射',
        '解决了普通Hash算法伸缩性差的问题，可保证上线、下线服务器时尽量有多的请求命中原来路由到的服务器'
    ]},
    {'缺点':[
        '可能出现节点不均衡的现象，或者节点均衡，数据不均衡的问题',
        '可通过增加虚拟节点(不仅仅用ip来映射)的方式解决'
    ]}
],
'hash slot 算法':[
    {'根据key寻找redis服务器':[
        '通过CRC16算法对key求哈希值：hashcode = CRC16(key);',
        '对槽总数求余得到哈希槽中的数字：n = hashcode % 16384',
        '根据服务器分配的槽区间，找到服务器'
    ]},
    {'分区扩展':[
        '每个master持有部分slot，比3个master，每个master持有5000多个hash slot',
        'hash slot让node的增加和移除很简单',
        '增加一个master，将其他master的hash slot移动部分过去',
        '减少一个master，将它的hash slot移动到其他master上去',
        '移动 hash slot 的成本是非常低的',
        '任何一台机器宕机，另外两个节点，不影响的。因为 key 找的是 hash slot，不是机器'
    ]},
    {'redis-cluster不可用情况':[
        {'1.集群主库半数宕机（无论是否从库存活）':[
            '无法做主从切换'
        ]},
        {'2.集群某一节点的主从全数宕机':[
            '构建不成哈希槽区间[0, 16383]'
        ]}
    ]}
]
}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 