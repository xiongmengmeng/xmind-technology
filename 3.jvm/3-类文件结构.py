import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
xmind_name="jvm"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("类文件结构(上)")
r2=s2.getRootTopic()
r2.setTitle("类文件结构(上)")


content={
'.java->.class(字节码)->虚拟机':[],
'class文件':[
    {'Source':[
        '源码'
    ]},
    {'Class':[
        '字节码,字节码形态经由Classloader加载变成运行时形态（内存中）'
    ]},
    {'Runtime':[
        '运行时'
    ]}
],
'特点':[
    '一组以8个字节为基础单位的二进制流',
    {'无分隔符':[
        '数据项在顺序和数量上严格限定，每个字节的含义，长度，先后顺序，均不允许改变'
    ]}
],
'两种数据类型':[
    {'无符号数':[
        '基本的数据类型，以u1、u2、u4、u8来分别代表1个字节、2个字节。。。',
        '用来描述数字、索引引用、数量值或者按照UTF-8编码构成字符串值'
    ]},
    {'表':[
        '多个无符号数或者其他表作为数据项构成的复合数据类型,命名习惯以"_info"结尾',
        '描述有层次关系的复合结构数据，Class文件本质上也是一张表',
        {'集合':[
            '当需描述同一类型但数量不定的多个数据时，形式：一个前置的容量计数器+若干连续的数据项'
        ]}
    ]},
],
'魔数与Class文件版本':[
    {'Class文件头4个字节称为魔数':[
        '0xCAFEBABE（咖啡宝贝？）',
    ]},
    {'作用':[
        '确定这个文件是否为一个能被虚拟机接受的Class文件'
    ]},
    '第5，6字节是次版本号（MinorVersion），第7，8字节是主版本号（Major Version）'
],
'常量池cp_info':[
    'Class文件里的资源库，是Class文件结构中与其他项目关联最多的数据',
    {'分类':[
        {'字面量':[
            '近Java常量概念，如文本字符串、final型常量值等',
            '常量池中每一项常量都是一个表(常量表中有17种不同类型的常量)',
        ]},
        {'符号引用(包含三类常量)':[
            {'类和接口的全限定名':[
                'CONSTANT_Class_info',
                'org.springframework.....Bean'
            ]},
            {'字段的名称和描述符':[
                'CONSTANT_Fieldref_info',
                'private/public/protected'
            ]},
            {'方法的名称和描述符':[
                'CONSTANT_Methodref_info',
                'private/public/protected'
            ]},
        ]}
    ]},
],



}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 