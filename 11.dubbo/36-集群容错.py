import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
xmind_name="dubbo"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("集群容错")
r2=s2.getRootTopic()
r2.setTitle("集群容错")


content={
'路由Router':[
    '决定一次dubbo服务调用的目标服务器',
    {'分类':[
        '对应dubbo-admin中三种不同的规则配置方式',
        {'条件路由':[
            '用户使用Dubbo定义的语法规则去写路由规则;文件路由则；脚本路由则是'
        ]},
        {'文件路由':[
            '需用户提交一个文件,里面写着对应的路由规则，框架基于文件读取对应的规则'
        ]},
        {'脚本路由':[
            '使用JDK自身的脚本引擎解析路由规则脚本，所有JDK脚本引擎支持的脚本都能解析，默认是JavaScrip'
        ]}
    ]},
    {'类':[
        {'RouterFactor':[
            'ConditionRouterFactory',
            'FileRouterFactory',
            'ScriptRouterFactory'
        ]},
        {'Router':[
            'ConditionRouter',
            'MockInvokerRouter',
            'ScriptRouter'
        ]}
    ]},
    {'参数规则':[
        '使用的是 condition://协议',
        {'URL 形式':[
            'condition:// 0.0.0.0/com.fbo.BarService?category=routers&dynamic=false&rule=n +',
            'URL.encode(host = 10.20.153.10 => host = 10.20.153.11")',
            '路由规则会用URL.encode进行编码',
            {'基于条件表达式的路由规则':[
                '=>前：消费者匹配条件',
                '=>后：提供者匹配条件'
            ]},
        ]}
    ]}
],
'负载均衡LoadBalance':[
    {'RandomLoadBalance':[
        '随机',
        {'按权重设置随机概率':[
            '1.权重相加',
            '2.在权重总内，取随机数'
        ]}
    ]},
    {'RoundRobinLoadBalance':[
        '轮询',
        {'平滑加权轮询':[
            '每个服务器对应两个权重，weight(固定)和currentWeight(会动态调整,初始值为0)',
            '有新的请求进来，遍历服务器列表，让它的currentWeight加上⾃身权重',
            '遍历完成，找到最⼤的currentWeight，并将其减去权重总和，然后返回相应的服务器'
        ]}
    ]},
    {'LeastActiveLoadBalance':[
        '最少活跃调用数',
        'count，待处理请求，取最小的',
        '相同活跃数的权重随机'
    ]},
    {'ConsistentHashLoadBalance':[
        '一致性hash',
        '相同参数请求总是发到同一提供者'
    ]},
],
'Mock':[
    '消费者调用接囗时使用',
    {'使用':[
        '<dubbo:reference id="" mock="" interface=""/>'
    ]},
    {'触发时机':[
        '容错机制不能处理故障时，调用mock实现'
    ]},
    {'应用':[
        '测试',
        '数据托底->服务降级'
    ]},
    '接口配置了 Mock,在RPC调用抛出RpcException时就会执行Mock方法',
    '服务降级在dubbo-admin中通过override协议更新Invoker的Mock参数实现',
    {'Mock参数':[
        {'force:return+null':[
            '强制Mock,让消费者对该服务的调用直接返回null,不再发起远程调用',
            '使用在非重要服务己不可用时，可屏蔽下游对上游系统造成的影响'
        ]},
        {'fail:return+null':[
            '消费者还是会发起远程调用，不过失败后会返回null,但是不抛出异常'
        ]}
    ]},
    'MockClusterWrapper'
]


}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 