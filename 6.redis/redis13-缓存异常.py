import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="redis"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("缓存异常")
r2=s2.getRootTopic()
r2.setTitle("缓存异常")


content={
'缓存预热':[
    '系统上线后将缓存数据加载到redis',
    '目的:避免高并发流量对数据库造成压力',
    {'解决':[
        '提供一个接囗来初始化热点数据到缓存系统',
        '上线脚本时，当项目启动完成后，自动调用接口'
    ]}
],
'缓存降级':[
    '并发量大增，影响到核心流程',
    '目的：防止Redis服务故障，导致数据库雪崩,保证核心服务可用'
],
'缓存异常':[
    {'缓存击穿':[
        '前提：缓存没有但数据库有数据（缓存到期）',
        '现象：并发查询数据，大量数量请求压力落在数据库上',
        {'解决':[
            {'对key加锁并排队':[
                '判断缓存没有，对key加锁，查缓存，查数据库，放缓存，释放锁',
                '第一个请求查数据库，放缓存',
                '后续请求直接查缓存'
            ]},
            '热点数据永不过期'

        ]}
    ]},
    {'缓存穿透':[
        '前提：缓存，数据库都没有，请求落到数据库上',
        '现象：并发查询不存在的key,，大量数量请求压力落在数据库上',
        {'解决':[
            '1.设置过滤器（使用布隆过滤器），将所有key哈希到一个足够大的bitmap中',
            '不存在的key会被这个bitmap拦截掉',
            '2.对请求进行鉴权，防止恶意请求'
        ]}
    ]},
    {'缓存雪崩':[
        '前提：缓存同一时间大面积失效',
        '现象：并发查询一批数据，大量数量请求压力落在数据库上',
        {'解决':[
            '缓存数据的过期时间+随机值'
        ]}
    ]},
]

}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 