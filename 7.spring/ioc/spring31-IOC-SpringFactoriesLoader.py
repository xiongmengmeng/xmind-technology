import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="spring"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("SpringFactoriesLoader")
r2=s2.getRootTopic()
r2.setTitle("SpringFactoriesLoader")


content={
'基础':[
    '性质：Spring内部提供的一个约定俗成的加载方式，与java spi类似',
    '使用文件地址：META-INF/spring.factories文件(Properties格式文件)',
    'key：接口、注解、或抽象类的全名',
    'value:以逗号 “ , “ 分隔的实现类',
    '作用：使相应的实现类注入Spirng容器中'
],
'以@EnableAutoConfiguration为例了解':[
    '类的注解：@Import(AutoConfigurationImportSelector.class)',
    {'AutoConfigurationImportSelector#selectImports()':[
        '核心：getCandidateConfigurations(annotationMetadata, attributes)：',
        'SpringFactoriesLoader.loadFactoryNames(getSpringFactoriesLoaderFactoryClass(),getBeanClassLoader())',

        '从文件中筛选出要加载的类，将类的名称返回'
    ]},
],
'SpringFactoriesLoader':[
    {'loadFactoryNames(Class<?> factoryType, @Nullable ClassLoader classLoader)':[
        '参数getSpringFactoriesLoaderFactoryClass()：EnableAutoConfiguration.class',
        '参数getBeanClassLoader()：AppClassLoader',
        '1.classLoader.getResources(FACTORIES_RESOURCE_LOCATION)',
        'FACTORIES_RESOURCE_LOCATION ="META-INF/spring.factories";',
        '加载文件中的属性',
        '2.String factoryTypeName = factoryType.getName();',
        'getOrDefault(factoryTypeName, Collections.emptyList())',
        '对相应的key值进行筛选'
    ]},
    {'loadFactories(Class<T> factoryType, @Nullable ClassLoader classLoader)方法':[
        '1.loadFactoryNames(factoryType, classLoaderToUse)',
        '查找要加载的类',
        '2.instantiateFactory(factoryImplementationName, factoryType, classLoaderToUse)',
        '通过反射加载类',
        '3.AnnotationAwareOrderComparator.sort(result)',
        '排序'
    ]},
],
'总结':[
    '使用SpringFactoriesLoader寻找jar包配置META-INF下的spring.fatories配置文件相应key的value类',
    '然后通过spring的@Configuration对相应的bean进行有选择（@ConditionalOnClass）的实例化'
]

}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 