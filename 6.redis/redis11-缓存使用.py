import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="redis"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("缓存使用")
r2=s2.getRootTopic()
r2.setTitle("缓存使用")


content={
'缓存使用':[
    {'新增':[
        '先操作数据库，再操作缓存',
        '防止先操作缓存，再操作数据库失败，缓存中出现脏数据'
    ]},
    {'更新':[
        '1.如有更新数据,先删除缓存，'
        '2.再更新数据库',
        '3.再删除一次缓存，防止1到2前有查询操作，新增了缓存（脏数据）',
        '当然还是有出问题的可能性',
        {'为什么是删除缓存，而不是更新缓存':[
            '更新数据可能影响到了多张表',
            '在复杂点的缓存场景，更新一条数据，可能影响多条缓存数据',
            '如缓存key：广州-收货点，value:广州-萝岗-收货点的路线',
            '删掉广州-萝岗的路线，整个路线数据都要删掉'
        ]},
        {'更新缓存的几种设计模式':[
            '1.先删除缓存，在更新数据库',
            '2.Cache aside：先更新数据库，再删除缓存',
            '3.Read/Write Through:应用的读写请求都直接与缓存服务打交道,缓存中数据变更的时候是同步去更新数据库的',
            '4.Write Behind Caching:更新数据的时候，只更新缓存，不更新数据库，而缓存会异步地批量更新数据库',
        ]}
    ]},
    {'查询':[
        '1.读取缓存中是否有相关数据',
        '2.如果缓存中有相关数据value，则返回',
        '3.如果缓存中没有相关数据，则从数据库读取相关数据放入缓存中key->value，再返回',
    ]},
],
'redis 支持的java客户端都有哪些':[
    {'jedis':[
        '指令全面，不支持异步，非线程安全，需要使用jedis连接池，大多时候用他'
    ]},
    {'Redisson':[
        '异步调用，线程安全，基于netty框架',
        '实现了分布式和可扩展的Java数据结构，功能较简单，不支持字符串操作,排序、事务、管道、分区等'
    ]},
    'Lettuce'
]

}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 