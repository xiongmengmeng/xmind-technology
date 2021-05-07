import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="netty"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("Buffer缓冲区")
r2=s2.getRootTopic()
r2.setTitle("Buffer缓冲区")


content={
'定义':[
    '可以【读写数据】的【内存块】',
    'channel提供从文件，网络读取数据的渠道，但读取或写入的数据必须经由Buffer',
    '有8种缓冲区类型,使用最多的是ByteBuffer二进制字节缓冲区类型',
],
'Buffer类':[
    '一个抽象类,非线程安全的，内部有一个byte[]数组内存块，作为内存缓冲区',
    '4个属性:记录读写的状态和位置',
    {'属性':[
        {'capacity(容量)':[
            '写入的数据对象数量(区分于数组大小)，缓冲区创建时设置,不能改变',
        ]},
        {'position(读写位置)':[
            '位置，缓冲区中下一个要被读写的元素索引',
            '调用flip翻转方法，将缓冲区的写模式切换为读模式'
        ]},
        {'limit(读写的限制)':[
            '表示读写的最大上限'
        ]},
        {'mark（标记）':[
            '一个暂存属性，暂时保存position的值，方便后面的重复使用position值'
        ]}
    ]},
    {'方法':[
        {'allocate()':[
            '创建缓冲区:分配内存、返回了实例对象',
        ]},
        {'put()':[
            '写入到缓冲区',
        ]},
        {'flip()':[
            '翻转,将写模式变为读模式',
            'limit变为写模式的position值',
            'position重置为0',
            '清除mark标记', 
        ]},
        {'clear()/compact()':[
            '将缓冲区转换为写模式'
        ]},
        {'get()':[
            '从缓冲区读取',
        ]},               
        {'rewind()':[
            '倒带,position重置为0,mark标记被清理'
        ]},
        {'mark( )&reset( )':[
            '重复读取缓冲区'
        ]}
    ]},
],
'Buffer类的使用步骤':[
    {'1.创建一个Buffer类的实例对象---调用allocate()方法':[
        'IntBuffer intBuffer=IntBuffer.allocate(20)',
        '创建了一个Intbuffer实例对象，分配20*4字节内存空间'
    ]},
    {'2.将数据写入到缓冲区中---调用put()方法':[
        'intBuffer.put(5)'
    ]},
    {'3.将缓冲区转换为读模式---调用flip()方法':[
        'intBuffer.flip()'
    ]},
    {'4.从缓冲区中读取数据---调用get()方法':[
        'intBuffer.get()'
    ]},
    {'5.将缓冲区转换为写入模式---调用Buffer.clear()或Buffer.compact()方法':[
        'intBuffer.clear()'
    ]}
]


}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 