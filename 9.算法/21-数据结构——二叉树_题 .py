import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="数据结构"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("二叉树——题")
r2=s2.getRootTopic()
r2.setTitle("二叉树——题")


content={
'二叉树结构':[
    'Class Node{',
    '   V value;',
    '   Node left;',
    '   Node right;',
    '   Node parent;',
    '}',
    '给一个二叉树的节点，返回该节点的后续节点'
],
'思路':[
    '1.找到头节点，开始中序遍历，然后找到x的下一个结点(暴力解),递归序，O(N)',
    {'2.找规律':[
        '如节点X有右子树，后续节点Y：右子树左边界最底层的节点',
        '如节点X无右子树，后续节点Y：X节点的父节点，若X为父节的左子树节点，父节点为后续节点，不然一直向上找'
    ]}
],
'实现':[
    'Node getSuccessorNode(Node node){',
    '   if(node==null){',
    '       return node;',
    '   }',
    '   if(node.right!=null){',
    '       return getLeftMost(node.right);',
    '   }else{',
    '       Node parent=node.parent;',
    '       while(parent!=null&&parent.left!=node){',
    '           node=parent;',
    '           parent=node.parent;',
    '   }',
    '   return parent;'
    '}',
    '-------------------------------------',
    'Node getLeftMost(Node node)',
    '   if(node==null){',
    '       return node;',
    '   }',
    '   while(node.left!=null){',
    '       node=node.left;',
    '   }',
    '   return node;',
    '}',
],
'拆纸':[
    '给定一个输入参数N，代表纸条都从下边向上方累坏对折N次，'
    '请从上到下打印有折痕的方向',
    '如：N=1，打印down,N=2,打印 down down up',
    {'实现':[
        'void printProcess(int i,int N,boolean down){',
        '   if(i>N){',
        '       return;',
        '   }',
        '   printProcess(i+1,N,true);',
        '   System.out.print(down?"凹":"凸");',
        '   printProcess(i+1,N,false);',
        '}',
        '------------------------------------------',
        '调用：printProcess(1,N,true);',
        {'注':[
            'i:节点的层数',
            'N:总层数',
            'down==true 凹，down==false 凸'
        ]}

    ]},
    {'总结与对比':[
        '递归(中序)模拟了脑海中的树，但树是不存在的',
        {'树是有明确规则的':[
            '左：凹',
            '右：凸',
            '头：凹'
        ]},
        '树高N,递归栈，最多压N层，O(N)',
        {'如果是创建数组来存数据':[
            '2^0+2^1+2^2+....=2^N-1',
            'O(2^n-1)=O(2^n)'
        ]}
    ]}
   
]

}
#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 