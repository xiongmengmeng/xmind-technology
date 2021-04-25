import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="swagger"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("线上问题")
r2=s2.getRootTopic()
r2.setTitle("线上问题")


content={
'sql':[
    {'sql过长':[
        '数据库通信负载过高->阻塞',
        {'临时解决方案':[
            '运维屏蔽系统使用该sql的链接',
            '重启服务器，释放已有的链接'
        ]},
        {'永久解决方案':[
            'sql拦截器限制长度'
        ]}
    ]},
    {'sql结果集大':[
        'fullGC',
        {'永久解决方案':[
            '大数据量查询通过分片循环实现',
            'sql拦截器限制传参一定要加条件，或自动加入limit做分页'
        ]}
    ]}
],
'gc':[
    {'fgc':[
        {'解决方案':[
            '找出问题原因，屏蔽相关入囗',
            '间断性fgc，可能之前频繁FGC导致堆内存有问题，重启应用初始化堆即可',
            '最大可能是sql查出大量数据，做下控制即可'
        ]},
    ]}
]
}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 