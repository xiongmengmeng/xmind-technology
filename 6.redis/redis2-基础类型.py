import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="redis"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("数据类型")
r2=s2.getRootTopic()
r2.setTitle("数据类型")


content={

'基础命令':[
    '获得符合规则的键名列表（*:多个字符，？：一个字符）:keys *',
    '判断一个键是否存在 exists key',
    '删除键,不支持通配符 del key',
    '获得键值的数据类型 type key'
],
'字符串类型string':[
    {'内存优化':[
        'String类型中的数字，有一个数字常量池'
    ]},
    {'适用场景':[
        '递增数字incr key,生成订单号',
        '分布式锁'
    ]},
    '赋值：set key value',
    '取值：get key'
],
'散列类型hash':[
    {'数据结构':[
        'zipmap压缩字典，几乎与ziplist一致，只是中间放了keyLen-key-valueLen-value，dict也就是hashtable'
    ]},
    {'适用场景':[
        '存储结构化的数据，如用户信息'
    ]},
    '赋值(不区分新增或更新)：hset key field value',
    'hmset key field1 value1 field2 value2',
    '取值：hmget key field1',
    'hmget key field1 field2'
],
'列表类型list':[
    {'数据结构':[
        'ziplist压缩数组',
        'linkedList双链表,两端添加元素的时间复杂度为O(1)'
    ]},
    {'适用场景':[
        '1.适合用来记录日志，加入新日志速度很快',
        '2.搭配lpush和lpop，把列表当做栈',
        '3.搭配lpush和rpop,把列表当做队列',
        '4.使用lrange实现分页',
        '5.微博关注人时间轴列表等'
    ]},
    '向两端增加元素:lpush key value1 value2',
    'rpush key value1 value2',
    '从列表两端弹出元素:lpop key',
    'rpop key'
],
'集合类型set':[
    {'数据结构':[
        '其实是hash类型，value放nil'
    ]},
    {'适用场景':[
        '去重、赞、踩、共同好友'
    ]},
    '增加/删除元素:sadd key member1 member2',
    'srem key member1 member2',
    '获得集合中的所有元素:smembers key'
],
'有序集合类型sorted set':[
    {'数据结构':[
        'ziplist压缩数组',
        'skipList跳表,访问中间数据也很快，时间复杂度O(log(N))'
    ]},
    {'适用场景':[
        '访问量排行榜',
        '点击量排行榜'
    ]},
    '增加元素(score可以是浮点数，+inf,-inf表示正无穷和负无穷）',
    'zadd key score member score1 member1',
    '获得元素分数 :zscore key membe'
],
'特殊类型':[
    'bitmaps，GEO，hyperLogLog'
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
    
}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 