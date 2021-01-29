import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="spring"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("@EnableTransactionManagement")
r2=s2.getRootTopic()
r2.setTitle("@EnableTransactionManagement")


content={
'什么是IOC':[
    '面向对象编程中的一种设计原则，可以用来减低计算机代码之间的耦合度',
    '最常见的方式叫做依赖注入（Dependency Injection，简称DI）',
    '还有一种方式叫“依赖查找”（Dependency Lookup）'
    '通过控制反转，对象在被创建的时候，由一个调控系统内所有对象的外界实体，将其所依赖的对象的引用传递给它'
],
'IOC 解决了什么问题':[
    '类与类之间的依赖关系',
    '将控制类与类之间依赖的权利交给了IOC，即：控制被反转了'
],
'IOC 的原理':[
    'java的反射'
],
'':[
    {'':[
        '',
        '',
        '',
        '',
        ''
    ]},
],
'':[
    {'':[
        '',
        '',
        '',
        '',
        ''
    ]},
],
}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 