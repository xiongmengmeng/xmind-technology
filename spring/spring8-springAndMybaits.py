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
'MyBatis的核心组件':[
    'SqlSessionFactory:创建SqlSession',
    'Java接口代理对象:实现接口访问数据库'
]
'整合原理':[
    '把某个Mapper的代理对象作为一个bean放入Spring容器中'
],

'':[
    {'SqlSessionFactoryBean':[
        'MyBatis Spring模块中提供,继承了FactoryBean',
        '作用：构建SqlSessionFactory对象，SqlSessionFactory对象创建SqlSession对象',
        'SqlSession是MyBatis提供的与数据库交互的接口',
        '核心属性:之前在配置文件中写的MyBatis的全部配置',
        '核心的方法buildSqlSessionFactory()',
        '创建时机:类实现InitializingBean接口，Bean初始化完成之后调用afterPropertiesSet()方法',
    ]},
    {'MapperFactoryBean':[
        '作用:创建Java接口的代理对象',
        {'实现了FactoryBean，getObject方法':[
            '获取SqlSession之后再获取Mapper对象',
            '本身不需要做太多工作，获取代理对象的工作委托给SqlSession'
        ]}
    ]},
    {'MapperScannerConfigurer':[
        '作用：扫描多个Java接口并创建对应的代理对象',
        '实现了BeanDefinitionPostProcessor接口，通过方法postProcessBeanDefinitionRegistry修改Bean定义信息',
        '将包下Java接口扫描并注册Bean定义信息，设置Bean类型是MapperFactoryBean类型，用于后面的MapperFactoryBean实例化'
    ]},
    {'@MapperScan​':[
        '同MapperScannerConfigurer一样作用',
        '原理是@Import(MapperScannerRegistrar.class)',
        'MapperScannerRegistrar是一个ImportBeanDefinitionRegistrar实现类，一种注册Bean的方式'
    ]},
    {'MapperScannerRegistrar':[
        '用来生成不同Mapper对象的LubanFactoryBean'
    ]},

],
'框架启动':[
    '1.扫描指定路径下的Mapper接口，将Mapper接口转换为Spring中的BeanDefinition对象',
    '2.根据BeanDefinition对象的beanClass属性(属性值MapperFactoryBean)创建Bean的实例'
],
'入囗':[
    'AnnotationConfigApplicationContext初始化->AnnotatedBeanDefinitionReader初始化',
    'AnnotationConfigUtils.registerAnnotationConfigProcessors(this.registry)',
    '把一些自动注解处理器加入到AnnotationConfigApplicationContext下的BeanFactory的BeanDefinitions中'
],
'加载MapperScan':[
    '1.MapperScan注解通过@Import注解导入了一个BeanDefinition注册类MapperScannerRegistrar',
    '2.MapperScannerRegistrar类实现了ImportBeanDefinitionRegistrar接口,重写了registerBeanDefinitions()方法',
    '3.首先创建了一个ClassPathMapperScanner对象',
    '4.然后获取MapperScan注解的属性信息',
    '5.根据MapperScan的annotationClass和markerInterface属性对扫描的Class进行过滤',
    '6.最后调用ClassPathMapperScanner对象的doScan()方法进行扫描',
    '扫描特定包下的Mapper接口，将Mapper接口信息转换为对应的BeanDefinition对象',
    {'':[
        '1.调用父类的doScan()方法，将指定包下的Mapper接口信息转换为BeanDefinitionHolder对象，BeanDefinitionHolder中持有一个BeanDefinition对象及Bean的名称和所有别名',
        '2.调用processBeanDefinitions()方法',
        '将BeanDefinition对象的beanClass属性设置为MapperFactoryBean，并向BeanDefinition对象中增加addToConfig和sqlSessionTemplate等属性',
        '',
        '',
        ''
    ]},
    {'将BeanDefinition对象的beanClass属性设置为MapperFactoryBean这一步很重要':[
        'BeanDefinition对象来实例化Bean时，',
        '当BeanDefinition对象的beanClass属性为MapperFactoryBean时，Spring在创建Bean时实例化的是MapperFactoryBean对象',
        ''
    ]}
]
'MapperScannerConfigurer':[
    '实现BeanFactoryPostProcessor接囗',
    {'重写postProcessBeanDefinitionRegistry(BeanDefinitionRegistry registry)':[
        '实例化ClassPathMapperScanner，并对scanner相关属性进行配置',
        '扫描指定的包以及其子包:scanner.scan',
        ''
    ]}
],
'ClassPathBeanDefinitionScanner':[
    '',
    'doScan(basePackages)',
    ''
],
'ClassPathBeanDefinitionScanner.doScan(basePackages)':[
    '',
    '',
    ''
]
}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 