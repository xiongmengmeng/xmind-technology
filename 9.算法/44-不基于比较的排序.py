import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="算法"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("不基于比较的排序算法")
r2=s2.getRootTopic()
r2.setTitle("不基于比较的排序算法")


content={
'不基于比较的排序':[
    '桶排序思想下的排序都是不基于比较的排序',
    '时间复杂度为O(N),额外空间负载度O(M)',
    '应用范围有限，需要样本的数据状况满足桶的划分',
],
'桶排序思想下的排序':[
    '计数排序',
    '基数排序'
],
'计数排序':[
    {'样本要求':[
        '整数,且范围比较窄'
    ]},
    {'一arr[]数组记录的是员工年龄，对其进行排序':[
        '1.建一个新数组newArr[],长度为200',
        '2.遍历arr数组,拿到数据c(在arr上索引为i),将新数组c索引上的数加1:newArr[arr[i]]++',
        '3.遍历完arr数组,开始遍历newArr数组',
        '4.当其j位置上的数为k,则将j在旧数组上重复写k次',
        '5.得到的旧数组即为排序好的数组'
    ]},
    {'额外空间负载度':[
        'O(M),根据数据状态考虑，上述例子M=200'
    ]}
],
'基数排序':[
    {'样本要求':[
        '非负,10进制的正整数'
    ]},
    '1.得到一批数据，求最大值的位数，将其余所有数据补齐位数',
    '2.建0-9十个桶，每个桶都是一个队列',
    '3.将数据按个位数，放到各个桶中',
    '4.将数据从左到右，从队列里依次拿出，覆盖原数组',
    '5.接下来，匹配值的数据进一位，将数据按十位数放到各个桶中，循环4-6的过程，直到最大位数',
    '6.最后得到的数组是排序好的',
    {'时间复杂度':[
        'O(N*log10^N)=O(N)',
        '因为有严格的限制条件,数据量不大,可忽略log10^N',
        {'注':[
            '基于比较的算法排序，时间复杂度最小还是O(N*logN)'
        ]}
        
    ]},
    {'代码实现':[
        '1.得到一批数据，求最大值的位数，将其余所有数据补齐位数',
        '2.建一个新数组count，长度为10',
        '3.遍历数组，拿到数据的个位c(在数组上索引为i),将新数组count上c索引对映的数加1:count[arr[i]]++',
        '4.遍历新数组count,将其索引及前索引上的数据值相加，作为索引上的最新数据：count[i]=sum(count[1]...count[i])',
        '5.建一个新数组help，长度与原数组一样',
        '6.从右到左遍历原数组，取数据个位数上的值h作为索引，去count中定位索引h对映的值k',
        '7.将数据放到help数组k-1索引位置上,将count上索引h对映的数据值--',
        '8.个位排序完成,将help数组数据拷贝回原数组',
        '9.清空count,help数组，重复3-8的过程，直到遍历到最大值的最高位'
    ]}
]
}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 