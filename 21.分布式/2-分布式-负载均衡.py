import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="分布式"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("分布式——负载均衡")
r2=s2.getRootTopic()
r2.setTitle("分布式——负载均衡")


content={
'升级版轮询，随机算法':[
    ''
],
'优秀的平滑加权轮询算法':[
    ''
],
'基于哈希环的一致性哈希算法':[
    ''
],
'最小活跃数算法':[
    ''
],
}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 