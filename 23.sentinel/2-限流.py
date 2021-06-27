import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="Sentinel"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("流控规则")
r2=s2.getRootTopic()
r2.setTitle("流控规则")


content={
'流量控制（flow control）':[
    '监控应用流量的QPS或并发线程数等指标',
    '当达到指定的阈值时对流量进行控制，以避免被瞬时的流量高峰冲垮，从而保障应用的高可用性',
    '同一个资源可以创建多条限流规则'
],
'限流规则':[
    {'resource 资源名':[
        '限流规则的作用对象'
    ]},
    'count 限流阈值',
    {'grade 限流阈值类型':[
        '1:QPS模式',
        '0:并发线程数模式'
    ]},
    {'limitApp 流控针对的调用来源':[
        'default:不区分调用来源'
    ]},
    {'strategy 调用关系限流策略':[
        '直接',
        '链路',
        '关联'
    ]},
    {'controlBehavior 流控效果':[
        '直接拒绝',
        'WarmUp',
        '匀速+排队等待'
    ]},
    {'clusterMode 是否集群限流':[
        '否'
    ]},
],
'BlockException异常统一处理':[
    'springwebmvc限流入口在拦截器HandlerInterceptor->',
    '实现类AbstractSentinelInterceptor的preHandle方法中->',
    '实现类BlockExceptionHandler对异常进行处理'
],
'限流阈值类型':[
    {'QPS（Query Per Second）':[
        '每秒请求数，即服务器在一秒的时间内处理了多少个请求',
        '限制QPS,可防止瞬时的大量请求'
    ]},
    {'并发线程数':[
        '限制并发数，保护业务线程池不被慢调用耗尽'
    ]}
],
'流控模式':[
    '调用关系(调用方、被调用方)的流量控制',
    '一个方法可能会调用其它方法，形成一个调用链路的层次关系',
    {'直接':[
        '资源调用达到设置的阈值后直接被流控抛出异常',
    ]},
    {'关联':[
        '当关联资源达到阈值后，对当前资源流控'
    ]},
    {'链路':[
        '当资源达到阈值后，对入口资源进行限流'
    ]}
],
'流控效果':[
    {'快速失败（直接拒绝）':[
        '默认',
        '当QPS超过阈值，新的请求会被立即拒绝，拒绝方式为抛出FlowException',
        '适用于对系统处理能力确切已知的情况，比如通过压测确定了系统的准确水位'
    ]},
    {'Warm Up（预热）':[
        '当系统长期处于低水位，当流量突然增加，把系统拉升到高水位可能瞬间把系统压垮',
        '通过"冷启动"，让通过的流量缓慢增加，在一定时间内逐渐增加到阈值上限',
        '给冷系统一个预热时间，避免冷系统被压垮',
        {'冷加载因子':[
            'codeFactor默认3，即请求QPS从threshold/3开始，经预热时长逐渐升至设定的QPS阈值'
        ]}
    ]},
    {'匀速排队（排队等待）':[
        '严格控制请求通过的间隔时间，让请求以均匀的速度通过，对应的是漏桶算法'
    ]}

]




}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 