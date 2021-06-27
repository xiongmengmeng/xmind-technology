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
'实现':[
    '1.宽度优先遍历，用队列',
    '2.通过设置flag变量的方式，来发现某一层的结束',
],
'使用map的方式':[
    'if(head==null){',
    '   return 0;',
    '}',
    'Queue<Node> queue=new LinkedList<>();',
    'queue.add(head);',
    'HashMap<Node,Integer> levelMap=new HashMap<>();',
    'levelMap.put(head,1);',
    'int curLevel=1;',
    'int curLevelNodes=0;',
    'int max=0;',
    'while(!queue.isEmpty()){',
    '   Node cur=queue.poll();',
    '   int curNodeLevel=levelMap.get(cur);',
    '   if(cur.left!=null){',
    '       levelMap.put(cur.left,curNodeLevel+1);',
    '       queue.add(cur.left);',
    '   }',
    '   if(cur.right!=null){',
    '       levelMap.put(cur.right,curNodeLevel+1);',
    '       queue.add(cur.right);',
    '   }',
    '   if(curNodeLevel==curLevel){',
    '       curNodeLevel++',
    '   }else{',
    '       max=Math.max(max,curNodeLevel);',
    '       curLevel++;',
    '       curNodeLevel=1;',
    '   }',
    '}',
    'max=Math.max(max,curLevelNodes_;',
    'return max',
    {'思路':[
        {'HashMap<Node,Integer> levelMap':[
            'value为节点所在层数'
        ]},
        {'int curLevel':[
            '当前节点所在层数'
        ]},
        {'int curLevelNodes':[
            '当前curLevel层的宽度'
        ]},
        '节点进入队列后，也会进入map',
        '弹出节点时，会拿到节点所在层数',
        '如跟当前统计层==当前节点所在层：统计值++',
        '如跟当前统计层!=当前节点所在层：更新max,重置当前统计层(+1)，统计值(=1)'
    ]}
],

}
#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 