import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
xmind_name="dubbo"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("Thrift协议")
r2=s2.getRootTopic()
r2.setTitle("Thrift协议")


content={
'介绍':[
    'dubbo支持的Thrift协议是Thrift原生协议的扩展',
    '在【Thrift原生协议】的基础上添加一些额外的头信息',
],
'使用':[
    '1.去Thrift官网查Thrift idl工具，设置Thrift环境变量',
    '2.定义Thrift文件',
    '3.用Thrift 命令生成java接囗文件',
    '4.用java编写实现类，实现接口',
    '5.注:Thrift生成的interface是一个内部类',
    '在spring bean中定义时，使用$引用内部类，而不是.',
],
'依赖':[
    'org.apache.thrift'
],
'详细配置':[ 
    '<dubbo:protocol name="thrift" port="9090"/>',
],
'问题':[
    '不支持null值，不能在协议中传递null值'
]

}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 