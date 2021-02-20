import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="spring"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("ConfigurationClassParser")
r2=s2.getRootTopic()
r2.setTitle("ConfigurationClassParser")


content={
'':[
    '用于分析@Configuration注解的配置类，产生一组ConfigurationClass对象',
    '该工具主要由ConfigurationClassPostProcessor使用',
    '',
    ''
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