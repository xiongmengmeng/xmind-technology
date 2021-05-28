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
    {'lock()':[
        'lockInterruptibly()->',
        'lockInterruptibly(-1, null)->'
    ]},
    {'lockInterruptibly(long leaseTime, TimeUnit unit)':[
        'Long ttl = tryAcquire(leaseTime, unit, threadId)',
    ]},
    {'tryAcquire(long leaseTime, TimeUnit unit, long threadId)':[
        'get(tryAcquireAsync(leaseTime, unit, threadId))'
    ]},
    {'tryAcquireAsync(long leaseTime, TimeUnit unit, final long threadId)':[
        {'1.异步执行lua脚本':[
            'tryLockInnerAsync(commandExecutor.getConnectionManager().getCfg().getLockWatchdogTimeout(), TimeUnit.MILLISECONDS, threadId, RedisCommands.EVAL_LONG)',
            '返回值RFuture<Long> ttlRemainingFuture'
        ]},
        {'2.加监听器，回调相关方法':[
            'ttlRemainingFuture.addListener()',
            {'回调方法operationComplete(Future<Long> future)':[
                'scheduleExpirationRenewal(threadId)'
            ]},
            {'scheduleExpirationRenewal(final long threadId)':[
                '1.创建一个任务TimerTask，延时执行，默认10s执行一次,作用是将锁过期时间延长',
                {'2.执行的脚本':[
                    {"判断锁是否还存在":[
                        "if (redis.call('hexists', KEYS[1], ARGV[2]) == 1)"
                    ]},
                    {'将过期时间重新设置为初始值':[
                        "redis.call('pexpire', KEYS[1], ARGV[1])"
                    ]}
                ]},
                '3.调用2的方法，实现递归'
            ]}
        ]}
    ]},
    {'tryLockInnerAsync(long leaseTime, TimeUnit unit, long threadId, RedisStrictCommand<T> command)':[
        '异步执行一段lua脚本',
        {'变量':[
            'KEYS[1]',
            'ARGV[1]:过期时间,默认30s',
            'ARGV[2]:线程id'
        ]},
        {'1.如果key为KEYS[1]的变量不存在':[
            "if (redis.call('exists', KEYS[1]) == 0)"
        ]},
        {'2.给变量赋值(线程id)并设置过期时间':[
            "redis.call('hset', KEYS[1], ARGV[2], 1)",
            "redis.call('pexpire', KEYS[1], ARGV[1])",
            "return nil"
        ]},
        {'3.如果key为KEYS[1]的变量存在':[
            "if (redis.call('hexists', KEYS[1], ARGV[2]) == 1)",
        ]},
        {'4.value值加1':[
            "redis.call('hincrby', KEYS[1], ARGV[2], 1)",
            "redis.call('pexpire', KEYS[1], ARGV[1])",
            "return nil"
        ]},
        {'5.返回值':[
            "return redis.call('pttl', KEYS[1])"
        ]}
    ]}
],
'学习':[
    'redissionlock锁：https://www.jianshu.com/p/47fd7f86c848',
    'http://blog.itpub.net/31545684/viewspace-2221023/'
],
'redisson学习文档':[
    'https://github.com/redisson/redisson/wiki'
],



}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 