import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="算法"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("异或运算")
r2=s2.getRootTopic()
r2.setTitle("异或运算")


content={

'异或运算':[
    '相同为0，不同为1',
    '记忆:无进位相加',
    '0^N===N  N^N==0',
    '满足交换率和结合率',
    {'不用额外变量交换两个数':[
        '前提：int a=甲,int b=乙',
        'a=a^b    =>a=甲^乙,b=乙',
        'b=a^b    =>a=甲^乙,b=甲^乙^乙=甲',
        'a=a^b    =>a=甲^乙^甲=乙,b=甲',
    ]},
    {'一个数组中有一种数出现了奇数次，其他数都出现了偶数次，怎么找到并打印这种数':[
        '所有数异或,得到的值为奇数次的数',
    ]},
    {'怎么把一个int类型的数,提取出最右侧的1来':[
        'int=N  N&(~N+1)',
        '       N=0...01101010000',
        '      `N=1...10010101111',
        '    `N+1=1...10010110000',
        'N&(~N+1)=0...00000010000'
    ]},
    {'一数组中有两种数出现了奇数次，其他数出现偶数次，怎么找到并打印这两种数':[
        'a!=b =>a^b!=0,一定存在某位为1',
        '1.所有数异或,得到的值为奇数次的数的异或a^b=c',
        '2.c&(`c+1)=d:查找最右侧为1的数',
        '3.遍历数组，数据&d!=0，代表其为a或者b',
        '4.如得到a,a^c=a^a^b=b,得到b,反之同理'
    ]},
    {'求一个二进制数组中1的位数':[
        '1.提取出最右侧的1来,rightOne=N&(~N+1)',
        '2.N^=rightOne,把数中最右测的1去掉',
        '3.循环1,2过程'
    ]}
],
'同或运算':[
    '相同为1，不同为0'
]

      
}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 