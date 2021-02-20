import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="redis_summary"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("redis")
r2=s2.getRootTopic()
r2.setTitle("redis")


content={
'五种基础类型':[
    {'基础命令':[
        '获得符合规则的键名列表（*:多个字符，？：一个字符）:keys *',
        '判断一个键是否存在 exists key',
        '删除键,不支持通配符 del key',
        '获得键值的数据类型 type key'
    ]},
    {'字符串类型':[
        '适用场景:递增数字incr key 来生成订单号',
        '赋值：set key value',
        '取值：get key'
    ]},
    {'散列类型':[
        '存储结构化的数据，比如一个对象',
        '赋值(不区分新增或更新)：hset key field value',
        'hmset key field1 value1 field2 value2',
        '取值：hmget key field1',
        'hmget key field1 field2'
    ]},
    {'列表类型':[
        '内部使用双向链表，向两端添加元素的时间复杂度为O(1)',
        {'用处':[
            '1.适合用来记录日志，加入新日志速度很快',
            '2.搭配lpush和lpop，把列表当做栈',
            '3.搭配lpush和rpop,把列表当做队列',
            '4.使用lrange实现分页'
        ]},
        '向两端增加元素:lpush key value1 value2',
        'rpush key value1 value2',
        '从列表两端弹出元素:lpop key',
        'rpop key'
    ]},
    {'集合类型':[
        '内部使用值为空的散列表实现',
        '增加/删除元素:sadd key member1 member2',
        'srem key member1 member2',
        '获得集合中的所有元素:smembers key'
    ]},
    {'有序集合类型':[
        '使用散列表和跳跃表实现，即使访问中间数据也很快，时间复杂度O(log(N))',
        '增加元素(score可以是浮点数，+inf,-inf表示正无穷和负无穷）',
        'zadd key score member score1 member1',
        '获得元素分数 :zscore key membe'
    ]}
],
'事务，生存时间，排序，消息，管道':[
    {'事务':[
        'multi…exec',
        'multi后的命令，redis会把其存入事务队列，当执行exec时，提交事务队列中的命令',
        '语法错误，全部命令都不会执行，运行错误，别的命令依旧继续执行'
    ]},
    {'生存时间':[
        '命令：设置过期时间 expire key sec',
        '用处：1.实现访问频率限制,2.实现缓存————session存储和过期'
    ]}
],
'数据结构':[
    'Redis的键值都使用redisObject结构体保存',
    {'redisObject':[
        'refcount：键值被引用数量',
        'type字：键值的数据类型',
        'encoding：键值的内部编码方式',
        'lru: lru time',
        'ptr:指向sdshdr类型的变量的地址'
    ]},
    {'sdshdr类型的变量':[
        '来存储字符串',
        'len：字符串的长度',
        'free：buf中的剩余空间',
        'buf：字符串的内容'
    ]}
],
'LUA脚本':[
    '减少网络开销（一个脚本只发送一个请求）',
    '原子操作',
    '可复用',
    'https://blog.csdn.net/qq_39172525/article/details/105779727'
],
'持久化':[
    {'RDB':[
        'redis默认采用',
        '符合条件时redis会自动将内存中的数据进行快照并存储到磁盘',
        'dump.rdb文件',
        '快照条件:save 900 1 (900秒内至少有一个键被更改)',
        '快照过程:fork函数，使用写时复制（copy-on-write)策略',
        '加载：redis启动后会读取RDB快照文件，将数据从磁盘载入内存',
        '风险:redis异常退出，会丢失最后一次快照后的更改数据'
    ]},
    {'AOF(append only file)':[
        '每次执行更改数据的操作，都会将命令记录在AOF文件',
        '纯文本文件，内容为redis客户端向redis发送的原始通信协议内容',
        '通过参数appendonly yes 开启，默认文件appendonly.aof',
        '风险:操作系统的缓存机制，数据并没有真正写入磁盘，而是进入系统的磁盘缓存，默认30s同步一次',
        '通过参数优化此行为:appendfsync everysec(默认)，每秒执行一次同步操作'
    ]}
],
'复制':[
    '目的：避免单点故障,读写分离，提高服务器负载',
    {'过程':[
        '从库启动后，向主库发送sync命令',
        '主库收到命令，在后台保存快照和缓存快照期间的命令,发送给从库',
        '从库先载入快照文件，并执行收到的缓存命令'
    ]}
],
'与spring结合':[
    'RedisTemplate:自动从RedisConnectionFactory工厂中获取连接，然后执行对应的Redis命令，在最后还会关闭Redis的连接。',
    {'序列化器':[
        'Spring提供了RedisSerializer接口,它有两个方法:',
        'serialize：把那些可以序列化的对象转换为二进制字符串',
        'deserialize：通过反序列化把二进制字符串转换为Java对象'
    ]},
    'StringRedisSerializer和JdkSerializationRedisSerializer(RedisTemplate默认的序列化器)',
    {'对Redis数据类型操作的封装':[
        '获取地理位置操作接口:redisTemplate.opsForGeo()',
        '获取散列操作接口:redisTemplate.opsForHash()',
        '获取基数操作接口:redisTemplate.opsForHyperLogLog()',
        '获取列表操作接口 redisTemplate.opsForList()',
        '获取集合操作接口 redisTemplate.opsForSet()',
        '获取字符串操作接口 redisTemplate.opsForValue()',
        '获取有序集合操作接口 redisTemplate.opsForZSet()'
    ]},
    '对某一个键值对（key-value）做连续的操作:BoundXXXOperations接口',
    {'回调':[
        'SessionCallback接口:提供了良好的封装，对于开发者比较友好，因此在实际的开发中应该优先选择使用它',
        'RedisCallback接口:接口比较底层，需要处理的内容也比较多，可读性较差，所以在非必要的时候尽量不选择使用它'
    ]}
],
'与springboot结合':[
    'https://blog.csdn.net/qq_39172525/article/details/106343275',
],
'Lua脚本':[
    'RedisScript接口',
    '获取脚本的Sha1 String getSha1()',
    '获取脚本返回值 Class<T> getResultType()',
    '获取脚本的字符串 String getScriptAsString()'
]

    
}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 