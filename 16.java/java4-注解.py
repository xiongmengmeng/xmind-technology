import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="java"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("注解")
r2=s2.getRootTopic()
r2.setTitle("注解")


content={
'格式':[
    'public @interface 注解名称{',
    '属性列表;',
    '}'
],
'三种分类':[
    '自定义注解',   
    'JDK内置注解',
    '第三方注解（框架）'
],
'作用':[
    '像一个标签，贴在一个类、一个方法或者字段上',
    '为当前读取该注解的程序提供判断依据'
],
'级别':[
    '和类、接口、枚举是同一级别',
],
'学习':[
    '定义注解',
    '使用注解',
    {'读取注解':[
        '反射获取注解信息:',
        'Class、Method、Field对象都有个getAnnotation()，可以获取各自位置的注解信息'
    ]}
],
'元注解':[
    '加在注解上的注解',
    '@Target:限定该注解的使用位置',
    {'@Retention':[
        '注解的保留策略',
        '要想被反射读取，保留策略只能用RUNTIME，即运行时仍可读取',
        '原因：注解主要被反射读取，反射只能读取内存中的字节码信息'
    ]}
],
'属性':[
    {'数据类型':[
        '八种基本数据类型',
        'String',
        '枚举',
        'Class',
        '注解类型',
        '以上类型的一维数组'
    ]},
    {'value属性':[
        '如果注解的属性只有一个，且叫value，那么使用该注解时，可以不用指定属性名，因为默认就是给value赋值',
        '注解的属性如果有多个，无论是否叫value，都必须写明属性的对应关系'
    ]}
],
'应用':[
    {'自定义Junit框架':[
        '自定义MyJunitFrameWork类，识别@Test方法，并执行',
    ]},
    {'实现JPA':[
        '通过注解将表与类映射起来',
        {'JPA':[
            'Java Persistence API:Java持久化API',
            '一套Sun公司Java官方制定的ORM(对象关系映射) 方案,是规范，是标准 ，sun公司自己并没有实现',
            'ORM作用：在操作数据库之前，先把数据表与实体类关联起来'
        ]}
    ]}
]
}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 