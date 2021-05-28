import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
xmind_name="dubbo"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("dubbo配置")
r2=s2.getRootTopic()
r2.setTitle("dubbo配置")


content={
'配置类型(4类)':[
    {'应用配置信息':[
        {'ApplicationConfig':[
            '配置当前应用，不管提供者都还是消费者'
        ]},
        {'RegistryConfig':[
            '配置注册中心'
        ]},
        {'MonitorConfig':[
            '配置监控中心'
        ]},
        {'ModuleConfig':[
            '配置当前模块'
        ]},
    ]},
    {'客户消费端':[
        {'ConsumerConfig':[
        ]},
        {'ReferenceConfig':[
            {'属性':[
                'ConsumerConfig consumer'
            ]},
            {'get()':[
                '创建一个远程服务代理',
                '一个引用可指向多个注册中心'
            ]}
        ]},
    ]},
    {'服务提供端':[
        {'ProviderConfig':[
        ]},
        {'ProtocolConfig':[
            '配置提供服务的协议',
            '协议由提供者指定，消费者被动接受'
        ]},
        {'ServiceConfig':[
            {'属性':[
                'ProviderConfig provider'
            ]},
            '暴露一个服务，定义服务的元信息',
            '一个服务可用多协议暴露，注册到多个注册中心'
        ]},
    ]},
    {'公用配置':[
        {'MethodConfig':[
            {'属性':[
                'List<ArgumentConfig> arguments'
            ]},
            'serviceConfig和ReferenceConfig指定方法级的配置信息'
        ]},
        {'ArgumentConfig':[
            {'属性':[
                'Integer index',
                'String type',
                'Boolean callback'
            ]},
            '方法参数配置'
        ]},
    ]}, 
],
'不同粒度配置的覆盖关系':[
    '方法>接囗>全局',
    '级别一样，消费方>提供方',
    '提供者配置通过URL经由注册中心传递给消费者',
    '例：以timeout为例'
],
'配置来源(4种)':[
    {'JVM System properties配置':[
        '-D参数',
        '-Ddubbo.registry.dubbo=zookeeper://127.0.0.1:1281'
    ]},
    {'Externalized Configuration外部化配置':[
        'Externalized Configuration',
        'dubbo.properties在外部平台存储',
        '外部平台，如nacos,apollo',
        'dubbo.registry.dubbo=zookeeper://127.0.0.1:1281'
    ]},
    {'spring/API配置':[
        'ServiceConfig,ReferenceConfig等编程接囗采集的配置',
        'RegistryConfig.setAddress("127.0.0.1:1281")',
    ]},
    {'本地文件配置':[
        'dubbo.registry.dubbo=zookeeper://127.0.0.1:1281'
    ]},
],
'加载流程':[
    '按预定优先级->',
    '自动实现配置间的覆盖->',
    '所有配置汇总到数据总线URL->',
    '驱动后续的服务暴露，引用流程'
],
# '配置项(3类)':[
#     '1.服务发现',
#     '2.服务治理',
#     '3.性能优化',
#     '可去官网的配置文档查看'
# ],
}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 