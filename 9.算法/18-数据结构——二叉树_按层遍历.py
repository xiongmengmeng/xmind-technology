import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="数据结构"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("二叉树——按层遍历")
r2=s2.getRootTopic()
r2.setTitle("二叉树——按层遍历")


content={
'无map的方式':[
    'if(head==null){',
    '   return 0;',
    '}',
    'Queue<Node> queue=new LinkedList<>();',
    'queue.add(head);',
    'Node curEnd=head;//当前层，最右节点',
    'Node nextEnd=null;//下一层，最右节点',
    'int max=0;',
    'int curLevelNodes=0//当前层节点数',
    'while(!queue.isEmpty()){',
    '   Node cur=queue.poll();',
    '   if(cur.left!=null){',
    '       queue.add(cur.left);',
    '       nextEnd=cur.left;',
    '   }',
    '   if(cur.right!=null){',
    '       queue.add(cur.right);',
    '       nextEnd=cur.right;',
    '   }',
    '   curNodeLevel++',
    '   if(cur==curEnd){',
    '       max=Math.max(max,curNodeLevel);',
    '       curLevelNodes=0;',
    '       curEnd=nextEnd;',
    '   }',
    '}',
    'return max',
]

}
#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 