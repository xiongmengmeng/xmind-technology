import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="数据结构"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("二叉树——遍历(非递归方式)")
r2=s2.getRootTopic()
r2.setTitle("二叉树——遍历(非递归方式)")


content={
'先序遍历(头左右)':[
    {'实现':[
        '1.弹出打印',
        '2.如有右，压入右',
        '3.如有左，压入左'
    ]},
    {'思想':[
        '先压右，再压左，栈是逆序'
    ]},
    {'代码':[
        'if(head!=null){',
        '   Stack<Node> stack=new Stack<Node>();',
        '   stack.add(head);',
        '   while(!stack.isEmpty()){',
        '       head=stack.pop();',
        '       Systme.out.print(head.value+"");',
        '       if(head.right!=null){',
        '           stack.push(head.right);',
        '       }',
        '       if(head.left!=null){',
        '           stack.push(head.left);',
        '       }',
        '   }',
        '}'
    ]}
],
'中序遍历(左头右)':[
    {'实现':[
        '1.把整条左边界依次入栈',
        '2.1无法继续 时，弹出打印，来到弹出节点的右子树上',
        '3.重复1,2过程',
    ]},
    {'思想':[
        '1.整棵树被左边界分解',
        '2.初始栈为：头左左左。。。(弹出顺序:左头)',
        '3.左边界到底时，弹出左节点，来到左头节点的右节点，添加其左边界，重复3'
    ]},
    {'代码':[
        'if(head!=null){',
        '   Stack<Node> stack=new Stack<Node>();',
        '   while(!stack.isEmpty()||head!=null){',
        '       if(head!=null){',
        '           stack.push(head);',
        '           head=head.left;',
        '       }else{',
        '           head=stack.pop();',
        '           Systme.out.print(head.value+"");',
        '           head=head.right;',
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