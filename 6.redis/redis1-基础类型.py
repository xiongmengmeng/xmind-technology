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
'字符串类型':[
    '适用场景:递增数字incr key 来生成订单号，缓存、计数器、分布式锁',
    '赋值：set key value',
    '取值：get key'
],
'散列类型':[
    '适用场景：用户信息、Hash 表等',
    '存储结构化的数据，比如一个对象',
    '赋值(不区分新增或更新)：hset key field value',
    'hmset key field1 value1 field2 value2',
    '取值：hmget key field1',
    'hmget key field1 field2'
],
'列表类型':[

    '内部使用双向链表，向两端添加元素的时间复杂度为O(1)',
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
'集合类型':[
    '适用场景:去重、赞、踩、共同好友',
    '内部使用值为空的散列表实现',
    '增加/删除元素:sadd key member1 member2',
    'srem key member1 member2',
    '获得集合中的所有元素:smembers key'
],
'有序集合类型':[
    '适用场景:访问量排行榜、点击量排行榜等',
    '使用散列表和跳跃表实现，即使访问中间数据也很快，时间复杂度O(log(N))',
    '增加元素(score可以是浮点数，+inf,-inf表示正无穷和负无穷）',
    'zadd key score member score1 member1',
    '获得元素分数 :zscore key membe'
]

    
}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 