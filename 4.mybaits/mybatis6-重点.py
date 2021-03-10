import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="mybatis"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("重点")
r2=s2.getRootTopic()
r2.setTitle("重点")


content={


'获取自动生成的(主)键值:@Options(useGeneratedKeys = true, keyProperty = "id")':[],
'mapper中如何传递多个参数':[
    '1.@param 注解',
    '2.map'
],
'半自动ORM映射工具':[
    '全自动：查询时，对象关系模型有记录关联对象或关联集合对象的关系;',
    '半自动：不记录上述关系'
],
'Mybatis的插件运行原理':[
    '插件的目标：ParameterHandler、ResultSetHandler、StatementHandler、Executor这4种接口',
    '使用JDK的动态代理，为需要拦截的接口生成代理对象以实现接口方法拦截功能',
    '每当执行这4种接口对象的方法时，就会进入拦截方法',
    '实现Interceptor接口并复写intercept()方法，注解指定要拦截的接囗方法'
],
'#{}和${}的区别':[
    '#{}是预编译处理，${}是字符串替换',
    '处理#{}时，会将sql中的#{}替换为?号，调用PreparedStatement的set方法来赋值',
    '处理${}时，就是把${}替换成变量的值'
],
'Mybatis可以映射Enum枚举类':[
    'Mybatis可以映射枚举类，不单可以映射枚举类，Mybatis可以映射任何对象到表的一列上',
    '映射方式为自定义一个TypeHandler，实现TypeHandler的setParameter()和getResult()接口方法',
    'TypeHandler作用:完成javaType和jdbcType的转换，修改setParameter()和getResult()两方法（设置sql问号占位符参数和获取列查询结果）'
],
'Mybatis的映射文件和内部数据结构关系':[
    '方法参数被解析为ParameterMap对象，其每个子元素会被解析为ParameterMapping对象 ',
    '方法返回值被解析为ResultMap对象，其每个子元素会被解析为ResultMapping对象',
    'sql 被解析为MappedStatement对象，标签内的sql会被解析为BoundSql对象'
],
'一级缓存与二级缓存的区别':[
    '一级缓存是SqlSession级别的缓存,默认开起',
    '二级缓存是mapper级别的缓存，默认不开，现在分布式，不适用'
],
'Mybatis的编程步骤':[
    '1.使用SqlSession组件，它是用户层面的API',
    '2.调用Executor，它是SQL执行器',
    '3.Executor会使用StatementHandler组件对JDBC的Statement对象进行操作',
    '4.当Statement类型为CallableStatement和PreparedStatement时，会通过ParameterHandler组件为参数占位符赋值',
    '5.ParameterHandler组件会根据Java类型找到对应的TypeHandler对象',
    '6.TypeHandler中会通过Statement对象提供的setXXX()方法为Statement对象中的参数占位符设置值',
    '7.SQL为SELECT，ResultSetHandler组件从Statement对象中获取ResultSet对象，然后将ResultSet对象转换为Java对象'
]



    
}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 