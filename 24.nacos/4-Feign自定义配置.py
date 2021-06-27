import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="nacos"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("Feign自定义配置")
r2=s2.getRootTopic()
r2.setTitle("Feign自定义配置")


content={
'日志配置':[
    'feign:client:config:loggerLevel:FULL',
    {'日志等级有4种':[
        {'NONE':[
            '【性能最佳，适用于生产】',
            '不记录任何日志（默认值）'
        ]},
        {'BASIC':[
            '【适用于生产环境追踪问题】',
            '仅记录请求方法、URL、响应状态代码以及执行时间'
        ]},
        {'HEADERS':[
            '记录BASIC级别的基础上',
            '记录请求和响应的header'
        ]},
        {'FULL':[
            '【适用于测试环境定位问题】',
            '记录请求和响应的header、body和元数据'
        ]},
    ]}
],
'拦截器配件':[
    '自定义拦截器：实现RequestInterceptor接囗，重写apply()方法',
    'feign:client:config:requestInterceptors[0]: xxxRequestInterceptor'
],
'超时时间配置':[
    'feign:client:config:mall‐order:',
    '# 连接超时时间，默认2s',
    'connectTimeout: 5000',
    '# 请求处理超时时间，默认5s',
    'readTimeout: 10000'
],
'客户端组件配置':[
    {'默认':[
        '使用JDK原生的URLConnection发送HTTP请求'
    ]},
    '可以集成别的组件来替换掉URLConnection，比如Apache HttpClient，OkHttp',
    'Feign发起调用真正执行逻辑：feign.Client#execute （扩展点）',
    {'配置Apache HttpClient':[
        {'引入依赖':[
            'httpclient',
            'feign‐httpclient'
        ]},
        {'修改yml配置':[
            'feign:httpclient:enabled:true'
        ]},
        {'测试':[
            '调用会进入feign.httpclient.ApacheHttpClient#execute'
        ]},
        '配置可参考源码:org.springframework.cloud.openfeign.FeignAutoConfiguration'
    ]}
],
'编码器解码器配置':[
    {'扩展点':[
        'Encoder',
        'Decoder'
    ]},
    {'yml配置方式':[
        'feign:client:config:',
        '# 配置编解码器',
        'encoder: feign.jackson.JacksonEncoder',
        'decoder: feign.jackson.JacksonDecoder',
    ]}
]


}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 