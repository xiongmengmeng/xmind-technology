import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
xmind_name="jvm"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("静态分派")
r2=s2.getRootTopic()
r2.setTitle("静态分派")


content={
'Java具备面向对象的3个基本特征':[
    '继承',
    '封装(get/set)',
    {'多态':[
        '继承，重写（Override），向上转型（Human h=new Man()）三大必要条件',
        '方法重载:同一个方法名，参数或者类型不同。（Overload）',
        '方法重写:父类与子类有同样的方法名和参数，这叫方法覆盖。（Override）'
    ]}
],
'任务':[
    '不等同于【方法执行】，该阶段唯一任务是确定【被调用方法版本】，不涉及方法内部具体运行过程'
],
'五条字节码指令':[
    {'invokestatic':[
        '调用静态方法'
    ]},
    {'invokespecial':[
        '调用实例构造器<init>()方法、私有方法和父类中的方法'
    ]},
    {'invokevirtual':[
        '调用所有的虚方法'
    ]},
    {'invokeinterface':[
        '调用接口方法，在运行时确定一个实现该接口的对象'
    ]},
    {'invokedynamic':[
        '运行时动态解析出调用点限定符所引用的方法，然后再执行该方法'
    ]}
],
'解析':[
    {'定义':[
        '静态过程',
        '编译期间确定',
        '把【符号引用】转变为【直接引用】,确定唯一的【方法调用版本】',
        '如能被invokestatic和invokespecial指令调用的方法'
    ]},
    {'分类':[
        {'静态方法':[
            '与类型直接关联，不能通过【重写】出现别的版本，适合类加载阶段进行解析'
        ]},
        {'私有方法':[
            '外部不可被访问，不能通过【继承】出现别的版本，适合类加载阶段进行解析'
        ]},
        '实例构造器',
        '父类方法',
        {'被final修饰的方法（invokevirtual指令调用)':[
            '【无法被覆盖】，没有其他版本的可能'
        ]}
    ]},
],
'静态分派':[
    {'定义':[
        '依赖【静态类型】决定【方法执行版本】',
        '发生在【编译阶段】，不由虚拟机来执行的',
        {'典型表现':[
            '方法重载'
        ]}
    ]},
    {'重载':[
        '通过【参数的静态类型】而不是实际类型作为判定依据的',
        '静态类型是在【编译期可知】',
        '实际类型在运行期才可确认'
    ]},
    {'重载时目标方法选择(字面量没有显示的静态类型时)':[
        '1.char>int>long>float>double的顺序转型进行匹配',
        '2.一次自动装箱,封装类型java.lang.Character',
        '3.java.lang.Serializable,是java.lang.Character类实现的一个接口,自动装箱之后还是找不到装箱类，会找装箱类所实现的接口类型',
        '4.Object,如果有多个父类，那将在继承关系中从下往上开始搜索',
        '5.变长参数的重载优先级是最低的'
    ]}
],


}

#构建xmind
xmind.build(content,r2)

#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 