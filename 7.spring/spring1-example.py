import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="spring"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("spring")
r2=s2.getRootTopic()
r2.setTitle("spring总述")


content={
'IOC':[
   'Spring的核心是提供了一个容器(Spring应用上下文)',
   {'容器作用':[
       '1.创建和管理应用组件(称为bean)',
       '2.将应用组件装配在一起(依赖注入（dependency injection，DI）)'
   ]},
   {'DI的本质':[
       '组件不去创建它所依赖的组件并管理它们的生命周期',
       'bean都通过容器创建与管理，组件的依赖组件，通过容器注入',
       '通常通过构造器参数和属性访问方法来实现'
   ]},
    {'自动配置':[
        '自动装配（autowiring）:自动为组件注入它们所依赖的其他bean',
        '组件扫描（componentscanning）:自动发现应用类路径下的组件，并将它们创建成容器中的bean'
    ]},
    {'Spring Boot':[
        '基于类路径中的条目、环境变量和其他因素',
        '合理猜测需要配置的组件并将它们装配在一起'
    ]}
],
'':[
    {'main()':[
        '会调用SpringApplication中静态的run()方法，后者会创建Spring的应用上下文',
        'run()的两个参数中，一个是配置类，另一个是命令行参数',
        '尽管传递给run()的配置类不一定要和引导类相同，但这是最便利和最典型的做法',
    ]},
    {'Test类':[
        '@RunWith(SpringRunner.class)注解:SpringRunner,一个Spring提供的测试运行器，会创建测试运行所需的Spring应用上下文',
        '@SpringBootTest会告诉JUnit在启动测试的时候要添加上Spring Boot的功能',
        '->测试类视同为在main()方法中调用SpringApplication.run()'
    ]}
],
'注解':[
    '@Configuration：告知Spring这是一个配置类，会为Spring应用上下文提供bean',
    '@Bean方法：方法所返回的对象会以bean的形式添加到Spring的应用上下文中',
    '@SpringBootApplication,一个组合注解，它组合了3个其他的注解:',
    '@SpringBootConfiguration：将该类声明为配置类',
    '@EnableAutoConfiguration：启用Spring Boot的自动配置',
    '@ComponentScan：启用组件扫描'
],
'其它':[
    {'使用属性文件':[
        '@Value注解，使用${......}这样的占位符读取配置在属性文件的内容',
        '@ConfigurationProperties'
    ]},
    {'@Profile':[
        '修改启动Profile机制',
        'spring.profiles.active',
        'spring.profiles.default',
        'spring.profiles.active优先于spring.profiles.default'
    ]},
    {'注解':[
        '@Configuration：代表这是一个Java配置文件，Spring的容器会根据它来生成IoC容器去装配Bean',
        '@Bean(name="user")：将方法返回的POJO装配到IoC容器中，属性name为Bean名称，如未配置，方法名作为Bean名称',
        '@Autowired:（根据属性的类型&&名称）找到对应的Bean进行注入'
    ]}
],
'XML的验证模式':[
    {'DTD':[
        '文档类型定义(Document Type Definition)，一种XML约束模式语言',
        {'DTD文档':[
            '元素的定义规则',
            '元素间关系的定义规则',
            '元素可使用的属性',
            '可使用的实体或符号规则'
        ]},
        '使用DTD验证模式:需在XML文件的头部声明'
    ]},
    {'XSD':[
        'XML Schemas Definition',
        '使用XML Schema文档对XML实例文档进行检验',
        '声明名称空间（xmlns=http://www.Springframework.org/schema/beans）',
        '通过schemaLocation指定该名称空间所对应的XML Schema文档的存储位置'
    ]}
]
}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 