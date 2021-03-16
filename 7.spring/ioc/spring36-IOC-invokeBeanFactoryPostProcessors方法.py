import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="spring-IOC"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("invokeBeanFactoryPostProcessors()")
r2=s2.getRootTopic()
r2.setTitle("invokeBeanFactoryPostProcessors()")


content={
'第一优先级':[
    '入参 beanFactoryPostProcessors 中的 BeanDefinitionRegistryPostProcessor',
    '调用 postProcessBeanDefinitionRegistry 方法'
],
'第二优先级':[
    'BeanDefinitionRegistryPostProcessor 接口实现类,并且实现了 PriorityOrdered 接口',
    '调用 postProcessBeanDefinitionRegistry 方法'
],
'第三优先级':[
    'BeanDefinitionRegistryPostProcessor 接口实现类，并且实现了 Ordered 接口',
    '调用 postProcessBeanDefinitionRegistry 方法'
],
'第四优先级':[
    '除去第二优先级和第三优先级，剩余的 BeanDefinitionRegistryPostProcessor 接口实现类',
    '调用 postProcessBeanDefinitionRegistry 方法'
],
'第五优先级':[
    '所有 BeanDefinitionRegistryPostProcessor 接口实现类',
    '调用 postProcessBeanFactory 方法'
],
'第六优先级':[
    '入参 beanFactoryPostProcessors 中的常规 BeanFactoryPostProcessor',
    '调用 postProcessBeanFactory 方法'
],
'第七优先级':[
    '常规 BeanFactoryPostProcessor 接口实现类，并且实现了 PriorityOrdered 接口',
    '调用 postProcessBeanFactory 方法'
],
'第八优先级':[
    '常规 BeanFactoryPostProcessor 接口实现类，并且实现了 Ordered 接口',
    '调用 postProcessBeanFactory 方法'
],
'第九优先级':[
    '除去第七优先级和第八优先级，剩余的常规 BeanFactoryPostProcessor 接口的实现类',
    '调用 postProcessBeanFactory 方法'
]
}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 