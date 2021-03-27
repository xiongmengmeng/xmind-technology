import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="redis"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("分布式锁")
r2=s2.getRootTopic()
r2.setTitle("分布式锁")


content={
'分布式锁的实现':[
    '基于数据库',
    'memcached',
    'Redis',
    'zookeeper'
],
'核心理念':[
    '加锁',
    '解锁',
    '锁超时'
],
'zookeeper锁':[
    '基于zookeeper临时有序节点实现',
    '客户端对某方法加锁，在zookeeper上的与该方法对应的指定节点目录下，生成一个唯一的瞬时有序节点',
    '判断是否获取锁:判断有序节点中序号最小的一个',
    '释放锁：将瞬时节点删除'
],
'redis实现一个分布式锁(不可重入)':[
    {'加锁':[
        '给Key键设置一个值，为避免死锁，并给定一个过期时间',
        '命令执行成功，则证明客户端获取到了锁',
        {'SET lock_key random_value NX PX 5000':[
            'random_value:客户端生成的唯一的字符串',
            'NX:只在键不存在时，才对键进行设置操作',
            'PX 5000:设置键的过期时间为5000毫秒'
        ]}
    ]},
    {'解锁':[
        '当客户端id为random_value，删除key',
        {'1.lua脚本':[
            'if redis.call("get",KEYS[1]) == ARGV[1] then ',
            '   return redis.call("del",KEYS[1]) ',
            'else',
            '   return 0 ',
            'end',
        ]},
        '2.jedis.eval来执行上段LUA'
    ]}
],
'redisson实现分布式锁':[
    '引入redisson',
    {'获取锁实例':[
        'RLock lock = client.getLock("lock1")',
        '返回一个RedissonLock对象'
    ]},
    {'加锁':[
        'boolean lockStatus = lock.tryLock();',
        {'redis内部加锁逻辑':[
            '1.通过exists判断，如果锁不存在，则设置值和过期时间，加锁成功',
            '2.通过hexists判断，如果锁已存在，并且锁的是当前线程，则证明是重入锁，加锁成功',
            '3.如果锁已存在，但锁的不是当前线程，则证明有其他线程持有锁。返回当前锁的过期时间，加锁失败'
        ]}
    ]},
    {'解锁':[
        'if (lock.isLocked()) {',
        '   if (lock.isHeldByCurrentThread()) {',
        '       lock.unlock();',
        '   }',
        '}',
        {'redis内部解锁逻辑':[
            '1.如果锁已经不存在，通过publish发布锁释放的消息，解锁成功',
            '2.如果解锁的线程和当前锁的线程不是同一个，解锁失败，抛出异常',
            '3.通过hincrby递减1，先释放一次锁',
            '4.若剩余次数还大于0，则证明当前锁是重入锁，刷新过期时间',
            '5.若剩余次数小于0，删除key并发布锁释放的消息，解锁成功'
        ]}
    ]},
],
'学习':[
    'redissionlock锁：https://www.jianshu.com/p/47fd7f86c848',
    'http://blog.itpub.net/31545684/viewspace-2221023/'
]



}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 