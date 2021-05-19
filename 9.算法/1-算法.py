import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="算法"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("算法评估")
r2=s2.getRootTopic()
r2.setTitle("算法评估")


content={

'算法优劣的指标':[
    {'时间复杂度':[
        '流程决定',
        '衡量算法流程的复杂程度的一种指标',
        '该指标只与数据量有关,与过程之外的优化无关',
        {'常见时间复杂度(由低到高)':[
            'O(1)',
            'O(logN)',
            'O(N)',
            'O(N*logN)',
            'O(N^2),O(N^3)....O(N^K)',
            'O(2^N)O(3^N)....O(K^N)',
            'O(N!)',
        ]}
    ]},
    {'额外空间复杂度':[
        '流程决定',
        '与功能无关,为了实现流程，计算过程使用的额外空间',
        '作为输入参数的空间，不算额外空间',
        '作为输出结果的空间，不算额外空间'
    ]},
    {'常数项时间':[
        '实现细节决定',
        '放弃理论分析，用实验结果来对比',
        '因为不同常数的时间操作，虽然都是固定时间，但还是有快慢之分',
        '如位运算的常数时间<算术运算的常数时间,两种运算的常数时间<数组寻址时间'
    ]}
],
'算法应用----一个问题的最优解':[
    '一个问题的算法流程，在时间复杂度的指标上，一定要尽可能的低',
    '先满足时间复杂度最低这个指标后，使用最少的空间的算法流程'
],
'算法学习的脉络':[
    '1.数组结构是算法的基础',
    '2.知道怎么算的算法',
    '3.知道怎么试的算法:递归'
],
'算法测试----对数器':[
    '1.想测试方法a',
    '2.实现复杂度不好但容易实现的方法b',
    '3.实现一个随机样本产生器',
    '4.把方法a和方法b跑相同的随机样本，看结果是否一样',
    '5.如有一个随机样本使得比对结果不一致，打印样本进行人工干预，改对方法a和方法b',
    '6.当样本数量很多时比对测试依然正确,可确定方法a已经正确'
],

}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 