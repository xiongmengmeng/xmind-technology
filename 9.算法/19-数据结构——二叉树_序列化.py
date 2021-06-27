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
'实现':[
    '1.用先序或中序或后序或按层遍历，来实现二叉树的序列化',
    '2.用什么方式序列化，就用什么样的方式反序列化',
],
'先序遍历序列化':[
    'Queue<String> preSerial(Node node){',
    '   Queue<String> ans=new LinkedList<>();',
    '   pres(head,ans);',
    'return ans;',
    '-----------------------------------------',
    'void pres(Node node,Queue<String> ans)',
    '   if(head==null){',
    '       ans.add(null);',
    '   }else{',
    '       ans.add(String.valueOf(head.value));',
    '       pres(head.left,ans);',
    '       pres(head.right,ans);',
    '   }',
    '}',
    {'反序列化':[
        'Node buildByPreQueue(Queue<String> prelist)'
        '   if(prelist==null||prelist.size()==0){',
        '       return null;',
        '   }',
        '   return preb(prelist);',
        '}',
        '---------------------------------------------',
        'Node preb(Queue<String> prelist){',
        '   String value=prelist.poll();',
        '   if(value==null){',
        '       return null;',
        '   }',
        '   Node head=new Node(Integer.valueOf(value))',
        '   head.left=preb(prelist);',
        '   head.right=preb(prelist);',
        '   return head;',
        '}'
    ]}
],


}
#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 