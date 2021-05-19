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

'查找数据加入过几次(search方法)':[
    '1.数据为null,直接返回',
    '2.将字符串转换为字符数组',
    '3.遍历字符数组(使用索引i)',
    '4.根据字符得到路的名称path=str[i]-"a"',
    {'5.判断这条路上是否有节点':[
        {'没有':[
            '返回0'
        ]},
        {'有':[
            '继续循环'
        ]}
    ]},
    '6.将遍历到的结点的end值返回'
],
'查询以数据做为前缀的字符串个数':[
    '1.数据为null,直接返回',
    '2.将字符串转换为字符数组',
    '3.遍历字符数组(使用索引i)',
    '4.根据字符得到路的名称path=str[i]-"a"',
    {'5.判断这条路上是否有节点':[
        {'没有':[
            '返回0'
        ]},
        {'有':[
            '继续循环'
        ]}
    ]},
    '6.将遍历到的结点的pass值返回'
],
'删除数据':[
    '1.通过search方法判断数据是否加入过，没有加入过返回0',
    '2.将字符串转换为字符数组',
    '3.将头结点的pass--',
    '4.创建一个变量path,代表结点的路',
    '5.遍历字符数组(使用索引i)',
    '6.得到路的名称path=str[i]-"a"',
    {'7.判断这条路上的子节点的pass-1后是否为0':[
        {'为0':[
            '将子节点删除,直接返回',
        ]},
        {'不为0':[
            '继续循环5-7的过程'
        ]}
    ]},
    '8.将遍历到的最后的结点的end--'
],
'新增，删除，查询的时间复杂度':[
    'O(K)----K为字符器的长度'
]


}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 