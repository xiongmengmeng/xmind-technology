import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
xmind_name="jvm"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("jvm_bytecode")
r2=s2.getRootTopic()
r2.setTitle("字节码指令")


content={
'重要概念':[
    'JVM采用【面向操作数栈】的架构(区别面向寄存器）',
    {'指令大多':[
        '只一个操作码，指令参数放在操作数栈中'
    ]},
    {'操作码长度':[
        '一个字节（即0～255）'
    ]},
    {'指令集的操作码总数':[
        '<=256条'
    ]},
    '处理超过一个字节数据时，运行时从字节中重建出具体数据结构'
],
'字节码与数据类型':[
    {'iload指令':[
        '从局部变量表中加载int型的数据到操作数栈中',
        'fload指令加载的是float类型数据'
    ]},
    {'两条指令区别':[
        'JVM内部可能是同一段代码',
        'Class文件中它们必须拥有各自独立的操作码'
    ]},
    '大部分与数据类型相关的字节码指令，其【操作码助记符】都有【特殊字符】表明为哪种【数据类型】服务'
],
'加载和存储指令':[
    {'作用':[
        '将数据在栈帧中的【局部变量表】和【操作数栈】之间来回传输'
    ]},
    {'iload':[
        '将一个局部变量加载到操作栈'
    ]},
    {'istore':[
        '将一个数值从操作数栈存储到局部变量表'
    ]},
    {'bipush':[
        '将一个常量加载到操作数栈'
    ]},
    {'wide':[
        '扩充局部变量表的访问索引的指令'
    ]}
],
'运算指令':[
    {'作用':[
        '对两个【操作数栈】上的值进行特定运算，并把结果重存入到【操作栈顶】'
    ]},
    {'iadd':[
        '加法指令'
    ]},
    {'isub':[
        '减法指令'
    ]},
    {'imul':[
        '乘法指令'
    ]},
    {'idiv':[
        '除法指令'
    ]},
    {'irem':[
        '求余指令'
    ]},
    {'ineg':[
        '取反指令'
    ]},
    {'ishl':[
        '位移指令'
    ]},
    {'ior':[
        '按位或指令'
    ]},
    {'iand':[
        '按位与指令'
    ]},
    {'dcmpg':[
        '比较指令'
    ]}
],
'类型转换指令':[
    {'作用':[
        '直接支持【宽化类型转换】,【窄化类型转换】须【显式】地使用转换指令'
    ]},
    'int类型到long、float或者double类型',
    'long类型到float、double类型',
    'float类型到double类型'
],
'对象创建与访问指令':[
    {'new':[
        '创建类实例指令'
    ]},
    {'newarray、anewarray、multianewarray':[
        '创建数组指令'
    ]},
    {'getfield、putfield、getstatic、putstatic':[
        '访问类字段（static字段）和实例字段指令'
    ]},
    {'baload、caload、saload、iaload、laload、faload、daload、aaload':[
        '把数组元素加载到操作数栈的指令'
    ]}
    {'bastore、castore、sastore、iastore、fastore、dastore、aastore':[
        '将操作数栈的值储存到数组元素中的指令'
    ]},
    {'arraylength':[
        '取数组长度指令'
    ]},
    {'instanceof、checkcast':[
        '检查类实例类型指令'
    ]}
],
'操作数栈管理指令':[
    {'pop、pop2':[
        '将操作数栈的栈顶一个或两个元素出栈'
    ]},
    {'dup、dup2、dup_x1、dup2_x1、dup_x2、dup2_x2':[
        '复制栈顶一或两个数值并将复制值或双份的复制值重新压入栈顶'
    ]},
    {'swap':[
        '将栈最顶端的两个数值互换'
    ]},
],
'控制转移指令':[
    {'ifeq、iflt、ifle、ifne':[
        '条件分支'
    ]},
    {'tableswitch、lookupswitch':[
        '复合条件分支'
    ]},
    {'goto、goto_w、jsr、jsr_w、ret':[
        '无条件分支'
    ]},
],
'方法调用和返回指令':[
    {'invokevirtual':[
        '调用对象的实例方法，根据对象的实际类型进行分派（虚方法分派）'
    ]},
    {'invokeinterface':[
        '调用接口方法，会在运行时搜索一个实现了接口方法的对象，找出适合的方法进行调用'
    ]},
    {'invokespecial':[
        '调用需要特殊处理的实例方法，包括实例初始化方法、私有方法和父类方法'
    ]},
    {'invokestatic':[
        '调用类静态方法（static方法）'
    ]},
    {'invokedynamic指令':[
        '在运行时动态解析出调用点限定符所引用的方法'
    ]}
],
'异常处理指令':[
    'athrow'
],
'同步指令':[
    'monitorenter+monitorexit'
]
}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 