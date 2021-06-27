import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="数据结构"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("二叉树——递归套路")
r2=s2.getRootTopic()
r2.setTitle("二叉树——递归套路")


content={
'递归套路':[
    '可解决面试中绝大多数二叉树问题，尤其是树型dp问题',
    '本质是利用递归遍历二叉树的便利性'
],
'思路':[
    '1.假设以x节点为为头，假设可以向X左树和X右树要任何信息',
    '2.在上一步的假设下，讨论以X为头节点的树，得到答案的可能性(最重要)',
    '3.列出所有可能性后，确定到底需要向左树还是右树要什么样的信息',
    '4.把左树信息和右树信息求全集，就是任何一棵子树都需要返回的信息S',
    '5.递归函数都返回S，每一棵子树都这么要求',
    '6.写代码，在代码中考虑如何把左树信息和右树信息整合出整棵树的信息'
],
'题目1':[
    '给定一棵二叉树的头节点head,返回这颗二叉树是不是平衡二叉树',
    {'思路':[
        '1.左子树是否平衡',
        '2.右子树是否平衡',
        '3.左树与右树高在2以内',
    ]},
    {'实现':[
        'Class Info(){',
        '  boolean isBalanced;',
        '  int height;',
        '}',
        '---------------------',
        'Info process(Node head){',
        '   if(node==null){',
        '       return node;',
        '   }',
        '   Info leftInfo=process(head.left);',
        '   Info rightInfo=process(head.right);',
        '   int height=Math.max(leftInfo.height,rightInfo.height)-1;',
        '   boolean isBalanced=true;',
        '   if(leftInfo.isBalanced&&rightInfo.isBalanced&&Math.abs(leftInfo.height-rightInfo.height)<2){',
        '       isBalanced=false;',
        '   }',
        '   return new Info(isBalanced,height);',
        '}'
    ]}
],
'题目2':[
    '给定一棵二叉树的头节点head,任何两个节点之前都存在距离',
    '返回整棵二叉树的最大距离',
    {'思路':[
        {'1.与头节点无关':[
            'max(左侧的最大距离，右侧的最大距离)',
        ]},
        {'2.与头节点有头':[
            '左树高+右树高+1'
        ]}
    ]},
    {'实现':[
        'Class Info(){',
        '  int maxDistance;',
        '  int height;',
        '}',
        '---------------------',
        'Info process(Node head){',
        '   if(head==null){',
        '       return new Info(0,0);',
        '   }',
        '   Info leftInfo=process(head.left);',
        '   Info rightInfo=process(head.right);',
        '   int height=Math.max(leftInfo.height,rightInfo.height)+1;',
        '   int maxDistance=Math.max(',
        '       Math.max(leftInfo.maxDistance,rightInfo.maxDistance),',
        '       leftInfo.height+rightInfo.height+1)',
        '   return new Info(maxDistance,height);',
        '}'
    ]}
   
]

}
#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 