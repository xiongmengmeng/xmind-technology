import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
xmind_name="dubbo"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("dubbo使用")
r2=s2.getRootTopic()
r2.setTitle("dubbo使用")


content={
'学习内容':[
    '高并发',
    '高可扩展',
    '高性能',
    '序列化/反序列化',
    '网络',
    '多线程',
    '设计模式的问题'
],
'依赖':[
    {'必需依赖':[
        'jdk1.6'
    ]},
    {'可选依赖':[
        'dubbo',
        'spring',
        'netty',
        'javassist'
    ]}
],
'三种配置方式':[
    {'1.dubbo注解':[
        {'启动类':[
            '@EnableDubbo(scanBasePackages = "edu.dongnao.study.dubbo.provider ")',
            '@PropertySource("classpath:/dubbo/dubbo-provider.properties")',
            '@PropertySource("classpath:/dubbo/dubbo-consumer.properties")'
        ]},
        {'消费方':[
            '@Reference'
        ]},
        {'提供方':[
            '@Service'
        ]}
    ]},
    {'2.集成spring xml':[
        '无侵入性，方便后续改用其他RPC框架',
        "<dubbo:reference id='' interface=''/>",
        "<dubbo:service ref='' interface=''/>",
    ]},
    {'3.原生API':[
        '测试API使用'
    ]}
],
'springboot集成dubbo':[
    {'第一种':[
        '引入jar',
        {'启动类上':[
            '@EnableDubbo'
        ]},
        {'yml文件中配置':[
            'dubbo:application:name',
            'dubbo:registry:address',
            'dubbo:protocol:name',
            'dubbo:protocol:port'
        ]}
    ]},
    {'第二种':[
        '引入jar',
        {'yml文件中配置':[
            '第一种的配置...',
            'dubbo:scan:base-packages'
        ]}
    ]}
]
}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 