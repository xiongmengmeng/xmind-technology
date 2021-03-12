import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="mybatis"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("动态SQL实现原理")
r2=s2.getRootTopic()
r2.setTitle("动态SQL实现原理")


content={


'SqlSource:描述XML文件或Java注解配置的SQL资源信息':[],
'SqlNode:描述动态SQL中<if>、<where>等标签信息':[],
'LanguageDriver:对Mapper SQL配置进行解析，将SQL配置转换为SqlSource对象':[],
'项目加载时':[
    '1.使用LanguageDriver解析sql语句',
    '2.将解析后sqlNode对象放入SqlSource对象中',
    '3.将SqlSource对象放入MappedStatement对象的属性保存'
],
'方法调用时':[
    '1.调用MappedStatement对象的getBoundSql()方法',
    '2.方法里会调用SqlSource对象的getBoundSql()方法获取BoundSql对象',
    '3.整个过程主要是将SqlNode对象转换为SQL语句'
],
'#{}和${}的区别':[
    '#{}:占位符内容会被替换成“？”，通过PreparedStatement对象的setXXX()方法设值,有效避免SQL注入',
    '${}参数占位符:内容会被直接替换为参数值'
]




    
}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 