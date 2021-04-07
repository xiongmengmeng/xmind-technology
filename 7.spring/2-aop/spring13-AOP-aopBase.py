import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="spring"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("aopBase")
r2=s2.getRootTopic()
r2.setTitle("aop基础")


content={
'三种配置方式':[
    {'Spring1.2基于接口':[
        '最早的 Spring AOP 是完全基于几个接口的，看源码可从这里开始',
        {'ProxyFactoryBean':[
            'proxyInterfaces',
            'target',
            {'interceptorNames':[
                'Advice',
                'Intercepter',
                'Advisor'
            ]}
        ]},
        'BeanNameAutoProxyCreator',
        'DefaultAdvisorAutoProxyCreator，实现了BeanPostProcessor接囗'
    ]},
    'Spring2.0基于schema-based：XML方式配置，使用命名空间 <aop />',
    {'Spring2.0基于@AspectJ':[
        '使用注解的方式来配置',
        '@AspectJ:标记切面,这个和 AspectJ没啥关系',
        '@Pointcut:切点，类似上面的Advisor',
        '@Before:通知，类似上面的Advice,传参使用：JoinPoint',
        '@Around:传参使用ProceedingJoinPoint，它有procceed()方法'
    ]}
],
'原理':[
    '动态代理:接口+真实实现类+代理类',
    '其中【真实实现类】和【代理类】都要实现接口，实例化时要使用代理类',
    {'Spring AOP实现':[
        '生成一个代理类，替换掉真实实现类来对外提供服务',
        '在Spring IOC容器中，getBean(…) 时返回代理类的实例->FactoryBean.getObject()'
    ]}
]
}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 