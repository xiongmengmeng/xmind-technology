import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="java"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("JavaWeb")
r2=s2.getRootTopic()
r2.setTitle("JavaWeb")


content={
'Tomcat':[
],
'Servlet、JSP':[
],
'Session、Cookie':[
],
'JDBC':[
],
'Filter':[
],
'Listener':[
    
],
'AJAX、JSON':[
    
]
}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 