import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="数据结构"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("二叉树——序列化")
r2=s2.getRootTopic()
r2.setTitle("二叉树——序列化")


content={
'按层遍历序列化':[
    'Node buildByLevleQueue(Queue<String> levelList)',
    '   if(levelList==null||levelList.size()==0){',
    '       return null;',
    '   }',
    '   Node head=generateNode(levelList.poll());',
    '   Queue<Node> ans=new LinkedList<Node>();',
    '   if(head!=null){',
    '       queue.add(head);'
    '   }',
    '   Node node=null;',
    '   while(!quque.isEmpty()){',
    '       node=quque.poll();',
    '       node.left=generateNode(levelList.poll());',
    '       node.right=generateNode(levelList.poll());',
    '       if(node.left!=null){',
    '           quque.add(node.left);',
    '       }',
    '       if(node.right!=null){',
    '           quque.add(node.right);',
    '       }',
    '   }',
    '   return head;',
    '}',
    '----------------------------------------------------',
    'Node generateNode(String val){',
    '   if(valu==null){',
    '       return null;',
    '   }',
    '   return new Node(Integer.valueOf(val))',
    '}'
]

}
#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 