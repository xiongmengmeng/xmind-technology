import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="redis"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("")
r2=s2.getRootTopic()
r2.setTitle("")


content={
'哈希槽':[
    'Redis集群的哈希槽大小为（214=16 384），也就是取值范围为区间[0, 16383]，最多能够支持16 384个节点',
    {'根据key寻找redis服务器':[
        '通过CRC16算法对key求哈希值：hashcode = CRC16(key);',
        '对槽总数求余得到哈希槽中的数字：n = hashcode % 16384',
        '根据服务器分配的槽区间，找到服务器'
    ]},
     {'redis-cluster不可用情况':[
        {'1.集群主库半数宕机（无论是否从库存活）':[
            '无法做主从切换'
        ]},
        {'2.集群某一节点的主从全数宕机':[
            '构建不成哈希槽区间[0, 16383]'
        ]}
    ]}
],
'扩容':[
    '可采用翻倍扩容，迁移数据量较小，50%'
],
'集群扩容和缩容':[
    '节点的加入和下线，槽和数据在节点之间的移动',
    {'迁移数据完整流程':[
        '',
        '',
        '',
        ''
    ]}
],
'客户端路由':[
    {'三种情况':[
        '槽命中:直接返回(cluster keyslot key可以直接算出槽)',
        '槽不命中：moved异常(slot迁移完）',
        '槽不命中：ask重定向(slot迁移中）'
    ]},
    'JedisCluster客户端':[
        '采用直连方式',
        {'初始化':[
            '从集群中选一个可运行的节点，使用cluster slots初始化槽和节点映射',
            '将cluster slots的结果映射到本地，为每个节点创建JedisPool，每个Redis单点都设置一个redis连接池',
            '即初始化设置成单例：内置了所有节点的连接池'
        ]},
        {'执行命令':[
            'JedisCluster内部缓存了slots和node的关系',
            '1.通过key可计算出slot，由此知道目标节点',
            '2.直接先连接目标节点',
            '3.如目标节点成功响应，结束',
            {'4.如连接出错,随机选择一个节点':[
                '返回ask异常:对连接进行重定向，然后进行重试',
                '返回moved异常:进行缓存的刷新'
            ]}
        ]}
    ]

]


}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 