import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
xmind_name="jvm"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("类加载")
r2=s2.getRootTopic()
r2.setTitle("类加载")


content={
'初始化':[
    '执行类构造器<clinit>()方法的过程(编译生成class文件时产生，类的初始化方法)',
    {'<clinit>()内容':[
        '所有类变量的赋值动作',
        '静态语句块（static{}块）',
        {'与构造器不同':[
            '不需要显示地调用父类构造器',
            '但jvm会保证子类调用方法<clinit>()前，调用父类的<clinit>()',
        ]}
    ]},
    {'条件':[
        '1.遇到new、getstatic、putstatic或invokestatic这四条字节码指令时',
        '2.使用java.lang.reflect包的方法对类型进行反射调用时',
        {'3.初始化类的时，其父类还未初始化':[
            '类在初始化时，要求其父类全部要初始化',
            '接口在初始化时，不要求其父接口初始化,在使用到父接口的时候才会初始化'
        ]},
        '4.虚拟机启动时，用户指定的主类（包含main()方法的那个类）',
        {'5.java.lang.invoke.MethodHandle实例解析结果为下面四种类型的方法句柄时':[
            'REF_getStatic',
            'REF_putStatic',
            'REF_invokeStatic',
            'REF_newInvokeSpecial'
        ]},
        '6.一个接口中定义了JDK8新加的默认方法，如接口的实现类发生了初始化，接口要在其之前被初始化'
    ]}
],
'卸载':[
    '类所有实例已被回收，即java堆中不存在该类的任何实例',
    '加载该类的ClassLoader已被回收',
    '类对应的java.lang.Class对象没有任何地方引用，无法通过反射访问该类方法'
],
'类的生命周期':[
    '加载（Loading）',
    {'连接':[
        '验证（Verification）',
        '准备（Preparation）',
        '解析（Resolution）'
    ]},
    '初始化（Initialization）',
    '使用（Using）',
    '卸载（Unloading）' 
],
}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 