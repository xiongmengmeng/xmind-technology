import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="netty"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("分布式缓存Redis")
r2=s2.getRootTopic()
r2.setTitle("分布式缓存Redis")


content={
'Jedis':[
    '一个高性能的Java客户端，是Redis官方推荐的Java开发工具',
    '一个Jedis对象代表一条和Redis服务进行连接的Socket通道'
],
'JedisPool连接池':[
    {'大连接数maxTotal':[
        '业务QPS/单连接的QPS = 最大连接数',
        '在实际的生产场景中，还要预留一些资源，通常来讲所配置的maxTotal要比理论值大一些',
        '如果连接数确实太多，可以考虑Redis集群，那么单个Redis节点的最大连接数的公式为：maxTotal = 预估的连接数 / nodes节点数'
    ]},
    {'maxIdle实际上才是业务可用的最大连接数':[
        '使得连接池达到最佳性能的设置是maxTotal = maxIdle',
        '尽可能避免由于频繁地创建和销毁Jedis连接所带来的连接池性能的下降'
    ]},
    '刚创建好的连接池，以最小空闲数量为JedisPool进行预热',
    '由于Jedis类实现了java.io.Closeable接口，故而在JDK 1.7或者以上版本中可以使用try-with-resources语句，在其隐藏的finally部分自动调用close方法'
],
'spring-data-redis':[
    '在Maven的pom文件中加上spring-data-redis库的依赖',
    '配置spring-data-redis库的连接池实例和RedisTemplate模板实例',
    'RedisTemplate模板API'
],
'SpringEL':[
    'Spring Expression Language,提供一种强大、简洁的Spring Bean的动态操作表达式',
    'JSP页面的表达式使用${}进行声明。而SpringEL表达式使用#{}进行声明',
    '一般来说，SpringEL表达式使用#{}进行声明。但是，不是所有注解中的SpringEL表达式都需要#{}进行声明'
]
}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 