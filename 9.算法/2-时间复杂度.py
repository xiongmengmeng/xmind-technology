import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="算法"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("时间复杂度")
r2=s2.getRootTopic()
r2.setTitle("时间复杂度")


content={
'常数时间的操作':[
    '一个操作的执行时间【不以具体样本量】为转移',
    '每次执行时间都是【固定时间】',
    '如：在数组上查询第i位的数据,不是遍历操作,是计算偏移量，然后直接取值',
    {'常见时间复杂度为O(1)的操作':[
        {'常见算术运算':[
            '+、-、*、/、&',
        ]},
        {'常见位运算':[
            '>>(带符号位右移)、>>>(不带符号位右移,补0)、<<、|、&、^',
        ]},
        {'赋值、比较、自增、自减':[
        ]},
        {'数组寻址':[
            '底层是连续区间，因此可用偏移量定位'
        ]},
    ]},
    {'总结':[
        '执行时间固定的操作都是常数时间的操作',
        '执行时间不固定的操作，都不是常数时间的操作'
    ]}
],
'确定算法流程的总操作数量与样本数量之间的表达式关系':[
   '1.想象算法流程所处理的数据状态,按最差的情况',
   '2.把整个流程彻底拆分为一个个基本动作,保证每个动作都是常数时间的操作',
   '3.如数据量为N,看看基本动作和数量N是什么关系',
    {'确定算法流程的时间复杂度':[
        '完成 表达式的建立,只把高阶项留下',
        '高阶项的系数去除,低阶项都去除',
        '记为:O(忽略掉系数的高阶项)'
    ]},
]
}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 