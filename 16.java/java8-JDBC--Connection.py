import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="java"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("JDBC--Connection")
r2=s2.getRootTopic()
r2.setTitle("JDBC--Connection")


content={
'JDBC':[
    '一组API（包括少量类），为访问不同数据库提供了统一的途径，为开发者屏蔽了一些细节问题',
],
'获得数据库链接Connection':[
    {'com.mysql.jdbc.Driver':[
        '驱动，可用来获得数据库连接',
        'JDBC是Java制定的接口，数据库产商依照该接口编写与自家数据库配套的实现类',
        'MySQL、Oracle、SqlServer等都有自己的不同实现，这些实现类的集合统称为数据库驱动',
        {'继承com.mysql.cj.jdbc.Driver':[
            {'继承NonRegisteringDriver类':[
                '实现了connect(String url, java.util.Properties info)方法'
            ]},
            '实现java.sql.Driver接囗',
            ''
        ]},
        '无参构造',
        '静态代码块：java.sql.DriverManager.registerDriver(new Driver());',
        {'使用Driver去获取数据库连接':[
            {'1. 创建一个 Driver 实现类的对象':[
                'Driver driver = new com.mysql.jdbc.Driver()'
            ]},
            {'2.准备连接数据库的基本信息: url, user, password':[
                'String url = "jdbc:mysql://192.168.136.128:3306/test";',
                'Properties info = new Properties();',
                'info.put("user", "root");',
                'info.put("password", "root");'
            ]},
            {'3. 调用 Driver 接口的　connect(url, info) 获取数据库连接':[
                'Connection connection = driver.connect(url, info);',
                'System.out.println(connection);'
            ]}
        ]}
    ]},
    {'DriverManager':[
        '驱动管理，也可用来获得数据库连接',
        '内部维护一个容器，存储所有已注册的Driver:CopyOnWriteArrayList<DriverInfo> registeredDrivers = new CopyOnWriteArrayList<>()',
        'getConnection():循环遍历所有驱动，找到当前注册的驱动后调用driver.connect()获得Connection',
        {'使用DriverDriverManager去获取数据库连接':[
            {'1. 驱动的全类名':[
                'String driverClass = "com.mysql.jdbc.Driver";'
            ]},
            {'2. 准备连接数据库的基本信息: url, user, password':[
                'String url = "jdbc:mysql://192.168.136.128:3306/test";',
                'String user = "root";',
                'String password = "root";'
            ]},
            {'3. 加载数据库驱动程序(对应的 Driver 实现类中有注册驱动的静态代码块)':[
                'Class.forName(driverClass);'
            ]},
            {'4. 通过 DriverManager 的 getConnection() 方法获取数据库连接':[
                'Connection connection =DriverManager.getConnection(url, user, password);'
            ]}
        ]},
        {'原理':[
            'Class.forName(driverClass)',
            '类被加载进内存',
            '静态代码块执行：java.sql.DriverManager.registerDriver(newDriver());',
            'com.mysql.jdbc.driver实例被注册进DriverManager',
        ]},
        {'相比Driver获取数据库连接优势':[
            'url、user、password、driver移到jdbc.properties文件中，做成可配置'
        ]}
    ]}
]
}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 