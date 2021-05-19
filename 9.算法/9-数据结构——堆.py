import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="数据结构"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("堆")
r2=s2.getRootTopic()
r2.setTitle("堆")


content={

'完全二叉树':[
    '要么每一层都是满的，在不满的层也是从左到右依次变满的',
    '数据量n，树高log2n',
    {'i位置':[
        '左孩子的下标2*i+1',
        '右孩子的下标2*i+2',
        '父的下标(i-1)/2'
    ]},
    {'i位置(数组0位置不用,方便使用位运算)':[
        '左孩子的下标2*i=i<<1',
        '右孩子的下标2*i+1=i<<1|1',
        '父的下标i/2=i>>1'
    ]}
],
'堆结构':[
    '用数组实现的完全二叉树结构',
    '学习heapInsert(数据添加在完全二叉树的最后，需要往上移)',
    '学习heapify操作(数据添加在完全二叉树的根节点，需要往下移)',
    '优先级队列结构，就是堆结构',
    {'分类':[
        {'大根堆':[
            '任何一节点为头的堆，最大值都是头节点的值'
        ]},
        {'小根堆':[
            '任何一节点为头的堆，最小值都是头节点的值'
        ]}
    ]}
],
'对数组进行排序(使用大根堆结构)':[
    '1.先将整个数组变成大根堆结构，建堆过程',
    '2.判断数据长度是否大于1，大于1继续',
    '3.将堆的最大值arr[0],与堆末尾的值arr[heapSize]交换,heapSize--',
    '4.调整堆,将arr[0]上的值调整到正常的位置，使arr[0...heapSize]为大根堆',
    '5.循环3,4过程，直到heapSize==0',
    {'时间复杂度':[
        {'添加数据':[
            '1.从上到下的方法，时间复杂度O(N*logN)',
            '2.从下到上的方法，时间复杂度O(N)'
        ]},
        {'删除最大值,并保证剩余数据也是大根堆':[
            '每个数据都进行heapify',
            '时间复杂度O(N*logN)'
        ]},
        {'总的时间复杂度':[
            'O(N*logN)'
        ]}
    ]}
],
'系统实现的堆':[
    'PriorityQueue<Integer>:默认小根堆',
    {'改成大根堆':[
        'PriorityQueue<Integer>((o1,o2)->o2-o1)'
    ]}
],
'一个几乎有序的数组,选择一个合适的排序算法，对这个数组进行排序':[
    {'几乎有序':[
        '如把数组排好顺序，每个元素移动距离一定不超过k(k相比数组长度较小)'
    ]},
    '假设k=5,每个数排序后移动不超过5',
    '1.创建一个小数组，大小为5，将数组前5位数据存入',
    '2.将小数组调整为小根堆，弹出根元素做为数组最小的元素',
    '3.将数组后续的值加入小数组(注意防止数组越界)',
    '4.重复4,5过程，直到小数组为空',
    {'时间复杂度':[
        'O(N*logK)'
    ]}
],

}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 