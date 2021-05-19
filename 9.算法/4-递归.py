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
'求数据arr[L..R]中的最大值':[
    '1.将[L..R]范围分成左右两半,左[L...Mid]右[Mid...R]',
    '2.左部分求最大值，右部分求最大值',
    '3.求[L...R]范围上的最大值：max{左部分最大值，右部分最大值}',
    '注：当范围上只有一个数，可以不用再递归',
    {'实现':[
        'f(int[] arr,int L,int R){',
        '   if(L==R){',
        '       return arr[L];',
        '   }',
        '   int mid=L+(R-L)>>1;',
        '   int leftMax=f(arr,L,mid);'
        '   int rightMax=f(arr,mid,R);',
        '   return Math.max(leftMax,rightMax);'
        '}'         
    ]},
    {'时间复杂度':[
        'T(N)=2T(N/2)+O(N^0) => O(N^log2^2)=O(N)',
    ]}
],
'让数据arr[L..R]有序':[
    '1.判断L==R,true直接返回',
    '2.将[L..R]范围分成左右两半,左[L...Mid]右[Mid...R]',
    '3.左部分让其变有序，右部分让其变有序',
    '4.建一个数组,大小为左部分+右部分，左右建两个指针,新数组再建一个指针',
    '5.比较两指针所指数据大小，小的放入新数组,新数组指针加1，指向小数据的数组指针也加1',
    '6.判断小数据的数组指针是否越界，没有越界，重复5，6的过程',
    '7.若指针越界了，将另一边的数组的剩余值依次添加到新数组',
    '8.将新数组返回',
    {'时间复杂度':[
        'T(N)=2T(N/2)+O(N^1) => O(N^1*logN)=O(N*logN)',
        '递归排序的时间复杂度O(N*logN),好于冒泡，选择，插入排序',
        '因为它们浪费了比较行为，每一行的比较行为，不能为后续行的比较行为带来方便',
        '而递归，是左边组队与右边组队的对比，内部已是有序的，后序不再进行内部排序'
    ]},
    '任何递归行为都可改成非递归行为',
    {'使用非递归方式':[
        '1.将2个数一组，变成有序',
        '2.将4个数一组，变成有序',
        '3.将K个数一组，变成有序',
        '当一组数据K大于N时，将结果输出'
    ]}
],



}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 