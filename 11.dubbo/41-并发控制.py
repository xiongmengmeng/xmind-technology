import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
xmind_name="dubbo"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("并发控制")
r2=s2.getRootTopic()
r2.setTitle("并发控制")


content={
'线程模型':[
    {'两种线程':[
        {'网络IO线程':[
            '用于接收网络请求，处理网络请求accept,connection,read,write相关事件',
            '防止其阻塞，阻塞，就无法再处理新的网络请求'
        ]},
        {'业务线程':[
            '处理复杂的业务逻辑'
        ]}
    ]},
    {'消费派遣方式(5种)':[
        {'1.all':[
            '所有消息【请求,响应,连接,断开,心跳检测】均派发到业务线程池',
            '<dubbo:protocol name="" dipatcher="all" threadpool="fixed" threads="100"/>'
        ]},
        {'2.direct':[
            '所有消息均不派发到业务线程池,都在IO线程上执行'
        ]},
        {'3.message':[
            '【请求,响应】消息派发到业务线程池,其它在IO线程上执行',
            '<dubbo:protocol name="" dipatcher="message" threadpool="cached" />'
        ]},
        {'4.execution':[
            '【请求】消息派发到业务线程池,其它在IO线程上执行'
        ]},
        {'5.connection':[
            '【连接,断开】消息派发到业务线程池,其它在IO线程上执行'
        ]},
    ]},
    {'线程池配置':[
        {'fixed':[
            '默认'
        ]},
        {'cached':[
            '空间一分钟自动删除，需要时重建'
        ]},
        {'limited':[
            '可伸缩线程池,中线程数只增加不收缩',
            '避免收缩时突然来了大流量引起性能问题'
        ]},
        {'eager':[
            '优化创建Work线程池',
            '任务大于maxinumpoolsize时，将任务放入阻塞队列',
            '区别与jdk的线程池'
        ]},
    ]}
],
'并发控制':[
    {'提供者':[
        {'方法级占用线程数控制':[
            '超过时抛异常,可用mock来承接，用来限流',
            '<dubbo:service interface="" executes="10"/>',
            '   <dubbo:method name="" executes="10"/>',
            '</dubbo>'
        ]},
        {'方法级占用连接数控制':[
            '连接请求数，如使用单一长连接，可限制客户端数量',
            '参数actives'
        ]}
    ]},
    {'消费者---并发的负载均衡':[
        '消费者如何识别每台提供者的并发情况？',
        '配置loadbalance来调整提供者的并发压力',
        'leastactive负载均衡策略，调用最小并发数的提供者',
        {'使用':[
            '<dubbo:service interface="" loadbalance="leastactive"/>',
        ]}
    ]}
],
'连接控制':[
    {'限制提供者接受的连接不超过10个':[
        '<dubbo:protocol protocol="dubbo" accepts="10"/>',
        '<dubbo:service interface="dubbo" connections="10"/>',
        '<dubbo:reference interface="dubbo" connections="10"/>',
    ]},
],
'粘滞连接与延迟连接':[
    {'粘滞连接':[
        '用于有状态的服务',
        '尽量让消费者总是向同一提供者发起调用',
        '将自动开启延迟连接，以减少长连接数'
    ]},
    {'延迟连接':[
        '用于减少长连接数',
        '当有调用发起时再创建长连接',
        '只对使用长连接的dubbo协议生效',
        '<dubbo:protocol name="dubbo" lazy="true"/>'
    ]}
]
}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 