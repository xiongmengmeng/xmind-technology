import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
xmind_name="dubbo"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("Exporter")
r2=s2.getRootTopic()
r2.setTitle("Exporter")


content={
'Exporter<T>':[
    'Invoker<T> getInvoker()',
    'void unexport()'
],
'InjvmExporter<T>':[
    {'InjvmExporter(Invoker<T> invoker, String key, Map<String, Exporter<?>> exporterMap)':[
        '将Exporter放入exporterMap中:',
        'exporterMap.put(key, this)'
    ]},
    {'unexport()':[
        '将Exporter从exporterMap中移除:',
        'this.exporterMap.remove(this.key)'
    ]}
],
'ListenerExporterWrapper<T>':[
    'Exporter的包装类',
    {'属性':[
        {'Exporter<T> exporter':[
        ]}
    ]},
    {'ListenerExporterWrapper(Exporter<T> exporter, List<ExporterListener> listeners)':[
        '遍历listeners，执行其方法listener.exported(this)'
    ]}
]




}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 