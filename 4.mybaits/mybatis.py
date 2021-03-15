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
        {'Configuration':[
            '控制MyBatis运行时的行为',
            '容器:Mapper,SQL,TypeHandler',
            {'组件的工厂类':[
                'Executor',
                'StatementHandler',
                'ResultSetHandler',
                'ParameterHandler',
                '方便实现插件拦截'
            ]}
        ]},
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
    'Mapper接囗注册：MapperRegistry--Map<Class<?>, MapperProxyFactory<?>> knownMappers',
    'MappedStatement对象注册：Map<String, MappedStatement> mappedStatements',
    {'Mapper方法调用':[
        '1.getMapper()->MapperProxy.invoke()',
        {'2.SqlSession.selectList()':[
            '2.1拿到MappedStatement',
            '2.2通过Exector得到BoundSql,创建StatementHandler',
            '2.3通过Statement执行sql',
            '2.4ResultSetHandler处理结果集'
        ]}
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