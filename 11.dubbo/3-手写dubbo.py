import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
xmind_name="dubbo"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("手写dubbo")
r2=s2.getRootTopic()
r2.setTitle("手写dubbo")


content={
'Protocal':[
    '提供者暴露请求，消费者发送请求，底层使用哪种协议,通过该类实现',
    {'start(URL url)':[
        '提供者暴露请求'
    ]},
    {'send(URL url,Invocation invocatin)':[
        '消费者发送请求'
    ]},
    {'实现方式':[
        '1.ProtocalFactory',
        '2.Dubbo API',
        {'Dubbo API优点':[
            '1.加载的类会缓存起来',
            '2.可单独获得某个指定实现类，可默认指定',
            '3.IOC(autowire,依赖别的类,自动注入)',
            '4.AOP(面向切而)'
        ]}
    ]}
],
'Dubbo SPI':[
    {'内容':[
        'key=value',
    ]},
    {'@SPI接囗类':[
        '略'
    ]},
    {'AOP':[
        {'包装类实现':[
            '构造器传参为接囗类',
            '加入配置文件里，不用有key'
        ]}
    ]},
    {'IOC':[
        '通过URL来确定实现类',
        {'接囗方法':[
            '@Adaptive(value="carType")',
            'getColor(URL url)'
        ]},
        {'使用':[
            'Map<String,String> map=new HashMap()',
            'map.put("catType","red")',
            'URL url=new URL("","",0,map)',
            'drive.driveCar(url)'
        ]}
    ]},
    {'使用':[
        'ExtensionLoader<Car> e=ExtensionLoader.getExtensionLoader(Car.class);',
        'Car redCar=e.getExtension("red")',
        'redCar.getColor()'
    ]}

]


}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 