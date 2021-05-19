import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="数据结构"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("大根堆")
r2=s2.getRootTopic()
r2.setTitle("大根堆")


content={

'添加数据':[
    'heapsize:表示堆大小，也表示新来的数放入的位置',
    '1.判断堆是否已满，满了报错',
    '2.堆不满，先将其放在数组的heapsize位上(假设数据所在数组索引为i),将heapSize+1',
    {'3.执行heapInsert,将数与其父类的值对比':[
        {'4.数据>父类的值(索引为(i-1)/2)':[
            '将数据与父类交换,i=(i-1)/2,i不等于0,循环3,4的过程'
        ]},
        {'5.数据<=父类的值(索引为(i-1)/2)':[
            '不做额外操作'
        ]}
    ]},
    {'时间复杂度':[
        'O(logN)',
        '添加数据到heapSize后，往上最多交换logN次(运行时间与树的高度成正比)'
    ]},
],

'取数据':[
    {'总结':[
        '将大根堆末尾的数据移到顶端，然后一边比较它与子结点数据的大小，一边往下移动'
    ]},
    '1.取出最大值int max=arr[0]',
    {'2.将最后一个位置的值放到第一个位置上':[
        'arr[0]=arr[heapSize],并将heapSize值减1'
    ]},
    '3.取arr[0](此时i=0)的子节点，对比左右节点的值(注意取值时判断下索引是否超过heapSize,防止越界)',
    '4.取左右节点中值最大的子节点与arr[i]对比',
    '5.如arr[i]<最大值的子节点,将arr[i]与其子节点交换，i=2*i+1或2*i+2继续3,4,5操作',
    '6.如arr[i]>最大值的子节点,不操作',
    {'时间复杂度':[
        'O(logN)',
        '最后一个数据放到堆首后，往下最多下沉logN级,即交换logN次(运行时间与树的高度成正比)',
        '注:取最大值的时间复杂度为O(1)'
    ]}
],
'把数组调整为大根堆':[
    '把数组想像成完全二叉树',
    '从后往前遍历数组，每个元素都进行heapify(保证它下面的堆是大根堆)',
    {'时间复杂度':[
        'O(N)',
        '假设有N个节点，最下一层约为N/2个节点，然后N/4,N/8....1',
        '最下层只是判断了一下，做了N/2*1个操作',
        '往上一层做了次判断+可能做了一次交换，做了N/4*2个操作',
        '往上一层做了次判断+可能做了两次交接，做了N/8*3个操作',
        '....',
        'T(N)=N/2*1+N/4*2+N/8*3+N/16*4+....',
        '2T(N)=N/2*2+N/2*2+N/4*3+N/8*4+....',
        '2T(N)-T(N)=T(N)=N+N/2+N/4+N/8+....=O(N)'
    ]},
    {'额外空间复杂度':[
        'O(1)'
    ]}
],


}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 