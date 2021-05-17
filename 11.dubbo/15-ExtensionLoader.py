import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
xmind_name="dubbo"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("ExtensionLoader")
r2=s2.getRootTopic()
r2.setTitle("ExtensionLoader")


content={
'getAdaptiveExtension()':[
    {'属性':[
        'Holder<Object> cachedAdaptiveInstance'
    ]},
    {'instance = this.createAdaptiveExtension()':[
        '创建自适应类',
        '核心this.injectExtension(this.getAdaptiveExtensionClass().newInstance())',
        {'getAdaptiveExtensionClass()':[
            {'this.getExtensionClasses();':[
                '加载配置文件中的类'
            ]},
            {'this.createAdaptiveExtensionClass()':[
                {'1.组装自适应类的代码':[
                    'this.createAdaptiveExtensionClassCode()'
                ]},
                {'2.查找类加载器':[
                    'ClassLoader classLoader = findClassLoader()'
                ]},
                {'3.通过spi方式加载Compiler类':[
                    # 'Compiler compiler=(Compiler)getExtensionLoader(Compiler.class).getAdaptiveExtension()'
                ]},
                {'4.加载自适应类':[
                    'compiler.compile(code, classLoader)'
                ]}
            ]}
        ]}
    ]},
    {'this.cachedAdaptiveInstance.set(instance)':[
        '将自适应类放入cachedAdaptiveInstance'
    ]}
],
'getActivateExtension(URL url, String[] values, String group)':[
    {'1.初始化所有扩展类实现的集合':[
        'this.getExtensionClasses()'
    ]},
    {'2.遍历,根据传入URL匹配条件(匹配group> name等)，得到符合激活条件的扩展类实现':[
        'this.isMatchGroup(group, activate.group())',
        'T ext = this.getExtension(name)'
    ]},
    {'3.根据用户URL配置的顺序，调整扩展点激活顺序':[
        'Collections.sort(exts, ActivateComparator.COMPARATOR);'
    ]}
]


}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 