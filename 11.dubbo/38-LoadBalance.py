import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
xmind_name="dubbo"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("LoadBalance")
r2=s2.getRootTopic()
r2.setTitle("LoadBalance")


content={
'LoadBalance':[
    '类注解:@SPI("random")',
    {'<T> Invoker<T> select(List<Invoker<T>> var1, URL var2, Invocation var3)':[
        '方法注解:@Adaptive({"loadbalance"})',
    ]},
],
'AbstractLoadBalance':[
    '类注解：@SPI("netty")',
    {'getWeight(Invoker<?> invoker, Invocation invocation)':[
        '是获取当前Invoker的权重'
    ]},
    {'calculateWarmupWeight(int uptime, int warmup, int weight)':[
        '计算具体的权重',
        '考虑了服务刚启动的时候需要有一个预热的过程,逐步分配流量'
    ]},
    {'select(List<Invoker<T>> invokers, URL url, Invocation invocation)':[
        {'invokers是一个':[
            'invokers.get(0)'
        ]},
        {'invokers不是一个':[
            'this.doSelect(invokers, url, invocation)'
        ]}
    ]},
    {'doSelect(List<Invoker<T>> var1, URL var2, Invocation var3)':[
        '模版方法，给子类实现'
    ]}
],
'RandomLoadBalance':[
    {'doSelect(List<Invoker<T>> invokers, URL url, Invocation invocation)':[
        {'1.计算总权重并判断每个Invoker的权重是否一样':[
            '遍历整个Invoker列表',
            '求和总权重',
            '在遍历过程中，会对比每个Invoker的权重，判断所有Invoker的权重是否相同'
        ]},
        {'2.如权重相同':[
            '每个Invoker的概率都一样，直接用nextlnt随机选一个'
        ]},
        {'3.如权重不同':[
            '首先得到偏移值，然后根据偏移值找到对应的Invoker'
        ]}
    ]},
],
'RoundRobinLoadBalance':[
    {'平滑轮询的算法':[
        '在轮询时会穿插选择其他节点',
        '让整个服务器选择的过程比较均匀，不会“逮住”一个节点一直调用'
    ]},
    '1.每次请求做负载均衡时，会遍历所有可调用的节点（Invoker列表）',
    '2.对于每个Invoker,让它的current = current + weight',
    '3.累加每个Invoker 的 weight 到 totalWeight,即 totalweight = totalweight + weight',
    '4.遍历完所有Invoker后，current值最大的节点就是本次要选择的节点',
    '5.最后,把该节点的 current 值减去 totalWeight,即 current = current - totalweight'
    '6.循环1-5的过程'
],
'LeastActiveLoadBalance':[
    '最少活跃调用数负载均衡',
    '使用要配合ActiveLimitFilter过滤器来计算每个接口方法的活跃数',
    {'ActiveLimitFilter':[
        '只要进来一个请求，该方法的调用的计数就会原子性+1',
        '整个Invoker调用过程会包在try-catch-finally中',
        '无论调用结束或出现异常，finally中都会把计数原子-1。该原子计数就是最少活跃数'
    ]}
],
'ConsistentHashLoadBalance':[
    '一致性Hash负载均衡'
]

}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 