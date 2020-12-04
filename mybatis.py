import xmind
from xmind.core.markerref import MarkerId
w = xmind.load("c:\\Users\\btr\\Desktop\\mybatis.xmind") 
s2=w.createSheet()
s2.setTitle("mybatis")
r2=s2.getRootTopic()
r2.setTitle("mybatis")


content={
'1.JDBC':[
    'JDBC:java语言中提供的访问关系型数据库的接囗',
    'mybatis框架是对JDBC API的轻量级封装',
    {'JDBC操作数据源步骤':[
        '1.与数据源建立连接--Connection',
        '2.执行sql语句--Statement',
        '3.检索sql执行结果--ResultSet',
        '4.关闭连接'
    ]},
    'DatabaseMetaData:提供底层数据源信息'
],
'2.Mybatis常用工具类':[
    'SQL：继承至AbstractSQL，重写了该类的getSelf()方法',
    'ScriptRunner：读取脚本文件中的sql语句并执行',
    'SqlRunner：结合SQL工具类，可以很方便地执行SQL语句并检索SQL执行结果',
    'MetaObject：反射工具类，主要获取和设置对象属性值',
    'MetaClass：反射工具类，主要获取类相关的信息',
    'ObjectFactory:对象工厂，用于创建Mapper映射实体对象',
    'ProxyFactory：代理工厂，用于创建动态代理对象，实现懒加载'
],
'3.SqlSession创建过程':[
    '1.获取mybatis配置文件输入流Reader',
    '2.创建SqlSessionFactoryBuilder对象',
    '3.SqlSessionFactoryBuilder.build(Reader reader)->DefaultSqlSessionFactory实例',
    {'细节':[
        '3.1.创建XMLConfigBuilder对象',
        '3.2.用XMLConfigBuilder.parse(Reader reader)->Configuration对象',
        '3.3.XMLConfigBuilder.build(Configuration config)->SqlSessionFactoryBuilder对象'
    ]},
    '4.SqlSessionFactory.openSession()->SqlSession对象',
    {'细节':[
        '4.1.获取mybatis主配置文件配置的环境信息',
        '4.2.创建事务管理器工厂',
        '4.3.创建事务管理器',
        '4.4.创建Executor对象',
        '4.5.创建DefaultSqlSession对象'
    ]}
],
'4.SqlSession执行Mapper过程':[
    {'1.Mapper接口的注册':[
        'Configuration类中，MapperRegistry mapperRegistry：注册Mapper接口信息',
        'MapperRegistry类中，Map<Class<?>, MapperProxyFactory<?>> knownMappers：Class对象--MapperProxyFactory对象',
        'MapperRegistry类addMapper()方法：向knownMappers注册Mapper接口信息(应用启动时调用)',
        {'MapperRegistry类getMapper()方法':[
            '根据Mapper接口的Class对象获取对应MapperProxyFactory',
            'MapperProxyFactory调用方法newInstance(SqlSession sqlSession)创建Mapper动态代理对象'
        ]},
        'MapperProxy:使用JDK内置的动态代理，实现了InvocationHandler接口，invoke()方法中为通用的拦截逻辑',
        '调用java.lang.reflect.Proxy类的newProxyInstance()方法创建代理对象'
    ]},
    {'2.MappedStatement对象的注册':[
        'Configuration类中,LanguageDriverRegistry languageRegistry：将配置信息转换为SqlSource对象',
        'Configuration类中,Map<String, MappedStatement> mappedStatements：描述SQL信息，Key为Mapper的Id，Value为MappedStatement对象',
        'Configuration类addMappedStatement()方法：将MappedStatement对象添加到mappedStatements属性中',
        '1.通过XMLConfigBuilder对象解析MyBatis主配置文件',
        '2.使用MapperBuilderAssistant对象的addMappedStatement()方法创建MappedStatement对象',
        '3.调用Configuration对象的addMappedStatement()方法将MappedStatement对象注册到Configuration对象中'
    ]},
    {'3.Mapper方法的调用过程':[
        'SqlSession对象的getMapper()方法->',
        'configuration.<T>getMapper(),->',
        'mapperRegistry.getMapper()->',
        'MapperProxyFactory,->MapperProxy,获取一个动态代理对象',
        '执行MapperProxy类的invoke()方法',
        {'MapperProxy类的invoke()方法':[
            '从缓存中取，取不到创建一个MapperMethod对象（根据mappedStatements内容）',
            '然后调用execute()方法，本质是根据sql类型，调用SqlSession相映方法'
        ]}
    ]},
    {'总结：':[
        '1.SqlSessionFactory调用openSession(),拿到SqlSession实例 ',
        '2.根据Mapper的Id从Configuration对象中获取对应的MappedStatement对象',
        '3.以MappedStatement对象作为参数，调用Executor实例的query()方法完成查询操作'
    ]}
],
'5.动态SQL实现原理':[
    'SqlSource:描述XML文件或Java注解配置的SQL资源信息',
    'SqlNode:描述动态SQL中<if>、<where>等标签信息',
    'LanguageDriver:对Mapper SQL配置进行解析，将SQL配置转换为SqlSource对象',
    {'项目加载时':[
        '1.使用LanguageDriver解析sql语句',
        '2.将解析后sqlNode对象放入SqlSource对象中',
        '3.将SqlSource对象放入MappedStatement对象的属性保存'
    ]},
    {'方法调用时':[
        '1.调用MappedStatement对象的getBoundSql()方法',
        '2.方法里会调用SqlSource对象的getBoundSql()方法获取BoundSql对象',
        '3.整个过程主要是将SqlNode对象转换为SQL语句'
    ]},
    {'#{}和${}的区别':[
        '#{}:占位符内容会被替换成“？”，通过PreparedStatement对象的setXXX()方法设值,有效避免SQL注入',
        '${}参数占位符:内容会被直接替换为参数值'
    ]}
],
'6.MyBatis插件':[
    'Configuration类，InterceptorChain interceptorChain，一个拦截器链，存放通过<plugins>标签注册的所有拦截器',
    {'MyBatis使用工厂方法创建Executor、ParameterHandler、ResultSetHandler、StatementHandler组件的实例':[
        '1.根据用户配置的参数创建不同实现类的实例',
        '2.在工厂方法中执行拦截逻辑'
    ]},
    {'拦截器的注册':[
        '1.获取<plugin>标签的interceptor属性',
        '2.获取用户指定的拦截器属性并转换为Properties对象',
        '3.通过Java的反射机制实例化拦截器对象，设置拦截器对象属性',
        '4.将拦截器对象添加到拦截器链中'
    ]},
    {'Interceptor接口':[
        '自定义的插件都必须实现Interceptor接口',
        'intercept()：定义拦截逻辑，方法在目标方法调用时执行,Invocation对象作参数',
        'plugin()：用于创建Executor、ParameterHandler、ResultSetHandler或StatementHandler的代理对象',
        'setProperties()：设置插件的属性值'
    ]},
    {'Invocation类':[
        '封装了目标对象、目标方法及参数信息',
        'proceed()：用于执行目标方法的逻辑'
    ]},
    {'Plugin工具类':[
        '实现了InvocationHandler接口，采用JDK内置的动态代理方式创建代理对象',
        'wrap()：简化动态代理对象的创建',
        'invoke()：会在调用目标对象的方法时执行'
    ]},
    {'拦截器的执行过程':[
        '1.SqlSession调用Configuration对象的newExecutor()方法获取Executor实例',
        '2.newExecutor()工厂方法中调用InterceptorChain对象的pluginAll()方法',
        '3.pluginAll()方法中会调用自定义拦截器的plugin()方法',
        '4.plugin()方法，通常会调用Plugin类的wrap()静态方法创建一个代理对象',
        '5.SqlSession获取到Executor组件的代理对象，查询操作时会调用代理对象的query()方法',
        '6.按照JDK动态代理机制，query()方法中会调用Plugin类的invoke()方法',
        '7.invoke()方法中会调用自定义拦截器对象的intercept()方法执行拦截逻辑',
        '8.intercept()方法调用完毕后，调用目标Executor对象的query()方法',
        '9.所有操作执行完毕后，会将查询结果返回给SqlSession对象'
    ]}
],
'7.MyBatis与Spring整合':[
    'MyBatis的Mapper实例通过动态代理创建,与Spring框架整合，Mapper动态代理对象作为Bean注册到Spring容器中',
    {'Spring框架的启动过程':[
        '1.对所有Bean的配置信息进行解析(XML配置文件、Java注解以及Java Config方式配置的Bean)',
        '2.Bean的配置信息->BeanDefinition对象，注册到BeanDefinitionRegistry容器',
        '3.执行BeanFactoryPostProcessor扩展逻辑对Bean工厂信息进行修改',
        '4.BeanDefinition对象->实例化所有单例Bean并注入依赖',
        '5.执行所有BeanPostProcessor对象的Bean的postProcessBeforeInitialization()方法',
        '6.执行Bean的初始化方法',
        '7.执行所有BeanPostProcessor对象的postProcessAfterInitialization()方法'
    ]},
    {'Mapper动态代理对象注册过程':[
        {'启动时':[
            '扫描指定路径下的Mapper接口',
            '将Mapper接口转换为Spring中的BeanDefinition对象',
            '并且beanClass属性为MapperFactoryBean'
        ]},
        {'启动后':[
            '每个Mapper接口创建一个MapperFactoryBean对象',
            '通过Mapper接口获取Bean时，获取到的是MapperFactoryBean对象的getObject()方法返回的对象'
        ]}
    ]},
    'Spring框架通过Java中的ThreadLocal机制保证同一个线程中获取到的始终是同一个Connection对象'
],
'重点':[
    '获取自动生成的(主)键值:@Options(useGeneratedKeys = true, keyProperty = "id")',
    {'mapper中如何传递多个参数':[
        '1.@param 注解',
        '2.map'
    ]},
    {'半自动ORM映射工具':[
        '全自动：查询时，对象关系模型有记录关联对象或关联集合对象的关系;',
        '半自动：不记录上述关系'
    ]},
    {'Mybatis的插件运行原理':[
        '插件的目标：ParameterHandler、ResultSetHandler、StatementHandler、Executor这4种接口',
        '使用JDK的动态代理，为需要拦截的接口生成代理对象以实现接口方法拦截功能',
        '每当执行这4种接口对象的方法时，就会进入拦截方法',
        '实现Interceptor接口并复写intercept()方法，注解指定要拦截的接囗方法'
    ]},
    {'#{}和${}的区别':[
        '#{}是预编译处理，${}是字符串替换',
        '处理#{}时，会将sql中的#{}替换为?号，调用PreparedStatement的set方法来赋值',
        '处理${}时，就是把${}替换成变量的值'
    ]},
    {'Mybatis可以映射Enum枚举类':[
        'Mybatis可以映射枚举类，不单可以映射枚举类，Mybatis可以映射任何对象到表的一列上',
        '映射方式为自定义一个TypeHandler，实现TypeHandler的setParameter()和getResult()接口方法',
        'TypeHandler作用:完成javaType和jdbcType的转换，修改setParameter()和getResult()两方法（设置sql问号占位符参数和获取列查询结果）'
    ]},
    {'Mybatis的映射文件和内部数据结构关系':[
        '方法参数被解析为ParameterMap对象，其每个子元素会被解析为ParameterMapping对象 ',
        '方法返回值被解析为ResultMap对象，其每个子元素会被解析为ResultMapping对象',
        'sql 被解析为MappedStatement对象，标签内的sql会被解析为BoundSql对象'
    ]},
    {'一级缓存与二级缓存的区别':[
        '一级缓存是SqlSession级别的缓存,默认开起',
        '二级缓存是mapper级别的缓存，默认不开，现在分布式，不适用'
    ]},
    {'Mybatis的编程步骤':[
        '1.使用SqlSession组件，它是用户层面的API',
        '2.调用Executor，它是SQL执行器',
        '3.Executor会使用StatementHandler组件对JDBC的Statement对象进行操作',
        '4.当Statement类型为CallableStatement和PreparedStatement时，会通过ParameterHandler组件为参数占位符赋值',
        '5.ParameterHandler组件会根据Java类型找到对应的TypeHandler对象',
        '6.TypeHandler中会通过Statement对象提供的setXXX()方法为Statement对象中的参数占位符设置值',
        '7.SQL为SELECT，ResultSetHandler组件从Statement对象中获取ResultSet对象，然后将ResultSet对象转换为Java对象'
    ]}
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