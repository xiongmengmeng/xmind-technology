import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="算法"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("贪心算法")
r2=s2.getRootTopic()
r2.setTitle("贪心算法")


content={
'贪心算法':[
    '1.最自然智慧的算法',
    '2.用一种局部最功利的标准，总是做出在当前看来最好的选择',
    '3.难点在于证明局部最功利的标准可以得到全局最优解',
    '4.对于贪心算法的学习主要以增加阅历和经验为主'
],
'求解的标准过程':[
    '1.分析业务',
    '2.根据业务逻辑找到不同的贪心策略',
    '3.对于能举出反例的策略直接跳过，不能举出反倒的策略要证明有效性',
],
'解题套路':[
    '1.实现一个不依靠贪心策略的解法X,可以用最暴力的尝试',
    '2.脑补出贪心策略A,贪心策略B,贪心策略C',
    '3.用解法X和对数器，用实验的方式得知哪个贪心策略正确',
    '4.不要去纠结贪心策略的证明',
    {'常用套路':[
        '排序',
        '堆结构'
    ]}
],
'题1':[
    '一些项目要用一个会议室宣讲，会议室不能同时容纳两个项目宣讲',
    '给你每一个项目开始的时间和结束的时间',
    '你来安排宣讲的日程，要求会议室进行的宣讲场次最多，返回最多的宣讲场次',
    {'思路':[
        '结束时间早的先安排'
    ]},
    {'实现':[
        'ProgramComparator implements Comparator<Program>{',
        '@Override',
        'public int compare(Program o1,Program o2){',
        '   return o1.end-o2.end;',
        '}',
        'int bestArrange(Program[] programs){',
        'int timeLine=0;',
        'int result=0;',
        'for(int i=0;i<programs.length;i++){',
        '   if(timeLine<=programs[i].start){',
        '       result++;',
        '       timeLine=programs[i].end;',
        '   }',
        '}',
        'return result;'
    ]}
]
}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 