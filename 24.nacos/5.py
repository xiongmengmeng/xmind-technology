import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="Sentinel"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("Ribbon")
r2=s2.getRootTopic()
r2.setTitle("Feign")


content={
'接口调用':[
     {'1.Httpclient':[
        'Apache Jakarta Common下的子项目',
        '支持HTTP协议最新版本',
    ]},
    {'2.Okhttp':[
        '一个处理网络请求的开源项目，安卓端最火的轻量级框架，由Square公司贡献',
        '拥有简洁的API、高效的性能',
    ]},
    {'3.HttpURLConnection':[
        'Java的标准类，它继承自URLConnection',
        '使用比较复杂，不像HttpClient那样容易使用',
    ]},
    {'4.RestTemplate':[
        'Spring提供的用于访问Rest服务的客户端',
        '提供了多种便捷访问远程HTTP服务的方法',
    ]},
],
'Feign':[
    'Netflix开发的声明式、模板化的HTTP客户端',
    {'Spring Cloud openfeign':[
        '对Feign进行了增强，使其支持Spring MVC注解',
        '整合了Ribbon和Eureka，从而使得Feign的使用更加方便',
    ]},
    {'设计架构':[
        '1.基于面向接囗的动态代理方式生成实现类',
        '2.根据接囗类的注解声明规则，解析出底层MethodHandler',
        '3.基于RequestBean,动态生成Request',
        '4.Encoder将Bean包装成请求',
        '5.拦截器负责对请求和返回进行装饰处理',
        '6.日志记录',
        '7.基于重试器发送http请求，可基于不同的http框架处理'
    ]}
],
'单独使用':[
    {'引入依赖':[
        'com.netflix.feign.feign‐core',
        'com.netflix.feign.feign‐jackson'
    ]},
    {'编写接口':[
        '方法上添加@Headers(),@RequestLine()'
    ]},
    {'调用':[
    ]},
],
'整合Spring Cloud Alibaba':[
    {'1.引入依赖':[
        'spring‐cloud‐starter‐openfeign'
    ]},
    {'2.编写调用接口+@FeignClient注解':[
        '接囗上添加@FeignClient(value = "mall‐order",path = "/order")',
        '方法上添加@RequestMapping("/findOrderByUserId/{userId}")'
    ]},
    {'3.调用端在启动类上添加@EnableFeignClients注解':[
    ]},
    {'4.发起调用':[
        '像调用本地方式一样调用远程服务',
    ]},
],
'自定义配置':[
    {'日志配置':[
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
    ]},
    {'拦截器配件':[
        '自定义拦截器：实现RequestInterceptor接囗，重写apply()方法',
        'feign:client:config:requestInterceptors[0]: xxxRequestInterceptor'
    ]},
    {'超时时间配置':[
        'feign:client:config:mall‐order:',
        '# 连接超时时间，默认2s',
        'connectTimeout: 5000',
        '# 请求处理超时时间，默认5s',
        'readTimeout: 10000'
    ]},
    {'客户端组件配置':[
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
    ]},
    {'编码器解码器配置':[
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
    ]}
],

}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 