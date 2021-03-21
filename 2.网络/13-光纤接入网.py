import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="internet"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("光纤接入网")
r2=s2.getRootTopic()
r2.setTitle("光纤接入网FTTH")


content={

'光纤':[
    '由一种双层结构的纤维状透明材质（玻璃和塑料）构成的',
    '通过纤芯中传导光信号来传输数字信号',
    '数字信息->电信号(1用高电压表示，0用低电压表示)->光信号'
],
'单模光纤':[
    '纤芯细，只有角度最小的光线能进入纤',
    '只能传导一条光线,对于光源和光敏元件的性能要求高',
    '信号失真较小'
],
'多模光纤':[
    '纤芯粗,可多条光线同时传导',
    '对光源和光敏元件的性能要求低'
],
'直连':[
    '互联网接入路由器',
    {'光纤收发器':[
        '将以太网的电信号转换成光信号',
        '连接的光纤一般是单模的'
    ]},
    {'多路光纤收发器':[
        '将光信号转换成电信号',
        '接收端的光敏元件:可根据光的亮度产生不同电压'
    ]},
    'BAS:将包转发到互联网内部',
    '注：上行和下行信号采用不同波长的光，通过棱镜原理进行分离'
],
'分路':[
    '互联网接入路由器',
    {'ONU':[
        '将以太网的电信号转换成光信号',
        '通过调整信号收发时机来避免碰撞'
    ]},
    '分光器：让光纤分路，同时连接多个用户',
    'OLT:将光信号转换成电信号',
    '运营商的BAS'
]



}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 