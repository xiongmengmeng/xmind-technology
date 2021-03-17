import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="MyBatis"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("Mapper扫描注册类")
r2=s2.getRootTopic()
r2.setTitle("Mapper扫描注册类")


content={
'@MapperScan':[
    '作用同MapperScannerConfigurer',
    '通过@Import注解导入类MapperScannerRegistrar' 
],
'MapperScannerRegistrar':[
    '作用：扫描Java接口并注册成BeanDefinition，设置beanClass属性为MapperFactoryBean，用于后面MapperFactoryBean实例化',
    '实现ImportBeanDefinitionRegistrar接囗,重写registerBeanDefinitions()方法',
    {'registerBeanDefinitions()':[
        '1.首先创建了一个ClassPathMapperScanner对象',
        '2.然后获取MapperScan注解的属性信息',
        '3.根据MapperScan的annotationClass和markerInterface属性对扫描的Class进行过滤',
        '4.调用ClassPathMapperScanner对象的doScan()方法进行扫描',
        '5.扫描特定包下的Mapper接口，将Mapper接口信息转换为对应的BeanDefinition对象',
        '6.给BeanDefinition对象beanClass属性设置为MapperFactoryBean,将来对象实例化为Bean时，实例化的是MapperFactoryBean对象',
        '7.向BeanDefinition对象中增加addToConfig和sqlSessionTemplate等属性'
    ]}
],
'MapperScannerConfigurer':[
    '作用：将包下Java接口扫描并注册Bean定义信息',
    '实现了BeanDefinitionRegistryPostProcessorr接口，重写postProcessBeanDefinitionRegistry()方法',
    {'postProcessBeanDefinitionRegistry()':[
        '1.创建Mapper扫描器',
        'ClassPathMapperScanner scanner=new ClassPathMapperScanner() ',
        '2.扫描basePackage下的所有候选对象,根据条件注册成BeanDefinition',
        'Set<BeanDefinitionHolder> beanDefinitions = super.doScan(basePackages);',
        '3.设置bean定义的Class类型,设置SqlSessionFactoryBean',
        'processBeanDefinitions(beanDefinitions);'
    ]}
],
'MyBatis与Spring整合重点':[
    'SqlSession的创建',
    'Mapper代理类的创建'
],
'学习':[
    'https://www.cnblogs.com/hei12138/p/mybatis-spring.html'
]
}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 