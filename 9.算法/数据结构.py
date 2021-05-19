import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="算法"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("数据结构")
r2=s2.getRootTopic()
r2.setTitle("数据结构")


content={
'二叉查找树':[
    '结点值>其左子树上任意一个结点的值',
    '结点值<其右子树上任意一个结点的值',
    '最小结点:从顶端开始，往其左下的末端寻找',
    '最大结点:从顶端开始，往其右下的末端寻找',
    '二分查找算法思想的树形结构',
    '比较大小和移动的次数最多log2n->时间复杂度为O（logn）',
    '如树的形状朝单侧纵向延伸，时间复杂度为O（n）',
    '平衡二叉查找树:数据结构可以修正形状不均衡的树，让其始终保持均衡形态，以提高查找效率',
    'B树:子结点数扩展为m,形状均衡的树'
],

}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 