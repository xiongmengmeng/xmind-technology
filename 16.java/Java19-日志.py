import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir) 

import xmind
from xmind.core.markerref import MarkerId
xmind_name="java"
w = xmind.load(os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 
s2=w.createSheet()
s2.setTitle("日志")
r2=s2.getRootTopic()
r2.setTitle("日志")


content={
'Log4j核心类':[
    {'LoggerConfig':[
        '日志配置,用于整合多个Appender,进行日志打印'
    ]},
    {'Appender':[
        '追加器,用于操作Layout和Manager,往单一目的地进行日志打印'
    ]},
    {'Layout':[
        '布局,用于把LogEvent日志事件序列化成字节序列,不同Layout实现具有不同的序列化方式'
        ''
    ]},
    {'Manager':[
        '管理器,用于管理输出目的地,如:RollingFileManager用于管理文件滚动以及将字节序列写入到指定文件中'
    ]},
    {'Filter':[
        '过滤器,用于对LogEvent日志事件加以过滤,LoggerConfig和Appender都可以配置过滤器,也就是说日志事件会经过一总一分两层过滤'
    ]}
],
'日志问题思考':[
    'https://zhuanlan.zhihu.com/p/28220648'
],
'源码学习':[
    'https://www.zhihu.com/search?type=content&q=Log4j2%E7%B1%BB%E5%9B%BE'
],
'org.slf4j.Logger':[
    'debug(String msg)'
],
'Log4jLogger':[
    '实现org.slf4j.Logger接囗，重写其方法',
    {'debug(java.lang.String)':[
        'logger.logIfEnabled(FQCN, Level.DEBUG, null, format);'
    ]},
    'org.apache.logging.slf4j.#debug(java.lang.String)'
],
'ExtendedLogger':[
    'logIfEnabled(String fqcn, Level level, Marker marker, String message)',
    'isEnabled(Level level, Marker marker, String message)',
    'logMessage(String fqcn, Level level, Marker marker, Message message, Throwable t)'
],
'AbstractLogger':[
    '实现ExtendedLogger接囗，重写其方法',
    {'logIfEnabled(String fqcn, Level level, Marker marker, String message)':[
        'if (isEnabled(level, marker, message)) {',
        '   logMessage(fqcn, level, marker, message);',
        '}'
    ]}
],
'Logger':[
    '继承AbstractLogger',
    {'isEnabled(final Level level, final Marker marker, final String message)':[
        'privateConfig.filter(level, marker, message)'
    ]},
    {'logMessage(final String fqcn,.....)':[
        'ReliabilityStrategy strategy = privateConfig.loggerConfig.getReliabilityStrategy();',
        'strategy.log(this, getName(), fqcn, marker, level, msg, t);'
    ]}
],
'AwaitCompletionReliabilityStrategy':[
    {'log(final Supplier<LoggerConfig> reconfigured,...)':[
        'final LoggerConfig config = getActiveLoggerConfig(reconfigured);',
        'config.log(loggerName, fqcn, marker, level, data, t);',
        'config.getReliabilityStrategy().afterLogEvent();  ',          
    ]}
],
'LoggerConfig':[
    {'getReliabilityStrategy()':[
        'return reliabilityStrategy;'
    ]},
    {'log(final String loggerName, ...)':[
        'LogEvent event = Log4jLogEvent.newBuilder().build():封装Log4jLogEvent',
        'log(logEventFactory.createEvent(loggerName, marker, fqcn, level, data, props, t));'
    ]},
    {'log(final LogEvent event)':[
        'if (!isFiltered(event)) {',
        '   processLogEvent(event);',
        '}'
    ]},
    {'processLogEvent(final LogEvent event)':[
        'event.setIncludeLocation(isIncludeLocation());',
        'callAppenders(event);',
        'logParent(event);'
    ]},
    {'callAppenders(final LogEvent event)':[
        'final AppenderControl[] controls = appenders.get();',
        'for (int i = 0; i < controls.length; i++) {',
        '   controls[i].callAppender(event);',
        '}'
    ]}
],
}


#构建xmind
xmind.build(content,r2)
#保存xmind
xmind.save(w,os.path.dirname(os.path.abspath(__file__))+"\\"+xmind_name+".xmind") 