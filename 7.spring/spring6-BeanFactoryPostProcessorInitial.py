import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="spring"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("BeanFactoryPostProcessor")
r2=s2.getRootTopic()
r2.setTitle("BeanFactoryPostProcessor--invokeBeanFactoryPostProcessors(beanFactory)")


content={
'1.String[] postProcessorNames = beanFactory.getBeanNamesForType(BeanDefinitionRegistryPostProcessor.class, true, false)':[],
'去容器中获取BeanDefinitionRegistryPostProcessor的bean处理器名称,第一次取到ConfigurationClassPostProcessor':[],
'2.currentRegistryProcessors.add(beanFactory.getBean(ppName, BeanDefinitionRegistryPostProcessor.class))':[],
'getBean()方式获取该对象然后加入到currentRegistryProcessors集合中':[],
'3.invokeBeanDefinitionRegistryPostProcessors(currentRegistryProcessors, registry)':[],
'执行BeanDefinitionRegistryPostProcessor的postProcessBeanDefinitionRegistry()方法':[],
'如ConfigurationClassPostProcessor执行postProcessBeanDefinitionRegistry(),解析配置类,导入一些类的BeanDefinition到容器':[],
'4.循环1.2.3步，因为3步中会添加一些BeanDefinitionRegistryPostProcessor,BeanFactorPostProcessor到容器':[],
'5.String[] postProcessorNames = beanFactory.getBeanNamesForType(BeanFactoryPostProcessor.class, true, false)':[],
'获取容器中所有BeanFactoryPostProcessor的名称':[],
'6.invokeBeanFactoryPostProcessors(registryProcessors, beanFactory)':[],
'调用BeanFactoryPostProcessor的postProcessBeanFactory(ConfigurableListableBeanFactory beanFactory)方法':[],
'7.String[] postProcessorNames = beanFactory.getBeanNamesForType(BeanFactoryPostProcessor.class, true, false)':[],
'获取容器中所有的 BeanFactoryPostProcessor':[],
'8.invokeBeanFactoryPostProcessors(priorityOrderedPostProcessors, beanFactory)':[],
'过滤掉已经执行过BeanFactoryPostProcessor的postProcessBeanFactory()方法的bean':[],
'按Priority，Ordered，无任何优化级的顺序依次执行BeanFactoryPostProcessor的postProcessBeanFactory()方法':[]
}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 