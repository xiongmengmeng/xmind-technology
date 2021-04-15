import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="netty"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("ByteBuf缓冲区")
r2=s2.getRootTopic()
r2.setTitle("ByteBuf缓冲区")


content={

'定义':[
    '一个字节容器，内部是一个字节数组'
],
'逻辑分类':[
    '废弃',
    '可读',
    '可写',
    '可扩容'
],
'AbstractByteBuf抽象类':[
    {'属性':[
        {'readerIndex（读指针）':[
            '指示读取的起始位置,readerIndex与writerIndex相等，则表示ByteBuf不可读了'
        ]},
        {'writerIndex（写指针）':[
            '写入的起始位置,writerIndex与capacity()容量相等，则表示ByteBuf已经不可写了'
        ]},
        'maxCapacity（最大容量'
    ]},
    {'方法':[
        {'容量系列':[
            'capacity()：表示ByteBuf的容量',
            'maxCapacity()：表示ByteBuf最大能够容纳的最大字节数'
        ]},
        {'写入系列':[
            'isWritable() ：ByteBuf是否可写,false，并不代表不能再往ByteBuf中写数据了,ByteBuf是可以扩容的',
            'writableBytes() ：取得可写入的字节',
            'writeBytes(byte[] src) ：把src字节数组中的数据全部写到ByteBuf',
            'markWriterIndex()与resetWriterIndex()：实现覆盖写'
        ]},
        {'读取系列':[
            'isReadable( ) ：ByteBuf是否可读',
            'readableBytes( ) ：ByteBuf当前可读取的字节数',
            'readBytes(byte[] dst)：读取ByteBuf中的数据,将数据从ByteBuf读取到dst字节数组中，这里dst字节数组的大小，通常等于readableBytes()',
            'markReaderIndex( )与resetReaderIndex( ) ：实现重复读'
        ]}
    ]}
],
'ByteBufe的内存回收':[
    '通过引用计数的方式管理的(对Pooled ByteBuf的支持)'
],
'ByteBufAllocato分配器':[
    {'定义':[
        '创建缓冲区和分配内存空间',
        '默认的分配器为ByteBufAllocator.DEFAULT,可以通过Java系统参数（SystemProperty）的选项io.netty.allocator.type进行配置'
    ]},
    {'两种实现':[
        'PoolByteBufAllocator:将ByteBuf实例放入池中,采用了jemalloc高效内存分配的策略',
        'UnpooledByteBufAllocator:通过Java的垃圾回收机制回收'
    ]},
    {'分配器分配ByteBuf的方法':[
        '初始容量为9，最大容量100的缓冲区:ByteBufAllocator.DEFAULT.buffer(9, 100)',
        '初始容量为256，最大容量Integer.MAX_VALUE的缓冲区:ByteBufAllocator.DEFAULT.buffer()'
    ]}
],
'缓冲区的类型':[
        '堆缓存区',
        '直接缓存区:使用堆外内存',
        '组合缓存区'
],
'ByteBuf的自动释放':[
    {'入站的ByteBuf':[
        {'TailHandler自动释放':[
            'Netty默认会在ChannelPipline通道流水线的最后添加一个TailHandler末尾处理器',
            '它实现了默认的处理方法，在这些方法中会帮助完成ByteBuf内存释放的工作'
        ]},
        {'SimpleChannelInboundHandler自动释放':[
            '继承SimpleChannelInboundHandler,它会在调用完实际的channelRead()方法后，帮忙释放ByteBuf实例'
        ]},
        {'手动释放ByteBuf':[
            '调用byteBuf.release()'
        ]}
    ]},
    {'出站的ByteBuf':[
        'HeadHandler自动释放'
    ]}
],
'ByteBuf的浅层复制':[
    'slice切片浅层复制',
    'duplicate整体浅层复制'
]

}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 