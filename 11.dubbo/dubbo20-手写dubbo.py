import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
xmind_name="dubbo"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("手写dubbo")
r2=s2.getRootTopic()
r2.setTitle("手写dubbo")


content={
'RPC':[
    '远程调用过程',
    '一个计算机能行协议',
    '一个分布式服务框架，致力于提供高性能和透明化的RPC远程服务调用方案，以及SOA服务治理方案'
],
'dubbo':[
    '一款高性能的RPC框架',
    {'优点':[
        {'面向接囗代理':[
            '以接囗为粒度'
        ]},
        '服务自动注册和发现',
        {'自动负载均衡':[
            '注册中心+客户端路由'
        ]},
        {'可扩展能力':[
            '注册中心选择',
            'RPC调用协议选择'
        ]},
        '运行期流量调度',
        {'可视化服务治理和运维':[
            '监控'
        ]}
    ]}
],
'手写模拟DUBBO':[
    {'Provider模块':[
        '提供API，实现API',
        '服务本地注册',
        '服务注册中心注册',
        '暴露(启动tomcat,nettyServer)'
    ]},
    {'Consumer模块':[
        '拿接囗从注册中心获取服务地址',
        '调用服务'
    ]},
    {'Registry模块':[
        '保存服务配置信息(服务名：List<URL>)'
    ]},
    {'RpcProtocol模块':[
        '基于Tomcat的HttpProtocol',
        '基于Netty的DubboProtocol'
    ]},
    {'Framework模块':[
        '框架实现'
    ]}
],
'Registry模块':[
    {'本地服务注册中心':[
        'LocalMapRegister类',
        {'参数':[
            'Map<String,Class> map=new HashMap();'
        ]},
        {'registry(String interface,Class implClass)方法':[
            '将传参放入map中'
        ]},
        {'get(String interface)方法':[
            'return map.get(interface)'
        ]}
    ]},
    {'远程服务注册中心':[
        'RemoteMapRegister类',
        {'参数':[
            'Map<String,List<URL>> map=new HashMap();'
        ]},
        {'registry(String interface,URL url)方法':[
            '将传参放入map中',
            '并保存到本地文件(让另一项目可获取)'
        ]},
        {'get(String interface)方法':[
            'return map.get(interface)'
        ]}
    ]},
],


}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 