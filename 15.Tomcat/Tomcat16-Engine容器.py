import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="tomcat"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("Engine容器")
r2=s2.getRootTopic()
r2.setTitle("Engine容器")


content={

'虚拟主机——Host:Engine容器的子容器，它表示一个虚拟主机':[],
'访问日志——AccessLog:负责客户端请求访问日志的记录':[],
'管道——Pipeline:搭配阀门（Valve）才能工作':[],
'Engine集群——Cluster':[],
'Engine域——Realm':[],
'生命周期监听器——LifeCycleListener':[],
'日志——Log':[]

}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 