import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="spring"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("@Conditional注解")
r2=s2.getRootTopic()
r2.setTitle("@Conditional注解")


content={
'@Conditional注解+一个实现了Condition接口的类':[
    'Condition接口:org.springframework.context.annotation.Condition'
    'Bean初始化前，对基属性进行一些校验，不满足校验时就不去装配',
    {'例子':[
        {'类A：实现Condition接口':[
            '重写matches方法，返回true或false',
        ]},
        {'类B：@Conditional(A.class)':[
            '类A的matches方法返回true,',
            '装配类B'
        ]},
    ]}
],

'注解@ImportResource':[
    '可以引入对应的XML文件，用以加载Bean',
    
],
'':[
    {'':[
        '',
        '',
        '',
        '',
        ''
    ]},
],
'':[
    {'':[
        '',
        '',
        '',
        '',
        ''
    ]},
],
}

#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 