import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="数据结构"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("二叉树——后序遍历(左右头)")
r2=s2.getRootTopic()
r2.setTitle("二叉树——后序遍历(左右头)")


content={
'实现1':[
    '1.弹出打印',
    '2.如有左，压入左',
    '3.如有右，压入右',
    {'思想':[
        '返过来就是:头右左',
        '只需把先序遍历的2，3交换',
        '再把结果逆序打印出来'
    ]},
],
'实现2':[
    {'实现':[
        'if(h!=null){',
        '   Stack<Node> stack=new Stack<Node>();',
        '   stack.push(h);',
        '   Node c=null;',
        '   while(!stack.isEmpty()){',
        '       c=stack.peek();',
        '       if(c.left!=null&&h!=c.left&&h!=c.right){',
        '           stack.push(c.left);',
        '       }else if(c.right!=null&&h!=c.right){',
        '           stack.push(c.right)',
        '       }else{',
        '           Systme.out.print(stack.pop().value+"");',
        '           h=c;',
        '       }',
        '   }',
        '}',
    ]},
    {'解释':[
        {'c.left!=null&&h!=c.left&&h!=c.right':[
            'c是新到的，左右子树还未处理:先去处理左子树'
        ]},
        {'c.right!=null&&h!=c.right':[
            '右子树不为空，且还未处理：先去处理右子树'
        ]},
        {'其它':[
            '左右子树已经处理了||左右子树都为空:弹出打印',
            '用h标记处理的结点'
        ]},
        {'h,c':[
            'h:跟踪上次打印节点，标记节点是否处理完',
            '上次打印了左孩子，下次就该打印右孩子了',
            '上次打印了右孩子，下次就该打印当前节点c了'
        ]}
    ]}
]


 
}
#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 