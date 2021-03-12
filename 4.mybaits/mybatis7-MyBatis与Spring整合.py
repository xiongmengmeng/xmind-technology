import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="mybatis"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("MyBatis与Spring整合")
r2=s2.getRootTopic()
r2.setTitle("MyBatis与Spring整合")


content={

'MyBatis的Mapper实例通过动态代理创建,与Spring框架整合，Mapper动态代理对象作为Bean注册到Spring容器中':[],
'Spring框架的启动过程':[
    '1.对所有Bean的配置信息进行解析(XML配置文件、Java注解以及Java Config方式配置的Bean)',
    '2.Bean的配置信息->BeanDefinition对象，注册到BeanDefinitionRegistry容器',
    '3.执行BeanFactoryPostProcessor扩展逻辑对Bean工厂信息进行修改',
    '4.BeanDefinition对象->实例化所有单例Bean并注入依赖',
    '5.执行所有BeanPostProcessor对象的Bean的postProcessBeforeInitialization()方法',
    '6.执行Bean的初始化方法',
    '7.执行所有BeanPostProcessor对象的postProcessAfterInitialization()方法'
],
'Mapper动态代理对象注册过程':[
    {'启动时':[
        '扫描指定路径下的Mapper接口',
        '将Mapper接口转换为Spring中的BeanDefinition对象',
        '并且beanClass属性为MapperFactoryBean'
    ]},
    {'启动后':[
        '每个Mapper接口创建一个MapperFactoryBean对象',
        '通过Mapper接口获取Bean时，获取到的是MapperFactoryBean对象的getObject()方法返回的对象'
    ]}
],
'Spring框架通过Java中的ThreadLocal机制保证同一个线程中获取到的始终是同一个Connection对象':[]



    
}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 