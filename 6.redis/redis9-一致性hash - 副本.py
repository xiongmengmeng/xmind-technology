import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="redis"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("一致性hash")
r2=s2.getRootTopic()
r2.setTitle("一致性hash")


content={
'解决问题':[
    '为使得集群能够水平扩展，首要问题是如何将整个数据集按照一定的规则分配到多个节点上',
    '常用的数据分片方法有：范围分片，哈希分片，一致性哈希算法和虚拟哈希槽等'
],
'普通的哈希算法':[
    '计算出哈希值,通过取余操作将key值映射到不同的服务器上',
    '问题：当服务器数量发生变化时，取余操作的除数发生变化，所有key所映射的服务器几乎都会改变'
],
'一致性哈希算法':[
    '尽可能减少了服务器数量变化所导致的缓存迁移',
    '能够在一定程度上改善缓存的雪崩问题，能够在移除/添加一台缓存服务器时，尽可能小的改变已存在的key映射关系，避免大量key的重新映射',
    '这种算法解决了普通余数Hash算法伸缩性差的问题，可以保证在上线、下线服务器的情况下尽量有多的请求命中原来路由到的服务器',
    {'算法内容':[
        '构造一个0到2^32的整数环(hash环，java中可用SortedMap实现)',
        '根据服务器名称(也可以是ip:port)计算出hash值，根据其hash值将服务器放置在hash环上',
        '根据数据的Key值计算得到其Hash值，在hash环上顺时针查找距离最近的服务器节点(SortedMap.tailMap(key)实现)，进行set/set操作'
    ]},
    {'实现':[
        'java实现(TreeMap)：https://zhuanlan.zhihu.com/p/34969287'
    ]},
    {'缺点':[
        '可能出现节点不均衡的现象，或者节点均衡，数据不均衡的问题',
        '可能通过增加虚拟节点(不仅仅用ip来映射)的方式解决'
    ]}
]

}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 