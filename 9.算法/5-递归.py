import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="算法"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("递归")
r2=s2.getRootTopic()
r2.setTitle("递归")


content={
'原理':[
    '系统栈',
    '函数及其变量做入栈,遇到函数操作再入栈,循环此过程',
    '直到可计算出函数值，出栈，将函数值赋值给下层的变量值,计算出函数值出栈，循环此过程',
    '直到栈底，最后将计算结果弹出'
],
'计算时间复杂度':[
    {'递归符合如下公式':[
        'T(N)=aT(N/b)+O(N^d),其中a,b,d为常数'
    ]},
    '1.如logb^a>d =>O(N^logb^a)',
    '2.如logb^a<d =>O(N^d)',
    '3.如logb^a==d =>O(N^d*logN)'
],
'一个数组，数左边比它小的数的总和，叫数的小和，所有数的小和累加，叫数组小和':[
    '等价于一个数右边有多少个数比它大，乘以此数',
    '1.判断L==R,true直接返回',
    '2.将[L..R]范围分成左右两半,左[L...Mid]右[Mid...R]',
    '3.左，右部分执行函数，分别求出其小和，并将数据在其数组上排序',
    '4.建一个新数组，长度为左部分+右部分，两个指针分别指向左右数组',
    '5.比较左指针与右指针大小',
    {'6.左指针<右指针':[
        '添加小和(右边数据总量(右边指针到右边数组末的数据量)*左指针指向数)',
        '同时将左指针的数据添加到新的数组，并将其指针右移'
    ]},
    {'7.左指针>=右指针':[
        '将右指针的数据添加到新的数组，并将其指针右移'
    ]},
    {'8.重复5,6,7的过程,直到指针越界':[
        '如左指针越界，将右指针后续数据添加到数组',
        '如右指针越界，将左指针后续数据添加到数组'
    ]},
    '9.将左右函数返回结果与3-8过程计算的小和数相加,得到数组小和',
    {'本质':[
        '在归并排序过程加了求小和的操作'
    ]},
    {'时间复杂度':[
        'T(N)=2T(N/2)+O(N^1) => O(N^1*logN)=O(N*logN)',
    ]},
    {'理解':[
        '前面的比较行为，可为后面的比较行为做基础，缩小后面行为的比较范围'
    ]}
],
'一个数组，数左边比它右边的数大，称作降序对，求有多少个降序对':[
    '原理同上',
    '在归并排序过程加了计算降序对的操作'
],



}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 