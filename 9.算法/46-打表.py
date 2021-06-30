import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="算法"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("打表")
r2=s2.getRootTopic()
r2.setTitle("打表")


content={
'打表法':[
    '1.问题如返回值不太多，可以用hardcode的方式列出，作为程序的一部分',
    '2.一个大问题解决时底层频繁使用规模不大的小问题的解',
    '如小问题的返回值满足条件1，可以把小问题的解列成一张表，作为程序的一部分',
    {'3.打表找规律':[
        '3.1.输入参数类型简单，并且只有一个实际参数',
        '3.2.要求的返回值类型也简单，并且只有一个',
        '3.3.用暴力方法，把输入参数对应的返回值，打印出来看看，进而优化code',
    ]}
],
'题1':[
    '给定一个正整数N,N=6X+8Y时，返回X,Y的值',
    '如N无法表示成6X+8Y，返回=1',
    {'规律':[
        '1.如果是奇数，返回-1',
        '2.如小于18，6，8时返回1;12,24,16时返回2;其余返回-1',
        '3.如大于18，(N-18)/8+3'
    ]}
],
'题2':[
    '给定一个参数N,返回是不是可以表示成若干连续正数的和',
    {'规律':[
        '1.如数<3,不能',
        '2.如数>=3,当数不为2的正数次幂时，能',
        '(num&(num-1))!=0,不是2的某次方',
    ]}
],
'题3':[
    '给定一个参数N(仓库存放N份草),一只牛，一只羊，轮流吃草',
    '牛先吃，羊后吃，每轮能吃的草量是1，4，16，64，谁先吃完谁胜',
    {'代码':[
        'String winner(int n){',
        '   if(n<5){',
        '       return (n==0||n==2)?"后手":"先手";',
        '   }',
        '   int base=1;',
        '   while(base<=n){',
        '       if(winner(n-base).equals("后手")){',
        '           return "先手";',
        '       }',
        '       if(base>n/4){',
        '           break;',
        '       }',
        '       base*=4;',
        '   }',
        '   return "后手";',
        '}'
    ]},
    {'规律':[
        '1.n对5取余，余数为0或2:"后手"',
        '2.其它:"先手"',
    ]}
],
}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 