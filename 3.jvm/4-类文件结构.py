import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
xmind_name="jvm"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("类文件结构(下)")
r2=s2.getRootTopic()
r2.setTitle("类文件结构(下)")


content={
'访问标志':[
    {'作用':[
        '识别类或者接口层次的访问信息'
    ]},
    {'内容':[
        '这个Class是类还是接口',
        '是否定义为public类型',
        '是否定义为abstract类型',
        '如果是类的话，是否被声明为final'
    ]}
],
'类索引、父类索引与接口索引集合':[
    {'类索引和父类索引':[
        '两个u2类型的索引值表示',
        '指向一个类型为CONSTANT_Class_info的类描述符常量',
        '常量中的索引值可以找到定义在CONSTANT_Utf8_info类型常量中的全限定名字符串'
    ]}
],

'字段表集合':[
    {'字段表(field_info)':[
        '描述接口或者类中声明的变量',
        {'包括':[
            '类级变量',
            '实例级变量'
        ]},
        {'不包括':[
            '方法内部声明的局部变量'
        ]}
    ]},
    {'字段修饰符(access_flags)':[
        '一个u2的数据类型'
    ]},
    '字段(name_index)索引',
    {'字段(name_index)描述符':[
        '一项索引值,是对常量池项的引用',
        {'描述字段':[
            '数据类型、方法参数列表（包括数量、类型以及顺序）和返回值'
        ]},
        '基本数据类型（byte,char,double,float,int,long,short,boolean）及void类型用一个大写字符表示',
        '对象类型用字符L加对象的全限定名来表示'
    ]}
],
'方法表集合':[
    '标志（access_flags）',
    '名称索引（name_index）',
    {'描述符索引（descriptor_index）':[
        '按照先参数列表、后返回值的顺序描述，参数列表按照顺序放在小括号“()”内'
    ]},
    '属性表集合（attributes）'
],
'属性表集合':[
    {'属性表（attribute_info）':[
        'Class文件、字段表、方法表都可携带自己的属性表集合'
    ]},
    {'Code属性':[
        {'attribute_name_index':[
            '一项指向CONSTANT_Utf8_info型常量的索引',
            '此常量值固定为“Code”，代表该属性的属性名称'
        ]},
        {'attribute_length':[
            '属性值长度，属性名称索+属性长度共6字节，属性值长度=整个属性表长度-6个字节'
        ]},
        {'max_stack':[
            '操作数栈最大深度',
            '在方法执行的任意时刻，操作数栈都不会超过这个深度'
        ]},
        {'max_locals':[
            '局部变量表所需的存储空间,单位变量槽（Slot）',
            {'变量槽':[
                '虚拟机为局部变量分配内存所使用的最小单位'
            ]}
        ]},
        {'code_length和code':[
            '存储Java源程序编译后生成的字节码指令',
            'code_length：字节码长度',
            'code：存储字节码指令的一系列字节流'
        ]}
    ]},
    {'Exceptions属性':[
        '列举出方法中可能抛出的受查异常，即方法描述时在throws关键字后面列举的异常'
    ]}
]


}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 