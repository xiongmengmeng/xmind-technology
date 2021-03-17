import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="MyBatis"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("MyBatis与Spring整合基础类")
r2=s2.getRootTopic()
r2.setTitle("MyBatis与Spring整合基础类")


content={
'InitializingBean':[
    'afterPropertiesSet()'
],
'DaoSupport':[
    '实现InitializingBean',
    {'重写afterPropertiesSet()方法':[
        'checkDaoConfig()：模版方法',
        'initDao()'
    ]}
],
'SqlSessionDaoSupport':[
    '继承DaoSupport',
    {'重写checkDaoConfig()方法':[
        '判断this.sqlSession是否为空，为空抛异常'
    ]}
],
'MapperFactoryBean':[
    '作用:创建Mapper的代理对象',
    {'继承SqlSessionDaoSupport,重写checkDaoConfig()方法':[
        '1.调用父类方法：super.checkDaoConfig()',
        '2.将Mapper封装为MapperProxyFactory，放入Map<Class<?>, MapperProxyFactory<?>> knownMappers:',
        'configuration.addMapper(this.mapperInterface)->',
        'knownMappers.put(type, new MapperProxyFactory<T>(type))'
    ]},
    {'继承FactoryBean类，重写getObject方法':[
        'getSqlSession().getMapper(this.mapperInterface)->',
        'configuration.getMapper(this.mapperInterface)'
    ]}
],
'SqlSessionFactoryBean':[
    '作用：构建SqlSessionFactory对象，SqlSessionFactory对象创建SqlSession对象（MyBatis提供的与数据库交互的接口）',
    '继承FactoryBean类,重写getObject()方法，返回sqlSessionFactory',
    '实现InitializingBean接囗，重写afterPropertiesSet()方法',
    '核心属性:之前在配置文件中写的MyBatis的全部配置',
    {'afterPropertiesSet()方法':[
        '类初始化后调用',
        'this.sqlSessionFactory = buildSqlSessionFactory();'
    ]},
    {'buildSqlSessionFactory()方法':[
        '1.解析配置文件，构造Configuration对象',
        '2.解析配置文件，如有configLocation和mapperLocations时,将Mapper封装为mapperProxyFactory存入到knownMappers中',
        '3.解析Mapper文件，将sql包装成mappedStatement，存入到mappedStatements这个map中'
    ]}
]

}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 