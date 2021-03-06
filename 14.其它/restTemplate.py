import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="restTemplate"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("restTemplate")
r2=s2.getRootTopic()
r2.setTitle("restTemplate")


content={
'1.基础':[
    'HTTP请求的同步阻塞式的客户端',
    '非spring环境，引入spring-web',
    'spring环境，引入spring-boot-starter-web',
    '底层实现可配置，Apache HttpComponents，okHttp，HttpURLConnection'
],
'2.底层HTTP客户端实现类库':[
    'SimpleClientHttpRequestFactory:对应的HTTP库是java JDK自带的HttpURLConnection',
    'HttpComponentsAsyncClientHttpRequestFactory。对应的HTTP库是Apache HttpComponents',
    'OkHttp3ClientHttpRequestFactory。对应的HTTP库是OkHttp',
    '通过设置setRequestFactory方法，来切换RestTemplate的底层HTTP客户端实现类库'
],
'3.HTTP GET请求':[
    'getForObject(),返回值是HTTP协议的响应体',
    {'getForEntity()':[
        '返回的是ResponseEntity(对HTTP响应的封装)',
        'responseEntity.getBody()获取响应体',
        'responseEntity.getStatusCode(); 获取整体的响应状态信息',
        'responseEntity.getStatusCodeValue(); 获取响应码值',
        'responseEntity.getHeaders(); 获取响应头'
    ]},
    '占位符,map传参'
],
'4.HTTP POST请求':[
    '主要方法同上',
    '请求头：new HttpHeaders()',
    '参数：可能pojo对象，可以map',
    '组装请求 new HttpEntity<MultiValueMap<String, String>>(map, headers);'
],
'5.DELETE,PUT请求':[
    '通用请求方法exchange方法',
    '专注于获取HTTP请求头:headForHeaders()',
    '获取HTTP资源支持的method:optionsForAllow()'
],
'6.文件上传和下载':[
    '文件上传:new FileSystemResource(new File(filePath))',
    '文件下载:接收类型为byte[].class',
    {'大文件下载':[
        '设置请求头APPLICATION_OCTET_STREAM，以流的形式进行数据加载',
        'RequestCallback结合File.copy保证了接收到一部分文件内容，就向磁盘写入一部分内容'
    ]}
],
'7.自定义请求失败异常处理':[
    {'ResponseErrorHandler':[
        'RestTemplate请求结果的异常处理器接口',
        '方法hasError用于判断HttpResponse是否是异常响应（通过状态码）',
        '方法handleError用于处理异常响应结果（非200状态码段）'
    ]},
    'DefaultResponseErrorHandler是ResponseErrorHandler的默认实现',
    {'自定义异常处理':[
        '创建MyRestErrorHandler,实现ResponseErrorHandler 接口',
        '将MyRestErrorHandler在RestTemplate实例化的时候进行注册'
    ]}
],
'8.自动重试':[
    'maven引入spring-retry,aspectjweaver',
    'Spring Boot应用启动类加@SpringRetry注解',
    '业务方法加@Retryable注解，注意注解的参数'
],
'9.HttpBasic认证':[
    '1.用户名密码使用Base64模式进行加密',
    '2.请求头中，authorization：加密后密码',
    '3.服务器收到请求，BasicAuthenticationFilter过滤器提取authorization值',
    '4.解码结果与登录验证的用户名密码匹配，成功则继续过滤器后续的访问',
    '客户端优化，拦截器方式携带认证信息'
],
'10.使用代理作为跳板发送请求':[
    'SimpleClientHttpRequestFactory上设置代理',
    'RestTemplate代理使用者'
],
'学习内容来源':[
    'http://www.zimug.com/tag/resttemplate'
]

    
}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 