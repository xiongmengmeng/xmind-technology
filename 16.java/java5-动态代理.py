import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="java"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("动态代理")
r2=s2.getRootTopic()
r2.setTitle("动态代理")


content={
'动态代理':[
    '不写代理类，通过反射调用代理类的方法',
    {'过程如下':[
        '代理Class对象',
        '->反射创建代理对象',
        '->调用代理对象的方法'
    ]},
    '思考：Class对象包含了一个类的所有信息，如构造器、方法、字段等,如不写代理类，这些信息从哪获取?接口',
    {'代理类和目标类实现同一组接口':[
        '尽可能保证代理对象的内部结构和目标对象一致',
        '这样对代理对象的操作最终都可以转移到目标对象身上，代理对象只需专注于增强代码的编写'
    ]}
],
'Proxy':[
    {'getProxyClass(ClassLoader, interfaces)':[
        '返回代理Class对象',
        '本质：以Class造Class',
        '1.从传入的接口Class中，“拷贝”类结构信息到一个新的Class对象中',
        '2.但新的Class对象带有构造器，可以创建对象'
    ]},
    {'newProxyInstance()':[
        '直接返回代理实例'
    ]}
],
'学习':[
    'https://www.zhihu.com/question/20794107/answer/658139129'
]
}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 