import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="spring"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("MyBatis与Spring整合")
r2=s2.getRootTopic()
r2.setTitle("MyBatis与Spring整合")


content={
'SqlSessionFactoryBean':[
    'MyBatis Spring模块提供,继承了FactoryBean,getObject()返回sqlSessionFactory',
    '作用：构建SqlSessionFactory对象，SqlSessionFactory对象创建SqlSession对象（MyBatis提供的与数据库交互的接口）',
    '核心属性:之前在配置文件中写的MyBatis的全部配置',
    '核心方法:buildSqlSessionFactory()',
    {'创建SqlSessionFactory时机':[
        '类实现InitializingBean接口,类初始化后,调用afterPropertiesSet()方法',
        '方法里调用this.sqlSessionFactory = buildSqlSessionFactory()'
    ]}
],
'MapperFactoryBean':[
    '作用:创建Java接口的代理对象',
    {'实现FactoryBean类，重写getObject方法':[
        '获取SqlSession之后再获取Mapper对象',
        '本身不需要做太多工作，获取代理对象的工作委托给SqlSession'
    ]}
],
'MapperScannerConfigurer':[
    '作用：将包下Java接口扫描并注册Bean定义信息',
    '实现了BeanDefinitionRegistryPostProcessorr接口，通过方法postProcessBeanDefinitionRegistry修改Bean定义信息',
    {'postProcessBeanDefinitionRegistry()':[
        'scanner.setSqlSessionFactory(this.sqlSessionFactory);',
        'scanner.setSqlSessionTemplate(this.sqlSessionTemplate);',
        'scanner.scan()->ClassPathMapperScanner.doScan()->definition.setBeanClass(this.mapperFactoryBean.getClass());'
    ]}
],
'@MapperScan':[
    '同MapperScannerConfigurer一样作用',
    '通过@Import注解导入了一个BeanDefinition注册类MapperScannerRegistrar' 
],
'MapperScannerRegistrar':[
    '作用：将包下Java接口扫描并注册Bean定义信息，设置Bean类型是MapperFactoryBean类型，用于后面MapperFactoryBean实例化',
    '实现ImportBeanDefinitionRegistrar接囗(一种注册Bean的方式)',
    {'重写registerBeanDefinitions()':[
        '1.首先创建了一个ClassPathMapperScanner对象',
        '2.然后获取MapperScan注解的属性信息',
        '3.根据MapperScan的annotationClass和markerInterface属性对扫描的Class进行过滤',
        '4.最后调用ClassPathMapperScanner对象的doScan()方法进行扫描',
        '5.扫描特定包下的Mapper接口，将Mapper接口信息转换为对应的BeanDefinition对象',
        '6.给BeanDefinition对象设置beanClass属性为MapperFactoryBean,将来对象实例化为Bean时，实例化的是MapperFactoryBean对象',
        '7.向BeanDefinition对象中增加addToConfig和sqlSessionTemplate等属性'
    ]}
],
'MybatisAutoConfiguration':[
    {'类的注解':[
        '@ConditionalOnClass({ SqlSessionFactory.class, SqlSessionFactoryBean.class}):提供 SqlSessionFactory 和 SqlSessionTemplate',
        '@ConditionalOnBean(DataSource.class)',
        '@EnableConfigurationProperties(MybatisProperties.class)',
        '@AutoConfigureAfter(DataSourceAutoConfiguration.class)'
    ]},
    {'方法':[
        '利用@ConditionalOnMissingBean，当容器不存在某个Bean的时候则自动装配一个Bean',
        '配置SqlSessionFactory:如没有SqlSessionFactory对应的Bean，通过SqlSessionFactoryBean装配一个',
        '配置SqlSessionTemplate:如果没有SqlSessionTemplate对应的Bean，装配一个',
        '配置MapperFactoryBean:如使用@MapperScan注解，注册该Bean',
        '如没有使用，导入AutoConfiguredMapperScannerRegistrar(实现@Mapper接口的扫描)'
    ]}
]

}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 