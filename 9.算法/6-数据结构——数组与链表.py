import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="数据结构"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("数组和链表")
r2=s2.getRootTopic()
r2.setTitle("数组和链表")


content={
'数组':[
    '连续空间',
    {'查找':[
        '时间复杂度O(1)'
    ]},
    {'添加或删除':[
        '时间复杂度O(N)'
    ]},
],
'链表':[
    '指针',
    '单向链表/双向链表',
    {'查找':[
        '时间复杂度O(N)'
    ]},
    {'添加或删除':[
        '时间复杂度O(1)'
    ]},
    {'单链表和双链表如何反转':[
        '1.新增两个变量pre,next,用于记录节点的前,后指针',
        '2.每轮循环,将当前节点的前后指针更新下,同时将pre,next都往后移一位,'
    ]},
    {'把给定的值删除':[
        '1.先遍历列表,找到第一个不为给定值的数,作为头部',
        '2.定义两个变量pre,cur,用于记录前节点,当前节点',
        '3.判断cur是否为给定值,如是pre.next=cur.next',
        '4.每轮循环,将pre,cur都往后移一位,循环3的过程',
    ]},
    {'在头部加节点':[
        '链表为空时,将head,tail都指向当前节点',
        {'链表不为空时':[
            '将节点的next指向head头节点',
            '将head头节点的pre,指向当前节点',
            '将当前节点更新为head头节点'
        ]}
    ]},
    {'在头部弹出节点':[
        {'链表为空':[
            '返回null'
        ]},
        {'链表只一个节点':[
            'head,tail都置为空'
        ]},
        {'链表不只一个节点':[
            '找到head头节点的下一节点head.next',
            '将下一节点更新为head头节点',
            '将当前节点的next设置为null'
            '将下一节点的pre,设置为null',
        ]},
    ]}
],


}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 