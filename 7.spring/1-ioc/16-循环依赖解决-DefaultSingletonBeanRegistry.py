import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="spring"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("DefaultSingletonBeanRegistry")
r2=s2.getRootTopic()
r2.setTitle("DefaultSingletonBeanRegistry")


content={
'分析代码段':[
    {'addSingletonFactory(beanName, () -> getEarlyBeanReference(beanName, mbd, bean))':[
        '代码所在类：AbstractAutowireCapableBeanFactory(继承自DefaultSingletonBeanRegistry)',
        'doCreateBean()方法内代码(AbstractAutowireCapableBeanFactory类)',
        '方法调用节点：bean反射创建实例，依赖注入前',
    ]},
    {'Object sharedInstance = getSingleton(beanName)':[
        '代码实现类：DefaultSingletonBeanRegistry',
        'populateBean()->getBean()->doGetBean()方法内代码(AbstractBeanFactory类)',
        '方法调用节点：getBean()获得实例，未到doCreateBean()'
    ]},
    {'Object sharedInstance = getSingleton(beanName, () -> {createBean(beanName, mbd, args)})':[
        '代码实现类：DefaultSingletonBeanRegistry',
        'populateBean()->getBean()->doGetBean()方法内代码(AbstractBeanFactory类)',
        '方法调用节点：getBean()获得实例，doCreateBean()执行完'
    ]}
],
'DefaultSingletonBeanRegistry':[
    {'变量':[
        {'一级缓存:beanName->bean实例':[
            'Map<String, Object> singletonObjects = new ConcurrentHashMap<>(256)'
        ]},
        {'二级缓存:beanName->bean实例':[
            'Map<String, Object> earlySingletonObjects = new HashMap<>(16)'
        ]},
        {'三级缓存:beanName->ObjectFactory':[
            'Map<String, ObjectFactory<?>> singletonFactories = new HashMap<>(16)'
        ]},
    ]},
    {'addSingletonFactory(String beanName, ObjectFactory<?> singletonFactory)':[
        'this.singletonFactories.put(beanName, singletonFactory)',
        'this.earlySingletonObjects.remove(beanName)',
        'this.registeredSingletons.add(beanName)'				
    ]},
    {'Object getSingleton(String beanName, boolean allowEarlyReference)':[
        '1.从一级缓存在中取，this.singletonObjects.get(beanName)，取不到',
        '1.从二级缓存在中取，this.earlySingletonObjects.get(beanName)，还取不到',
        '3.从三级缓存在中取，this.singletonFactories.get(beanName)',
        {'4.singletonFactory不为空':[
            '获得bean实例：singletonFactory.getObject()',
            '将其放入二级缓存：this.earlySingletonObjects.put(beanName, singletonObject)',
            '将其从三级缓存去除：this.singletonFactories.remove(beanName)'
        ]}
    ]},
    {'addSingleton(String beanName, Object singletonObject)':[
        '1.将bean放入一级缓存：this.singletonObjects.put(beanName, singletonObject)',
        '2.将bean从二级缓存删除：this.earlySingletonObjects.remove(beanName)',
        '3.将bean从三级缓存删除：this.earlySingletonObjects.remove(beanName)'
    ]}
],
'AbstractAutoProxyCreator':[
    {'变量Map<Object, Object> earlyProxyReferences':[
        '标记Object是否进行过代理，执行过BeanPostProcess方法'
    ]},
    {'getEarlyBeanReference()':[
        {'1.this.earlyProxyReferences.put(cacheKey, bean)':[
            '标记Object进行过代理'
        ]},
        {'2.wrapIfNecessary(bean, beanName, cacheKey)':[
            '遍历拦截器，如果匹配advice,创建代理'
        ]}
    ]},
    {'postProcessAfterInitialization':[
        '判断this.earlyProxyReferences是否存在bean，存在删除并返回',
        '不存在，执行wrapIfNecessary(bean, beanName, cacheKey)方法'
    ]}
],
'ObjectFactory':[
    {'T getObject()':[
        '类似FactoryBean中的getObject()'
    ]}
]
}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 