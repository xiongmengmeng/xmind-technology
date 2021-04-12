import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0,parentdir) 


import xmind
from xmind.core.markerref import MarkerId
xmind_name="spring"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("IoC容器的设计路线")
r2=s2.getRootTopic()
r2.setTitle("IoC容器的设计路线")


content={
'BeanDefinitionRegistry接口':[
    'BeanDefinition的注册中心,使DefaultListableBeanFactory具备操作BeanDefinition的能力',
    'registerBeanDefinition(String beanName, BeanDefinition beanDefinition):注册BeanDefinition的方法',
    'removeBeanDefinition(String beanName):删除BeanDefinition的方法',
    'BeanDefinition getBeanDefinition(String beanName):获取BeanDefinition的方法'
    '具体实现在DefaultListableBeanFactory中'
],
'SingletonBeanRegistry接口':[
    'registerSingleton(String beanName, Object singletonObject):单例Bean的注册接口',
    'Object getSingleton(String beanName):定义获取单例的方法'
],
'DefaultSingletonBeanRegistry':[
    '让IoC容器拥有作为“容器”的能力，最终存储单例（singleton）Bean的地方',
    {'Map<String, Object> singletonObjects':[
        '缓存单例对象',
        'bean name --> bean instance'
    ]},
    {'Map<String, ObjectFactory<?>> singletonFactories':[
        '缓存单例工厂',
        'bean name --> ObjectFactory'
    ]},
    {'Map<String, Object> earlySingletonObjects':[
        '缓存提前暴露的对象',
        'bean name --> bean instance'
    ]}
],
'学习':[
    'https://www.cnblogs.com/hello-shf/p/11057861.html'
]

}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 