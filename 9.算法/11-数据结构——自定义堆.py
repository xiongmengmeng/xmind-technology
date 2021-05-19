import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="数据结构"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("自定义堆")
r2=s2.getRootTopic()
r2.setTitle("自定义堆")


content={
'属性':[
    {'List<T> heap':[
        '存入堆数据'
    ]},
    {'Map<T,Integer> indexMap':[
        '记录节点位置'
    ]},
    {'int heapSize':[
        '堆大小'
    ]},
    {'Comparator<? super T> comparator':[
        '两个节点如何比大小'
    ]},
],
'push(T value)':[
    'heap.add(value);',
    'indexMap.put(value,heapSize);',
    'heapInsert(heapSize++);'
],
'heapInsert(int index)':[
    'while(comparator.compare(heap.get(index),heap.get((index-1)/2))<0){',
    '   swap(index,(index-1)/2);',
    '   index=(index-1)/2;',
    '}'
],
'swap(int i,int j)':[
    'T o1=heap.get(i);      T o2=heap.get(j);',
    'heap.set(i,o2);        heap.set(j,o1);',
    'indexMap.put(o1,j);    indexMap.put(o2,i);'
],
'pop()':[
    'T ans=heap.get(0);',
    'int end=heapSize-1',
    'swap(0,end)',
    'heap.remove(end)',
    'indexMap.remove(ans)',
    'heapify(0,--heapSize)',
    'return ans'
],
'pop()':[
    'T ans=heap.get(0);',
    'int end=heapSize-1',
    'swap(0,end)',
    'heap.remove(end)',
    'indexMap.remove(ans)',
    'heapify(0,--heapSize)',
    'return ans'
],
'heapify(int index,int heapSize)':[
    'int left=index*2+1;',
    'while(left<heapSize){',
    '   int largest=left+1<heapSize&&(comparator.compare(heap.get(left+1),heap.get(left))<0)',
    '       ? left+1: left;',
    '   largest=comparator.compare(heap.get(largest),heap.get(index))<0',
    '      ? largest: index;',
    '   if(largest==index){break;}',
    '   swap(largest,index);',
    '   index=largest;',
    '   left=index*2+1;',
    '}'
],
'resign(T value)':[
    'int valueIndex=indexMap.get(value);',
    'heapInsert(valueIndex);//heapInsert与heapify只会执行一个',
    'heapify(valueIndex,heapSize);'
],
'注':[
    '更新对象的属性值，如属性什是比较器的内容，更改后调用下resign()方法',
    '如加入地址相同的样本，一些方法要修改'
]


}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 