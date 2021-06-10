import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
xmind_name="jvm"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("前端编译")
r2=s2.getRootTopic()
r2.setTitle("前端编译")


content={
'注解处理器':[
    '类似插件，可CRUD抽象语法树中的任意元素',
    '解析与填充符号表->注解处理器,是一个循环过程，直到注解处理器不再对语法树进行修改',
    {'应用':[
        'Lombok:通过注解来实现自动产生getter/setter/equals()/hashCode()方法等'
    ]},
    'com.sun.tools.javac.processing.JavacProcessingEnvironment类的doProcessing()方法',
    '生成一个新的JavaCompiler对象，对编译的后续步骤进行处理'
],
'语义分析与字节码生成':[
    {'作用':[
        '对结构上正确的源程序进行上下文相关检查'
    ]},
    {'标注检查':[
        '变量使用前是否已被声明',
        '变量与赋值之间的数据类型是否能够匹配',
        '实现类com.sun.tools.javac.comp.Attr',
        '实现类com.sun.tools.javac.comp.Check'
    ]},
    {'数据及控制流分析':[
        '程序局部变量在使用前是否有赋值',
        '方法的每条路径是否都有返回值',
        '是否所有的受查异常都被正确处理',
        '实现类com.sun.tools.javac.comp.Flow'
    ]},
    {'解语法糖':[
        {'语法糖定义':[
            '某种语法，对语言的编译结果和功能并没有实际影响，但可以方便程序员使用'
        ]},
        {'应用':[
            {'泛型':[
                '本质：参数化类型（Parameterized Type）',
                '能够用在类、接口和方法的创建中，分别构成泛型类、泛型接口和泛型方法',
                {'擦除法实现':[
                    '对方法的Code属性中的字节码进行擦除',
                    '元数据中会保留泛型信息，反射手段可以取得参数化类型',
                    '缺点是比较慢，会频繁构造包装类和装箱、拆箱'
                ]}
            ]},
            {'自动装箱、拆箱与遍历循环':[
                '包装类的“==”运算遇到算术运算自动拆箱',
                '包装类的equals()方法不处理数据转型'
            ]},
            '条件编译'
        ]},
        {'解语法糖定义':[
            '编译阶段被还原回原始的基础语法结构'
        ]},
        '实现类com.sun.tools.javac.comp.TransTypes',
        '实现类com.sun.tools.javac.comp.Lower'
    ]},
    {'字节码生成':[
        'com.sun.tools.javac.jvm.Gen类完成',
        '把前面各步骤所生成的信息（语法树、符号表）转化成字节码指令写到磁盘',
        {'进行了少量代码添加和转换':[
            '将实例构造器<init>()和类构造器<clinit>()方法添加到语法树中',
            '如把字符串的加操作替换为StringBuffer或StringBuilder'
        ]}
    ]} 
]
}

#构建xmind
xmind.build(content,r2)

#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 