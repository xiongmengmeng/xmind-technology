import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0,parentdir) 


import xmind
from xmind.core.markerref import MarkerId
xmind_name="Transaction"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("@EnableTransactionManagement")
r2=s2.getRootTopic()
r2.setTitle("@EnableTransactionManagement")


content={
'作用':[
    '开启对事务的支持'
],
'内容':[
    '其上注解：@Import(TransactionManagementConfigurationSelector.class)',
    {'方法：':[
        {'1.boolean proxyTargetClass() default false':[
            'proxyTargetClass=false:JDK动态代理支持接口代理,true:Cglib代理支持子类继承代理'
        ]},
        {'2.AdviceMode mode() default AdviceMode.PROXY':[
            '事务通知模式(切面织入方式)，默认代理模式（同一个类中方法互相调用拦截器不会生效），可选择增强型AspectJ'
        ]},
        {'3.int order() default Ordered.LOWEST_PRECEDENCE':[
            '连接点上有多个通知时，排序，默认最低。值越大优先级越低'
        ]}
    ]}
],
'TransactionManagementConfigurationSelector':[
    '继承自AdviceModeImportSelector实现了ImportSelector接口',
    'selectImports方法导入需要加载的类',
    'proxy模式下，载入了AutoProxyRegistrar、ProxyTransactionManagementConfiguration2个类'
],
'AutoProxyRegistrar':[
    '实现了ImportBeanDefinitionRegistrar接口',
    {'复写registerBeanDefinitions()方法':[
        '将InfrastructureAdvisorAutoProxyCreator注册到容器',
    ]},
    {'InfrastructureAdvisorAutoProxyCreator':[
        {'继承AbstractAutoProxyCreator':[
            {'postProcessBeforeInstantiation()':[
                '事务类无多余处理',
                '注意：基础构建包括Advice、Pointcut、Advisor、AopInfrastructureBean',
                '基础构件执行：advisedBeans.put(cacheKey, Boolean.FALSE)'
            ]},
            {'postProcessAfterInitialization()':[
                '1.getAdvicesAndAdvisorsForBean(bean.getClass(), beanName, null):',
                '获取增强List<Advisor> advisors',
                '会将与事务相关的增强器BeanFactoryTransactionAttributeSourceAdvisor找出',
                '2.this.advisedBeans.put(cacheKey, Boolean.TRUE):如果存在增强,加入缓存',
                '3.根据增强器名称获取对应的实例，并生成拦截链',
                '4.createProxy()：根据不同的代理类型和拦截链创建代理对象'
            ]}
        ]},

    ]}
],
'ProxyTransactionManagementConfiguration':[
    '一个配置类，定义了事务Advisor',
    {'TransactionInterceptor':[
        '定义事务拦截器',
        '本身也是一个方法拦截器，在invoke方法中进行了事务的处理'
    ]},
    {'TransactionAttributeSource':[
        '定义基于注解的事务属性资源',
        '@Transaction注解标签解析器'
    ]},
    {'BeanFactoryTransactionAttributeSourceAdvisor':[
        'transactionAdvisor()事务织入',
        '定义事务增强器',
        {'组件':[
            'TransactionInterceptor',
            'TransactionAttributeSource'
        ]}
    ]}
]
}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 