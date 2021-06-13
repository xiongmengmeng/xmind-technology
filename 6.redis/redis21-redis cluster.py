import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="redis"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("redis cluster")
r2=s2.getRootTopic()
r2.setTitle("redis cluster")


content={
'集群伸缩':[
    '节点的加入和下线，槽和数据在节点之间的移动',
    {'集群扩容':[
        '1. 准备新节点',
        '2. 加入集群',
        '3. 迁移槽和数据',
    ]},
    {'集群收缩，节点下线步骤':[
        '1.槽迁移：下线节点的槽和节点数据迁移到在线节点上',
        '2.忘记节点',
        '3.关闭节点'
    ]}
],
'客户端路由':[
    {'三种情况':[
        '槽命中:直接返回(cluster keyslot key可以直接算出槽)',
        '槽不命中+slot迁移中：ask重定向',
        '槽不命中+slot迁移完：moved异常'
    ]},
    {'JedisCluster客户端':[
        '采用直连方式',
        {'初始化':[
            '从集群中选一个可运行的节点，使用cluster slots初始化槽和节点映射',
            '将cluster slots的结果映射到本地，为每个节点创建JedisPool，每个Redis单点都设置一个redis连接池',
            '即初始化设置成单例：内置了所有节点的连接池'
        ]},
        {'执行命令':[
            'JedisCluster内部缓存了slots和node的关系',
            '1.通过key可计算出slot，由此知道目标节点',
            '2.直接连接目标节点',
            '3.如目标节点成功响应，结束',
            {'4.如连接出错,随机选择一个节点':[
                '返回ask异常:对连接进行重定向，然后重试',
                '返回moved异常:进行缓存的刷新'
            ]}
        ]}
    ]}
]
}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 