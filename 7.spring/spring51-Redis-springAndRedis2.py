import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="spring"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("spring-redis(下)")
r2=s2.getRootTopic()
r2.setTitle("spring-redis(下)")


content={


'几个关键注解':[
    {'@Cacheable':[
        '标注在方法上，将方法返回的结果存入缓存中',
        '可指定cachename或value来对ConcurrentMapCache的name属性进行设置',
        '可通过keyGenerator制定缓存键值对中生成key的规则',
        {'@Cacheable工作原理':[
            {'第一次查询':[
                '1.ConcurrentMapCacheManager.getCache(String name)',
                '查看cacheMap中是否存在名为emp的Cache',
                '如存在返回这个cache',
                '如不存在，以传入的name作为cache的name创建并返回',
                '2.由于第一次查，缓存中不存在停止，会执行真正的查询方法，调用数据库操作',
                '3.返回结果后，调用cache.put(Object key, @Nullable Object value)，把信息，以键值对的方式存入cache中',
            ]},
            {'第二次查询':[
                '1.进入ConcurrentMapCacheManager的getCache方法查找cache,因为第一次的操作，cacheMap中存在名为emp的cache，直接返回cache',
                '2.调用cache.lookup(Object key)，通过键查找值',
                '3.将查找到的值返回，没有调用实际的数据库操作'
            ]},
            {'总结':[
                '在第一次查询时，会创建cache，然后调用方法，最后将方法的返回值存入cache',
                '查找相同内容时直接从cache中获取，无需调用方法操作数据库来查找'
            ]}
        ]}
    ]},
    {'@CachePut':[
        '标注在方法上，先执行方法，再用方法返回的值来更新缓存内容'
    ]},
    {'@CacheEvict':[
        '清除缓存'
    ]},
    {'@Caching':[
        '复杂的cache配置，可在里面配置上面几个注解'
    ]},
    {'@CacheConfig':[
        '标注在类上，对类中的缓存操作作统一配置'
    ]},
    {'@EnableCaching:开启基于注解的缓存':[
        '类注解：@Import(CachingConfigurationSelector.class)',
        {'CachingConfigurationSelector类':[
            '实现ImportSelector接囗，重写selectImports(AnnotationMetadata importingClassMetadata)方法',
            '导入类AutoProxyRegistrar，会注册InfrastructureAdvisorAutoProxyCreator(实现AbstractAutoProxyCreator)',
            '导入类ProxyCachingConfiguration,封装advisor'
        ]}
    ]}
],
'整合Redis':[
    '1.加入redis的startor，加入相关redis的类',
    '2.创建配置类(可选):jedisPoolConfig->redisConnectionFactory->redisTemplate'
]
}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 