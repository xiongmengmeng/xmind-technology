import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="spring"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("MyBatis与Springboot整合")
r2=s2.getRootTopic()
r2.setTitle("MyBatis与Springboot整合")


content={
'MyBatis的核心组件':[
    'SqlSessionFactory:创建SqlSession',
    'Java接口代理对象:实现接口访问数据库'
],
'pom.xml引入mybatis-spring-boot-starter包，它又引入mybatis-spring-boot-autoconfigure包':[],
'springboot启动文件':[
    '1.@SpringbootApplication注解上，有@EnableAutoConfiguration注解',
    '2.@EnableAutoConfiguration注解上有@Import注解，注入一个ImportSelector的实现类AutoConfigurationImportSelector',
    '3.AutoConfigurationImportSelector在selectImports()方法:',
    'List<String> configurations = SpringFactoriesLoader.loadFactoryNames(this.getSpringFactoriesLoaderFactoryClass(), this.getBeanClassLoader());',
    '作用：从所有jar包的META-INF/spring.factories文件中，加载EnableAutoConfiguration对应的实现类',
    'mybatis-spring-boot-autoconfigure.jar包中是MybatisAutoConfiguration'
],
'整合原理':[
    {'入囗':[
        '1.ConfigurationClassPostProcessor(实现BeanFactoryPostProcessor)初始化',
        '执行postProcessBeanDefinitionRegistry(BeanDefinitionRegistry registry)方法',
        '@SpringBootApplication->@EnableAutoConfiguration->@Import->AutoConfigurationImportSelector',
        '2.AutoConfigurationImportSelector的selectImports()方法',
        '扫描spring.factories中需org.springframework.boot.autoconfigure.EnableAutoConfiguration的类',
        '3.读取到这些类然后注册'
    ]},
    {'注册':[
        '4.注册MybatisAutoConfiguration过程中',
        '5.根据@MapperScan扫描指定路径下的Mapper接口，将Mapper接口转换为BeanDefinition对象',
        '并设置BeanDefinition对象的beanClass属性为MapperFactoryBean',
        '6.创建SqlSessionFactoryBean'
    ]},
    {'初始化':[
        '7.将Mapper接口对映BeanDefinition对象初始化为MapperFactoryBean',
        '8.初始化SqlSessionFactoryBean后，执行afterPropertiesSet()方法,创建SqlSessionFactory',
        '9.SqlSessionFactory持有Configuration对象，将相关属性填充到Configuration中',
        '10.将当前接口和对应的mapperProxyFactory存入到knownMappers中',
        '11.将sql包装成mappedStatement，存入到mappedStatements这个map中'
    ]}
],

}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 