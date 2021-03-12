import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="mybatis"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("JDBC规范")
r2=s2.getRootTopic()
r2.setTitle("JDBC规范")


content={
'JDBC':[
    'java database connectivity:java语言提供的访问关系型数据库的接囗',
    'mybatis框架:对JDBC API的轻量级封装',
    {'JDBC操作数据源步骤':[
        '1.与数据源建立连接--Connection',
        {'获得Connection的两种方式':[
            'DriverManager',
            'DataSource'
        ]},
        '2.执行sql语句--Statement',
        '3.检索sql执行结果--ResultSet',
        '4.关闭连接'
    ]},
],
'JDBC API中的类与接囗':[
    'JDBC API主要有两个包',
    {'java.sql包':[
        '涵盖了JDBC最核心的API',
        '1.数据类型',
        '2.枚举',
        '3.API相关',
        '4.驱动相关',
        '5.异常'
    ]},
    {'javax.sql':[
        '1.数据源',
        '2.连接池相关',
        '3.ResultSet扩展',
        '4.分布式扩展'
    ]}
],
'Connection':[
    {'两种获得Connection对象的方式':[
        'DriverManager：加载JDBC驱动，调用getConnection()方法，获取Connection对象',
        'DataSource：一个DataSource对象属性被设置后，代表一个数据源，调用getConnection()方法，获取Connection对象'
    ]}
],
'Statement':[
    'JDBC API操作数据库的核心接囗，具体实现由JDBC驱动来完成',
    '创建：调用Connection对象的createStatement()方法',
    '不支持参数输入',
    'PreparedStatement接囗：增加参数占位符的功能，用"?"代表占位符 ，其实例代表可以被预编译的sql语句',
    'CallableStatement接囗：增加了调用存储过程以及检索存储过程调用结果的方法'
],
'ResultSet':[
    '提供了检索和操作sql执行结果相关的方法',
    '接囗的实现类封装了sql查询的结果，可以对ResultSet进行遍历，通过getxxx()方法获取查询结果集'
],
'重要类':[
    'MetaObject工具类：反射工具类，主要获取和设置对象属性值',
    'ObjectFactory工具类:对象工厂，用于创建Mapper映射实体对象',
    'ProxyFactory工具类：代理工厂，用于创建动态代理对象，实现懒加载'
]   
}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 