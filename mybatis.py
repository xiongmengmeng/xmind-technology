import xmind
from xmind.core.markerref import MarkerId
w = xmind.load("c:\\Users\\btr\\Desktop\\mybatis.xmind") 
s2=w.createSheet()
s2.setTitle("mybatis")
r2=s2.getRootTopic()
r2.setTitle("mybatis")
Core components

content={
'1.JDBC':[
    'JDBC:java语言中提供的访问关系型数据库的接囗',
    'mybatis框架是对JDBC API的轻量级封装',
    {'JDBC操作数据源的步骤':[
        '1.与数据源建立连接--Connection',
        '2.执行sql语句--Statement',
        '3.检索sql执行结果--ResultSet',
        '4.关闭连接'
    ]},
    'DatabaseMetaData:提供底层数据源信息'
],
'2.Mybatis常用工具类':[
    'SQL工具类：继承至AbstractSQL，只重写了该类的getSelf()方法',
    'ScriptRunner工具类：读取脚本文件中的sql语句并执行。',
    'SqlRunner工具类：结合SQL工具类，可以很方便地执行SQL语句并检索SQL执行结果',
    'MetaObject工具类：反射工具类，主要获取和设置对象属性值',
    'MetaClass工具类：反射工具类，主要获取类相关的信息',
    'ObjectFactory工具类:对象工厂，用于创建Mapper映射实体对象，是mybatis提供的一种扩展机制，可以自定义',
    'ProxyFactory工具类：代理工厂，用于创建动态代理对象，实现懒加载'
],
'SqlSession创建过程':[
    'Configuration实例创建',
    'SqlSessionFactory实例创建',
    'SqlSession实例创建',
    {'过程':[
        '1.获取mybatis配置文件输入流Reader',
        '2.创建SqlSessionFactoryBuilder对象',
        '3.SqlSessionFactoryBuilder.build(Reader reader)->DefaultSqlSessionFactory实例',
        {'细节':[
            '3.1.创建XMLConfigBuilder对象',
            '3.2.用XMLConfigBuilder.parse(Reader reader)->Configuration对象',
            '3.3.XMLConfigBuilder.build(Configuration config)->SqlSessionFactoryBuilder对象'
        ]}
        '4.SqlSessionFactory.openSession()->SqlSession对象',
         {'细节':[
            '4.1.获取mybatis主配置文件配置的环境信息',
            '4.2.创建事务管理器工厂',
            '4.3.创建事务管理器'，
            '4.4.创建Executor对象',
            '4.5.创建DefaultSqlSession对象'
        ]}
    ]}
],
'SqlSession执行Mapper过程':[
    {'1.Mapper接口的注册过程':[
        'Configuration类中，MapperRegistry mapperRegistry：注册Mapper接口信息',
        'MapperRegistry类中，Map<Class<?>, MapperProxyFactory<?>> knownMappers：注册Mapper接口对应的Class对象和MapperProxyFactory对象间关系',
        'MapperRegistry类addMapper()方法：向knownMappers属性中注册Mapper接口信息，MyBatis框架在应用启动时会解析所有的Mapper接口，然后调用此方法',
        'MapperRegistry类getMapper()方法：根据Mapper接口的Class对象获取对应的MapperProxyFactory，然后使用MapperProxyFactory对象调用方法newInstance(SqlSession sqlSession)创建Mapper动态代理对象',
        'MapperProxy类实现动态代理:使用了JDK内置的动态代理，实现了InvocationHandler接口，invoke()方法中为通用的拦截逻辑',
        '调用java.lang.reflect.Proxy类的newProxyInstance()方法创建代理对象'
    ]},
    {'2.MappedStatement对象的注册过程':[
        'Configuration类中，languageRegistry：注册LanguageDriver，用于将配置信息转换为SqlSource对象',
        'Configuration类中，mappedStatements：描述SQL信息，Key为Mapper的Id，Value为MappedStatement对象',
        'Configuration类addMappedStatement()方法：将MappedStatement对象添加到mappedStatements属性中',
        'MappedStatement对象的创建及注册过程：通过XMLConfigBuilder对象解析MyBatis主配置文件',
        '解析工作完成后，使用MapperBuilderAssistant对象的addMappedStatement()方法创建MappedStatement对象',
        '创建完成后，调用Configuration对象的addMappedStatement()方法将MappedStatement对象注册到Configuration对象中'
    ]},
    {'3.Mapper方法的调用过程':[
        'SqlSession对象的getMapper()方法->configuration.<T>getMapper(),->mapperRegistry.getMapper(),MapperProxyFactory,->MapperProxy,获取一个动态代理对象，然后通过代理对象调用方法，即执行MapperProxy类的invoke()方法',
        'MapperProxy类的invoke()方法:从缓存中取，取不到创建一个MapperMethod对象（根据mappedStatements中内容）,然后调用execute()方法，本质是根据sql类型，调用SqlSession相映方法',
        '',
        ''
    ]},
    {'4.SqlSession执行Mapper的过程':[
        'SqlSessionFactory调用openSession(),拿到SqlSession实例 ',
        '根据Mapper的Id从Configuration对象中获取对应的MappedStatement对象',
        '以MappedStatement对象作为参数，调用Executor实例的query()方法完成查询操作',
        ''
    ]}
],
'动态SQL实现原理':[
    '',
    '',
    '',
    ''
]


    
}

for key in content:
    t1 = r2.addSubTopic()
    t1.setTopicHyperlink(s2.getID()) 
    list=key.split(":")
    t1.setTitle(list[0])
    if len(list)>1:
        t1.setPlainNotes(list[1]) 
    # print(content[key])
    for i in content[key]:
        # print(type(i))
        if(type(i).__name__=='dict'):
            for t in i:
                t2 = t1.addSubTopic()
                t2.setTopicHyperlink(t1.getID()) 
                t2.setTitle(t)
                for j in i[t]:
                    #print(j)
                    if(type(j).__name__=='dict'):
                        for h in j:
                            t3 = t2.addSubTopic()
                            t3.setTopicHyperlink(t2.getID()) 
                            t3.setTitle(h) 
                            for m in j[h]:
                                if(type(m).__name__=='dict'):
                                    for n in m:
                                        t4 = t3.addSubTopic()
                                        t4.setTitle(n) 
                                        for l in m[n]:
                                            if(type(l).__name__=='dict'):
                                                for k in l:
                                                    t5 = t4.addSubTopic()       
                                                    t5.setTitle(k)
                                                    for p in l[k]:
                                                        if(type(p).__name__=='dict'):
                                                            for u in p:
                                                                t6 = t5.addSubTopic()
                                                                t6.setTitle(u)
                                                                for y in p[u]:
                                                                    if(type(y).__name__=='dict'):
                                                                        for a in y:
                                                                            t7 = t6.addSubTopic()
                                                                            t7.setTitle(a)
                                                                            for b in y[a]:
                                                                                t8 = t7.addSubTopic()
                                                                                t8.setTitle(b)
                                                                    else:
                                                                        t7 = t6.addSubTopic()
                                                                        t7.setTopicHyperlink(t2.getID()) 
                                                                        t7.setTitle(y)              
                                                        else:
                                                            t6 = t5.addSubTopic()
                                                            t6.setTopicHyperlink(t2.getID()) 
                                                            t6.setTitle(p)                                                        
                                            else:
                                                t5 = t4.addSubTopic()
                                                t5.setTopicHyperlink(t3.getID()) 
                                                t5.setTitle(l) 
                                else:
                                    t4 = t3.addSubTopic()
                                    t4.setTopicHyperlink(t3.getID()) 
                                    t4.setTitle(m) 
                    else:
                        t3 = t2.addSubTopic()
                        t3.setTopicHyperlink(t2.getID()) 
                        t3.setTitle(j) 
        else:
            t2 = t1.addSubTopic()
            t2.setTopicHyperlink(t1.getID()) 
            t2.setTitle(i) 



topics=r2.getSubTopics()
for topic in topics:
    topic.addMarker(MarkerId.starBlue)

xmind.save(w,"c:\\Users\\btr\\Desktop\\mybatis.xmind") 