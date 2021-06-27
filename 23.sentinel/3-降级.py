import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="Sentinel"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("降级规则")
r2=s2.getRootTopic()
r2.setTitle("降级规则")


content={
'降级规则':[
    '对不稳定的弱依赖服务调用进行熔断降级',
    '暂时切断不稳定调用，避免局部不稳定因素导致整体的雪崩',
],
'规则属性':[
    {'resource 资源名':[
        '规则作用对象'
    ]},
    {'grade 熔断策略':[
        '慢调用比例',
        '异常比例',
        '异常数策略'
    ]},
    {'count':[
        '慢调用比例模式下为慢调用临界RT（超出该值计为慢调用）',
        '异常比例/异常数模式下为对应的阈值'
    ]},
    {'timeWindow 熔断时长':[
        '单位s'
    ]},
    {'minRequestAmount 熔断触发的最小请求数':[
        '请求数小于该值时即使异常比率超出阈值也不会熔断'
    ]},
    {'statIntervalMs 统计时长(单位为 ms)':[
        '如60*1000代表分钟级（1.8.0 引入）1000 ms'
    ]},
    {'slowRatioThreshold 慢调用比例阈值':[
        '仅慢调用比例模式有效（1.8.0 引入）'
    ]}
],
'熔断策略':[
    {'慢调用比例':[
        'SLOW_REQUEST_RATIO',
        '以慢调用比例作为阈值，需设置允许的慢调用RT(即最大的响应时间)',
        '请求的响应时间>该值则统计为慢调用',
        {'熔断条件':[
            '单位统计时长(statIntervalMs)内请求数目>设置的最小请求数目&&慢调用的比例>阈值'
        ]},
        '接下来的熔断时长内请求会自动被熔断',
        {'探测恢复状态':[
            'HALF­OPEN 状态',
            '经过熔断时长,若接下来的一个请求响应时间小于设置的慢调用RT则结束熔断',
            '若大于设置的慢调用 RT 则会再次被熔断'
        ]}
    ]},
    {'异常比例':[
        'ERROR_RATIO',
        {'熔断条件':[
            '单位统计时长(statIntervalMs)内请求数目>设置的最小请求数目&&异常比例>阈值'
        ]},
        '接下来的熔断时长内请求会自动被熔断',
        {'探测恢复状态（HALF­OPEN 状态）':[
            '经过熔断时长,若接下来的一个请求成功完成（没有错误）则结束熔断',
            '否则会再次被熔断'
        ]}
    ]},
    {'异常数':[
        'ERROR_COUNT',
        {'熔断条件':[
            '当单位统计时长内的异常数目>阈值'
        ]},
        '接下来的熔断时长内请求会自动被熔断',
        {'探测恢复状态（HALF­OPEN 状态）':[
            '经过熔断时长,若接下来的一个请求成功完成（没有错误）则结束熔断',
            '否则会再次被熔断'
        ]},
        {'注':[
            '异常降级仅针对业务异常，对Sentinel限流降级本身的异常（BlockException）不生效'
        ]}
    ]},
]



}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 