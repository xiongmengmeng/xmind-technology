import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="mybatis"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("SqlSession执行Mapper过程")
r2=s2.getRootTopic()
r2.setTitle("SqlSession执行Mapper过程")


content={
'1.Mapper接口的注册':[
    'Configuration类中，MapperRegistry mapperRegistry：注册Mapper接口信息',
    'MapperRegistry类中，Map<Class<?>, MapperProxyFactory<?>> knownMappers：Class对象--MapperProxyFactory对象',
    'MapperRegistry类addMapper()方法：向knownMappers注册Mapper接口信息(应用启动时调用)',
    {'MapperRegistry类getMapper()方法':[
        '根据Mapper接口的Class对象获取对应MapperProxyFactory',
        'MapperProxyFactory调用方法newInstance(SqlSession sqlSession)创建Mapper动态代理对象'
    ]},
    'MapperProxy:使用JDK内置的动态代理，实现了InvocationHandler接口，invoke()方法中为通用的拦截逻辑',
    '调用java.lang.reflect.Proxy类的newProxyInstance()方法创建代理对象'
],
'2.MappedStatement对象的注册':[
    'Configuration类中,LanguageDriverRegistry languageRegistry：将配置信息转换为SqlSource对象',
    'Configuration类中,Map<String, MappedStatement> mappedStatements：描述SQL信息，Key为Mapper的Id，Value为MappedStatement对象',
    'Configuration类addMappedStatement()方法：将MappedStatement对象添加到mappedStatements属性中',
    '1.通过XMLConfigBuilder对象解析MyBatis主配置文件',
    '2.使用MapperBuilderAssistant对象的addMappedStatement()方法创建MappedStatement对象',
    '3.调用Configuration对象的addMappedStatement()方法将MappedStatement对象注册到Configuration对象中'
],
'3.Mapper方法的调用过程':[
    'SqlSession对象的getMapper()方法->',
    'configuration.<T>getMapper(),->',
    'mapperRegistry.getMapper()->',
    'MapperProxyFactory,->MapperProxy,获取一个动态代理对象',
    '执行MapperProxy类的invoke()方法',
    {'MapperProxy类的invoke()方法':[
        '从缓存中取，取不到创建一个MapperMethod对象（根据mappedStatements内容）',
        '然后调用execute()方法，本质是根据sql类型，调用SqlSession相映方法'
    ]}
],
'总结：':[
    '1.SqlSessionFactory调用openSession(),拿到SqlSession实例 ',
    '2.根据Mapper的Id从Configuration对象中获取对应的MappedStatement对象',
    '3.以MappedStatement对象作为参数，调用Executor实例的query()方法完成查询操作'
]



    
}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 