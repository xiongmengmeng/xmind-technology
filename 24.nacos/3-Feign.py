import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="nacos"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("Feign")
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
        '方法上添加@RequestMapping("/findOrderByUserId/userId")'
    ]},
    {'3.调用端在启动类上添加@EnableFeignClients注解':[
    ]},
    {'4.发起调用':[
        '像调用本地方式一样调用远程服务',
    ]},
],


}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 