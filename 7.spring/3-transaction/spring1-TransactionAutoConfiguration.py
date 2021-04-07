import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="Transaction"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("TransactionAutoConfiguration")
r2=s2.getRootTopic()
r2.setTitle("TransactionAutoConfiguration")


content={
'入囗':[
    'pom.xml引入spring-boot-autoconfigure包(',
    'org.springframework.boot.autoconfigure.EnableAutoConfiguration=',
    'org.springframework.boot.autoconfigure.transaction.TransactionAutoConfiguration',
    'org.springframework.boot.autoconfigure.transaction.jta.JtaAutoConfiguration'
],
'TransactionAutoConfiguration':[
    {'类注解':[
        '@Configuration',
        '@ConditionalOnClass(PlatformTransactionManager.class)',
        '@AutoConfigureAfter({ JtaAutoConfiguration.class, HibernateJpaAutoConfiguration.class',
        '  DataSourceTransactionManagerAutoConfiguration.class',
        '  Neo4jDataAutoConfiguration.class })',
        '@EnableConfigurationProperties(TransactionProperties.class)',
        {'解释':[
            '@ConditionalOnClass(PlatformTransactionManager.class)',
            '类路径下包含PlatformTransactionManager类,即引入spring-tx包,这个自动配置生效',
            '@AutoConfigureAfter():配置在括号中的4个配置类后才生效',
            '使TransactionProperties类上@ConfigurationProperties生效，作用同在类上加@Component'
        ]}
    ]},
    {'2个内部类':[
        {'TransactionTemplateConfiguration':[
            '事务模板配置类',
            '如果没有定义TransactionOperations,创建一个TransactionTemplate'
        ]},
        {'EnableTransactionManagementConfiguration':[
            '开启事务管理器配置类',
            '支持2种代理方式',
            'JdkDynamicAutoProxyConfiguration',
            'CglibAutoProxyConfiguration',
            '默认没有spring.aop.proxy-target-class=true',
            '走的Cglib代理,说明@Transactional注解支持直接加在类上',
        ]}
    ]}
]
}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 