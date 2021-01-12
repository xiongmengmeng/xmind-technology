import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="thread"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("分布式锁")
r2=s2.getRootTopic()
r2.setTitle("分布式锁")


content={

'Redisson+RLock':[
    'Redisson：java的Redis客户端之一，官网推荐的java语言实现分布式锁的项目',
    'RedissonLock类：分布式锁的实现代码，对映RLock 接口',
    '源码中加锁、释放锁等操作使用Lua脚本来完成的',
    '如客户端是一个Redis集群,会根据Hash节点选择一台机器,发送一段Lua脚本到Redis上',
    {'LUA代码参数':[
        'KEYS[1]:加锁的Key',
        'ARGV[1]:锁Key的默认生存时间，默认30秒',
        'ARGV[2]:加锁的客户端的ID，类：8743c9c0-0795-4907-87fd-6c719a6b4586:1',
    ]},
    {'加锁机制':[
        '1.判断加锁的key是否存在：exists KEYS[1]',
        '2.不存在，设置一个Hash数据结构，hset KEYS[1] ARGV[2]',
        '3.设置KEYS[1]锁的生存时间是30秒，加锁完成'
    ]},
    {'锁互斥机制':[
        '1.判断加锁的key是否存在',
        '2.存在,判断KEYS[1]锁的Hash数据结构中，是否存在客户端2的ARGV[2]',
        '3.不存在，返回锁的剩余生存时间'
    ]},
    {'watch dog自动延期机制':[
        '客户端1加锁成功，会启动一个watchdog看门狗',
        '这个后台线程，会每隔10秒检查一下，如客户端1还持有锁，会延长锁Key的生存时间'
    ]},
    {'可重入加锁机制':[
        '1.判断加锁的key是否存在',
        '2.不存在，判断KEYS[1]锁的Hash数据结构中，是否存在客户端2的ARGV[2]',
        '3.存在，对客户端1的加锁次数，累加1',
        'incrby myLock 8743c9c0-0795-4907-87fd-6c71a6b4586:11'
    ]},
    {'释放锁机制':[
        '每次都对myLock数据结构中的那个加锁次数减1',
        '如发现加锁次数是0，说明这个客户端已不再持有锁',
        '此时用：“del myLock”命令，从Redis里删除这个Key'
    ]},
    {'缺点':[
        'Master宕机->主备切换->可能导致多客户端对一个分布式锁完成了加锁'
    ]}
],
'ZooKeeper':[
    '使用框架Curator',
    {'原理':[
        '1.在锁节点下创建一个接一个的临时顺序节点',
        '2.如自己不是第一个节点，就对自己上一个节点加监听器',
        '3.只要上一个节点释放锁，自己就排到前面去，相当于是一个排队机制'
    ]},
    '用临时顺序节点,如某客户端创建临时顺序节点后宕机，ZK感知到那个客户端宕机:',
    '会自动删除对应的临时顺序节点，相当于自动释放锁，或者是自动取消自己的排队'
],
'分布式锁并发能力不能，如要提高并发能力，可考虑分段':[]





}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 