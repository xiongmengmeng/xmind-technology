import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
xmind_name="dubbo"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("dubbo")
r2=s2.getRootTopic()
r2.setTitle("dubbo")


content={
# '接囗代理':[
#     '入囗ReferenceConfig.get()',
# ],
# '注册中心':[
#     {'zk':[
#         'root:dubbo',
#         'service:接囗全量限定名',
#         'type:consumers,prividers,configuration,route',
#         'url',
#     ]}
# ],
# '负载均衡':[
#     {'RandomLoadBalance':[
#         '随机',
#         {'按权重设置随机概率':[
#             '1.权重相加',
#             '2.在权重总内，取随机数'
#         ]}
#     ]},
#     {'RoundRobinLoadBalance':[
#         '轮询',
#         '按公约后的权重设置轮询比率'
#     ]},
#     {'LeastActiveLoadBalance':[
#         '最少活跃调用数',
#         'count，待处理请求，取最小的',
#         '相同活跃数的权重随机'
#     ]},
#     {'ConsistentHashLoadBalance':[
#         '一致性hash',
#         '相同参数请求总是发到同一提供者'
#     ]}
# ],
# '容错机制':[
#     {'FailoverCluster':[
#         '失败自动切换',
#         '自动重试其它服务器',
#         'FailoverClusterInvoker#doInvoke'
#     ]},
#     {'FailfastCluster':[
#         '快速失败',
#         '立即报错，只发起一次调用'
#     ]},
#     {'FailsafeCluster':[
#         '失败安全',
#         '出现异常，直接忽略'
#     ]},
#     {'FailbackCluster':[
#         '失败自动恢复',
#         '记录失败请求，定时重发'
#     ]},
#     {'ForkingCluster':[
#         '并行调用多个服务器，只要一个成功即返回',
#     ]},
#     {'BroadcastCluster':[
#         '广播逐个调用所有提供者，任意一个报错则报错',
#     ]},
# ],
'RPC协议':[
    {'各种博文性能测试报告分析':[
        '1KPOJO场景下',
        'dubbo序列化+netty的TPS值更高',
        '但到了50kPOJO场景下',
        'dubbo序列化+netty就没邓优势',
        {'估计一个对象的大小':[
            {'对象头':[
                '64位机，指针压缩尾部下12字节'
            ]},
            {'对象体':[
                '假设字段为所有数据类型各一个',
                'boolean:1字节',
                'byte:1字节',
                'short:2字节',
                'char:2字节',
                'int:4字节'
                'float:4字节',
                'long:8字节',
                'double:8字节'
            ]},
            {'共计':[
                '46+6(字节填充，保证8字节对齐)'
            ]}
        ]}
    ]},
    {'Dubbo协议':[
        '单一长连接与NIO异步通讯',
        '适用小数据量，大并发的服务调用',
        '不适用传递大数据量，如文件，视频',
        {'两部分':[
            '协议头',
            '协议体'
        ]},
        {'Header(16字节数组)':[
            {'Magic':[
                '一个固定的特殊标志',
                '2字节'
            ]},
            {'Flag':[
                '区分请求/响应/序列化方式',
                '1字节'
            ]},
            {'Status':[
                '请求执行后的响应状态',
                '1字节'
            ]},
            {'messageId':[
                '序列号，第几次请求',
                '消费者与提供者间是一条基于TCP长连接的通道',
                'messageId将请求响应一一对应起来',
                '8字节'
            ]},
            {'bodyLength':[
                'Body内容长度',
                '4字节'
            ]},

        ]},
        {'请求Body':[
            {'RPC版本':[
                '2.0.1'
            ]},
            {'服务接囗路径':[
                'com.study.dubbo.DemoService'
            ]},
            {'服务版本号':[
                '0.0.0'
            ]},
            {'服务方法名':[
                'test'
            ]},
            {'参数描述符':[
                'Ljava/lang/String;'
            ]},
            {'参数值序列化':[
                '123'
            ]},
            {'Dubbo内置参数':[
                '{}'
            ]},

        ]},
        {'响应Body':[
            {'响应结果类型':[
                ''
            ]},
            {'返回值':[
                ''
            ]},
            {'':[
                ''
            ]},
        ]}
    ]}
],
}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 