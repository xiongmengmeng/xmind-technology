import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="spring-Bean"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("bean")
r2=s2.getRootTopic()
r2.setTitle("bean")


content={
'装配Bean':[
    {'1.@Component和@ComponentScan':[
        '@Component标明哪个类被扫描进入Spring IoC容器',
        '@ComponentScan标明采用何种策略去扫描装配Bean',
        '配置项basePackages定义扫描的包名，没有定义的情况下，它只扫描当前包和其子包下的路径'
    ]},
    '2.引入XML配置Bean:xml文件+@ImportResource，通过它可以引入对应的XML文件'
],
'常见类':[
    {'BeanPostProcessor':[
        {'方法':[
            'postProcessBeforeInitialization(Object bean, String beanName)',
            'postProcessAfterInitialization(Object bean, String beanName)'
        ]},
        '处理Bean对应的Java类中的注解信息或者创建Bean的代理对象',
        '初始化Bean时,"临时"修改Bean属性，注意临时修改'
    ]},
    {'BeanFactoryPostProcessor':[
        '方法：postProcessBeanFactory(ConfigurableListableBeanFactory beanFactory)',
        '修改BeanDefinnition（存在map），map存在BeanFactory中,所以传参BeanFactory',
        '修改的是BeanFactory的BeanDefinition，从根本上改',
    ]},
    {'BeanDefinitionRegistryPostProcessor':[
        '一个接口，继承了BeanFactoryPostProcessor',
        '方法：postProcessBeanDefinitionRegistry(BeanDefinitionRegistry registry)',
        '可向BeanFactory中添加BeanDefinition',
    ]},
    {'FactoryBean':[
        '一个接口，一个Bean实现这个接口，变成一个Factory，通过getObject()将一个Object暴露出去',
        'factorybean中getObject中返回的对象==beanfactory.getbean返回的bean',
        '用于处理配置较为复杂或者由动态代理生成的Bean实例',
        {'通过beanfactory获取':[
            'beanfactory.getbean("beanFactoryName"),获得factorybean中getObject中返回的对象',
            'beanfactory.getbean("&beanFactoryName"),获得factorybean本身'
        ]}
    ]},
    {'BeanFactoryAware':[
        '方法：setBeanFactory(BeanFactory beanFactory)',
        '实现接口的bean知道自己属于哪一个beanfactory'
    ]},
    {'BeanNameAware':[
        '方法：setBeanName(String name)',
        '实现接口的bean知道自己在spring容器里的名字'
    ]},
    {'@Import':[
        '一个注解，用来向Spring容器中导入Bean',
        '比起在某个类上加上@Component注解，更灵活',
        '@Import注解参数有className,ImportBeanDefinitionRegistrar,ImportSelector'   
    ]},
    {'ImportBeanDefinitionRegistrar':[
        '一个接口，其实现类作用于解析Bean的配置阶段',
        '当解析@Configuration注解时，可以向BeanDefinitionRegistry容器中添加额外的BeanDefinition对象（动态的注册bean）',
        '方法：registerBeanDefinitions(AnnotationMetadata importingClassMetadata, BeanDefinitionRegistry registry)',
        'importingClassMetadata：@Import所在注解的配置信息',
        'registry：BeanDefinition容器'
    ]},
    {'ImportSelector':[
        '方法：selectImports(AnnotationMetadata importingClassMetadata)',
        '需要返回需要导入的组件的全类名数组，作用同上',
        'AnnotationMetadata:可获取当前类（被@Import标记）的注解信息，使用反射来获取制定类的内部注解信息'
    ]}
]

}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 