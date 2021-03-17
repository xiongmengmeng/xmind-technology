import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) 
sys.path.insert(0,parentdir) 
import xmind
from xmind.core.markerref import MarkerId
xmind_name="MyBatis"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("MyBatis与Springboot整合")
r2=s2.getRootTopic()
r2.setTitle("MyBatis与Springboot整合")


content={
'入囗':[
    'pom.xml引入mybatis-spring-boot-starter包(引入mybatis-spring-boot-autoconfigure包)',
    'org.springframework.boot.autoconfigure.EnableAutoConfiguration=',
    'org.mybatis.spring.boot.autoconfigure.MybatisAutoConfiguration'
],
'MybatisAutoConfiguration':[
    {'类的注解':[
        '@ConditionalOnClass({ SqlSessionFactory.class, SqlSessionFactoryBean.class}):提供 SqlSessionFactory 和 SqlSessionTemplate',
        '@ConditionalOnBean(DataSource.class)',
        '@EnableConfigurationProperties(MybatisProperties.class)',
        '@AutoConfigureAfter(DataSourceAutoConfiguration.class)'
    ]},
    {'MybatisAutoConfiguration()构造方法':[
        {'参数':[
            'MybatisProperties:',
            'Interceptor[]:拦截器',
            'ResourceLoader ',
            'DatabaseIdProvider:根据不同的数据库筛选不同的sql语句，通过设置 statement sql 节点上来实现',
            {'List<ConfigurationCustomizer>':[
                {'ConfigurationCustomizer接囗 ':[
                    '属于mybatis-spring包中的接口',
                    '方法：customize(Configuration configuration)',
                    '获取 mybatis 的 configuration 或者更改 configuration 中的属性，比如向configuration 中注册插件',
                    'SqlSessionFactory 的时候调用了ConfigurationCustomizer，提供了接口供我们回调'
                ]}
            ]}
        ]}
    ]},
    {'SqlSessionFactory sqlSessionFactory(DataSource dataSource)方法':[
        '方法注解@ConditionalOnMissingBean',
        '创建SqlSessionFactoryBean，然后设置一堆属性',
        '通过sqlSessionFactoryBean.getObject()获得SqlSessionFactory'
    ]},
    {'SqlSessionTemplate sqlSessionTemplate(SqlSessionFactory sqlSessionFactory)方法':[
        '根据sqlSessionFactory创建SqlSessionTemplate',
        '本质：SqlSessionTemplate=代理(SqlSession+SqlSessionInterceptor拦截器)'
    ]},
    {'MapperScannerRegistrarNotFoundConfiguration内部类':[
        {'类注解':[
            '@Import({ AutoConfiguredMapperScannerRegistrar.class })',
            '@ConditionalOnMissingBean(MapperFactoryBean.class)'
        ]},
        {'AutoConfiguredMapperScannerRegistrar':[
            {'registerBeanDefinitions()':[
                '实现ImportBeanDefinitionRegistrar接囗，重写其registerBeanDefinitions()方法',
                '1.创建ClassPathMapperScanner:',
                'new ClassPathMapperScanner(registry)',
                '2.扫描@Mapper的类注册为BeanDefinition(beanClass属性为MapperFactoryBean):',
                'scanner.setAnnotationClass(Mapper.class)',
                'scanner.doScan(StringUtils.toStringArray(packages));'
            ]}
        ]}
    ]},
    {'总结':[
        '配置SqlSessionFactory',
        '配置SqlSessionTemplate',
        {'实现Mapper接口的扫描与注册':[
            '配置MapperFactoryBean(xml中配置),不用启动mapper的注册器',
            '否则导入AutoConfiguredMapperScannerRegistrar(实现Mapper接口的扫描与注册)'
        ]}
    ]}
]

}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 