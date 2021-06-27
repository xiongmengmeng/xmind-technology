import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
xmind_name="dubbo"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("限流功能的过滤器")
r2=s2.getRootTopic()
r2.setTitle("限流功能的过滤器")


content={
'ActiveLimitFilter':[
    '限制消费者端的最大并行数',
    {'作用范围':[
        '消费者'
    ]},
    {'使用参数':[
        'actives'
    ]},
    {'代码逻辑':[
        '1.获取方法名、最大并发数等参数',
        '2.当并发数达到阈值，加锁抢占当前接口的RpcStatus对象，然后通过wait方法等待',
        '2.1某个Invoker调用结束，把计数器原子-1触发一个notify,wait状态的线程被唤醒继续执行逻辑',
        '2.2wait等待超时都没有被唤醒，直接抛出异常',
        '3.满足调用阈值，直接进行调用，成功或失败都会把计数器原子-1,唤醒一个等待中的线程',
    ]}
],
'ExecuteLimitFilter':[
    '限制服务端的最大并行数',
    {'作用范围':[
        '服务提供者'
    ]},
    {'使用参数':[
        'executes'
    ]},
    {'原理':[
        '1.使用一个ConcurrentMap缓存了并发数的计数器',
        'key:每个请求URL生成一个IdentityString',
        'value:RpcStatus对象,于记录对应的并发数',
        '2.过滤器中，会以try-catch-finally的形式调用过滤器链的下一个节点',
        '3.开始调用前，会通过URL获得RpcStatus对象，把对象中的并原子计数器+1',
        'finally中再将原子-1',
        '在计数器+1时，发现当前计数比设置的最大并发数大时，抛出异常'
    ]}
],
'TpsLimitFilter':[
    '用于服务端的限流',
    {'作用范围':[
        '服务提供者'
    ]},
    {'原理':[
        '基于令牌',
        '一个时间段内只分配N个令牌，每个请求过来都会消耗一个令牌，耗完，后面的请求会被拒绝',
        {'限流对象的维度':[
            '支持分组、版本和接口级别',
            '默认通过interface +group+version作为唯一标识'
        ]},
        {'配置':[
            '每次发放1000个令牌',
            '<dubbo:parameter key="tps" value="1000" />',
            '令牌刷新的间隔是1秒，如果不配置，则默认是60秒',
            '<dubbo:parameter key="tps.interval" value="1000" />'
        ]}
    ]},
    {'实现逻辑':[
        'DefaultTPSLimiter#isAllowable',
        '1.获取URL中的参数，包含每次发放的令牌数、令牌刷新时间间隔',
        '2.如果设置了每次发放的令牌数则开始限流校验',
        '一个ConcurrentMap缓存每个接口的令牌数',
        'key是interface + group + version',
        ',value是一个Statitem对象，包装了令牌刷新时间间隔、每次发放的令牌数等属性',
        '3.判断上次发放令牌的时间点到现在是否超过时间间隔',
        '如超过了就重新发放令牌，之前没用完的不会叠加，而是直接覆盖',
        '然后通过CAS的方式-1令牌，减掉后令牌数如果小于0则会触发限流',
    ]}
]


}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 