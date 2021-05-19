import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="数据结构"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("栈和队列")
r2=s2.getRootTopic()
r2.setTitle("栈和队列")


content={
'栈':[
    '后进先出',
    {'入栈，出栈':[
        '时间复杂度O(1)'
    ]},
    {'实现':[
        '双向链',
        '数组:用一个index标识上方数据的位置'
    ]},
    {'实现一特殊的栈,实现返回栈中最小元素':[
        '1.建两个栈,一个普通栈,一个最小栈',
        '2.添加数据时,普通栈正常添加,最小栈,将添加的数据与栈顶数据对比,谁小加谁',
        '3.弹出数据时,普通栈、最小栈,正常弹出',
        '4.取最小值时，弹出最小栈的数据',
        '还有一种方式：添加数据时，如添加数据比栈顶数据大，不添加',
        '但弹出时要多做判断,节省空间但浪费时间'
    ]},
    {'用栈结构实现队列结构':[
        '用两个栈:push栈和pop栈来实现',
        {'添加数据时':[
            'pop栈要为空，如不空，先将pop栈中数据弹出添加到push栈，清空pop栈',
            '在push栈添加数据'
        ]},
        {'弹出数据时':[
            '先判空',
            'pop栈不空，直接从pop栈弹出数据',
            'pop栈为空，将push栈中数据弹出添加到pop栈，然后从pop栈弹出数据'
        ]}
    ]}
],
'队列':[
    '先进先出',
    {'入队，出队':[
        '时间复杂度O(1)'
    ]},
    {'实现':[
        '双向链表',
        {'数组':[
            'pollIndex=0:取用数据的指针',
            'putIndex=0:存放数据的指针',
            'size=0:有几个数',
            'limit=7:限制数组大小',
            {'添加数据':[
                '1.判断数组是否满了,满了抛异常',
                '2.size++',
                '3.arr[putIndex]=新数据',
                '4.putIndex=putIndex<limit-1?putIndex+1:0'
            ]},
            {'弹出数据':[
                '1.判断size是否为空,为空抛异常',
                '2.size--',
                '3.取数据arr[pollInsize]',
                '4.pollInsize=pollInsize<limit-1?:pollInsize+1:0',
            ]}
        ]}
    ]},
    {'用队列结构实现栈结构':[
        '用两队列来实现，复制实现',
        {'弹出数据':[
            '将一个队列数据复制到另一队列',
            '最后一个元素不复制,弹出,然后将自己清空'
        ]}
    ]}
],

}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 