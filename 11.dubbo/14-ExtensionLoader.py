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
'属性':[
    {'ConcurrentMap<Class<?>, ExtensionLoader<?>> EXTENSION_LOADERS':[
        '每个Class都有一个对映的ExtensionLoader'
    ]},
    {'ConcurrentMap<Class<?>, Object> EXTENSION_INSTANCES':[
        '每个Class都有一个实例'
    ]},
],

'getExtensionLoader(Class<T> type)':[
    '从缓存里取，取不到，就构造一个',
    'ExtensionLoader<T> loader = (ExtensionLoader<T>) EXTENSION_LOADERS.get(type);',
    'if (loader == null) {',
    '   EXTENSION_LOADERS.putIfAbsent(type, new ExtensionLoader<T>(type));',
    '   loader = (ExtensionLoader<T>) EXTENSION_LOADERS.get(type);',
    'return loader;'
],
'getExtension(String name)':[
    {'核心createExtension(name)':[
        {'Class<?> clazz = getExtensionClasses().get(name);':[
            '获得类'
        ]},
        {'T instance = (T) EXTENSION_INSTANCES.get(clazz);':[
            '获得实例'
        ]},
        {'injectExtension(instance);':[
            'IOC依赖注入,通过set方法注入需要的扩展点'
        ]},
        {'instance = injectExtension((T) wrapperClass.getConstructor(type).newInstance(instance))':[
            'AOP,通过包装类实现，装饰器模式',
            '包装类Wrapper',
            '封闭了通用的逻辑,通过有无当前扩展参数构造函数来判断,并注入依赖扩展'
        ]}
    ]},
    {'getExtensionClasses()':[
        {'核心loadExtensionClasses();':[
            '校验类是否有@SPI注解',
            {'loadFile(extensionClasses,目录);':[
                '反射创建类',
                '类是否有@Adaptive注解',
                '类是否为包装类，构造器传参为接类型',
                '将数据存入extensionClasses(Map<String, Class<?>>)[不放包装类]'
            ]}
        ]}
    ]},
    {'injectExtension(instance)':[
        {'核心AdaptiveExtensionFactory.getExtension()':[
            '遍历ExtensionFactory实现类，调用其getExtension(type, name)方法',
            {'实现类':[
                {'SpiExtensionFactory':[
                    'loader=ExtensionLoader.getExtensionLoader(type)',
                    'return loader.getAdaptiveExtension();',
                    'getAdaptiveExtension():生成相映代理类'
                ]},
                {'SpringExtensionFactory':[
                    'getBean()'
                ]}
            ]}
        ]}
    ]},
    {'injectExtension((T) wrapperClass.getConstructor(type).newInstance(instance))':[
        '同上',
        '传参为包装类的实例'
    ]}
],
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