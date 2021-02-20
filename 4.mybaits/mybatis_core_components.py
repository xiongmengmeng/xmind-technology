import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="mybatis"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("mybatis_core_components")
r2=s2.getRootTopic()
r2.setTitle("mybatis核心组件")


content={
'操作数据库':[
    '1.调用SqlSession组件（用户层面的API）',
    '2.调用Executor（SQL执行器）,使用StatementHandler组件对JDBC的Statement对象进行操作',
    {'细节':[
        '当Statement类型为Callable...和PreparedStatement时,通过ParameterHandler组件为参数占位符赋值',
        'ParameterHandler组件中根据Java类型找到对应的TypeHandler对象',
        'TypeHandler通过Statement对象提供的setXXX()方法为Statement对象中的参数占位符设置值'
    ]},
    '3.ResultSetHandler组件从Statement对象中获取ResultSet对象（sql为selecet），并将期转换为Java对象'
],

'1.Configuration':[
    'MyBatis配置信息',
    '项目启动时加载,配置信息转换为Configuration对象',
    {'配置信息':[
        '框架属性的主配置',
        'SQL语句的Mapper配置'
    ]},
    {'内容':[
        '1.控制MyBatis运行时的行为',
        '2.容器：存放TypeHandler（类型处理器）、Mapper SQL',
        '3.组件的工厂类：Executor、StatementHandler、ResultSetHandler、ParameterHandler，方便实现插件拦截'
    ]},
    {'重要属性':[
        'mapperRegistry：注册Mapper接口信息，建立Mapper接口的Class对象和MapperProxyFactory对象之间的关系',
        'interceptorChain：注册MyBatis插件信息（拦截器）',
        'languageRegistry：注册LanguageDriver，用于将配置信息转换为SqlSource对象',
        'mappedStatements：描述SQL信息，Key为Mapper的Id，Value为MappedStatement对象',
        'resultMaps：建立Java实体属性与数据库字段间映射关系，Key为ResultMap的Id，Value为ResultMap对象',
        'parameterMaps：参数映射信息，Key为ParameterMap的Id，Value为ParameterMap对象'

    ]}
],
'2.SqlSession':[
    '面向用户的API',
    'MyBatis与数据库交互的接口，Executor组件的外观'
],
'3.Executor':[
    'SQL执行器，定义了对数据库的增删改查方法',
    {'使用':[
        '1.调用Configuration对象的getMappedStatement()方法,获取对应MappedStatement对象',
        '2.根据SQL类型调用Executor对象的query()或update()方法'
    ]}
],
'4.MappedStatement':[
    '描述SQL信息',
    '项目启动时，XML文件或注解配置的SQL转换为MappedStatement对象',
    '并注册到Configuration组件中',
    {'重要属性':[
        'id：命名空间中唯一的标识符',
        'lang：指定LanguageDriver（解析SQL语句，生成SqlSource对象）',
        'sqlSource：解析SQL语句为SqlSource对象'
    ]}
],
'5.StatementHandler':[
    '封装了对JDBC Statement对象的操作',
    '如为Statement对象设置参数，调用Statement接口提供的方法与数据库交互等',
    {'重要方法':[
        'prepare()：创建JDBC Statement对象，完成对象的属性设置',
        'update()：调用Statement对象的execute()方法执行更新语句',
        'query()：执行查询语句，使用ResultSetHandler处理查询结果集',
        'getBoundSql()：BoundSql封装了动态SQL解析后的SQL文本和参数映射信息'
    ]}
],
'6.TypeHandler':[
    '类型处理器，处理Java类型与JDBC类型之间的转换',
    {'使用场景':[
        '1.PreparedStatement对象为参数占位符设置值时：',
        '调用PreparedStatement接口的setXXX()方法，将Java类型转换为JDBC类型并为参数占位符赋值',
        '2.执行SQL语句获取ResultSet对象后:',
        '调用ResultSet对象的getXXX()方法获取字段值，将JDBC类型转换为Java类型'
    ]},
    {'方法':[
        '1.setParameter():为PreparedStatement对象参数的占位符设置值',
        '2.getResult():从ResultSet对象中获取列的值'
    ]}
],
'7.ParameterHandler':[
    '处理SQL中的参数占位符，为参数占位符设置值',
    {'方法':[
        '1.getParameterObject()：获取执行Mapper时传入的参数对象',
        '2.setParameters()：为JDBC PreparedStatement对象设置参数值'
    ]}
],
'8.ResultSetHandler':[
    '封装了对ResultSet对象的处理逻辑，将结果集转换为Java实体对象',
    'handleResultSets()：对ResultSet对象进行处理'
]

    
}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 