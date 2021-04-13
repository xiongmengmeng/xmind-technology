import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="spring"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("ioc中的常见扩展类")
r2=s2.getRootTopic()
r2.setTitle("ioc中的常见扩展类")


content={
'BeanFactoryAware':[
    {'方法':[
        'setBeanFactory(BeanFactory beanFactory)'
    ]},
    {'作用':[
        '实现接口的bean知道自己属于哪一个beanfactory'
    ]},
],
'BeanNameAware':[
    {'方法':[
        'setBeanName(String name)'
    ]},
    {'作用':[
        '实现接口的bean知道自己在spring容器里的名字'
    ]},
],
'@Import':[
    '一个注解，用来向Spring容器中导入Bean',
    '比起在某个类上加上@Component注解，更灵活',
    '@Import注解参数有className,ImportBeanDefinitionRegistrar,ImportSelector'   
],
'ImportBeanDefinitionRegistrar':[
    '一个接口，其实现类作用于解析Bean的配置阶段',
    {'方法':[
        'registerBeanDefinitions(AnnotationMetadata importingClassMetadata, BeanDefinitionRegistry registry)',
        'importingClassMetadata：@Import所在注解的配置信息',
        'registry：BeanDefinition容器'
    ]},
    {'作用':[
        '当解析@Configuration注解时，可以向BeanDefinitionRegistry容器中添加额外的BeanDefinition对象（动态的注册bean）'
    ]},
],
'ImportSelector':[
    {'方法':[
        'selectImports(AnnotationMetadata importingClassMetadata)',
        '返回需要导入的组件的全类名数组',
        'AnnotationMetadata:可获取当前类（被@Import标记）的注解信息，使用反射来获取制定类的内部注解信息'
    ]},
    {'作用':[
        '同上'
    ]}
]


}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 