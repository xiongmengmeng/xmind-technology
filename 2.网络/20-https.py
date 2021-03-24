import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="internet"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("HTTPS")
r2=s2.getRootTopic()
r2.setTitle("HTTPS")


content={
'进程的切换过程 ':[
    '切换会保存寄存器,栈等线程相关的现场',
    '需要由用户态切换到内核态,可以用vmstat命令查看线程上下文的切换状况'
]
}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 