import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="mybatis"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("核心组件(下)")
r2=s2.getRootTopic()
r2.setTitle("核心组件(下)")


content={
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