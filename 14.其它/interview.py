import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="interview"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("interview")
r2=s2.getRootTopic()
r2.setTitle("interview")


content={
'离职的原因':[
    '',
    ''
],
'投入最多的项目':[
    '',
    ''
],
'当前在面试其他公司的情况':[
    '',
    ''
],
'学习习惯，怎么学习，现在在学习什么':[
    '',
    ''
],
'未来的规则':[
    '',
    ''
],
'':[
    '',
    ''
],
}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 