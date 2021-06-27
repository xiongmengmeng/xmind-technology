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
'1.描述下BeanFactory':[
    '',
],
'2.BeanFactory和ApplicationContext的区别':[
    '',
],
'3.简述SpringIoC的加载过程':[
    '',
],
'4.简述Bean的生命周期':[
    '',
],
'5.Spring中有哪些扩展接口及调用时机':[
    ''
],
'6.BeanFactory和FactoryBean的区别':[
    ''
],
'7.请介绍BeanFactoryPostProcessor在Spring中的用途':[
    ''
],
'8.Spring中有哪些扩展接口及调用时机':[
    ''
],
'9.Spring是怎样避免读取到不完整Bean的':[
    ''
],
'10.怎么样可以在所有Bean创建完后做扩展代码':[
    ''
],
'11.请介绍下Spring事件监听器的原理':[
    ''
],
'？
？
':[
    ''
],

}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 