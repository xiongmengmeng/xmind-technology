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
'1.JDBC':[
    'java语言提供的访问关系型数据库的接囗',
    'mybatis框架:对JDBC API的轻量级封装',
    {'JDBC操作数据源步骤':[
        '1.与数据源建立连接--Connection',
        {'获得Connection的两种方式':[
            'DriverManager',
            'DataSource'
        ]}
        '2.执行sql语句--Statement',
        '3.检索sql执行结果--ResultSet',
        '4.关闭连接'
    ]},
],
'Configuration：':[
    '述MyBatis配置信息，例如<settings>标签配置的参数信息',
    '作为容器注册MyBatis其他组件，例如TypeHandler、MappedStatement等',
    '提供工厂方法，创建ResultSetHandler、StatementHandler、Executor、ParameterHandler等组件实例'
],
'MappedStatement：':[

    '描述<select|update|insert|delete>或者@Select、@Update等注解配置的SQL信息',
    'sqlSource：解析<select|update|insert|delete>，将SQL语句配置信息解析为SqlSource对象',
    '',
    ''
],
'StatementHandler':[
    '封装了对JDBC Statement对象的操作',
    '如为Statement对象设置参数，调用Statement接口提供的方法与数据库交互，等等',
    '',
    ''
],
'TypeHandler':[
    '类型处理器，用于处理Java类型与JDBC类型之间的转换',
    {'使用的两种场景':[
        '1.PreparedStatement对象为参数占位符设置值时，需要调用PreparedStatement接口中提供的一系列的setXXX()方法，将Java类型转换为对应的JDBC类型并为参数占位符赋值',
        '2.执行SQL语句获取ResultSet对象后，需要调用ResultSet对象的getXXX()方法获取字段值，此时会将JDBC类型转换为Java类型'
    ]}
    '',
    '',
    ''
],
'ParameterHandler':[
    '用于处理SQL中的参数占位符，为参数占位符设置值',
    '',
    '',
    ''
],
'ResultSetHandler':[
    '封装了对ResultSet对象的处理逻辑，将结果集转换为Java实体对象',
    '',
    '',
    ''
],
'':[
    '',
    '',
    '',
    ''
],


SqlSession：
面向用户的API，是MyBatis与数据库交互的接口，是Executor组件的外观。

Executor：
SQL执行器，MyBatis中对数据库所有的增删改查操作都是由Executor组件完成的。

StatementHandler：
。

。

。



    
}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 