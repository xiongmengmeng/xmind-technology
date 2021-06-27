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
'题目3':[
    '给定一棵二叉树的头节点head,',
    '返回这棵二叉树中最大的二叉搜索子树的头节点',
    {'搜索子树':[
        '每个节点的值都不重复',
        '左节点都比父节点小',
        '右节点都比父节点大'
    ]}
],
'思路':[
    {'1.与头节点无关':[
        'max(左侧的最大二叉搜索子树，右侧的最大最大二叉搜索子树)',
    ]},
    {'2.与头节点有头':[
        '左侧的是二叉搜索子树',
        '右侧的是二叉搜索子树',
        '左侧最大<头节点',
        '右侧最小>头节点'
    ]}
],
'实现':[
    'Class Info(){',
    '  boolean isBST;',
    '  int maxSubBSTsize;',
    '  int min;',
    '  int max;',
    '}',
    'Info process(Node head){',
    '   if(head==null){',
    '       return null;',
    '   }',
    '   Info leftInfo=process(head.left);',
    '   Info rightInfo=process(head.right);',
    '   int min=head.value;',
    '   int max=head.value;',
    '   int maxSubBSTSize=0;',
    '   if(leftInfo!=null){',
    '       min=Math.min(min,leftInfo.min);',
    '       max=Math.max(max,leftInfo.max);',
    '       maxSubBSTSize=Math.max(maxSubBSTSize,leftInfo.maxSubBSTSize);',
    '   }',
    '   if(rightInfo!=null){',
    '       min=Math.min(min,rightInfo.min);',
    '       max=Math.max(max,rightInfo.max);',
    '       maxSubBSTSize=Math.max(maxSubBSTSize,rightInfo.maxSubBSTSize);',
    '   }',
    '   boolean isBST=false;',
    '   if((leftInfo==null?true:leftInfo.isALLSBT)',
    '       &&(rightInfo==null?true:rightInfo.isALLSBT)',
    '       &&(leftInfo==null?true:leftInfo.max<head.value)',
    '       &&(rightInfo==null?true:rightInfo.min>head.value)){',
    '       maxSubBSTSize=(leftInfo==null?0:leftInfo.maxSubBSTSize)+',
    '                 (rightInfo==null?0:rightInfo.maxSubBSTSize)+1;',
    '       isALLBST=true;',
    '   }',
    '   return new Info(isBST,maxSubBSTSize,min,max);'
    '}'
]




}
#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 