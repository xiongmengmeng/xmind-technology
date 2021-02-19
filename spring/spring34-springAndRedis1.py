import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="spring"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("spring-redis(上)")
r2=s2.getRootTopic()
r2.setTitle("spring-redis(上)")


content={
'核心接囗':[
    'CachingProvider：管理并创建CacheManager，一个CachingProvider可管理多个CacheManager',
    'CacheManager：管理并创建Cache，一个CacheManager管理多个Cache  ',
    'Cache：结构类似于Map<CacheName,Cache>，每个Cache有唯一的名字',
    'Entry：结构类似于Map<KeyObject,ValueObject>，以键值对的形式储存在Cache中',
    'Expiry：Cache中每个条目都有有效期，过期则会被删除或更新'
],
'SpringBoot是通过XXXAutoConfiguration来向容器中注册组件的':[
    'spring.factories->CacheAutoConfiguration'
],
'CacheAutoConfiguration':[
    '类注解:@Import({ CacheConfigurationImportSelector.class, CacheManagerEntityManagerFactoryDependsOnPostProcessor.class })'
],
'CacheConfigurationImportSelector':[
    '实现ImportSelector接囗',
    {'重写selectImports(AnnotationMetadata importingClassMetadata)方法':[
        '无配置情况下，使用SimpleCacheConfiguration作为缓存配置类（默认）'
    ]},
],
'SimpleCacheConfiguration':[
    {'@ConditionalOnMissingBean(CacheManager.class)':[
        '当容器中存在CacheManager时，本配置类不会生效',
    ]},
    '发现配置类中注册了ConcurrentMapCacheManager作为CacheManager',
    'ConcurrentMapCacheManager:有ConcurrentMap<String, Cache> cacheMap(管理的Cache结构)',
    'ConcurrentMapCache:两个属性，name为cache的名字，store用于储存键值对'
],
'RedisCacheConfiguration':[
    '@AutoConfigureAfter(RedisAutoConfiguration.class)：而RedisAutoConfiguration也要在redis相关类加载后才能加载',
    {'RedisAutoConfiguration':[
        '@ConditionalOnClass(RedisOperations.class):加入redis相关jar包后，才会有',
        '@Import({JedisConnectionConfiguration.class }):JedisConnectionConfiguration里会创建RedisConnectionFactory',
        '@ConditionalOnMissingBean(name = "redisTemplate"):创建redisTemplate'
    ]}
]
}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 