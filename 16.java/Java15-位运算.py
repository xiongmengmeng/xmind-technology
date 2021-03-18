import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="java"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("位运算")
r2=s2.getRootTopic()
r2.setTitle("位运算")


content={
'&--且':[
    '6&3=110&11=010=2',
],
'|--或':[
    '6|3=110&11=111=7',
],
'^--异或':[
    '6^3=110&11=101=5',
],
'>>--向右移动两位':[
    '6>>2=1',
],
'<<--向左移动三位':[
    '6<<3=110000=48',
],
'>>>--右移位运算符':[
    '6>>>2=1',
    '无论正负，都在高位插入0'
]

}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 