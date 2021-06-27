import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
xmind_name="dubbo"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("@Reference解析")
r2=s2.getRootTopic()
r2.setTitle("@Reference解析")


content={
'ReferenceAnnotationBeanPostProcessor':[
    '⽗类是AnnotationInjectedBeanPostProcessor',
    '⼀个BeanPostProcessor'
],
'作用时机':[
    '对Bean进⾏依赖注⼊时',
    '调⽤AnnotationInjectedBeanPostProcessor的postProcessPropertyValues()⽅法',
    '将某个Bean按照ReferenceAnnotationBeanPostProcessor的逻辑进⾏依赖注⼊',
    {'过程':[
        {'1.查找注⼊点':[
            '被@Reference注解的属性或⽅法'
        ]},
        {'2.注入':[
            '调⽤ReferenceAnnotationBeanPostProcessor#doGetInjectedBean()',
            '得到⼀个对应服务接⼝的代理对象，将对象赋值给属性'
        ]}
    ]}
],
'判断所引⼊的服务是否是本地服务':[
    {'前提':[
        {'Dubbo通过@Service来提供服务，⽣成两个Bean':[
            '服务实现类本身Bean',
            'ServiceBean类型的Bean',
        ]},
        {'ServiceBean类型Bean的名字':[
            '接⼝类型+group+version'
        ]}
    ]},
    {'实现':[
        '判断当前Spring容器中是否存在对应的ServiceBean对象',
        '如存在直接取出ServiceBean对象的ref属性所对应的对象，作为注⼊的结果'
    ]}
],
'判断所引⼊的服务是否已被引⼊过':[
    '在第⼀次引⼊某个服务后（⽣成代理对象后）进⾏缓存',
    {'过程':[
        '1.根据@Reference注解信息+属性接⼝类型⽣成⼀个字符串,作为beanName',
        '2.组装⼀个ReferenceBean对象(get⽅法得到⼀个代理对象,为服务引⼊的⼊⼝⽅法)',
        '3.beanName为key,ReferenceBean为value,注册到Spring容器,同时放⼊referenceBeanCache'
    ]}
],
'@Reference注解服务引⼊过程':[
    '1.组装服务对应的ServiceBean的beanName（源码中叫referencedBeanName）',
    '2.根据@Reference注解信息+属性接⼝类型组装⼀个字符串,叫referenceBeanName',
    {'3.创建⼀个ReferenceBean':[
        '从缓存中拿，拿不到，创建一个，并放入缓存ReferenceBeanCache'
    ]},
    {'4.把ReferenceBean放入spring容器':[
        {'referencedBeanName在容器中存在':[
           '给其对映bean设置一个别名referenceBeanName'
        ]},
        {'referencedBeanName在容器中不存在':[
            'referenceBeanName为key',
            'ReferenceBean为value',
            '存入spring容器'
        ]}
    ]},
    {'5.创建代理':[
        '调⽤ReferenceBean的get()⽅法'
    ]}
]

}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 