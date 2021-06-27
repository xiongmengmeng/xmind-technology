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
'题目4':[
    '公司人员可看作一棵多叉树，头节点是公司唯一老板',
    {'员工信息':[
        'class Employee{',
        '   int happy;//员工可以带来的快乐值',
        '   List<Employee> subordinates;//员工有哪些直接下级',
        '}'
    ]},
    {'求派对最大快乐值':[
        '1.如某员工来了，那么这个员工的所有直接下级都不能来',
        '2.派对整体快乐值是所有到场员工快乐值的累加',
        '3.目标：让派对的整体快乐值尽量大'
    ]}
],
'思路':[
    {'1.头节点来':[
        '头节点快乐值+所有子结点不来的最大快乐值',
    ]},
    {'2.与头节点不来':[
        'max(节点来的最大快乐值，节点不来的最大快乐值)',
        '汇总名下所有节点的max'
    ]}
],
'实现':[
    'class Info{',
    '   int yes;',
    '   int no;',
    '}',
    '-------------------',
    'Info process(Employee e){',
    '   if(x.nexts.isEmpty()){',
    '       return new Info(x.happy,0);',
    '   }',
    '   int yes=x.happy;',
    '   int no=0;',
    '   for(Employee next:x.nexts){',
    '       Info nextInfo=process(next);',
    '       yes+=nextInfo.no;',
    '       no+=Math.max(nextInfo.yes,nextInfo.no);',
    '   }',
    'return new Info(yes,no);'
]



}
#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 