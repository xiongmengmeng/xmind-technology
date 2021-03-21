import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="netty"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("缓冲区Buffer")
r2=s2.getRootTopic()
r2.setTitle("缓冲区Buffer")


content={

'Java NIO组件':[
    '提供了统一的API，为大家屏蔽了底层的不同操作系统的差异'
],
'三个核心组件':[
    'Channel（通道）',
    'Buffer（缓冲区）·',
    'Selector（选择器）'
],
'NIO和OIO的对比':[
    'OIO是面向流（Stream Oriented）的，NIO是面向缓冲区（Buffer Oriented）的',
    'OIO的操作是阻塞的，NIO的操作是非阻塞的',
    'OIO没有选择器（Selector）概念，而NIO有选择器的概念'
],
'缓冲区Buffer':[
    '定义：本质上是一个内存块，既可以写入数据，也可以从中读取数据',
    {'Buffer类':[
        '一个抽象类,非线程安全的，内部有一个byte[]数组内存块，作为内存缓冲区',
        {'4个重要的属性:记录读写的状态和位置':[
            {'capacity（容量）':[
                '容量是指写入的数据对象的数量，缓冲区创建时设置,不能改变'
            ]},
            {'position属性':[
                '位置，缓冲区中下一个要被读写的元素索引',
                '使用（即调用）flip翻转方法，将缓冲区的写模式切换为读模式'
            ]},
            {'limit属性':[
                '表示读写的最大上限'
            ]},
            {'mark（标记）':[
                '一个暂存属性，暂时保存position的值，方便后面的重复使用position值'
            ]}
        ]},
        {'常用方法':[
            {'allocate()':[
                '创建缓冲区:分配内存、返回了实例对象'
            ]},
            {'put()':[
                '写入到缓冲区'
            ]},
            {'flip()':[
                '翻转,将写模式变为读模式',
                'limit变为写模式的position值',
                'position重置为0',
                '清除mark标记'
            ]},
            {'clear()/compact()':[
                '将缓冲区转换为写模式'
            ]},
            {'get()':[
                '从缓冲区读取'
            ]},               
            {'rewind()':[
                '倒带,position重置为0,mark标记被清理'
            ]},
            {'mark( )&reset( )':[
                '重复读取缓冲区'
            ]}
        ]},
        {'Java NIO Buffer类的使用步骤':[
            {'1.创建一个Buffer类的实例对象':[
                '使用创建子类实例对象的allocate()方法'
            ]},
            {'2.将数据写入到缓冲区中':[
                '调用put方法'
            ]},
            {'3.将缓冲区转换为读模式':[
                '写入完成后，在开始读取数据前，调用Buffer.flip()方法'
            ]},
            {'4.从缓冲区中读取数据':[
                '调用get方法'
            ]},
            {'5.将缓冲区转换为写入模式':[
                '读取完成后，调用Buffer.clear() 或Buffer.compact()方法，将缓冲区转换为写入模式'
            ]}
        ]}
    ]}
]

}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 