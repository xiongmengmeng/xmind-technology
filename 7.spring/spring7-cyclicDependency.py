import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="spring"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("circulDependence(上)")
r2=s2.getRootTopic()
r2.setTitle("circulDependence(上)")


content={
'问题假设':[
    'A依赖于B，B依赖于A'
],
'三级缓存':[
    {'一级缓存':[
        'singletonObjects',
        '缓存：初始化后的bean对象',
        '原始对象还未进行属性注入和后续BeanPostProcessor等过程'
    ]},
    {'二级缓存':[
        'earlySingletonObjects',
        '缓存：提前拿原始对象进行AOP后得到的代理对象'
    ]},
    {'三级缓存':[
        'singletonFactories',
        '缓存:ObjectFactory，表示对象工厂，用来创建某个对象',
        '生成时机：bean对象反射创建后，依赖注入前',
        '作用：生成原始对象进行AOP后得到的代理对象',
        {'出现循环依赖时使用':[
            'B依赖注入时，getBean()获取A的bean,通过singletonFactories得到ObjectFactory',
            'ObjectFactory执行方法得到一个AOP后的代理对象(如无需AOP，直接得到一个原始对象)'
        ]}
    ]},
    {'其余缓存':[
        'earlyProxyReferences',
        '缓存：某个原始对象是否进行过AOP'
    ]},
],
'AbstractAutowireCapableBeanFactory':[
    {'getEarlyBeanReference()方法':[
        '获得bean的beanPostProcessors',
        '如果它是SmartInstantiationAwareBeanPostProcessor类型',
        '依次执行getEarlyBeanReference(Object bean, String beanName)方法',
        'SmartInstantiationAwareBeanPostProcessor的主要实现类是AbstractAutoProxyCreator'
    ]}
],
'AbstractAutoProxyCreator':[
    {'getEarlyBeanReference()方法':[
        '把bean存放到earlyProxyReferences中(一个map),key为beanName，value为bean',
        '如果有通知则创建代理'
    ]}
]

}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 