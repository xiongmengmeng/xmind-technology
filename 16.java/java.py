import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="java"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("java")
r2=s2.getRootTopic()
r2.setTitle("java")


content={
'this/static':[
    '区别：是否处理差异化数据'
],
'类加载器ClassLoader':[
    'Class对象',
    {'组成':[
        'Field',
        'Constructor',
        'Method'
    ]}
],
'反射':[
    '创建实例',
    '调用方法'
],
'注解':[
    '通过反射获得'
],
'动态代理':[
    {'过程':[
        '1.组装.class文件',
        '2.类加载器->Class对象',
        '3.反射->代理类'
    ]},
    {'核心类':[
        'Proxy',
        'InvocationHandler'
    ]}

],
'泛型':[
    '编辑期变为真实类型' 
],
'JDBC':[
    {'Connection':[
        'Driver',
        'DriverManager'
    ]},
    'DataSource',

    
]
}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 