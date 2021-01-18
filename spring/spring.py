import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="spring"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("spring")
r2=s2.getRootTopic()
r2.setTitle("spring")


content={
'Core Container':[
   'Core:包含Spring框架基本的核心工具类',
   'Beans:所有应用都要用到的，它包含访问配置文件、创建和管理bean以及进行Inversion of Control / Dependency Injection（IoC/DI）操作相关的所有类',
   'Context:提供了一种类似于JNDI注册器的框架式的对象访问方法。Context模块继承了Beans的特性，为Spring核心提供了大量扩展,ApplicationContext接口是Context模块的关键。',
   'Expression Language:提供了一个强大的表达式语言用于在运行时查询和操纵对象'
],
'Data Access/Integration':[
    'JDBC:提供了一个JDBC抽象层,块包含了Spring对JDBC数据访问进行封装的所有类',
    'ORM模块为流行的对象-关系映射API',
    'OXM模块提供了一个对Object/XML映射实现的抽象层',
    ' JMS（Java Messaging Service）模块主要包含了一些制造和消费消息的特性',
    'Transaction模块支持编程和声明性的事物管理，这些事物类必须实现特定的接口，并且对所有的POJO都适用'
],
'Web':[
    '',
    '',
    '',
    '',
    ''
]
}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 