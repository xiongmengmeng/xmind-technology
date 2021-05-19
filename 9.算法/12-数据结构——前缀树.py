import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="数据结构"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("前缀树")
r2=s2.getRootTopic()
r2.setTitle("前缀树")


content={
'前缀树':[
    '单个字符串中，字符从前到后的加到一棵多叉树上',
    '字符放在路上',
    {'节点上有专属的数据项':[
        {'pass':[
            '加字符串的过程中，它被通过了多少次'
        ]},
        {'end':[
            '加字符串的过程中，它成了多少字符串的结尾'
        ]}
    ]},
    '所有样本都这样添加，如没有路就新建,如有路就复用',
    '沿途节点的pass值增加1,每个字符串结束时来到的节点end值增加1'
],
'结构':[
    'int pass',
    'int end',
    {'Node1[] nexts=new Node1[26]':[
        'nexts[i]==null i方向的路不存在',
        'nexts[i]!=null i方向的路存在',
        '26个字符时可使用',
        '当字符很多时，用HashMap<Integr,Node2> nexts来代替上面的数组'
    ]},
    {'初始化':[
        '创建一个头结节'
    ]}
],
'添加数据':[
    '1.数据为null,直接返回',
    '2.将字符串转换为字符数组',
    '3.将头结点的pass++',
    '4.创建一个变量path,代表结点的路',
    '5.遍历字符数组(使用索引i)',
    '6.得到路的名称path=str[i]-"a"',
    {'7.判断这条路上是否有节点':[
        {'没有':[
            '新建node.nexts[path]=new Node1()',
            '将结点的pass++'
        ]},
        {'有':[
            '将结点的pass++'
        ]}
    ]},
    '8.循环5-7的过程',
    '9.将遍历到的最后的结点end++'
]


}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 