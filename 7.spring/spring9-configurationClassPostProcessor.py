import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="spring"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("ConfigurationClassPostProcessor")
r2=s2.getRootTopic()
r2.setTitle("ConfigurationClassPostProcessor")


content={
'实现BeanDefinitionRegistryPostProcessor接口，而BeanDefinitionRegistryPostProcessor接口继承BeanFactoryPostProcessor接口':[],
'重写postProcessBeanDefinitionRegistry(BeanDefinitionRegistry registry)方法和postProcessBeanFactory()方法':[],
'作用：解析加了@Configuration的配置类，还会解析@ComponentScan、@ComponentScans注解扫描的包，以及解析@Import等注解':[],
'postProcessBeanDefinitionRegistry()':[
    {'作用':[
        '解析加了@Configuration注解的类',
        '解析加了@ComponentScan和@ComponentScans扫描出的Bean',
        '解析加了@Bean注解的方法所注册的Bean',
        '解析加了@Import注解注册的Bean和@ImportResource注解导入的配置文件中配置的Bean'
    ]},
    {'过程':[
        '1.checkConfigurationClassCandidate():',
        '判断类是否是一个配置类,并为BeanDefinition设置属性为lite或者full',
        '@Configuration，对应的BeanDefinition为full',
        '@Bean,@Component,@ComponentScan,@Import,@ImportResource，对应的BeanDefinition为lite',
        '2.parser.pase():ConfigurationClassParser.parse(),解析配置类',
        '解析配置类上的注解(ComponentScan扫描出的类，@Import注册的类，以及@Bean方法定义的类)',
        '将解析结果放入到parser的configurationClasses属性中(一个Map)',
        '3. this.reader.loadBeanDefinitions():'
        '将通过@Import、@Bean等注解方式注册的类解析成BeanDefinition，然后注册到BeanDefinitionMap中',
        '如果bean上存在@Import注解，且import的类实现了ImportBeanDefinitionRegistrar接口,执行类的registerBeanDefinitions()方法',
    ]}
],
'postProcessBeanFactory()':[
    '作用：对BeanFactory进行处理，用来干预BeanFactory的创建过程',
    {'过程':[
        '对加了@Configuration注解的类进行CGLIB代理',
        '向Spring中添加一个后置处理器ImportAwareBeanPostProcessor'
    ]}

],
'https://blog.csdn.net/qq_34436819/article/details/100944204':[]

}



#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 