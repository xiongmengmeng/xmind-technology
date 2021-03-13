import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="mybatis"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("Mapper方法调用过程")
r2=s2.getRootTopic()
r2.setTitle("Mapper方法调用过程")


content={
'1.Mapper接口的注册':[
    'Configuration类中，MapperRegistry mapperRegistry：注册Mapper接口信息',
    'MapperRegistry类中，Map<Class<?>, MapperProxyFactory<?>> knownMappers：Class对象--MapperProxyFactory对象',
    {'MapperRegistry类addMapper()方法':[
        '向knownMappers注册Mapper接口信息(应用启动时调用)'
    ]},
    {'MapperRegistry类getMapper()方法':[
        '根据Mapper接口的Class对象获取对应MapperProxyFactory',
        'MapperProxyFactory调用方法newInstance(SqlSession sqlSession)创建Mapper动态代理对象:',
        '调用java.lang.reflect.Proxy类的newProxyInstance()方法创建代理对象'
    ]},
    'MapperProxy:实现了InvocationHandler接口，invoke()方法中为通用的拦截逻辑'
],
'2.MappedStatement对象的注册':[
    'Configuration类中,LanguageDriverRegistry languageRegistry：将配置信息转换为SqlSource对象',
    'Configuration类中,Map<String, MappedStatement> mappedStatements：描述SQL信息，Key为Mapper的Id，Value为MappedStatement对象',
    'Configuration类addMappedStatement()方法：将MappedStatement对象添加到mappedStatements属性中',
    '1.通过XMLConfigBuilder对象解析MyBatis主配置文件',
    '2.使用MapperBuilderAssistant对象的addMappedStatement()方法创建MappedStatement对象',
    '3.调用Configuration对象的addMappedStatement()方法将MappedStatement对象注册到Configuration对象中'
],
'3.Mapper方法调用过程':[
    {'SqlSession对象的getMapper()方法':[
        'configuration.getMapper(),->',
        'mapperRegistry.getMapper()->',
        'MapperProxyFactory.newInstance()->',
        'MapperProxy的实例（一个动态代理对象）',
    ]},
    {'MapperProxy类的invoke()方法':[
        'MapperProxy类实现了InvocationHandler接口，重写invoke()方法：',
        '1.从缓存中取，取不到创建一个MapperMethod对象（根据mappedStatements内容）',
        '2.MapperMethod对象调用execute()方法，本质：根据sql类型，调用SqlSession相映方法',
        {'SqlSession执行Mapper过程':[
            '2.1据Mapper的Id从Configuration对象中获取对应MappedStatement对象',
            '2.2以MappedStatement对象为参数，调用Executor实例的query()方法',
            {'BaseExecutor类的query()方法':[
                '从MappedStatement对象中获取BoundSql对象',
                '调用Configuration对象的newStatementHandler()创建StatementHandler对象',
                '据Mapper的statementType属性创建对应StatementHandler实例进行处理'
            ]}
        ]}
    ]}
]



    
}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 