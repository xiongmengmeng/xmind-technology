import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="swagger"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("swagger")
r2=s2.getRootTopic()
r2.setTitle("swagger")


content={
'swagger：在线生成接囗文档，Knife4j在swagger基础上做了封装，用户体验更好',
'与ssm项目整合':[
    {'1.在maven项目的pom.xml中引入Knife4j的依赖包':[
        '<dependency>',
        '   <groupId>com.github.xiaoymin</groupId>',
        '   <artifactId>knife4j-spring-mvc</artifactId>',
        '   <version>2.0.5</version>',
        '</dependency>'
    ]},
    {'2.创建Swagger配置依赖(生产环境禁用，通过swagger.enablep实现)':[
        '@Configuration',
        '@EnableSwagger2',
        '@EnableKnife4j',
        'public class SwaggerConfig extends WebMvcConfigurationSupport{',
        '   @Value("${swagger.enable:false}")',
        '   private Boolean swaggerEnable;'
        '   @Bean',
        '   public Docket api() {',
        '       return new Docket(DocumentationType.SWAGGER_2).',
        '           .enable(swaggerEnable)',
        '           .apiInfo(apiInfo())',
        '           ...',
        '           .build();',
        '}'
    ]},
    {'3.xml文件中配置':[
        '<bean class="com.baturu.config.SwaggerConfig" />',
        '<mvc:resources location="classpath:/META-INF/resources/" mapping="doc.html"/>',
        '<mvc:resources location="classpath:/META-INF/resources/webjars/" mapping="/webjars/**"/>'
    ]},
    {'4.web.xml':[
        'DispatcherServlet只处理/的数据'
    ]}
],
'knife4j':[
    'https://doc.xiaominfo.com/knife4j/documentation/get_start.html',
    'https://blog.csdn.net/emprere/article/details/104352171?utm_medium=distribute.pc_relevant_t0.none-task-blog-BlogCommendFromMachineLearnPai2-1.control&dist_request_id=1328627.10429.16153613956335291&depth_1-utm_source=distribute.pc_relevant_t0.none-task-blog-BlogCommendFromMachineLearnPai2-1.control'
]
}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 