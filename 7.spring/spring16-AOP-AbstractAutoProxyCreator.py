import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="spring"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("AbstractAutoProxyCreator")
r2=s2.getRootTopic()
r2.setTitle("AbstractAutoProxyCreator")


content={
'aop源码入囗':[
    'doCreateBean()中，回调方法：initializeBean()->',
    'DefaultAdvisorAutoProxyCreator.postProcessAfterInitialization()[方法是继承父类]->',
    'AbstractAutoProxyCreator.postProcessAfterInitialization()',
    '注：AbstractAutoProxyCreator实现BeanPostProcessor',
],
'AbstractAutoProxyCreator':[
    {'postProcessAfterInitialization()方法':[
        '1.getAdvicesAndAdvisorsForBean(bean.getClass(), beanName, null)',
        '得到所有的可用于拦截当前 bean 的 advisor、advice、interceptor',
        {'2.createProxy()':[
            '1.new ProxyFactory():创建一个ProxyFactory的实例',
            '2.set一堆内容',
            '3.proxyFactory.getProxy(classLoader)->proxyFactory.createAopProxy().getProxy(classLoader)',
            {'createAopProxy()':[
                '实现类DefaultAopProxyFactory',
                '返回JdkDynamicAopProxy'
            ]},
            {'getProxy(classLoader)':[
                '实现类JdkDynamicAopProxy'
            ]}
        ]}
    ]}
],
'开启@AspectJ的两种方式':[
    {'1.<aop:aspectj-autoproxy/>':[
        '解析上面的xml信息用到了AopNamespaceHandler',
        {'AopNamespaceHandler':[
            'init():加载AspectJAutoProxyBeanDefinitionParser'
        ]},
        {'AspectJAutoProxyBeanDefinitionParser':[
            {'parse()方法':[
                '注册AnnotationAwareAspectJAutoProxyCreator类（继承AbstractAutoProxyCreator类）',
            ]}
        ]}
    ]},
    {'2.@EnableAspectJAutoProxy':[
        '@Import(AspectJAutoProxyRegistrar.class)',
        {'AspectJAutoProxyRegistrar':[
            '实现ImportBeanDefinitionRegistrar接囗，重写registerBeanDefinitions方法：',
            '注册AnnotationAwareAspectJAutoProxyCreator类'
        ]}
    ]},
    '原理一样，都通过注册一个bean（AnnotationAwareAspectJAutoProxyCreator）来实现'
]

}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 