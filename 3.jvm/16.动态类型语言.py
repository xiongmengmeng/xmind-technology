import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
xmind_name="jvm"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("动态类型语言")
r2=s2.getRootTopic()
r2.setTitle("动态类型语言")


content={
'关键特征':[
    '类型检查的主体过程是在【运行期】而不是编译期进行的',
    '变量无类型而变量值才有类型'
],
'Java与动态类型':[
    '之前：单纯依靠符号引用来确定调用的目标方法',
    'java.lang.invoke包:提供一种新的动态确定目标方法的机制(方法句柄)'
],
'invokedynamic指令':[
    {'动态调用点':[
        '每一处含有invokedynamic指令的位置'
    ]},
    'CONSTANT_InvokeDynamic_info常量',
    {'常量细节':[
        {'引导方法':[
            '存放在新增的BootstrapMethods属性中，有固定的参数',
            '返回值是java.lang.invoke.CallSite对象,代表真正要执行的目标方法',
            '据常量中的信息，虚拟机可找到并执行引导方法，获得一个CallSite对象',
            '通过CallSite对象，最终调用到要执行的目标方法'
        ]},
        '方法类型',
        '名称'
    ]},
    '不再是代表方法符号引用的CONSTANT_Methodref_info常量'
]


}

#构建xmind
xmind.build(content,r2)

#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 