import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="spring"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("spring事务")
r2=s2.getRootTopic()
r2.setTitle("spring事务")


content={
'事务':[
    {'spring中两种实现方式':[
        '编程式事务管理：使用底层源码可实现更细粒度的事务控制。spring推荐使用TransactionTemplate,典型的模板模式',
        '申明式事务管理：添加@Transactional注解，并定义传播机制+回滚策略,基于Spring AOP实现',
    ]},
],
'PlatformTransactionManager接口':[
    '顶级接口,定义了最核心的事务管理方法',
    '下面一层是AbstractPlatformTransactionManager抽象类，实现了PlatformTransactionManager接口的方法并定义了一些抽象方法',
    {'再下面一层是2个经典事务管理器':[
        'DataSourceTransactionmanager,即JDBC单数据库事务管理器，基于Connection实现',
        'JtaTransactionManager,即多数据库事务管理器（又叫做分布式事务管理器），其实现了JTA规范，使用XA协议进行两阶段提交'
    ]},
    {'方法':[
        '获取事务状态:TransactionStatus getTransaction(TransactionDefinition definition)',
        '事务提交:void commit(TransactionStatus status)',
        '事务回滚:void rollback(TransactionStatus status)',
    ]}
],
'申明式事务@Transactional':[
    'springboot 容器启动时的自动配置载入',
    '在/META-INF/spring.factories配置文件中查找',
    {'载入2个关于事务的自动配置类':[
        'org.springframework.boot.autoconfigure.transaction.TransactionAutoConfiguration',
        'org.springframework.boot.autoconfigure.transaction.jta.JtaAutoConfiguration'
    ]}
],
'TransactionAutoConfiguration':[
    {'类注解':[
        '@Configuration',
        '@ConditionalOnClass(PlatformTransactionManager.class)',
        '@AutoConfigureAfter({ JtaAutoConfiguration.class, HibernateJpaAutoConfiguration.class',
        '  DataSourceTransactionManagerAutoConfiguration.class',
        '  Neo4jDataAutoConfiguration.class })',
        '@EnableConfigurationProperties(TransactionProperties.class)'
    ]},
    {'2个内部类':[
        {'TransactionTemplateConfiguration事务模板配置类':[
            '如果没有定义TransactionTemplate bean生成一个'
        ]},
        {'EnableTransactionManagementConfiguration开启事务管理器配置类':[
            '支持2种代理方式',
            'JdkDynamicAutoProxyConfiguration',
            'CglibAutoProxyConfiguration',
            '默认没有spring.aop.proxy-target-class=true，配置，走的Cglib代理。说明@Transactional注解支持直接加在类上',
            '@EnableTransactionManagement'
        ]}
    ]}
],
'链接':[
    'https://www.jianshu.com/p/8ff9201ed7d6',
    'https://www.cnblogs.com/dennyzhangdd/p/9549535.html'
]
}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 