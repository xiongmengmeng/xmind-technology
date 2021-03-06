import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="netty"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("netty:Decoder与Encoder")
r2=s2.getRootTopic()
r2.setTitle("netty:Decoder与Encoder")


content={

'Decoder解码器':[
    {'定义':[
        '将输入类型为ByteBuf缓冲区,或Java POJO对象的数据进行解码，输出一个一个的Java POJO对象',
        'Inbound入站处理器类型'
    ]},
    {'ByteToMessageDecoder':[
        {'decode()':[
            '子类实现，将解码后得到的Object，加入到父类传递过来的List<Object>实参中',
        ]},
        {'decode方法处理完后，基类会继续后面的传递处理':[
            '将List<Object>结果传递到下一个Inbound入站处理器',
            '调用ReferenceCountUtil.release(in)方法释放ByteBuf缓冲区的内存'
        ]}
    ]},
    {'ReplayingDecoder':[
        {'作用':[
            '内部定义了一个新的二进制缓冲区类，对ByteBuf缓冲区进行了装饰，名为ReplayingDecoderBuffer',
            '读取ByteBuf缓冲区的数据前，会检查缓冲区是否有足够的字节(内部进行)',
            '若ByteBuf中有足够的字节，正常读取；反之，停止解码',
            '适用于【分包传输】的应用场景'
        ]},
        {'state属性':[
            '当前解码器在解码过程中的阶段'
        ]},
        {'字符串的分包解码':[
            {'可采用普通的Header-Content内容传输协议':[
                '1.在协议的Head部分，放置字符串的字节长度',
                '2.在协议的Content部分，放置字符串的字节数组'
            ]},
            '实际传输过程中，一个Header-Content内容包，在发送端会被编码成为一个ByteBuf内容发送包'
        ]},
        {'缺点':[
            '数据解析逻辑复杂的应用场景，性能较差'
        ]}
    ]},
    {'MessageToMessageDecoder<I>':[
        '将一种POJO对象解码成另外一种POJO对象',
        '泛型实参<I>：指定入站消息Java POJO类型'
    ]},
    {'Netty内置Decoder':[
        '固定长度数据包解码器——FixedLengthFrameDecoder',
        '行分割数据包解码器——LineBasedFrameDecoder',
        '自定义分隔符数据包解码器——DelimiterBasedFrameDecoder',
        {'自定义长度数据包解码器——LengthFieldBasedFrameDecoder':[
            '基于Header-Content协议的内容传输，尽量使用它',
            {'5个参数':[
                'maxFrameLength：发送的数据包的最大长度',
                'lengthFieldOffset：长度字段偏移量',
                'lengthFieldLength：长度字段所占的字节数',
                'lengthAdjustment：长度的矫正值',
                'initialBytesToStrip：丢弃的起始字节数'
            ]}
        ]}
    ]}
],
'Encoder编码器':[
    {'定义':[
        '一个Outbound出站处理器，负责处理“出站”数据',
        '负责将“出站”的某种Java POJO对象编码成二进制ByteBuf，或者编码成另一种Java POJO对象'
    ]},
    {'MessageToByteEncoder编码器':[
        {'encode()':[
            '由子类实现'
        ]}
    ]},
    {'MessageToMessageEncoder<I>':[
        '将一种POJO对象解码成另外一种POJO对象',
        '泛型实参<I>:指定入站消息Java POJO类型',
    ]},
],
'解码器和编码器的结合':[
    {'ByteToMessageCodec编解码器':[
        '包含ByteToMessageDecoder解码器和MessageToByteEncoder编码器这两个基类',
        '包含了编码encode和解码decode两个抽象方法'
    ]},
    {'MessageToMessageCodec（编解码器）':[
        '包含MessageToMessageEncoder编码器和MessageToMessageDecoder解码器',
        '包含了编码encode和解码decode两个抽象方法'
    ]},
    'CombinedChannelDuplexHandler组合器'
]
}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 