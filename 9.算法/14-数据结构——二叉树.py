import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="数据结构"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("二叉树")
r2=s2.getRootTopic()
r2.setTitle("二叉树")


content={
'结构':[
    'Class Node{',
    ' V value;',
    ' Node left;',
    ' Node right;',
    '}'
],
'先序，中序，后序遍历':[
    {'先序遍历(头左右)':[
       '任何子树的处理顺序都是',
       '先头节点、再左子树、然后右子树',
    ]},
    {'中序遍历(左头右)':[
       '任何子树的处理顺序都是',
       '先左子树、再头节点、然后右子树',
    ]},
    {'后序遍历(左右头)':[
       '任何子树的处理顺序都是',
       '先左子树、再右子树、然后头节点',
    ]}, 

],
'实现(递归方式)':[
    {'1.理解递归序':[
        '在树上动态规则的基础上',
        '任一个结点可向左转一遍，收集些信息',
        '也可向右转一遍，收集些信息',
        '也能回到它，对左右两个信息做整合',
        '递归很强，可以让一个节点被来到三次'
    ]},
    '2.先序，中序，后序都可以在递归序的基础上加工出来',
    '3.第一次到达一个节点就打印是先序',
    '第二次到达一个节点即中序',
    '第三次到达一个节点即后序',
    {'代码':[
        'f(Node head){',
        '   if(head==null){',
        '       return;',
        '   }',
        '   //打印行为放在此处:先序遍历',
        '   f(head.left);',
        '   //打印行为放在此处:中序遍历',
        '   f(head.right);',
        '   //打印行为放在此处:后序遍历',
        '}',
    ]}
],
'实现(非递归方式)':[
    '1.任何递归函数都可以改成非递归',
    '2.自己设计压栈来实现', 
],



}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 