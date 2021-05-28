import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="redis"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("其他数据类型")
r2=s2.getRootTopic()
r2.setTitle("其他数据类型")


content={
# '基础命令':[
#     '获得符合规则的键名列表（*:多个字符，？：一个字符）:keys *',
#     '判断一个键是否存在 exists key',
#     '删除键,不支持通配符 del key',
#     '获得键值的数据类型 type key'
# ],
'bitmap':[
    '位图,byte 数组,用二进制表示,只有0和1两个数字',
    {'原理':[
        '8位=8bit=1byte=1b=1字节 = 0.001kb',
        '通过对bit进行0或1的设置，表示某个元素对应的值'，
        '本质是string类型数据',
    ]},
    {'命令':[
        'setbit key offset value:返回该位在setbit之前的值,value只能取0或1',
        'getbit key offset:对key所存储的字符串值，取指定偏移量上的位（bit）'
    ]},
    {'使用场景':[
        '用户在线状态:一个key，用户id为偏移量offset，如在线设置为1，不在线设置为0，3亿用户只需36MB空间,可考虑分片，10w分一片',
        '统计活跃用户:时间作为缓存的key，然后用户id为offset，如果当日活跃过就设置为1,之后通过bitOp进行二进制计算算出在某段时间内用户的活跃情况'
    ]},
    {'优势':[
        '基于最小的单位bit进行存储，省空间',
        '设置时时间复杂度O(1)、读取时时间复杂度O(n)，操作非常快',
        '二进制数据的存储，计算非常快'
    ]},
    {'缺点':[
        'redis中bit映射被限制在512MB之内，最大是2^32位',
        '建议每个key的位数都控制下，因读取时候时间复杂度O(n)，越大的串读时间花销越多'
    ]}
],
'Geospatial 地理位置':[
    {'命令':[
        'geoadd key longitude latitude member:将给定的空间元素（纬度、经度、名字）添加到指定的键里面',
        'geopos key member: 从键里面返回所有给定位置元素的位置（经度和纬度）',
        'geodist key member1 member2 km:返回两个给定位置之间的距离',
        'georadius key member 300 km   :以给定的经纬度为中心， 返回与中心的距离不超过给定最大距离的所有位置元素',
        'geohash key member:返回一个或多个位置元素的 Geohash 表示',
    ]},
    '本质是zset类型数据',
    '学习：https://www.imooc.com/article/288961'
],
'Hyperloglog（基数）':[
    {'命令':[
        'pfadd key value:添加值',
        'pfcount key：统计值',
        'pfmerge newKey key1 key2:合并key1,key2到newKey'
    ]},
    '本质是string类型数据',
    '使用场景：统计页面访客量',
    '缺点：HyperLogLog的计数统计是有一定的误差的，误差最大在1%以下',
],
'血液':[
    '以上三种数据结构本质也是六种数据结构中的一种'
]
# 'LUA脚本':[
#     '减少网络开销（一个脚本只发送一个请求）',
#     '原子操作',
#     '可复用',
#     'https://blog.csdn.net/qq_39172525/article/details/105779727'
# ],
    
}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 