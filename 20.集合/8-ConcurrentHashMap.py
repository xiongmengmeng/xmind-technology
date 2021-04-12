import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="集合"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("ConcurrentHashMap方法")
r2=s2.getRootTopic()
r2.setTitle("ConcurrentHashMap方法")


content={
'initTable()':[
    '实例初始化',
    '延缓到第一次put操作进行，且初始化只会执行一次',
    '防止初始化后的首次操作就需要扩容（如putAll），从而影响效率'
],
'put()':[
    {'1.table是否为空':[
        '1.1.是：对table进行初始化',
        {'1.2.否，bucket是否为空':[
            '是，使用cas操作，将Node放入对应bucket中',
            {'否：当前map是否在扩容':[
                '是，f.hash==MOVED，则跟其他线程一起进行扩容',
                {'否':[
                    '出现hash冲突，采用synchronized关键字',
                    '若当前节点是链表的头节点，遍历链表，更新或增加节点',
                    '若当前节点是红黑树的根节点，遍历树，更新或增加节点'
                ]}
            ]}

        ]}
    ]},
    '2.链表节点超过8，链表转为红黑树:treeifyBin()',
    '3.统计节点个数，检查是否需要resize:addCount()'
],
'table扩容':[
    {'treeifyBin()':[
        {'tab的长度<MIN_TREEIFY_CAPACITY(默64)':[
            '是：将数组长度扩大到原来的两倍,触发transfer，调整节点位置',
            '否：将链表转为红黑树'
        ]}
    ]},
    {'addCount()':[
        '利用cas更新baseCount',
        'tab中的节点个数baseCount>阈值sizeCtl，会触发transfer，重新调整节点位置'
    ]},
    {'transfer()':[
        '1.构建一个nextTable，大小为table的两倍',
        '2.通过for自循环处理每个槽位中的链表元素',
        '3.如所有的节点都已完成复制，把nextTable赋值给table，清空临时对象nextTable',
        {'细节':[
            '扩容时，并发地复制与插入',
            '1.遍历整个table，当前节点为空，采用cas方式在当前位置放入fwd',
            '2.当前节点已为fwd(with hash field “MOVED”)，说明已有线程处理完，直接跳过（控制并发扩容的核心）',
            {'3.当前节点为链表或红黑树':[
                '重新计算链表节点的hash值，移动到nextTable相应位置',
                '移动完，cas在tab原位置赋fwd, 表示当前节点已完成扩容'
            ]}
        ]}
    ]}
],
'get()':[
    '不需要同步控制，较简单',
    '1.空tab，直接返回null',
    '2.计算hash值，找到相应的bucket位置，为node节点直接返回，否则返回null'
],
# '学习':[
#     'https://blog.csdn.net/programmer_at/article/details/79715177'
# ]
}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 