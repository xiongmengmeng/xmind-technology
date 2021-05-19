import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="算法"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("数组的查找")
r2=s2.getRootTopic()
r2.setTitle("数组的查找")


content={
'线性查找':[],
'二分查找':[
    {'在一个有序数组中,找某个数是否存在':[
        'O(logN):N=2^x,求x'
    ]},
    {'在一个有序数组中,找>=某个数最左侧的位置':[
    ]},
    {'在一个有序数组中,找>=某个数最右侧的位置':[
    ]},
    {'局部最小(三种情况)':[
        '1.比较0位与1位的数，0位的数<1位的数，返回0位的数',
        '2.比较N位与N-1位的数，N位的数<N-1位的数，返回N位的数',
        '3.二分查找M位的数',
        {'4.比较M-1,M+1,如M<M-1并且M<M+1':[
            {'满足':[
                '返回M位的数'
            ]},
            {'不满足':[
                '取不满足条件的一方，继续二分查找'
            ]}
        ]}
    ]},
    {'注意':[
        '不一定有序才能二分',
        '只要有一种标准可以排除另外一边(有一种排它性的原则出现),就可以二分'
    ]}
]


}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 