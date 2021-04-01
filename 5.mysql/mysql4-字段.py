import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="mysql"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("字段")
r2=s2.getRootTopic()
r2.setTitle("字段")


content={

'varchar和char的区别':[
    {'char':[
        '定长字段',
        'char(10)的空间:无论实际存储多少内容.该字段都占用10个字符'
    ]},
    {'varchar':[
        '变长',
        '申请的只是最大长度,占用的空间为实际字符长度+1,最后一个字符存储使用的空间长度'
    ]},
    '检索效率上:char > varchar'
],
'varchar(10)和的区别':[
    {'varchar(10)':[
        '申请的空间长度,也是可以存储数据的最大长度',
        '插入需要判断，时间换空间'
    ]},
    {'int(10)':[
        '展示的长度,不足10位以0填充',
        'int(1)和int(10)所能存储的数字大小以及占用的空间都是相同的,只是在展示时按照长度展示'
    ]}
],
'float和double的区别':[
    '精度不同和数据范围不同',
    {'double':[
        '64位,在小数点后到15位'
    ]},
    {'float':[
        '32位,在小数点后到7位'
    ]}
],
}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 