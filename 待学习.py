import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="java"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("待学习")
r2=s2.getRootTopic()
r2.setTitle("待学习")


content={
'ForkJoinPool':[
    'https://blog.csdn.net/niyuelin1990/article/details/78658251',
],
'算法':[
    'https://blog.csdn.net/kobe_k/category_9649663.html'
],
'jvm':[
    '《尚硅谷宋红康JVM教程》',
    ''
],
'java':[
    'Class loader也可以总结一篇',
    ''
],
'mybatis':[
    'mapper代理都做了什么'
],
'spring:[
    'httpServlet  是servlet包的',
    'ioc扩展：https://blog.csdn.net/lzb348110175/article/details/106071906',
    'ioc扩展：https://www.jianshu.com/p/1e212eac42ac'
]
'面试':[
    'https://joonwhee.blog.csdn.net/article/details/115364158?utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7EBlogCommendHotData%7Edefault-1.control&dist_request_id=1331645.9431.16183670589760127&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7EBlogCommendHotData%7Edefault-1.control'
],
'学习':[
    '链接: https://pan.baidu.com/s/1-EYhMO7noEMjZctCMxMSHw 密码: fhrm',
],
'简历':[
    'https://joonwhee.blog.csdn.net/article/details/109709619'
]
'操作系统':[
    'https://baijiahao.baidu.com/s?id=1672241268742313112',
    'https://baijiahao.baidu.com/s?id=1672241268742313112'
]

}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 