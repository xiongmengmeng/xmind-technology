import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
xmind_name="jvm"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("jvm_.class")
r2=s2.getRootTopic()
r2.setTitle("jvm_类文件")


content={
'.java->.class(字节码)->虚拟机':[],
'class文件':[
    'Source: 源码',
    'Class: 字节码,字节码形态经由Classloader加载变成运行时形态（内存中）',
    'Runtime: 运行时'
],
'特点':[
    '一组以8个字节为基础单位的二进制流',
    '无分隔符，数据项在顺序和数量上严格限定，每个字节的含义，长度，先后顺序，均不允许改变',
    '两种数据类型:"无符号数"和"表"',
    {'无符号数':[
        '基本的数据类型，以u1、u2、u4、u8来分别代表1个字节、2个字节。。。',
        '可用来描述数字、索引引用、数量值或者按照UTF-8编码构成字符串值'
    ]},
    {'表':[
        '多个无符号数或者其他表作为数据项构成的复合数据类型,命名习惯以"_info"结尾',
        '描述有层次关系的复合结构数据，Class文件本质上也是一张表'
    ]},
    {'集合':[
        '当需描述同一类型但数量不定的多个数据时，形式：一个前置的容量计数器+若干连续的数据项'
    ]}
],
'结构(上)':[
    {'魔数与Class文件版本':[
        '每个Class文件头4个字节称为魔数，作用是确定这个文件是否为一个能被虚拟机接受的Class文件',
        '魔数内容：0xCAFEBABE（咖啡宝贝？）',
        '第5，6字节是次版本号（MinorVersion），第7，8字节是主版本号（Major Version）'
    ]},
    {'常量池':[
        '紧接主、次版本号',
        'Class文件里的资源库，是Class文件结构中与其他项目关联最多的数据',
        {'分类':[
            {'字面量':[
                '近Java常量概念，如文本字符串、final型常量值等',
                '常量池中每一项常量都是一个表',
                '常量表中有17种不同类型的常量'
            ]},
            {'符号引用,包含三类常量':[
                '类和接口的全限定名 org.springframework.....Bean',
                '字段的名称和描述符 private/public/protected',
                '方法的名称和描述符 private/public/protected'
            ]}
        ]},
    ]}
],
'结构（下）':[

    {'访问标志':[
        '常量池后，紧接着的2个字节',
        '用于识别类或者接口层次的访问信息',
        {'包括':[
            '这个Class是类还是接口',
            '是否定义为public类型',
            '是否定义为abstract类型',
            '如果是类的话，是否被声明为final'
        ]}
    ]},
    {'类索引、父类索引与接口索引集合':[
        '按顺序排列在访问标志后',
        '类索引和父类索引:用两个u2类型的索引值表示',
        '指向一个类型为CONSTANT_Class_info的类描述符常量',
        '常量中的索引值可以找到定义在CONSTANT_Utf8_info类型常量中的全限定名字符串'
    ]},
    {'字段表集合':[
        {'字段表（field_info）':[
            '描述接口或者类中声明的变量',
            '包括类级变量以及实例级变量',
            '不包括方法内部声明的局部变量'
        ]},
        '字段修饰符(access_flags):一个u2的数据类型',
        '字段的简单名称(name_index)和方法的描述符(descriptor_index):两项索引值,是对常量池项的引用',
        {'方法和字段的描述符':[
            '描述字段数据类型、方法参数列表（包括数量、类型以及顺序）和返回值',
            '描述方法时，按照先参数列表、后返回值的顺序描述，参数列表按照顺序放在小括号“()”内',
            '基本数据类型（byte,char,double,float,int,long,short,boolean）及void类型用一个大写字符表示',
            '对象类型用字符L加对象的全限定名来表示'
        ]}
    ]},
    {'方法表集合':[
        '标志（access_flags）',
        '名称索引（name_index）',
        '描述符索引（descriptor_index）',
        '属性表集合（attributes）'
    ]},
    {'属性表集合':[
        '属性表（attribute_info）:Class文件、字段表、方法表都可携带自己的属性表集合',
        {'Code属性':[
            {'attribute_name_index':[
                '一项指向CONSTANT_Utf8_info型常量的索引',
                '此常量值固定为“Code”，代表该属性的属性名称'
            ]},
            'attribute_length:属性值长度，属性名称索+属性长度共6字节，属性值长度=整个属性表长度-6个字节',
            'max_stack:操作数栈最大深度,在方法执行的任意时刻，操作数栈都不会超过这个深度',
            {'max_locals':[
                '局部变量表所需的存储空间,单位变量槽（Slot）',
                '变量槽:虚拟机为局部变量分配内存所使用的最小单位'
            ]},
            'code_length和code：存储Java源程序编译后生成的字节码指令',
            'code_length：字节码长度',
            'code：存储字节码指令的一系列字节流'
        ]},
        {'Exceptions属性':[
            '列举出方法中可能抛出的受查异常，即方法描述时在throws关键字后面列举的异常'
        ]}
    ]}
]

}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 