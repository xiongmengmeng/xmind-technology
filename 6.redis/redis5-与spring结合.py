import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="redis"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("与spring结合")
r2=s2.getRootTopic()
r2.setTitle("与spring结合")


content={
'与spring结合':[
    'RedisTemplate:自动从RedisConnectionFactory工厂中获取连接，然后执行对应的Redis命令，在最后还会关闭Redis的连接',
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