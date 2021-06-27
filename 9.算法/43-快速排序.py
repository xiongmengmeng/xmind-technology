import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="算法"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("快速排序")
r2=s2.getRootTopic()
r2.setTitle("快速排序")


content={
# '快速排序':[
#     '在序列中随机选择一个基准值，将除基准值以外的数分为“比基准值小的数”和“比基准值大的数”',
#     '每行中每个数字都需要和基准值比较大小，每行O（n）',
#     '总的时间复杂度为O（nlogn）',
# ],
'partition过程':[
    '给定一个数组arr和一个整数num',
    '把小于等于num的数放在数组左边,大于num的数放在数组右边',
    '要求额外空间复杂度O(1),时间复杂度O(N)',
    {'算法':[
        '创建一个指针k=-1，用来分割小于等于num数与大于num数',
        {'拿着序号i遍历数组':[
            {'当数组i位置上的数<=num':[
                'k++,数组i位置上的数与指针k指向数交换',
                'i++'
            ]},
            {'当数组i位置上的数>num':[
                'i++'
            ]}
        ]},

    ]},
    {'进阶1.0':[
        '把小于num的数放在数组左边,等于num的数放在中间,大于num的数放在数组右边',
        {'算法':[
        '创建一个小于区指针k=-1，一个大于区指针h=数组长度',
            {'拿着序号i遍历数组':[
                {'当数组i位置上的数<num':[
                    'k++,数组i位置上的数与指针k指向数交换',
                    'i++'
                ]},
                {'当数组i位置上的数>num':[
                    'h--,数组i位置上的数与指针h指向数交换',
                    {'当i==h':[
                        '程序退出，数组已排好'
                    ]}
                ]},
                {'当数组i位置上的数==num':[
                    'i++'
                ]}
            ]},

        ]}
    ]},
    {'进阶2.0':[
        'arr[L...R]玩荷兰国旗总量的划分,以arr[R]做划分值',
        '<arr[R]   ==arr[R]  >arr[R]'
    ]}
],
'快排1.0':[
    '递归partition来完成排序',
    {'实现':[
        'f(int[] arr,int L,int R){',
        '   if(L>=R){return;}',
        '   int M=partition(arr,L,R);',
        '   f(arr,L,M);',
        '   f(arr,M,R);'
        '}' 
    ]},
    {'partition(arr,L,R)':[
        '按上述逻辑实现',
        '返回M为arr[R]在操作完partition后的在数组中的首个元素位置'
    ]}
],
'快排2.0':[
    '对partition(arr,L,R)升级',
    '返回int[] equalData为arr[R]在操作完partition后的在数组中的首尾元素位置',
    {'后续递归改为':[
        'f(arr,L,equalData[0]-1)',
        'f(arr,equalData[1]+1,R)'
    ]},
    {'时间复杂度':[
        '最坏情况O(N^2)',
    ]}
],
'快排3.0':[
    '随机选中一个数,与arr[R]交换',
    {'时间复杂度':[
        'T(N)=2T(N/2)+O(N^1) => O(N^1*logN)=O(N*logN)',
        '为什么不按最坏情况，因为arr[R]为最大数的概率为1/N(有随机行为，最差情况就是概率事件)',
        '期望值计算后时间复杂度为O(N*logN)',
    ]},
    {'额外空间复杂度(记录中间区间的范围)':[
        '最坏情况O(N),依旧概率等加，结果O(logN)'
    ]}
],


}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 