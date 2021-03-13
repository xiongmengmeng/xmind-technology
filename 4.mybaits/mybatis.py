import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="mybatis"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("mybatis")
r2=s2.getRootTopic()
r2.setTitle("mybatis")


content={
'JDBC':[
    '操作数据库规范',
    {'组件':[
        'Connection',
        'Statement',
        'ResultSet'
    ]}
],
'mybatis':[
    '对JDBC的轻量级封装',
    {'组件':[
        'Configuration',
        'MappedStatement',
        'SqlSession',
        'Executor',
        'StatementHandler',
        'ParameterHandler',
        'ResultSetHandler',
        'TypeHandler'
    ]}
],
'SqlSession创建':[
    'SqlSessionFactory',
    '创建Exector对象',
    '创建DefaultSqlSession对象'
],
'SqlSession执行Mapper':[
    'Mapper接囗注册--MapperRegistry--Map<Class<?>, MapperProxyFactory<?>> knownMappers',
    'MappedStatement对象注册--Map<String, MappedStatement> mappedStatements',
    {'Mapper方法调用':[
        'getMapper()->MapperProxy',
        'invoke()->拿到MappedStatement->创建Statement'
    ]},
    {'动态SQL':[
        'MappedStatement',
        'SqlSource',
        'SqlNode'
    ]}
],
'插件':[
    'Interceptor接口',
    'InterceptorChain拦截器链',
    'Plugin工具类'

]

    
}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 