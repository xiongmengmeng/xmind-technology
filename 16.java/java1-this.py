import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="java"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("this")
r2=s2.getRootTopic()
r2.setTitle("this")


content={
'对象的本质':[
    '对象的本质理解为“多个相关数据的统一载体”'
],
'理解this':[
    '对象在堆中，有多个',
    '方法在方法区中，只有一个',
    '不同对象调用同一个方法，会产生不同结果：',
    {'理解':[
        '对象内部持有一个引用',
        '调用某个方法时，必须传递这个对象引用,只是java是隐式传递',
        '然后方法根据这个引用知道当前这套指令是对哪个对象的数据进行操作'
    ]}
],
'理解static':[
    'static修饰的属性或方法其实都是属于类的，是所有对象共享的',
    {'一个变量或者方法能声明为static，原因':[
        'static变量：大家共有的，大家都一样，不是特定的差异化数据',
        'static方法：方法不处理差异化数据'
    ]},
],
'理解this与static的关系':[
    'Java中静态方法无法访问非静态数据（实例字段）和非静态方法（实例方法）：',
    '因为Java不会在调用静态方法时传递this，静态方法内没有this当然无法调用实例相关的一切'
]
}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 