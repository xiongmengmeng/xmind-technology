import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="数据结构"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("图的遍历")
r2=s2.getRootTopic()
r2.setTitle("图的遍历")


content={
'宽度优先遍历':[
    '1.利用队列实现',
    '2.从源节点开始依次按照宽度进队列，然后弹出',
    '3.每弹出一个点，把该节点所有没有进过队列的邻接点放入队列',
    '4.直到队列变空',
    {'代码':[
        'void bfs(Node node){',
        '   if(node==null){',
        '       return;',
        '   }',
        '   Queue<Node> queue=new LinkedList<>();',
        '   HashSet<Node> set=new HashSet<>();',
        '   queue.add(node);',
        '   set.add(node);',
        '   while(!queue.isEmpty()){',
        '       Node cur=queue.poll();',
        '       System.out.println(cur.value);',
        '       for(Node next:cur.nexts){',
        '           if(!set.contains(next)){',
        '               set.add(next);',
        '               queue.add(next);',
        '           }',
        '       }',
        '   }',
        '}'
    ]}
],
'尝试优先遍历':[
    '1.利用栈实现',
    '2.从源节点开始把节点按照深度放入栈，然后弹出',
    '3.每弹出一个点，把该节点下一个没有进过栈的邻接点放入栈',
    '4.直接栈变空',
    {'代码':[
        'void dfs(Node node){',
        '   if(node==null){',
        '       return;',
        '   }',
        '   Stack<Node> stack=new Stack<>();',
        '   HashSet<Node> set=new HashSet<>();',
        '   stack.add(node);',
        '   set.add(node);',
        '   while(!stack.isEmpty()){',
        '       Node cur=stack.poll();',
        '       for(Node next:cur.nexts){',
        '           if(!set.contains(next)){',
        '               stack.push(cur);',
        '               stack.push(next);',
        '               set.add(next);',
        '               System.out.println(next.value);',
        '               break;',
        '           }',
        '       }',
        '   }',
        '}'
    ]}
]

}
#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 