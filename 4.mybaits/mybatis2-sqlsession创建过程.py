import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="mybatis"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("SqlSession创建过程")
r2=s2.getRootTopic()
r2.setTitle("SqlSession创建过程")


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
]


    
}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 