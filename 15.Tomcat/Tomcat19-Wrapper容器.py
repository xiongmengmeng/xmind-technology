import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="tomcat"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("Wrapper容器")
r2=s2.getRootTopic()
r2.setTitle("Wrapper容器")


content={

'对应的是Servlet':[],
'Servlet工作机制':[
    'Request→StandardEngineValve→',
    'StandardHostValve→StandardContextValve→StandardWrapperValve→',
    '实例化(会耗时)并初始化Servlet对象→',
    '由过滤器链执行过滤操作→',
    '调用该Servlet对象的service方法→Response',

],
'Servlet对象池':[
    '栈结构，需要时就pop出一个对象，使用完就push回去'
],
'过滤器链':[
    '从Context容器中获取所有过滤器的相关信息',
    '通过URL匹配过滤器，匹配的加入到过滤器链中',
    '通过Servlet名称匹配过滤器，匹配的加入到过滤器链中'
],
'Servlet种类':[
    '普通Servlet请求则路由到普通Servlet',
    'JSP页面则路由到JspServlet',
    '静态资源则路由到DefaultServlet'
],
'Comet模式':[
    '服务器端通过长连接推数据',
    '需要NIO配合',
    {'CometProcessor接口':[
        'event方法,传参CometEvent（表示Comet相关的事件）'
    ]}
],
'https://www.jianshu.com/p/c5494b63d564':[]

}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 