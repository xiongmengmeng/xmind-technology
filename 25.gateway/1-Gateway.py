import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="Sentinel"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("Gateway")
r2=s2.getRootTopic()
r2.setTitle("Gateway")


content={
'Spring Cloud Gateway':[
    '是Spring Cloud官方推出的第二代网关框架(取代Zuul)',
    '由WebFlux + Netty + Reactor实现的响应式API网关',
    {'注':[
        '不能在传统的servlet容器中工作，也不能构建成war包'
    ]},
    {'目的':[
        '提供一种简单且有效的 API 路由的管理方式',
        '基于Filter方式提供网关的基本功能，例如说安全认证、监控、限流等等'
    ]}
],
'核心概念':[
    {'路由（route)':[
        '网关中最基础的部分',
        '路由信息包括一个ID、一个目的URI、一组断言工厂、一组Filter组成',
        '如果断言为真，则说明请求的URL和配置的路由匹配'
    ]},
    {'断言(predicates)':[
        '断言函数类型是Spring5.0框架中的ServerWebExchange',
        '断言函数允许开发者去定义匹配Http request中的任何信息，比如请求头和参数等'
    ]},
    {'过滤器（Filter)':[
        '分为Gateway FilIer和Global Filter',
        'Filter可以对请求和响应进行处理'
    ]},
],
'过程':[
    '客户端向Spring Cloud Gateway发出请求',
    '如请求与网关程序定义的路由匹配，则该请求就会被发送到网关Web处理程序',
    '此时处理程序运行特定的请求过滤器链',
    '过滤器可能会在发送代理请求的前后执行逻辑',
    '所有pre过滤器逻辑先执行，然后执行代理请求；代理请求完成后，执行 post 过滤器逻辑',
    {'类似于springMVC':[
        'springMvc--------spring webFlux',
        'dispatchservlet--------dispatchservlet',
        'handlermapping--------handlermapping(处理路由)',
        'handleradapter--------handleradapter',
        'handler--------webhandler(包含过滤器，此处过滤器是增强作用)'
    ]}
],
'':[
    {' 引入依赖':[
        '//gateway网关',
        'spring‐cloud‐starter‐gateway',
        '//nacos服务注册与发现',
        'spring‐cloud‐starter‐alibaba‐nacos‐discovery'
    ]},
    {'':[
        '',
        'gateway:discovery:locator:
        '#默认false，设为true开启通过微服务创建路由的功能，即可以通过微服务名访问服务'
        'enabled: true',
        '#是否开启网关'
        'enabled: true',
        {' 路由断言工厂（Route Predicate Factories）配置':[
            {'时间匹配':[
                '用在限时抢购的一些场景中',
                '',
                '',
                '',
                'routes:
                'id: order_route #路由ID，全局唯一
                'uri: http://localhost:8020 #目标微服务的请求地址和端口
                'predicates:
                '# 测试：http://localhost:8888/order/findOrderByUserId/1
                '# 匹配在指定的日期时间之后发生的请求 入参是ZonedDateTime类型
                'After=2021‐01‐31T22:22:07.783+08:00[Asia/Shanghai]'
            ]},
            {'Cookie匹配':[
                'Cookie=username, fox'
            ]},
            {'Header匹配':[
                '#Header匹配 请求中带有请求头名为 x‐request‐id，其值与 \d+ 正则表达式匹配',
                'Header=X‐Request‐Id, \d+'
            ]},
            {'路径匹配':[
                'Path=/order/** #Path路径匹配'
            ]},
            {'自定义路由断言工厂':[
                '继承 AbstractRoutePredicateFactory 类，重写 apply 方法的逻辑'
            ]}
        ]},
        {'过滤器工厂（ GatewayFilter Factories）配置':[
            {'添加请求头':[
                'filters:',
                'AddRequestHeader=X‐Request‐color, red #添加请求头',
            ]},
            {'添加请求参数':[
                'AddRequestParameter=color, blue # 添加请求参数'
            ]},
            {'为匹配的路由统一添加前缀':[
                'PrefixPath=/mall‐order # 添加前缀 对应微服务需要配置context‐path'
            ]},
            {'自定义过滤器工厂':[
                '继承AbstractNameValueGatewayFilterFactory,重写 apply 方法'
            ]}
            '',
            '',
            ''
        ]}
    ]}
]

}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 