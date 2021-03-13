import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="mybatis"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("MyBatis插件(上)")
r2=s2.getRootTopic()
r2.setTitle("MyBatis插件(上)")


content={
'拦截器的注册':[
    '1.获取<plugin>标签的interceptor属性',
    '2.获取用户指定的拦截器属性并转换为Properties对象',
    '3.通过Java的反射机制实例化拦截器对象，设置拦截器对象属性',
    '4.将拦截器对象添加到拦截器链中'
],
'拦截器加入组件实例':[
    '组件:Executor、ParameterHandler、ResultSetHandler、StatementHandler',
    '1.根据用户配置的参数创建不同实现类的实例',
    '2.在工厂方法中执行拦截逻辑',
    '在newParameterHandler()、newResultSetHandler()、newStatementHandler()、newExecutor()工厂方法中，调用了InterceptorChain对象的pluginAll()'
],
'拦截器的执行过程':[
    '1.SqlSession调用Configuration对象的newExecutor()方法获取Executor实例',
    '2.newExecutor()工厂方法中调用InterceptorChain对象的pluginAll()方法',
    '3.pluginAll()方法中会调用自定义拦截器的plugin()方法',
    '4.plugin()方法，通常会调用Plugin类的wrap()静态方法创建一个代理对象',
    '5.SqlSession获取到Executor组件的代理对象，查询操作时会调用代理对象的query()方法',
    '6.按照JDK动态代理机制，query()方法中会调用Plugin类的invoke()方法',
    '7.invoke()方法中会调用自定义拦截器对象的intercept()方法执行拦截逻辑',
    '8.intercept()方法调用完毕后，调用目标Executor对象的query()方法',
    '9.所有操作执行完毕后，会将查询结果返回给SqlSession对象'
]



    
}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 