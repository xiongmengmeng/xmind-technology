import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="Gateway"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("Gateway使用")
r2=s2.getRootTopic()
r2.setTitle("Gateway使用")


content={
'引入依赖':[
    '//gateway网关',
    'spring‐cloud‐starter‐gateway',
    '//nacos服务注册与发现',
    'spring‐cloud‐starter‐alibaba‐nacos‐discovery'
],
'配置':[
    'gateway:discovery:locator:false(默认)',
    '设为true开启通过微服务创建路由的功能，即可以通过微服务名访问服务',
    'enabled: true',
    '是否开启网关',
    {'路由断言工厂（Route Predicate Factories）配置':[
        {'时间匹配':[
            '用在限时抢购的一些场景中',
            {'routes':[
                'id: order_route #路由ID，全局唯一',
                'uri: http://localhost:8020 #目标微服务的请求地址和端口',
            ]},
            {'predicates':[
                '测试：http://localhost:8888/order/findOrderByUserId/1',
                '匹配在指定的日期时间之后发生的请求 入参是ZonedDateTime类型',
                'After=2021‐01‐31T22:22:07.783+08:00[Asia/Shanghai]'
            ]}
        ]},
        {'Cookie匹配':[
            'Cookie=username, fox'
        ]},
        {'Header匹配':[
            'Header匹配:请求中带有请求头名为x‐request‐id，其值与\d+正则表达式匹配',
            'Header=X‐Request‐Id, \d+'
        ]},
        {'路径匹配':[
            'Path=/order/** Path路径匹配'
        ]},
        {'自定义路由断言工厂':[
            '继承AbstractRoutePredicateFactory类，重写apply方法'
        ]}
    ]},
    {'过滤器工厂(GatewayFilter Factories)配置':[
        {'添加请求头':[
            'filters:',
            'AddRequestHeader=X‐Request‐color, red #添加请求头',
        ]},
        {'添加请求参数':[
            'AddRequestParameter=color, blue #添加请求参数'
        ]},
        {'为匹配的路由统一添加前缀':[
            'PrefixPath=/mall‐order # 添加前缀 对应微服务需要配置context‐path'
        ]},
        {'自定义过滤器工厂':[
            '继承AbstractNameValueGatewayFilterFactory,重写apply方法'
        ]}
    ]}
]

}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 