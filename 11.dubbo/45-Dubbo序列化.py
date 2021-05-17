import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
xmind_name="dubbo"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("Dubbo序列化")
r2=s2.getRootTopic()
r2.setTitle("Dubbo序列化")


content={
'PRC协议组成':[
    {'组成':[
        '序列化',
        '通讯模块',
    ]},
    'dubbo协议使用【hessian2序列化】+【Netty通讯框架】',
],
'各序列化方式特点':[
    {'hessian2':[
        '跨语言，高效'
    ]},
    {'json':[
        '阿里fastjson实现的json序列化方式'
    ]},
    {'jdk':[
        'JDK自带的java序列化实现'
    ]},
    {'kryo':[
        '高效的java序列化/反序列化库',
        '大数据领域使用较多'
    ]},
    {'avro':[
        'Hadoop子项目',
        '便捷，快速处理大量数据'
    ]},
    {'protostuff':[
        '基于谷歌Protocol Buffer的序列化库',
        '不需依赖.proto文件',
        '可直接对POJO进行序列化和反序列化'
    ]},
    {'fst':[
        'fast-serialization',
        '只支持java到java的序列化'
    ]},
],
'序列化方式的性能对比':[
    {'序列化后文件大小':[
        'protostuff<kryo<fst<hessian<json<jdk<xml'
    ]},
    {'序列化时间':[
        'thrift<avro<protostuff<thrift<json<jdk'
    ]},
]

}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 